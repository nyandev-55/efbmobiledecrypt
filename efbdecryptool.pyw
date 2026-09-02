import json
import os
import zlib
import msgpack
import tkinter as tk
from tkinter import messagebox, ttk
from Crypto.Cipher import AES

# 32 byte Key
KEY_HEX = "43740981523cdc171e71de2ccab1a5a9b86f4b833196c55facd4bd25846c33f5"
KEY = bytes.fromhex(KEY_HEX)


def decode_packet():
    # Get input and strip spaces
    raw_input = input_text.get("1.0", tk.END)
    packet_hex = "".join(raw_input.split())

    if not packet_hex:
        messagebox.showwarning("Warning", "Please enter encrypted hex payload!")
        return

    try:
        packet_bytes = bytes.fromhex(packet_hex)

        if len(packet_bytes) < 16:
            raise ValueError("Packet data must contain at least 16 bytes (IV)!")

        # 1. AES Decrypt (CBC Mode)
        iv = packet_bytes[:16]
        ciphertext = packet_bytes[16:]
        cipher = AES.new(KEY, AES.MODE_CBC, iv)
        decrypted_bytes = cipher.decrypt(ciphertext)

        # 2. Gzip Decompress
        decompressed_data = zlib.decompress(decrypted_bytes, 16 + zlib.MAX_WBITS)

        # 3. MessagePack Decode
        unpacked_data = msgpack.unpackb(
            decompressed_data, raw=False, strict_map_key=False
        )

        # 4. Convert to JSON Format
        json_output = json.dumps(unpacked_data, indent=4, ensure_ascii=False)

        # 5. Dynamic File Path & Safe Save
        script_dir = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(script_dir, "result.json")

        try:
            with open(json_path, "w", encoding="utf-8") as f:
                f.write(json_output)
            file_saved = True
        except PermissionError:
            file_saved = False

        # Display Output
        output_text.config(state=tk.NORMAL)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, json_output)
        output_text.config(state=tk.DISABLED)

        # Update Status
        if file_saved:
            status_label.config(
                text="[+] Success! Decoded and saved to 'result.json'.",
                foreground="green",
            )
        else:
            status_label.config(
                text="[!] Decoded successfully, but 'result.json' is locked/permission denied.",
                foreground="orange",
            )
            messagebox.showwarning(
                "File Warning",
                "Packet decoded successfully, but 'result.json' could not be overwritten because it is open or locked by another process.",
            )

    except Exception as e:
        status_label.config(text=f"[Error] {e}", foreground="red")
        messagebox.showerror("Error", f"Failed to decode packet!\nReason: {e}")


# --- GUI Design ---
root = tk.Tk()
root.title("eFB Mobile Packet Decoder by nyan")
root.geometry("650x600")
root.minsize(500, 400)
root.iconbitmap("app.ico")

# Main Frame
main_frame = ttk.Frame(root, padding="10")
main_frame.pack(fill=tk.BOTH, expand=True)

# Input Area
ttk.Label(
    main_frame, text="Encrypted Packet Hex Data:", font=("Helvetica", 10, "bold")
).pack(anchor=tk.W)
input_text = tk.Text(main_frame, height=6, wrap=tk.WORD)
input_text.pack(fill=tk.X, pady=(5, 10))

# Decode Button
decode_btn = ttk.Button(main_frame, text="Decode Packet", command=decode_packet)
decode_btn.pack(fill=tk.X, ipady=5, pady=(0, 10))

# Status Label
status_label = ttk.Label(main_frame, text="", font=("Helvetica", 9, "italic"))
status_label.pack(anchor=tk.W, pady=(0, 5))

# Output Area
ttk.Label(
    main_frame, text="Decoded JSON Output:", font=("Helvetica", 10, "bold")
).pack(anchor=tk.W)
output_text = tk.Text(main_frame, height=15, wrap=tk.WORD, state=tk.DISABLED)
output_text.pack(fill=tk.BOTH, expand=True, pady=(5, 0))

root.mainloop()
# eFB Mobile Packet Decoder 

A lightweight, Python-based GUI application designed to decrypt and decompress network traffic payloads from **eFootball Mobile**. 

It handles **AES-256 (CBC mode)** decryption, **Gzip** decompression, and **MessagePack** unpacking, outputting cleanly formatted, human-readable JSON files.

---

<img width="651" height="633" alt="Ekran görüntüsü 2026-09-02 143843" src="https://github.com/user-attachments/assets/6e4a0449-dc6c-4398-9c9d-0d4ae15028d0" />


## 🌟 Key Features

- 🔐 **AES-256 (CBC) Decryption:** Automatically handles initialization vectors (IV) and decrypts hex payload strings.
- 📦 **Decompression & Parsing:** Unpacks Gzip binary streams and decodes MessagePack data into JSON.
- 💾 **Automatic Output Export:** Automatically formats and saves the parsed payload to `result.json` in the working directory.
- 🖥️ **User-Friendly Desktop GUI:** Built using Python's native `tkinter` for fast and seamless execution.

---

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3.8+ installed on your system.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com
   cd efbmobiledecrypt
   ```

2. Install the required dependencies:
   ```bash
   pip install pycryptodome msgpack
   ```

---

## 💻 Usage

1. Run the script:
   ```bash
   python efbdecryptortool.pyw
   ```

2. Paste your encrypted **Hex Payload** into the top text box.
3. Click **Decode Packet**.
4. The readable JSON structure will display in the output area and automatically update `result.json`.

---

## 🛠️ Tech Stack

* **GUI:** `tkinter` (Python standard library)
* **Cryptography:** `pycryptodome` (AES CBC)
* **Decompression:** `zlib`
* **Serialization:** `msgpack`, `json`

---

## ⚠️ Disclaimer

This tool is created for educational, research, and debugging purposes only. Use responsibly.

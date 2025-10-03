# 🏛 Caesar Cipher

A simple Python program that implements the **Caesar Cipher** encryption and decryption algorithm. It allows you to **encode** (encrypt) or **decode** (decrypt) messages by shifting the alphabet by a given number.
Day 5 of learning Python.

## 📜 Features

* Encrypts text by shifting letters in the alphabet.
* Decrypts messages back using the same shift value.
* Preserves non-alphabet characters (numbers, spaces, symbols, etc.).
* User-friendly loop to encode/decode multiple times.
* Includes an ASCII art logo for a fun terminal experience.

## 🚀 How to Run

1. Clone or download this repository.
2. Make sure you have **Python 3.x** installed.
3. Install the required package (for ASCII art):

```bash
pip install art
```

or create a file `art.py` with your own `logo`.

4. Run the program:

```bash
python main.py
```

## 💻 Usage Example

```
Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
hello world
Type the shift number:
5
The encoded text is: mjqqt btwqi

Type 'yes' if you want to go again. Otherwise type 'no'.
yes
Type 'encode' to encrypt, type 'decode' to decrypt:
decode
Type your message:
mjqqt btwqi
Type the shift number:
5
The decoded text is: hello world
```

## 🧠 How It Works

* Each letter is shifted in the alphabet by the given number.
* Example with shift = 3:
  * `a → d`, `b → e`, `c → f`, ..., `x → a`, `y → b`, `z → c`
* To **decode**, the shift is reversed.

## 📂 File Structure

```
📦 CaesarCipher
 ┣ 📜 main.py        # Main program with Caesar Cipher logic
 ┣ 📜 art.py         # (Optional) ASCII logo file
 ┗ 📜 README.md      # Documentation
```

## ✅ Future Improvements

* Add support for uppercase letters while keeping their case.
* Add command-line arguments (so no need for user input).
* Add option to save encoded/decoded text to a file.

## 📝 License

This project is open source and available for educational purposes.

## 🤝 Contributing

Feel free to fork this repository and submit pull requests for any improvements or bug fixes!

---

**Happy Encrypting! 🔐**
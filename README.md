
# 🎶 Mariachi Bot

Analyze mariachi song lyrics from the command line for fun and insight!

![Mariachi Image](https://images.unsplash.com/photo-1729638276657-0a0978e66d38?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D)

---

## 📜 About

Mariachi Bot is a Python CLI tool that analyzes the lyrics of mariachi songs and provides useful statistics, such as:

- **Word count**
- **Character frequency**
- **Customizable metrics**

Great for music lovers, linguists, and anyone curious about mariachi lyrics!

---

## 🚀 Features

- Analyze any text file with mariachi lyrics
- Command-line interface (CLI)
- Instant statistics output
- Easily extendable for more metrics

---

## �️ Setup

1. **Clone the repository:**
	```sh
	git clone https://github.com/gabriel-conde/mariachi-bot.git
	cd mariachi-bot
	```
2. **(Optional) Create a virtual environment:**
	```sh
	python3 -m venv venv
	source venv/bin/activate
	```
3. **No dependencies required!**

---

## 🎤 Usage

Place your song lyrics as `.txt` files in the `songs/` directory (or anywhere you like).

Run the bot from the command line:

```sh
python3 main.py songs/amor_eterno.txt
```

**Example Output:**

```
============ MARIACHI SONG BOT ============
Analyzing song found at songs/amor_eterno.txt ...
----------- Word Count ----------
Found 120 total words
--------- Character Count -------
a: 45
e: 38
o: 30
 ...
============= END ===============
```

---

## 📂 Project Structure

```
mariachi-bot/
├── main.py           # CLI entry point
├── stats.py          # Statistics functions
├── songs/            # Example song lyrics
│   ├── amor_eterno.txt
│   ├── hermoso_carino.txt
│   └── ...
└── README.md         # This file
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for new features, bug fixes, or improvements.

---

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.

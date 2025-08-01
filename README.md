# 🤖 RAM — Discord Bot

RAM is a lightweight Discord bot designed for data management, user automation, and command execution via slash commands. Built as part of a CIS30A course project, RAM demonstrates the use of file I/O, custom modules, classes, error handling, and Discord interactions.

---

## 📌 Features

- Slash command support:
  - `/blacklist [user]` — Adds a user to a blacklist
  - `/update [field] [value]` — Updates a config field
  - `/authcmd [key]` — Authorizes access based on a key
- Embed-rich output for better UX
- Persistent storage via `ram_data.json`
- Custom data manager module (`ram_data_manager.py`)
- Error handling with `try` / `except` blocks

---

## 🧠 Tech Stack

- **Python 3.10+**
- **discord.py** (install with `pip install -U discord.py`)
- **Custom Modules**: `ram_data_manager.py`
- **JSON** for persistent file storage

---

## 📂 Project Structure
📁 RAM-Discord-Bot
├── ram_discord_bot.py # Main bot logic
├── ram_data_manager.py # Custom module for file I/O
├── ram_data.json # Data file (auto-created)
└── README.md # This file

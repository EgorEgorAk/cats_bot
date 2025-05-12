
# 🐾 Cat Bot – Telegram Bot for Cat Images

Cat Bot is a simple Telegram bot that sends random cat images to users using [TheCatAPI](https://thecatapi.com/).  
It supports both reply and inline keyboards for user interaction.

---

## 🚀 Features

- 📸 Sends random cat photos from TheCatAPI
- 📱 Inline and reply keyboard buttons
- 🧠 Handles `/start`, `/help`, and keyword `"cats"`
- ❌ Responds to unknown messages with an error

---

## ⚙️ Installation and Usage

### 1. Clone the repository or download the script:

```bash
git clone https://github.com/EgorEgorAk/cat_bot.git
cd cat_bot
```

### 2. Create a `config.py` file in the same directory:

```python
# config.py
TOKEN = "your_telegram_bot_token"
X_api_key = "your_thecatapi_key"
```

### 3. Install dependencies:

```bash
pip install pyTelegramBotAPI requests
```

### 4. Run the bot:

```bash
python bot.py
```

---

## 💡 How to Use

- Type `/start` or `/help` to get a welcome message with buttons.
- Click **"Send the cat 🐈"** or type **`cats`** to receive a cat image.
- If you send an unknown message, the bot will respond with an error message.

---

## 🧰 Technologies Used

- Python 3.x
- [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)
- [TheCatAPI](https://thecatapi.com/)
- requests



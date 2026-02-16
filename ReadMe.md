# Keylogger - Educational Cybersecurity Project

A simple Python keylogger for educational purposes, demonstrating keyboard event monitoring, file logging, and Telegram integration.

⚠️ **DISCLAIMER: This tool is for educational purposes only. Only use on systems you own or have explicit permission to test. Unauthorized use is illegal.**

## Features

- 🔑 Captures all keystrokes in real-time
- 📁 Saves logs to local `logs.txt` file
- 🤖 Sends log files to Telegram every 1 houre
- 🧵 Runs in background with threading

## How It Works

1. **Keylogger Module**: Listens for keyboard events using `pynput`
2. **File Storage**: Appends keystrokes to `logs.txt` with UTF-8 encoding
3. **Telegram Integration**: Sends the log file via Telegram Bot API
4. **Scheduler**: Automatically sends logs every 10 minutes

## Prerequisites

- Python 3.6+
- Telegram account
- Telegram Bot

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/amid322/Keylogger-Telegram-API.git
cd keylogger
................
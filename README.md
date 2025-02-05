# 🚀 **aido**

*A lightweight command-line tool that transforms natural language into valid Linux commands using AI.*

![Example](./example.png)

---

## 📌 **Features**

✔️ **Supports multiple AI models**: OpenAI, Anthropic, and Ollama.  
✔️ **Multilingual input support** – use your preferred language! 🌎  
✔️ **Easily configurable** via `aido.config` file.  
✔️ **System-wide installation available** – use `aido` like any other Linux command.  

---

## ⚙️ **Setup**

### 📥 **Install Dependencies**
```bash
pip3 install -r requirements.txt
```

### 🔑 **Set API Keys**
You need API keys for OpenAI and Anthropic. Set them in your config file before running the script.

- **OpenAI API Key:** [Get it here](https://platform.openai.com/account/api-keys)
- **Anthropic API Key:** [Get it here](https://support.anthropic.com/en/articles/8114521-how-can-i-access-the-claude-api)
- **Ollama:** Install and configure it from [Ollama GitHub](https://github.com/ollama/ollama)

---

## 🛠️ **Configuration File**

Ensure your API keys and settings are in the config file (`~/.config/aido`). Use `aido.config` as a template.

Example:
```bash
DEFAULT_PROVIDER=ollama
OLLAMA_DEFAULT_MODEL=codegemma
```

---

## 🏃 **Usage**

### 🎯 **Basic Command**
```bash
python3 aido.py "Show the contents of text.txt" --provider openai --model gpt-3.5-turbo
```

### 📌 **Specifying a Provider and Model**
```bash
python3 aido.py --provider ollama --model codegemma "Count occurrences of 'AI' in ~/my-project/file.txt"
```

💡 **Tip:** You can set default values in the `aido` config file to avoid typing the provider and model every time.

---

## 💾 **System-Wide Installation**

If you love `aido`, install it as a global command! 😜

```bash
chmod +x aido.py
sudo cp aido.py /usr/bin/aido
```

Now, use `aido` anywhere in your system:
```bash
aido "Create a new folder called 'projects'"
```

---

## 🌎 **Contribute & Support**

🛠️ Found a bug? Want a feature? Open an issue or contribute to the project!

🚀 Happy coding with `aido`! 🤖

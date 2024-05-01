# aido

Implementation of a (toy) command called `aido` (A.I. Do, like... sudo - Super User Do) that receives an input in natural language and converts it into a valid Linux (Ubuntu, in this case) command using a LLM Model.

![Example](./example.png)

The prompt can be written in your preferred language as well, to better suit your preferences!

## Setup

Install dependencies:

```
pip3 install -r requirements.txt
```

This scripts uses the following AI models providers:
- OpenAI
- Anthropic
- Ollama

You must set the API keys for OpenAI and Anthropic in your config file before executing the script (see `aido.config` file).

To use OpenAI API, you should create an OpenAI API account, obtain an API key, and set that key as an environment variable before executing it. To get your API key, access https://platform.openai.com/account/api-keys and set it in the environment using:

```
export OPENAI_API_KEY=<your-api-key>
```

To use Anthropic API, you should create an Anthropic API account, obtain an API key, and set that key as an environment variable before executing it. To get your API key, access https://support.anthropic.com/en/articles/8114521-how-can-i-access-the-claude-api and set it in the environment using:

```
export ANTHROPIC_API_KEY=<your-api-key>
```

To use Ollama API, you will need to install Ollama in your system and download a pre-trained model (`codegemma`, for example), following instructions at https://github.com/ollama/ollama.

## Configuration File

Ensure all settings (API keys and other configurations) are correctly set in the `aido` config file (`~/.config/aido`) before executing the script. You can use the `aido.config` file as a template.

## Use

Execute with python:

```
python3 aido.py <Your prompt> --provider <provider> --model <model>
```

Replace `<Your prompt>` with the natural language input that you want to convert into a Linux command. For example:

```
python3 aido.py "Exibir o conteúdo do arquivo texto.txt" --provider openai --model gpt-3.5-turbo
```

This will convert the input "Exibir o conteúdo do arquivo texto.txt" into a valid Linux command using the OpenAI API.

## Provider and model

You must set the provider and model to be used by the script by setting the `provider` and `model` in command line. The `provider` key can be set to `openai`, `anthropic`, or `ollama`. The `model` depends on the provider. For OpenAI, it can be `gpt-3.5-turbo` or `gpt-4`, for example. For Anthropic, it can be `claude-3-haiku-20240307`. For Ollama, it can be `codegemma`.

```
python3 aido.py --provider ollama --model codegemma "Count how many times the word AI appears in the file ~/my-secret-project/features.txt"
```

You can set the default provider and model in the `aido` config file (`~/.config/aido`). For example:

```
DEFAULT_PROVIDER=ollama
OLLAMA_DEFAULT_MODEL=codegemma
```

This way, you can run the script without setting the provider and model in the command line:

```
python3 aido.py "Count how many times the word AI appears in the file ~/my-secret-project/features.txt"
```

## If you really like this script 😜

You can install it in your system, as a command, by copying it to a directory in your `$PATH`, such as `/usr/bin`. To do this, run the following commands:

```
chmod +x aido.py
sudo cp aido.py /usr/bin/aido
```

Note that you may need to use sudo to copy the file to a directory owned by the root user.

After this, you can use it anywhere in your system:

```
aido <Your prompt>
```

Like in the last example, replace `<Your prompt>` with the natural language input that you want to convert into a Linux command.


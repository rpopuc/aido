from lib.command_executor import CommandExecutor
from lib.providers.openai_provider import OpenAIProvider
from lib.providers.ollama_provider import OllamaProvider
from lib.providers.anthropic_provider import AnthropicProvider
from colorama import Fore, Style

class CLIAssistant:
    def __init__(self, command, provider, model):
        self.executor = CommandExecutor(command)
        self.provider_name = provider
        self.model = model
        self.command = command

    def choose_provider(self, provider_name, model):
        if provider_name == 'anthropic':
            return AnthropicProvider(model)

        if provider_name == 'ollama':
            return OllamaProvider(model)

        return OpenAIProvider(model)

    def present_provider(self, provider_name, provider):
        providerName = Fore.YELLOW + provider_name + Style.RESET_ALL
        modelName = Fore.YELLOW + provider.model + Style.RESET_ALL
        print(f"Using provider {providerName} with model {modelName}\n")

    def main(self):
        # prompt = "Você é um assistente de comando de linha de comando do Ubuntu. Responda apenas com o comando solicitado. Por exemplo:\n\n" \
        #         "P: Listar arquivos do diretório atual?\nR: ls -la\n\n" \
        #         "P: Buscar arquivos iniciados com src- a partir do diretório atual?\nR: find -i name 'src-*'\n\n" \
        #         "P: Criar pasta teste/um/dois/tres?\nmkdir -p teste/um/dois/tres\n\n" \
        #         "Qual o comando para:\n" \
        #         f"P: {self.command}\nR: "
        prompt = "You are an Ubuntu command-line assistant. Answer only with the requested command. For example:\n\n" \
                "Q: List files in the current directory?\nA: ls -la\n\n" \
                "Q: Find files starting with src- from the current directory?\nA: find . -iname 'src-*'\n\n" \
                "Q: Create directory test/one/two/three?\nA: mkdir -p test/one/two/three\n\n" \
                "What's the command for:\n" \
                f"Q: {self.command}\nA: "

        provider = self.choose_provider(self.provider_name, self.model)
        self.present_provider(self.provider_name, provider)

        command_response = provider.get_response(prompt)
        self.executor.command = command_response
        self.executor.menu()

#!/usr/bin/python3
import openai
from colorama import Fore, Style, init
import enquiries
import sys
import os
import uuid

def run(command):
    print(command)
    os.system(command)

def edit(command):
    filename = os.path.join("/tmp", str(uuid.uuid4()))
    with open(filename, "w") as file:
        file.write(command)
    os.system(f"mcedit {filename}")
    with open(filename, 'r') as file:
        command = file.read()
    menu(command.strip())

def cancel(command):
    sys.exit()

def menu(command):
    options = ['Run', 'Edit', 'Cancel']
    choice = enquiries.choose(
        Fore.GREEN + f"{command.strip()}\n" + Style.RESET_ALL,
        options
    )

    switch_dict = {
        "Run": run,
        "Edit": edit,
        "Cancel": cancel
    }
    func = switch_dict.get(choice, cancel)
    func(command)

def main(question):
    prompt = "Qual o comando para executar no CLI do ubuntu:\n\n" \
            "P: Listar arquivos do diretório atual?\nls -la\n\n" \
            "P: Buscar arquivos iniciados com src- a partir do diretório atual?\nfind -i name 'src-*'\n\n" \
            "P: Criar pasta teste/um/dois/tres?\nmkdir -p teste/um/dois/tres\n\n" \
            f"P: {question}\n"
    openai.api_key = os.getenv('OPENAI_API_KEY')

    complete = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0,
        max_tokens=150,
        frequency_penalty=0,
        presence_penalty=0
    )
    command = complete.choices[0].text
    menu(command)

init()
if (os.environ.get('OPENAI_API_KEY') == '' or os.environ.get('OPENAI_API_KEY') is None):
    print(Fore.RED + "You must set OPENAI_API_KEY environment variable.\n" + Style.RESET_ALL)
    print("You can set, for example, using export:\n")
    print("   export OPENAI_API_KEY=" + Fore.YELLOW + "<your api key>" + Style.RESET_ALL)
else:
    question = sys.argv[1]
    if __name__ == '__main__':
        main(question)
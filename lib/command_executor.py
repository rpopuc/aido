import os
import sys
import uuid
from colorama import Fore, Style
import enquiries

class CommandExecutor:
    def __init__(self, command):
        self.command = command

    def run(self):
        print(self.command)
        with open(os.path.expanduser("~/.bash_history"), "a") as file:
            file.write(self.command + "\n")
        os.system(self.command)

    def edit(self):
        filename = os.path.join("/tmp", str(uuid.uuid4()))
        with open(filename, "w") as file:
            file.write(self.command)
        os.system(f"nano {filename}")
        with open(filename, 'r') as file:
            self.command = file.read()
        self.menu()

    def cancel(self):
        print(Fore.GREEN + f"{self.command.strip()}\n" + Style.RESET_ALL)
        print("Canceled")
        sys.exit()

    def menu(self):
        options = ['Run', 'Edit', 'Cancel']
        choice = enquiries.choose(Fore.GREEN + f"{self.command.strip()}\n" + Style.RESET_ALL, options)
        getattr(self, choice.lower())()

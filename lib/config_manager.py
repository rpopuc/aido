import os
import sys
from colorama import Fore, Style
from dotenv import load_dotenv

class ConfigManager:
    def __init__(self):
        self.program_folder = os.path.dirname(os.path.abspath(__file__))
        self.home = os.path.expanduser("~")
        self.config_path = os.path.join(self.home, '.config/aido')

    def load_config(self):
        if not os.path.exists(self.config_path):
            print(Fore.RED + "Config file not found in ~/.config/aido. Please create it based on " + self.program_folder + "/aido.config\n" + Style.RESET_ALL)
            sys.exit(1)
        load_dotenv(self.config_path)

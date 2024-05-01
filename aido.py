#!/usr/bin/env python3
from colorama import  init
from lib.cli_assistant import CLIAssistant
from lib.cli_config import CommandLineConfig

if __name__ == '__main__':
    init()
    config = CommandLineConfig()
    assistant = CLIAssistant(config.get_command(), config.get_provider(), config.get_model())
    assistant.main()


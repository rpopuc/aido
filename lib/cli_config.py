import os
import argparse
from lib.config_manager import ConfigManager

class CommandLineConfig:
    def __init__(self):
        # Load configuration file
        config_manager = ConfigManager()
        config_manager.load_config()

        # Parse command line arguments
        parser = argparse.ArgumentParser(description="AIDO - Command line assistant.")
        parser.add_argument('command', type=str, help='Command to be executed')
        parser.add_argument('--provider', type=str, help='Specify the provider to be used', required=False)
        parser.add_argument('--model', type=str, help='Specify the model to be used', required=False)
        self.args = self.args = parser.parse_args()

    def get_command(self):
        return self.args.command

    def get_model(self):
        return self.args.model if self.args.model else None

    def get_provider(self):
        return self.args.provider if self.args.provider else os.getenv('DEFAULT_PROVIDER')

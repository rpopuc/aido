#!/bin/bash

pip3 install -r requirements
cp aido.config ~/.config/aido
sudo ln -s "$PWD/aido.py" /usr/bin/aido_command

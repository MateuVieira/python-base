#!/usr/bin/env python3

"""Hello World Multi Languages

Using the current language config on the env 
the program will show a message for that language.

How to use:

Is needed to have the LANG var settled, ex:
    
    export LANG=pt_BR

Execution:

    python hello.py
    or
    ./hello.py
"""
__version__ = "0.0.1"
__author__ = "MVP"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = 'Hello, World!!'

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour, Monde!"

# This script print on the terminal a 'Hello, World!!' message
print(msg)

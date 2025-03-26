#!/usr/bin/env python3
"""Ponto de entrada para a CLI da TESS."""

import sys
from arcee_cli.chat import start_chat

COMMANDS = {
    "chat": start_chat,
    "conversar": start_chat,
}

def main():
    """Função principal do CLI."""
    if len(sys.argv) < 2 or sys.argv[1] not in COMMANDS:
        print("Uso: python -m arcee_cli [comando]")
        print("Comandos disponíveis:")
        for cmd in COMMANDS:
            print(f"  - {cmd}")
        sys.exit(1)
    
    command = sys.argv[1]
    COMMANDS[command]()

if __name__ == "__main__":
    main()
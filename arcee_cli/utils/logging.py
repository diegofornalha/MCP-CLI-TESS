"""Configuração de logging para o CLI."""

import logging
import sys
from rich.console import Console
from rich.logging import RichHandler

console = Console()

def setup_logging(level=logging.INFO):
    """Configura o sistema de logging.
    
    Args:
        level: Nível de logging (default: logging.INFO)
    """
    logging.basicConfig(
        level=level,
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(console=console, rich_tracebacks=True)]
    )
    
    return logging.getLogger("arcee_cli")

logger = setup_logging()
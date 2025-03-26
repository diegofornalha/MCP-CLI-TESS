"""Implementação do chat interativo com a API TESS."""

import os
import sys
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.styles import Style
from rich.console import Console
from rich.markdown import Markdown
from dotenv import load_dotenv

from arcee_cli.providers.tess_provider import TessProvider
from arcee_cli.utils.logging import logger

# Carrega variáveis de ambiente
load_dotenv()

# Define estilo para o prompt
style = Style.from_dict({
    "prompt": "ansicyan bold",
})

# Configuração do console
console = Console()

def print_welcome_message():
    """Exibe mensagem de boas-vindas."""
    console.print("\n[bold blue]Bem-vindo ao Chat TESS![/bold blue]")
    console.print("Digite [bold green]ajuda[/bold green] para ver os comandos disponíveis.")
    console.print("Digite [bold green]sair[/bold green] para encerrar o chat.\n")

def print_help():
    """Exibe ajuda sobre os comandos disponíveis."""
    console.print("\n[bold]Comandos disponíveis:[/bold]")
    console.print("  [green]ajuda[/green] - Exibe esta mensagem de ajuda")
    console.print("  [green]limpar[/green] - Limpa o histórico da conversa atual")
    console.print("  [green]sair[/green] - Encerra o chat\n")

def start_chat():
    """Inicia o chat interativo com a TESS."""
    # Verifica se a API key está configurada
    if not os.getenv("TESS_API_KEY"):
        console.print("[bold red]Erro:[/bold red] TESS_API_KEY não encontrada.")
        console.print("Configure a variável de ambiente TESS_API_KEY ou adicione ao arquivo .env")
        sys.exit(1)
    
    # Cria diretório para histórico se não existir
    os.makedirs(os.path.expanduser("~/.arcee_cli"), exist_ok=True)
    
    # Inicializa o provedor TESS
    try:
        tess_provider = TessProvider()
    except ValueError as e:
        console.print(f"[bold red]Erro:[/bold red] {e}")
        sys.exit(1)
    
    # Configura sessão com histórico
    session = PromptSession(
        history=FileHistory(os.path.expanduser("~/.arcee_cli/history"))
    )
    
    # Inicializa variáveis do chat
    conversation_id = None
    
    # Exibe mensagem de boas-vindas
    print_welcome_message()
    
    # Loop principal do chat
    while True:
        try:
            # Obtém entrada do usuário
            user_input = session.prompt("Você: ", style=style)
            
            # Verifica comandos especiais
            if user_input.lower() == "sair":
                console.print("[bold blue]Encerrando chat. Até logo![/bold blue]")
                break
            elif user_input.lower() == "ajuda":
                print_help()
                continue
            elif user_input.lower() == "limpar":
                conversation_id = None
                console.print("[italic]Histórico da conversa limpo.[/italic]")
                continue
            elif not user_input.strip():
                continue
            
            # Envia mensagem para API TESS
            console.print("[dim]Enviando mensagem...[/dim]")
            response = tess_provider.send_message(user_input, conversation_id)
            
            if "error" in response:
                console.print(f"[bold red]Erro:[/bold red] {response['error']}")
                continue
            
            # Atualiza ID da conversa se for uma nova
            if "conversation_id" in response:
                conversation_id = response["conversation_id"]
            
            # Exibe resposta formatada
            console.print("\n[bold green]TESS:[/bold green]")
            
            # Verifica se a resposta pode ser formatada como markdown
            if "reply" in response:
                try:
                    console.print(Markdown(response["reply"]))
                except Exception:
                    console.print(response["reply"])
            else:
                console.print("[bold red]Resposta inesperada da API.[/bold red]")
            
            console.print()  # Linha em branco para separar mensagens
            
        except KeyboardInterrupt:
            console.print("\n[bold blue]Encerrando chat. Até logo![/bold blue]")
            break
        except Exception as e:
            logger.exception("Erro não tratado")
            console.print(f"[bold red]Erro inesperado:[/bold red] {e}")

if __name__ == "__main__":
    start_chat()
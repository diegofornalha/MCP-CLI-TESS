# MCP-CLI-TESS

CLI simples para interação com a API TESS através do MCP.

## Descrição

Este projeto fornece uma interface de linha de comando (CLI) para interagir com a API TESS. Ele permite enviar mensagens para agentes da TESS e receber respostas em um formato de chat interativo.

## Estrutura do Projeto

```
arcee_cli/
  ├── __init__.py           # Inicializador do pacote
  ├── __main__.py           # Ponto de entrada da CLI
  ├── chat.py               # Implementação principal do chat
  ├── providers/            # Provedores de serviços
  │   ├── __init__.py
  │   └── tess_provider.py  # Provedor específico para API TESS
  └── utils/                # Utilitários
      ├── __init__.py
      └── logging.py        # Configuração de logging
```

## Requisitos

- Python 3.8+
- Bibliotecas listadas em `requirements.txt`

## Instalação

1. Clone o repositório
2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```
3. Configure as variáveis de ambiente:
   ```
   cp .env.example .env
   ```
   E edite o arquivo `.env` com suas credenciais.

## Uso

### Método 1: Via script

```bash
python chat.py
```

### Método 2: Via módulo

```bash
python -m arcee_cli chat
# ou
python -m arcee_cli conversar
```

## Comandos do Chat

- `ajuda` - Exibe ajuda sobre os comandos disponíveis
- `limpar` - Limpa o histórico da conversa
- `sair` - Encerra o chat

## Configuração

As seguintes variáveis de ambiente são necessárias:

- `TESS_API_KEY` - Chave de API para a TESS
- `TESS_API_URL` - URL da API TESS (opcional, padrão: https://tess.pareto.io/api)

## Licença

Este projeto é licenciado sob a MIT License.
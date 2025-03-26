"""Provedor para API TESS."""

import os
import requests
from dotenv import load_dotenv
from arcee_cli.utils.logging import logger

# Carrega variáveis de ambiente
load_dotenv()

class TessProvider:
    """Provedor para comunicação com a API TESS."""
    
    def __init__(self):
        """Inicializa o provedor TESS."""
        self.api_key = os.getenv("TESS_API_KEY")
        if not self.api_key:
            raise ValueError("TESS_API_KEY não encontrada. Configure no arquivo .env")
        
        self.api_url = os.getenv("TESS_API_URL", "https://tess.pareto.io/api")
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        })
    
    def send_message(self, message, conversation_id=None):
        """Envia mensagem para a API TESS.
        
        Args:
            message: Texto da mensagem
            conversation_id: ID da conversa (opcional)
            
        Returns:
            Resposta da API formatada
        """
        endpoint = f"{self.api_url}/chat"
        
        payload = {
            "message": message,
        }
        
        if conversation_id:
            payload["conversation_id"] = conversation_id
        
        try:
            logger.debug(f"Enviando mensagem para {endpoint}")
            response = self.session.post(endpoint, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Erro ao comunicar com API TESS: {e}")
            return {"error": str(e), "reply": "Erro ao comunicar com a API TESS"}
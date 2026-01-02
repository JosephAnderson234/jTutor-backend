import os
from openai import OpenAI
from typing import Optional

# Validar que el token de GitHub esté configurado
github_token = os.getenv("GITHUB_TOKEN")
if not github_token:
    raise ValueError("GITHUB_TOKEN no está configurada en variables de entorno")

# Configuración de GitHub AI
ENDPOINT = "https://models.github.ai/inference"
CHAT_MODEL = "openai/gpt-5-nano"
EMBEDDING_MODEL = "text-embedding-3-small"

# Cliente de OpenAI configurado para GitHub AI
client = OpenAI(
    base_url=ENDPOINT,
    api_key=github_token,
)

def get_chat_client() -> OpenAI:
    """Obtiene el cliente de OpenAI configurado para GitHub AI."""
    return client

def get_chat_model_name() -> str:
    """Obtiene el nombre del modelo de chat."""
    return CHAT_MODEL

def get_embedding_model_name() -> str:
    """Obtiene el nombre del modelo de embeddings."""
    return EMBEDDING_MODEL

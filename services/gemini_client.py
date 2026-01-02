import google.generativeai as genai
import os
from typing import Optional

# Validar que la API key esté configurada
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY no está configurada en variables de entorno")

genai.configure(api_key=api_key)

# Configuración centralizada de modelos
CHAT_MODEL = "gemini-2.5-flash"
EMBEDDING_MODEL = "models/embedding-001"

def get_chat_model() -> genai.GenerativeModel:
    """Obtiene el modelo de chat de Gemini."""
    return genai.GenerativeModel(CHAT_MODEL)

def get_embedding_model() -> str:
    """Obtiene el nombre del modelo de embeddings de Gemini."""
    return EMBEDDING_MODEL
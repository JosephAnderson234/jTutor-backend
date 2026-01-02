from services.embedding_service import search
from services.gpt_client import get_chat_client, get_chat_model_name

def answer_question(question: str) -> str:
    context_chunks = search(question)

    if not context_chunks:
        return "La respuesta no se encuentra en el material proporcionado."

    context = "\n\n".join(context_chunks)

    prompt = f"""
Eres un tutor académico.
Responde únicamente usando el contexto proporcionado.
Si la respuesta no está en el contexto, di que no se encuentra.

Contexto:
{context}

Pregunta:
{question}
"""

    client = get_chat_client()
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "Eres un tutor académico. Responde únicamente usando el contexto proporcionado."},
            {"role": "user", "content": f"Contexto:\n{context}\n\nPregunta:\n{question}"}
        ],
        model=get_chat_model_name()
    )
    return response.choices[0].message.content

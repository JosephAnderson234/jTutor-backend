from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from services.rag_service import answer_question

chat_bp = Blueprint("chat", __name__)

@chat_bp.post("/")
@jwt_required()
def chat():
    question = request.json.get("question")
    answer = answer_question(question)
    return {"answer": answer}

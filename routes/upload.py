import os
from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from services.pdf_service import extract_text_from_pdf
from services.embedding_service import add_documents

upload_bp = Blueprint("upload", __name__)

@upload_bp.post("/")
@jwt_required()
def upload():
    file = request.files.get("file")

    if not file:
        return {"msg": "No file"}, 400

    path = f"uploads/{file.filename}"
    os.makedirs("uploads", exist_ok=True)
    file.save(path)

    text = extract_text_from_pdf(path)

    chunks = [text[i:i+800] for i in range(0, len(text), 800)]
    add_documents(chunks)

    return {"msg": "Documento procesado", "chunks": len(chunks)}

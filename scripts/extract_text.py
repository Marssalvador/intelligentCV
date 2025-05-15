import os
from PyPDF2 import PdfReader
from docx import Document
import requests

def ocr_groq(image_path: str) -> str:
    url = 'https://api.groq.com/vision/ocr'
    files = {'file': open(image_path, 'rb')}
    headers = {'Authorization': 'Bearer YOUR_GROQ_API_KEY'}
    resp = requests.post(url, files=files, headers=headers)
    resp.raise_for_status()
    return resp.json().get('text', '')


def extract_text(file_path: str) -> str:
    ext = file_path.lower().split('.')[-1]
    text = ''
    if ext == 'pdf':
        for page in PdfReader(file_path).pages:
            text += page.extract_text() or ''
    elif ext == 'docx':
        for p in Document(file_path).paragraphs:
            text += p.text + '\n'
    elif ext in ('jpg', 'jpeg', 'png'):
        text = ocr_groq(file_path)
    elif ext == 'txt':
        text = open(file_path, encoding='utf-8').read()
    return text


def extract_and_score(file_path: str, job_id: int):
    raw = extract_text(file_path)
    # Aquí integrar meta-llama/llama-4-scout para scoring...
    score = 0.0
    summary = ''
    alignment = 0.0
    return score, summary, alignment
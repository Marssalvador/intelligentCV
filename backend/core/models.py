from django.db import models

class JobDescription(models.Model):
    """Modelo para almacenar la descripción del puesto."""
    title = models.CharField(max_length=200)
    skills_required = models.TextField()      # Habilidades técnicas y blandas
    experience = models.CharField(max_length=100)
    competencies = models.TextField()         # Competencias clave
    values = models.TextField()               # Valores y cultura empresarial

class CandidateCV(models.Model):
    """Modelo para almacenar el CV del candidato."""
    name = models.CharField(max_length=100)
    document = models.FileField(upload_to='cvs/')  # PDF, DOCX, TXT
    upload_date = models.DateTimeField(auto_now_add=True)

class Evaluation(models.Model):
    """Modelo para guardar la evaluación de un CV contra un puesto."""
    job = models.ForeignKey(JobDescription, on_delete=models.CASCADE)
    candidate = models.ForeignKey(CandidateCV, on_delete=models.CASCADE)
    score = models.FloatField()                # Puntuación de ajuste
    summary = models.TextField()               # Resumen de puntos fuertes/deb.
    alignment = models.FloatField()            # Alineación con valores (0-1)
    created_at = models.DateTimeField(auto_now_add=True)
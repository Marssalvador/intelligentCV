from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import JobDescription, CandidateCV, Evaluation
from .serializers import JobDescriptionSerializer, CandidateCVSerializer, EvaluationSerializer
from .scripts.extract_text import extract_and_score

class CandidateCVViewSet(viewsets.ModelViewSet):
    queryset = CandidateCV.objects.all()
    serializer_class = CandidateCVSerializer

    @action(detail=True, methods=['post'])
    def evaluate(self, request, pk=None):
        cv = self.get_object()
        job_id = request.data.get('job_id')
        score, summary, alignment = extract_and_score(cv.document.path, job_id)
        eval_obj = Evaluation.objects.create(
            job_id=job_id, candidate=cv,
            score=score, summary=summary, alignment=alignment
        )
        return Response(EvaluationSerializer(eval_obj).data)
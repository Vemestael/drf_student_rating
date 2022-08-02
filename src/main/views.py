from django.contrib.auth.views import LoginView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

import main.models as models
import main.serializers as serializers


class Login(LoginView):
    template_name = 'main/sign_in.html'
    next_page = '/'


class FacultyAPI(ModelViewSet):
    queryset = models.Faculty.objects.all()
    serializer_class = serializers.FacultySerializer


class StudyGroupAPI(ModelViewSet):
    queryset = models.StudyGroup.objects.all()
    serializer_class = serializers.StudyGroupSerializer
    filterset_fields = ['faculty']


class ExamSessionAPI(ModelViewSet):
    queryset = models.ExamSession.objects.all()
    serializer_class = serializers.ExamSessionSerializer
    filterset_fields = ['season', 'year']


class RatingAPI(ModelViewSet):
    queryset = models.Rating.objects.all()
    serializer_class = serializers.RatingSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['faculty', 'group', 'scholarship']
    search_fields = ['full_name']


class ExtraPointAPI(ModelViewSet):
    queryset = models.ExtraPoint.objects.all()
    serializer_class = serializers.ExtraPointSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['student_id', 'date']
    search_fields = ['student_id__full_name']


class InviteKeyAPI(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = models.InviteKey.objects.all()
    serializer_class = serializers.InviteKeySerializer


class ExcelFileAPI(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = models.ExcelFile.objects.all()
    serializer_class = serializers.ExcelFileSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['uploaded_by_user', 'date']
    search_fields = ['uploaded_by_user', 'excel_file']


class CertificateAPI(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = models.Certificate.objects.all()
    serializer_class = serializers.CertificateSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['uploaded_by_student', 'date']
    search_fields = ['uploaded_by_student', 'certificate_file']

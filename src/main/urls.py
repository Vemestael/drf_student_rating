from django.urls import path, include
from rest_framework import routers

from main import views

router = routers.DefaultRouter()
router.register(r'faculty', views.FacultyAPI)
router.register(r'study-group', views.StudyGroupAPI)
router.register(r'exam-session', views.ExamSessionAPI)
router.register(r'rating', views.RatingAPI)
router.register(r'extra-point', views.ExtraPointAPI)
router.register(r'invite-key', views.InviteKeyAPI)
router.register(r'excel-file', views.ExcelFileAPI)
router.register(r'certificate', views.CertificateAPI)

urlpatterns = [
    path('login', views.Login.as_view(), name='login'),
    path("api-auth/", include("rest_framework.urls")),
]
urlpatterns += router.urls

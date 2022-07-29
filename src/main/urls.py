from rest_framework import routers

from main import views

router = routers.DefaultRouter()
router.register(r'faculty', views.FacultyAPI)
router.register(r'rating', views.RatingAPI)
router.register(r'extra-point', views.ExtraPointAPI)
router.register(r'invite-key', views.InviteKeyAPI)
router.register(r'excel-file', views.ExcelFileAPI)
router.register(r'certificate', views.CertificateAPI)

urlpatterns = router.urls

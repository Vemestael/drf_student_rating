from rest_framework.serializers import HyperlinkedModelSerializer

import main.models as models


class FacultySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.Faculty
        fields = '__all__'


class StudyGroupSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.StudyGroup
        fields = '__all__'


class ExamSessionSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.ExamSession
        fields = '__all__'


class RatingSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.Rating
        fields = '__all__'


class ExtraPointSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.ExtraPoint
        fields = '__all__'


class InviteKeySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.InviteKey
        fields = '__all__'


class ExcelFileSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.ExcelFile
        fields = '__all__'


class CertificateSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.Certificate
        fields = '__all__'

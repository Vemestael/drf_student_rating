from django.contrib import admin

import main.models as models


@admin.register(models.Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('id', 'initialism', 'faculty_name')


@admin.register(models.StudyGroup)
class StudyGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'faculty', 'group_name')


@admin.register(models.ExamSession)
class ExamSessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'season', 'year')


@admin.register(models.Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'exam_session', 'faculty', 'full_name', 'group', 'avg_score', 'extra_score', 'total_score', 'scholarship')


@admin.register(models.ExtraPoint)
class ExtraPointAdmin(admin.ModelAdmin):
    list_display = ('id', 'student_id', 'date', 'point', 'description', 'certificate')


@admin.register(models.InviteKey)
class InviteKeyAdmin(admin.ModelAdmin):
    list_display = ('id', 'invite_key')


@admin.register(models.ExcelFile)
class ExcelFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'uploaded_by_user', 'excel_file', 'date')


@admin.register(models.Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('id', 'uploaded_by_student', 'certificate_file', 'date')

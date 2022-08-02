from django.db import models


class Faculty(models.Model):
    """
    Model contains a list of university departments
    """
    initialism = models.CharField(max_length=10,
                                  help_text="An abbreviation consisting of the first letters of each word in the name")
    faculty_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.initialism}'


class StudyGroup(models.Model):
    """
    Model contains a list of study groups
    """
    faculty = models.ForeignKey(to=Faculty, on_delete=models.CASCADE)
    group_name = models.CharField(max_length=10, help_text="Abbreviation and study group number")

    def __str__(self):
        return f'{self.group_name}'


class ExamSession(models.Model):
    """
    Model contains a list of exam sessions
    """
    SEASON_CHOICES = (("Зимняя", "Зимняя"), ("Летняя", "Летняя"))
    YEAR_CHOICES = ((i, i) for i in range(2016, 2099))
    season = models.CharField(max_length=50, choices=SEASON_CHOICES, help_text="""The period of the examination session 
                                      (the most common is the scheme with two sessions - winter and spring)""")
    year = models.IntegerField(choices=YEAR_CHOICES)

    def __str__(self):
        return f'{self.year} {self.season}'


class Rating(models.Model):
    """
    Model contains a list of students rating
    """
    exam_session = models.ForeignKey(to=ExamSession, on_delete=models.CASCADE)
    faculty = models.ForeignKey(to=Faculty, on_delete=models.CASCADE)
    group = models.ForeignKey(to=StudyGroup, on_delete=models.CASCADE)

    full_name = models.CharField(max_length=255, help_text="Student's full name")
    avg_score = models.FloatField(help_text="The average score of the student "
                                            "at the end of the semester and examination session")
    extra_score = models.IntegerField(help_text="Student points for additional activity", blank=True)
    total_score = models.FloatField()
    scholarship = models.IntegerField(blank=True)

    class Meta:
        ordering = ["-total_score"]

    def __str__(self):
        return f'{self.full_name} {self.group}'


class ExtraPoint(models.Model):
    """
    Model contains detailed information about the student's extra points
    """
    student_id = models.ForeignKey(to=Rating, on_delete=models.CASCADE)

    date = models.DateField(auto_now=False, auto_now_add=True)
    point = models.IntegerField()
    description = models.TextField(help_text="A description of the activity for which points were received")
    certificate = models.FileField(upload_to="certificate", blank=True)

    def __str__(self):
        return f'{self.student_id} {self.point}'


class InviteKey(models.Model):
    """
    Model contains a list of invitation keys needed to register new users
    """
    invite_key = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.invite_key}'


class ExcelFile(models.Model):
    """
    Model contains a list of uploaded Excel files
    """
    uploaded_by_user = models.CharField(max_length=255, default='admin')
    excel_file = models.FileField(upload_to="excel")
    date = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return f'{self.uploaded_by_user} {self.excel_file}'


class Certificate(models.Model):
    """
    Model contains a list of uploaded Certificate files
    """
    uploaded_by_student = models.ForeignKey(to=Rating, on_delete=models.CASCADE)
    certificate_file = models.FileField(upload_to="certificate")
    date = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return f'{self.uploaded_by_student} {self.certificate_file}'

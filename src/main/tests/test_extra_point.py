from main.models import Faculty, StudyGroup, ExamSession, Rating, ExtraPoint
from main.tests.test_base import BaseApiTestCases


class ExtraPointApiTest(BaseApiTestCases.BaseApiTest):
    @classmethod
    def setUpClass(cls):
        super(ExtraPointApiTest, cls).setUpClass()
        faculty_obj = Faculty.objects.create(initialism='ФИТ', faculty_name='Факультет информационных технологий')
        faculty_obj.save()
        cls.faculty_id = faculty_obj.id

        study_group_obj = StudyGroup.objects.create(group_name='ВТ-17', faculty=Faculty.objects.get(id=cls.faculty_id))
        study_group_obj.save()
        cls.study_group_id = study_group_obj.id

        exam_session_obj = ExamSession.objects.create(season='Зимняя', year=2016)
        exam_session_obj.save()
        cls.exam_session_id = exam_session_obj.id

        rating_obj = Rating.objects.create(full_name='Григорьев Владимир',
                                           avg_score=100.0,
                                           extra_score=10,
                                           total_score=110.0,
                                           scholarship=2900,
                                           exam_session=ExamSession.objects.get(id=cls.exam_session_id),
                                           faculty=Faculty.objects.get(id=cls.faculty_id),
                                           group=StudyGroup.objects.get(id=cls.study_group_id))
        rating_obj.save()
        cls.rating_id = rating_obj.id

        cls.model_data = {'date': '2022-08-07',
                          'point': 10,
                          'description': 'Песни. Пляски',
                          'student_id': f'http://testserver/rating/{cls.rating_id}/'}
        cls.model_abridged_data = {'description': 'Пляски. Песни'}
        cls.path = '/extra-point/'

    def setUp(self):
        extra_point_obj = ExtraPoint.objects.create(date='2022-08-07',
                                                    point=10,
                                                    description='Песни. Пляски',
                                                    certificate=None,
                                                    student_id=Rating.objects.get(id=self.rating_id))
        extra_point_obj.save()
        self.model_id = extra_point_obj.id

        self.equal_data = [{'url': f'http://testserver/extra-point/{self.model_id}/',
                            'date': '2022-08-07',
                            'point': 10,
                            'description': 'Песни. Пляски',
                            'certificate': None,
                            'student_id': f'http://testserver/rating/{self.rating_id}/'}]

from main.models import Faculty, StudyGroup, ExamSession, Rating
from main.tests.test_base import BaseApiTestCases


class RatingApiTest(BaseApiTestCases.BaseApiTest):
    @classmethod
    def setUpClass(cls):
        super(RatingApiTest, cls).setUpClass()
        faculty_obj = Faculty.objects.create(initialism='ФИТ', faculty_name='Факультет информационных технологий')
        faculty_obj.save()
        cls.faculty_id = faculty_obj.id

        study_group_obj = StudyGroup.objects.create(group_name='ВТ-17', faculty=Faculty.objects.get(id=cls.faculty_id))
        study_group_obj.save()
        cls.study_group_id = study_group_obj.id

        exam_session_obj = ExamSession.objects.create(season='Зимняя', year=2016)
        exam_session_obj.save()
        cls.exam_session_id = exam_session_obj.id

        cls.model_data = {'full_name': 'Vemestael',
                          'avg_score': 100.0,
                          'extra_score': 5,
                          'total_score': 105.0,
                          'scholarship': 2900,
                          'exam_session': f'http://testserver/exam-session/{cls.exam_session_id}/',
                          'faculty': f'http://testserver/faculty/{cls.faculty_id}/',
                          'group': f'http://testserver/study-group/{cls.study_group_id}/'}
        cls.model_abridged_data = {
            'avg_score': 100.0,
            'extra_score': 10,
            'total_score': 110.0}
        cls.path = '/rating/'

    def setUp(self):
        rating_obj = Rating.objects.create(full_name='Григорьев Владимир',
                                           avg_score=100.0,
                                           extra_score=10,
                                           total_score=110.0,
                                           scholarship=2900,
                                           exam_session=ExamSession.objects.get(id=self.exam_session_id),
                                           faculty=Faculty.objects.get(id=self.faculty_id),
                                           group=StudyGroup.objects.get(id=self.study_group_id))
        rating_obj.save()
        self.model_id = rating_obj.id

        self.equal_data = [
            {'url': f'http://testserver/rating/{self.model_id}/',
             'full_name': 'Григорьев Владимир',
             'avg_score': 100.0,
             'extra_score': 10,
             'total_score': 110.0,
             'scholarship': 2900,
             'exam_session': f'http://testserver/exam-session/{self.exam_session_id}/',
             'faculty': f'http://testserver/faculty/{self.faculty_id}/',
             'group': f'http://testserver/study-group/{self.study_group_id}/'}]

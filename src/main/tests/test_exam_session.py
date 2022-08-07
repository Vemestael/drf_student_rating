from main.models import ExamSession
from main.tests.test_base import BaseApiTestCases


class ExamSessionApiTest(BaseApiTestCases.BaseApiTest):
    @classmethod
    def setUpClass(cls):
        super(ExamSessionApiTest, cls).setUpClass()
        cls.model_data = {
            'season': 'Летняя',
            'year': 2017}
        cls.model_abridged_data = {'season': 'Летняя'}
        cls.path = '/exam-session/'

    def setUp(self):
        exam_session_obj = ExamSession.objects.create(season='Зимняя', year=2016)
        exam_session_obj.save()
        self.model_id = exam_session_obj.id

        self.equal_data = [{'url': f'http://testserver/exam-session/{exam_session_obj.id}/',
                            'season': 'Зимняя',
                            'year': 2016}]

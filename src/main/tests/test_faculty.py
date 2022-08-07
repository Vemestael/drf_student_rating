from main.models import Faculty
from main.tests.test_base import BaseApiTestCases


class FacultyApiTest(BaseApiTestCases.BaseApiTest):
    @classmethod
    def setUpClass(cls):
        super(FacultyApiTest, cls).setUpClass()
        cls.model_data = {
            'initialism': 'СГФ',
            'faculty_name': 'Социально-гуманитарный факультет'}
        cls.model_abridged_data = {'initialism': 'СГФ'}
        cls.path = '/faculty/'

    def setUp(self):
        faculty_obj = Faculty.objects.create(initialism='ФИТ', faculty_name='Факультет информационных технологий')
        faculty_obj.save()
        self.model_id = faculty_obj.id

        self.equal_data = [{'url': f'http://testserver/faculty/{faculty_obj.id}/',
                            'initialism': 'ФИТ',
                            'faculty_name': 'Факультет информационных технологий'}]

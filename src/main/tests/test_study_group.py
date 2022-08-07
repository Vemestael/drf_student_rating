from main.models import Faculty, StudyGroup
from main.tests.test_base import BaseApiTestCases


class StudyGroupApiTest(BaseApiTestCases.BaseApiTest):
    @classmethod
    def setUpClass(cls):
        super(StudyGroupApiTest, cls).setUpClass()
        faculty_obj = Faculty.objects.create(initialism='ФИТ', faculty_name='Факультет информационных технологий')
        faculty_obj.save()
        cls.faculty_id = faculty_obj.id

        cls.model_data = {
            'group_name': 'КН-17',
            'faculty': f'http://testserver/faculty/{cls.faculty_id}/'}
        cls.model_abridged_data = {'group_name': 'КН-17'}
        cls.path = '/study-group/'

    def setUp(self):
        study_group_obj = StudyGroup.objects.create(group_name='ВТ-17', faculty=Faculty.objects.get(id=self.faculty_id))
        study_group_obj.save()
        self.model_id = study_group_obj.id

        self.equal_data = [{'url': f'http://testserver/study-group/{study_group_obj.id}/',
                            'group_name': 'ВТ-17',
                            'faculty': f'http://testserver/faculty/{self.faculty_id}/'}]

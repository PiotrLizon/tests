import pytest
from form_page import FormPage
from read_excel import ExcelReader
from conftest import MainTest


@pytest.mark.usefixtures('setup')
class TestForm(MainTest):

    def test_just_submit(self, setup):
        form_page = FormPage(self.driver)
        form_page.submit()
        values = form_page.get_msgs()
        assert values[0] == values[1] == values[2] == 'Required', 'failed'

    @pytest.mark.parametrize('data', ExcelReader.get_data())
    def test_form_validation_negative(self, setup, data):
        form_page = FormPage(self.driver)
        form_page.filling_the_form(data.username, data.email, data.age, data.phone_number)
        form_page.submit()
        values = form_page.get_msgs()
        value = form_page.get_msg()
        answers = ['Must be 2 characters or more', 'Must be 15 characters or less',
                   'Only alphanumeric characters', 'Invalid email address',
                   'Must be at least 13', 'Invalid phone number, must be 10 digits']
        assert values[0] == answers[0] or answers[1] or answers[2], 'failed'
        assert values[1] == answers[4], 'failed'
        assert values[2] == answers[5], 'failed'
        assert value == answers[3], 'failed'

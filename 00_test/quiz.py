import logging
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def get_answer(source):
    if 'Spodek' in source:
        return 'w Katowicach'
    elif 'Sanktuarium' in source:
        return 'w Licheniu'
    elif 'Browar' in source:
        return 'Poznaniu'
    elif 'Mariacki' in source:
        return 'bracia-architekci pokłócili się i młodszy zamordował starszego'
    elif 'Filharmonia' in source:
        return 'Szczecina'
    elif 'Modlin' in source:
        return 'Twierdza Modlin'
    elif 'Malbork' in source:
        return 'w XIII'
    elif 'Hala' in source:
        return 'Wrocławia'
    elif 'Domek' in source:
        return 'Sopocie'
    elif 'Palac' in source:
        return 'Stanisława Augusta Poniatowskiego'
    elif 'Ratusz' in source:
        return 'Torunia'
    elif 'Biala' in source:
        return 'Łodzi'
    elif '56Q' in source:
        return 'Gdańsku'
    elif 'Miasto' in source:
        return 'Zamościem'
    elif 'z18314166Q' in source:
        return 'Poznaniu'


class Test:

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.time = 10
        self.link = 'https://wiadomosci.gazeta.pl/wiadomosci/13,129662,5475,'
        'Te-polskie-budowle-musisz-znac-Znasz-je-wszystkie-QUIZ.html?bo=1#_ga=2.60508782.2105060801'
        '.1585397319 '
        '-1866812263.1547918487'
        self.close_popup_css = 'p.close'
        self.attribute_source = 'src'
        self.btn_check_class = 'answers_submit'
        self.score_class = 'quiz_title'
        self.attribute_value = 'value'
        self.expected_result = '15/15'
        self.message_if_failed = 'Assertion failed'

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(self.time)
        self.driver.get(self.link)
        self.driver.maximize_window()
        yield
        self.driver.quit()

    def close_popup(self):
        self.logger.info('closing popup')
        self.driver.find_element_by_css_selector(self.close_popup_css).click()

    def select_correct_answers(self):
        self.logger.info('selecting the correct answers')
        question = 0
        while question < 15:
            src = self.driver.find_element_by_css_selector(
                'div.question.number_' + str(question) + ' img').get_attribute(self.attribute_source)
            answer = get_answer(src)
            self.driver.find_element_by_xpath("//span[text()='" + answer + "']").click()
            question += 1

    def check_result(self):
        self.logger.info('checking result')
        self.driver.find_element_by_class_name(self.btn_check_class).click()

    def get_result(self):
        self.logger.info('getting result:')
        score = self.driver.find_element_by_class_name(self.score_class).get_attribute(self.attribute_value)
        self.logger.info(score)
        return score

    def test(self, setup):
        self.close_popup()
        self.select_correct_answers()
        self.check_result()
        score = self.get_result()
        assert self.expected_result in score, self.message_if_failed

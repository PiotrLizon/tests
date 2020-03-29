from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def get_answer(source):
    if 'Spodek' in src:
        return 'w Katowicach'
    elif 'Sanktuarium' in src:
        return 'w Licheniu'
    elif 'Browar' in src:
        return 'Poznaniu'
    elif 'Mariacki' in src:
        return 'bracia-architekci pokłócili się i młodszy zamordował starszego'
    elif 'Filharmonia' in src:
        return 'Szczecina'
    elif 'Modlin' in src:
        return 'Twierdza Modlin'
    elif 'Malbork' in src:
        return 'w XIII'
    elif 'Hala' in src:
        return 'Wrocławia'
    elif 'Domek' in src:
        return 'Sopocie'
    elif 'Palac' in src:
        return 'Stanisława Augusta Poniatowskiego'
    elif 'Ratusz' in src:
        return 'Torunia'
    elif 'Biala' in src:
        return 'Łodzi'
    elif '56Q' in src:
        return 'Gdańsku'
    elif 'Miasto' in src:
        return 'Zamościem'
    elif 'z18314166Q' in src:
        return 'Poznaniu'


# setup
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get('https://wiadomosci.gazeta.pl/wiadomosci/13,129662,5475,'
           'Te-polskie-budowle-musisz-znac-Znasz-je-wszystkie-QUIZ.html?bo=1#_ga=2.60508782.2105060801.1585397319'
           '-1866812263.1547918487')
driver.maximize_window()

# closing popup
driver.find_element_by_css_selector('p.close').click()

# selecting the correct answers
question = 0
while question < 15:
    src = driver.find_element_by_css_selector('div.question.number_' + str(question) + ' img').get_attribute('src')
    answer = get_answer(src)
    driver.find_element_by_xpath("//span[text()='" + answer + "']").click()
    question += 1

# checking
driver.find_element_by_class_name('answers_submit').click()

# getting result
score = driver.find_element_by_class_name('quiz_title').get_attribute('value')
assert '15/15' in score, 'Assertion filed'

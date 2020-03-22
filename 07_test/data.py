import mysql.connector
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class Data:

    @staticmethod
    def get_driver(browser):
        if browser == 'chrome':
            return webdriver.Chrome(ChromeDriverManager().install())
        elif browser == 'firefox':
            return webdriver.Firefox(executable_path=GeckoDriverManager().install())
        raise Exception('Provide valid driver name')

    @staticmethod
    def get_data():
        try:
            my_database = mysql.connector.connect(host="localhost", user="root",
                                                  passwd="**********",
                                                  database="calculator")
            cursor = my_database.cursor()
            query = "SELECT float_a, char_a, " \
                    "float_b, char_b, " \
                    "float_c, char_c, " \
                    "float_d, char_d FROM fields_circuits_data"
            cursor.execute(query)
            figures = []
            for line in cursor:
                figures.append(line)
            return figures
        except mysql.connector.Error as err:
            print('Error while connecting', err)

    @staticmethod
    def setup_data():
        data = ['assertion filed', ('chrome', 'firefox'),
                10, 'https://www.calculat.org/pl/pole-obwod/']
        return data

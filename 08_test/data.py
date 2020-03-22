from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import mysql.connector


def get_driver(driver):
    if driver == 'chrome':
        return webdriver.Chrome(ChromeDriverManager().install())
    elif driver == 'firefox':
        return webdriver.Firefox(executable_path=GeckoDriverManager().install())


def get_setup_data():
    data = ['assertion failed', 10, 'https://www.calculat.org/pl/objetosc-pole/', 'chrome', 'firefox']
    return data


def get_data():
    try:
        my_database = mysql.connector.connect(host="localhost", user="root",
                                              passwd="**********",
                                              database="calculator")
        cursor = my_database.cursor()
        query = "SELECT float_a, char_a, " \
                "float_b, char_b, " \
                "float_c, char_c FROM volume_surface_data"
        cursor.execute(query)
        blocks = []
        for line in cursor:
            blocks.append(line)
        return blocks
    except mysql.connector.Error as err:
        print('Error while connecting', err)

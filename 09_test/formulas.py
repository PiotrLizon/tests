import datetime
import logging

logger = logging.getLogger(__name__)


# BMI calculator
def bmi_calculator(x, y):
    # x - mass [kg]
    # y - growth [m]
    return round(x / y ** 2, 0)


def weight_message(bmi):
    if bmi < 18.5:
        return 'niedowagę'
    elif 18.5 <= bmi <= 25:
        return 'wagę w normie'
    elif 25 < bmi < 30:
        return 'nadwagę'
    elif bmi >= 30:
        return 'otyłość'


# converting seconds to HH:MM:SS
def seconds_to_hhmmss(seconds):
    time = str(datetime.timedelta(seconds=seconds))
    if len(time) == 7:
        time = '0' + time
    return time


# one_mile_result
def get_one_mile_expected_results(seconds):
    return round((seconds * 1.615) / 1.5, 0)


def get_expected_running_time(distance, pace):
    # distance [km]
    # pace [s]
    return seconds_to_hhmmss(pace * float(distance))


def get_bmi_expected_results(height, weight):
    logger.info('Getting bmi expected results with {}, {}:'.format(height, weight))
    bmi = bmi_calculator(weight, height)
    expected_bmi = str(bmi).replace('.0', '')
    expected_message = weight_message(bmi)
    logger.info('{}, {}'.format(expected_bmi, expected_message))
    return expected_bmi, expected_message


def get_probable_result_expected_result(seconds):
    logger.info('Getting probable expected result with {}:'.format(seconds))
    expected_one_mile = seconds_to_hhmmss(get_one_mile_expected_results(seconds))
    logger.info(expected_one_mile)
    return expected_one_mile


def get_expected_running_pace_calculator_result(distance, pace):
    logger.info('Getting expected running pace result with {}, {}:'.format(distance, pace))
    expected_time = get_expected_running_time(distance, pace)
    logger.info(expected_time)
    return expected_time

import xlrd
from search_data import SearchData


class ExcelReader:

    @staticmethod
    def get_data():
        workbook = xlrd.open_workbook('data.xlsx')
        sheet = workbook.sheet_by_index(0)
        data = []
        for i in range(1, sheet.nrows):
            search_data = SearchData(sheet.cell(i, 0).value, sheet.cell(i, 1).value,
                                     int(sheet.cell(i, 2).value), int(sheet.cell(i, 3).value))
            data.append(search_data)
        return data


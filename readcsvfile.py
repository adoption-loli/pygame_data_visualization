import csv
from pprint import *


class data_list():
    def __init__(self, filename):
        self.filename = filename
        self.datas = []
        with open(filename, 'r', encoding='utf-8') as csv_file:
            self.reader = csv.reader(csv_file)
            for cell in self.reader:
                self.datas.append(cell)

    def analyze(self):
        '''
        [
            [
                date,
                [name, value],
                [name, value],
            ],
            [
                date,
                [name, value],
                [name, value],
            ],
        ]
        '''
        information = {}
        for cell in self.datas:
            try:
                c_name = cell.index('name')
                c_value = cell.index('value')
                c_date = cell.index('date')
            except:
                try:
                    information[cell[c_date]].append([cell[c_name], int(cell[c_value])])
                except:
                    information[cell[c_date]] = []
                    information[cell[c_date]].append([cell[c_name], int(cell[c_value])])
        result = []
        # pprint(information)
        for cell in information:
            temp = [cell]
            temp.extend(information[cell])
            # pprint(temp)
            result.append(temp)
        # pprint(result)
        return result


if __name__ == '__main__':
    test = data_list('danmu_an.csv')
    test.analyze()

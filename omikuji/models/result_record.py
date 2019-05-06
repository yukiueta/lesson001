import collections
import csv
import os
import pathlib


CSV_FILE_NAME = 'omikuji_record.csv'
CSV_COLUMN_USER = 'USER'
CSV_COLUMN_MAIL = 'MAIL'
CSV_COLUMN_RESULT = 'RESULT'


class CsvModel(object):
    def __init__(self, user, mail):
        self.csv_file_name = CSV_FILE_NAME
        self.column = [CSV_COLUMN_USER, CSV_COLUMN_MAIL, CSV_COLUMN_RESULT]
        self.user = user,
        self.mail = mail,
        self.data = collections.defaultdict(int)
        if not os.path.exists(self.csv_file_name):
            pathlib.Path(self.csv_file_name).touch()

    def load_data(self):
        with open(self.csv_file_name, 'r+', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                self.data[(row[CSV_COLUMN_USER], row[CSV_COLUMN_MAIL])] = row[CSV_COLUMN_RESULT]
        return self.data

    def save(self):
        with open(self.csv_file_name, 'w+', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.column)
            writer.writeheader()

            for user, result in self.data.items():
                writer.writerow({
                    CSV_COLUMN_USER: user[0],
                    CSV_COLUMN_MAIL: user[1],
                    CSV_COLUMN_RESULT: result
                })

    def update_record(self, user, mail, result):
        self.load_data()
        self.data[(user, mail)] = result
        self.save()

    def previous_result(self, user, mail):
        self.load_data()
        if (user, mail) in self.data:
            return self.data[(user, mail)]
        else:
            pass










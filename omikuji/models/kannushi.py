import random

from omikuji.models import result_record
from omikuji.views import console


DEFAULT_NAME = '神主ロボ'
OMIKUJI_DICT = {
    1: '大吉',
    2: '中吉',
    3: '吉',
    4: '凶'
}


class Kannushi(object):
    def __init__(self, name=DEFAULT_NAME, user_name='', mail='', selected_num='', initial_set=[]):
        self.name = name
        self.user_name = user_name
        self.mail = mail
        self.selected_num = selected_num
        self.initial_set = initial_set
        self.csv_model = result_record.CsvModel(self.user_name, self.mail)

    def hello(self):
        while True:
            template = console.get_template('hello.txt')
            print(template.substitute({
                'name': self.name,
            }))
            self.user_name = input('名前を入力してください。')
            self.mail = input('メールアドレスを入力して下さい。')
            if self.user_name:
                break

    def previous_result(self):
        """csvファイルの中に同じ名前とメアドのペアがあるかを探す。あれば内容に応じたコメントを返す。"""
        previous_result = self.csv_model.previous_result(self.user_name, self.mail)
        template = console.get_template('previous_result.txt')
        if previous_result:
            print(template.substitute({
                'user_name': self.user_name,
                'previous_result': previous_result,
                'comment': 'テスト'
            }))
        else:
            pass

    def omikuji(self):
        """神主がおみくじを選びユーザーにどれがいいかをきく"""
        self.initial_set = [random.randint(1, 4) for _ in range(4)]
        template = console.get_template('omikuji.txt')
        while True:
            self.selected_num = input(template.substitute({
                'user_name': self.user_name,
                'omikuji_count': str(len(self.initial_set))
            }))
            if 1 <= int(self.selected_num) < 5:
                break

    def omikuji_result(self):
        """おみくじの結果をユーザーに教え、結果をCSVファイルに保存する"""
        template = console.get_template('omikuji_result.txt')
        selected_set = self.initial_set[int(self.selected_num)-1]
        omikuji_result = OMIKUJI_DICT[selected_set]
        print(template.substitute({
            'user_name': self.user_name,
            'result': omikuji_result,
            'comment': 'いい結果だったかの？'
        }))
        self.csv_model.update_record(self.user_name, self.mail, omikuji_result)




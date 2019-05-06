import os
import string


TEMPLATE_DIR_NAME = 'templates'


def get_template_dir_path():
    """テンプレートディレクトリのパスを取得する"""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    template_dir_path = os.path.join(base_dir, TEMPLATE_DIR_NAME)
    return template_dir_path


class NoTemplateError(Exception):
    pass


def find_template(template_file_name):
    """テンプレート名からテンプレートファイルのパスを取得する"""
    template_dir_path = get_template_dir_path()
    template_file_path = os.path.join(template_dir_path, template_file_name)
    if not os.path.exists(template_file_path):
        raise NoTemplateError('I could not found {}'.format(template_file_name))
    return template_file_path


def get_template(template_file_name):
    """テンプレート名からテンプレートの中身を取得する"""
    template_file_path = find_template(template_file_name)
    with open(template_file_path, 'r+', encoding='utf-8') as temp_file:
        contents = temp_file.read().rstrip(os.linesep)
        contents = '{splitter}{sep}{contents}{sep}{splitter}'.format(
            splitter="="*60,
            sep=os.linesep,
            contents=contents
        )
    return string.Template(contents)




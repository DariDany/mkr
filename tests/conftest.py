import os
import pytest


@pytest.fixture(autouse=True)
def prepare_text_file(tmp_path):
    target_file = os.path.join(tmp_path, 'test.txt')
    with open(target_file, 'w') as file:
        lines = ['а-37\n',
                 'і-33\n',
                 'не-23\n',
                 'червона-20\n',
                 'в-20\n',
                 'й-18\n',
                 'шапочка-18\n',
                 'що-14\n',
                 'її-13\n',
                 'бабуся-13\n'
                 ]
        file.writelines(lines)
    return target_file
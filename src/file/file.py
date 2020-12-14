import os
class File:
    @staticmethod
    def read(file_name):
        with open(file_name, 'r') as _file:
            file_content_list = _file.readlines()
            wyn = ''
            for line in file_content_list:
                wyn += line + '\n'
            return wyn

    @staticmethod
    def write(file_path, content):
        with open(file_path, 'w') as file:
            file.write(content)

    @staticmethod
    def delete(file_path):
        if os.path.exists(file_path):
            os.remove(file_path)
            return 'Removed'
        else:
            return 'File does not exist'

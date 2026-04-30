import os
import sys
import os

def normalize(file_name):
    translit_dict = {
        # нижний регистр
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
        'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
        'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
        'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
        'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'ts', 'ч': 'ch',
        'ш': 'sh', 'щ': 'sch', 'ь': '', 'ы': 'y', 'ъ': '',
        'э': 'e', 'ю': 'yu', 'я': 'ya',

        # ВЕРХНИЙ регистр
        'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D',
        'Е': 'E', 'Ё': 'Yo', 'Ж': 'Zh', 'З': 'Z', 'И': 'I',
        'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N',
        'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T',
        'У': 'U', 'Ф': 'F', 'Х': 'H', 'Ц': 'Ts', 'Ч': 'Ch',
        'Ш': 'Sh', 'Щ': 'Sch', 'Ь': '', 'Ы': 'Y', 'Ъ': '',
        'Э': 'E', 'Ю': 'Yu', 'Я': 'Ya'
    }

    latin_number_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

    normalize_name = ""

    for symbol in file_name:
        if latin_number_str.find(symbol) != -1:
            normalize_name += symbol
        else:
            normalize_name += translit_dict.get(symbol, "_")

    return normalize_name

class File:
    def __init__(self, folder, fullname):
        self.folder   = folder
        self.fullname = fullname

        last_dot_index = fullname.rfind('.')

        if last_dot_index != -1:
            self.app = fullname[last_dot_index + 1:]
            self.name = fullname[:last_dot_index]
        else:
            self.app = ""
            self.name = fullname

    def _print(self):
        print(f"Folder: {self.folder} name: {self.name} app: {self.app}")


def read_file_names_from_folder(folder, files):

    for file in os.listdir(folder):
        if os.path.isdir(file):
            read_file_names_from_folder(folder + "\\" + file, files)
        else:
            files_fullnames = {file_elem.fullname: i for i, file_elem in enumerate(files)}

            if file in files_fullnames:
                temp_name = file
                index = 1
                while temp_name in files_fullnames:
                    temp_name = str(index) + "_" + temp_name
                    index += 1
                files.append(File(folder, temp_name))
            else:
                files.append(File(folder, file))


def sort_files(folder):
    files = []
    read_file_names_from_folder(folder, files)

    for file in files:
        file._print()

    image_app = ('JPEG', 'PNG', 'JPG', 'SVG')
    video_app = ('AVI', 'MP4', 'MOV', 'MKV')
    documents_app = ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX')
    music_app = ('MP3', 'OGG', 'WAV', 'AMR')
    archive_app = ('ZIP', 'GZ', 'TAR')



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if sys.argv.__len__() > 1:
        folder = sys.argv[1]
        sort_files(folder)
    else:
        print("don`t enter folder name")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

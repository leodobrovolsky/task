import os
import sys
import os
import shutil

class File:
    def __init__(self, folder, fullname):
        self.folder         = folder
        self.fullname       = fullname
        self.path           = folder + "\\" + fullname

        last_dot_index = fullname.rfind('.')

        if last_dot_index != -1:
            self.app  = fullname[last_dot_index + 1:]
            self.name = fullname[:last_dot_index]
        else:
            self.app  = ""
            self.name = fullname

    def _print(self):
        print(f"Folder: {self.folder}    name: {self.name}    app: {self.app}  path: {self.path}")

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


def read_file_names_from_folder(folder, files):

    for file in os.listdir(folder):

        if os.path.isdir(folder + "\\" + file):
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

    images_app     = ('JPEG', 'PNG', 'JPG', 'SVG')
    videos_app     = ('AVI', 'MP4', 'MOV', 'MKV')
    documents_app = ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX')
    musics_app     = ('MP3', 'OGG', 'WAV', 'AMR')
    archives_app   = ('ZIP', 'GZ', 'TAR')

    #create temp folder
    temp_folder = "." + folder
    while os.path.exists(temp_folder):
        temp_folder = "." + temp_folder

    os.mkdir(temp_folder)

    #create app folder
    os.mkdir(temp_folder + "\\images")
    os.mkdir(temp_folder + "\\videos")
    os.mkdir(temp_folder + "\\documents")
    os.mkdir(temp_folder + "\\musics")
    os.mkdir(temp_folder + "\\archives")

    #copy files
    for file in files:
        normalize_name = normalize(file.name)
        file.normalize_name = normalize_name
        folder_app_name = "\\other\\"

        if file.app in images_app:
            folder_app_name = "\\images\\"
        elif file.app in videos_app:
            folder_app_name = "\\videos\\"
        elif file.app in documents_app:
            folder_app_name = "\\documents\\"
        elif file.app in musics_app:
            folder_app_name = "\\musics\\"
        elif file.app in archives_app:
            folder_app_name = "\\archives\\"

        symbol_dot = ""
        if file.app != "":
            symbol_dot = "."

        print(f"from : {file.path} to : {temp_folder + folder_app_name + normalize_name + symbol_dot + file.app}")
        shutil.copy(file.fullname, temp_folder + folder_app_name + normalize_name + symbol_dot + file.app)

    #delete origin files
    for file in folder:
        os.remove(file)

    #copy in origin folder
    for _folder in os.listdir(temp_folder):
        shutil.copytree(temp_folder + "\\" + _folder, folder + "\\" + _folder)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if sys.argv.__len__() > 1:
        folder = sys.argv[1]
        sort_files(folder)
    else:
        print("don`t enter folder name")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

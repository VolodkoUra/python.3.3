"""Дано имя файла. Необходимо вывести его расширение."""


def power():
    FILENAME = 'folder1/folder2/file.ext'
    result = FILENAME.find(".")
    print(FILENAME[(result)::])



if __name__ == '__main__':
    power()

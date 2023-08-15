import os


def del_pyc(path):
    """
    删除工程指定目录下的所有的编译文件(.pyc)
    """
    for prefix, dirs, files in os.walk(path):
        for name in files:
            if name.endswith('.pyc'):
                filename = os.path.join(prefix, name)
                os.remove(filename)

def del_xls(path):
    """
    删除工程指定目录下的所有的xls（.xls）
    """
    for prefix, dirs, files in os.walk(path):
        for name in files:
            if name.endswith('.xls'):
                filename = os.path.join(prefix, name)
                print(filename)
                os.remove(filename)

def del_xlsx(path):
    """
    删除工程指定目录下的所有的xls（.xlsx）
    """
    for prefix, dirs, files in os.walk(path):
        for name in files:
            if name.endswith('.xlsx'):
                filename = os.path.join(prefix, name)
                print(filename)
                os.remove(filename)



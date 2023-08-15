from common.all_path import conffile_path

def wirte_txt( sort, filePath):
    """
    做审核流时，需要切换不同用户登录，这边指定登录人在配置文件里序号，写入文件（覆盖写入）
    :param filePath:
    :param sort:
    :return:
    """
    with open (filePath, 'w', encoding='utf-8') as f1:
            f1.write(str(sort))
    print(str(sort))

def wirte_add_txt(sort,filePath):
    """
    做审核流时，需要切换不同用户登录，这边指定登录人在配置文件里序号，写入文件(追加写入)
    :param filePath:
    :param sort:
    :return:
    """
    with open (filePath,'a+',encoding='utf-8') as f1:
            f1.write(str(sort))
    print(str(sort))

def read_txt(filePath):
    """
    做审核流时，需要切换不同用户登录，这边指定登录人在配置文件里序号，写入文件
    :param filePath:
    :return:
    """
    list_info = []
    with open(filePath, 'r', encoding='utf-8') as file:
        for line in file:
            list_info.append(line.strip('\n'))
            sortnum = list_info[0]

    return sortnum

if __name__ == '__main__':
    file_path=conffile_path+'get_user.txt'#用户登录序号文件
    # test.wirte_txt("0")
    info=read_txt(file_path)
    print(info,type(info),type(eval(info)))
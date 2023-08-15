# -*- coding: utf-8 -*-
# @Time    : 2021/08/08
# @Author  : guanzhong.zhou
# @File    : 读取yaml文件方法封装

import yaml,os


def read_yaml(config_path):
    """读取yaml文件内容"""
    if not os.path.exists(config_path):
        # 如果文件不存在，则新建
        with open(config_path, "w") as f:
            f.write("")
    with open(config_path, encoding='utf-8') as r:
        config_info = yaml.load(r, Loader=yaml.SafeLoader)
        return config_info


def save_yaml(path, date):
    """保存yaml文件内容"""
    if not os.path.exists(path):
        # 如果文件不存在，则新建
        with open(path, "w") as f:
            f.write("")
    with open(path, 'w', encoding='utf-8') as s:  # 写入模式获取的URL地址到yaml文件中
        yaml.safe_dump(date, s, allow_unicode=True)


if __name__ == '__main__':
    pass

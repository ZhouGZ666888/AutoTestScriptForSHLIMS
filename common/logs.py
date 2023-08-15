# encoding:utf-8
import logging
import time
import os
from common.all_path import log_path


# print(log_path)


class Log1:
    log_path = log_path  # 指定输出日志到目录,将要执行脚本的目录追加上/logs目录，形成log日志

    def __init__(self):
        # 判断目录是否存在
        if not os.path.exists(log_path):
            os.makedirs(log_path)
            print(log_path + "目录创建成功")

        self.logname = os.path.join(log_path, '%s.log' % time.strftime('%Y_%m_%d'))
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        # 日志输出格式
        self.formatter = logging.Formatter(
            '[%(asctime)s] - %(filename)s[line:%(lineno)d] - fuc:%(funcName)s- %(levelname)s: %(message)s')

        # 创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        # 创建一个FileHandler，用于写到本地
        fh = logging.FileHandler(self.logname, 'a', encoding='utf-8')  # 追加模式
        fh.setLevel(logging.INFO)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

    def __console(self, level, message):

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)


class Log:

    def __init__(self):
        # 文件的命名
        self.logname = os.path.join(
            log_path, '%s.log' % time.strftime('%Y_%m_%d'))
        # print(self.logname)
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        # 日志输出格式
        self.formatter = logging.Formatter(
            '[%(asctime)s] - %(filename)s[line:%(lineno)d] - fuc:%(funcName)s- %(levelname)s: %(message)s')

    def __console(self, level, message):
        # 创建一个FileHandler，用于写到本地
        fh = logging.FileHandler(self.logname, 'a', encoding='utf-8')  # 追加模式
        fh.setLevel(logging.INFO)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # 创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        # 这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)


log = Log()
if __name__ == "__main__":
    log = Log()
    log.info("---测试开始ssss----")
    log.info("输入内容sss")
    log.warning("----ssssss----")
    log.debug("----测试结束----")

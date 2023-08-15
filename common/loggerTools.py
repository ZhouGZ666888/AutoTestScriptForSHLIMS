import logging
import os
import time


class Logger:
    """
    日志记录工具类
    日志等级从低到高的顺序是: DEBUG < INFO < WARNING < ERROR < CRITICAL
    """
    
    def __init__(self,logger_name,log_level = logging.INFO):
        """
        :param logger_name:记录日志的名称
        :param log_level:日志显示等级，显示当前等级及以上等级的日志打印 默认：info等级
        """

        self.logpath = '/pythonlogs'
        self.logfilepath = self.logpath + "/logs/uitest"
        self.logpic = self.logpath + "/pics/"
        self.logger = logging.getLogger(logger_name)
        self.creat_logs(log_level)

    def creat_logfolder(self):
        """
        生成日志文件夹
        :return:null
        """
        if not os.path.exists(self.logpath):
            os.makedirs(self.logpath)
        if not os.path.exists(self.logpath):
            return None
        if not os.path.exists(self.logfilepath):
            os.makedirs(self.logfilepath)
        if not os.path.exists(self.logpic):
            os.makedirs(self.logpic)

    def creat_logs(self,log_level):
        """
        :param log_level:日志显示等级，显示当前等级及以上等级的日志打印
        :return:null
        """

        self.logger.setLevel(log_level)

        timeFormater = "%Y%m%d%H%M%S"
        nowTime = time.strftime(timeFormater, time.localtime())

        # 将日志文件命名
        fileName = nowTime + ".log"

        if not os.path.exists(self.logfilepath) :
            self.creat_logfolder()

        # 给日志文件设置路径
        logfilepath = os.path.join(self.logfilepath ,fileName)

        fh = logging.FileHandler(logfilepath)

        ch = logging.StreamHandler()

        logFormater = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(logFormater)
        ch.setFormatter(logFormater)

        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def critical(self,msg):
        """
        以critical等级显示日志信息
        :param msg:显示的日志信息
        :return:null
        """
        self.logger.critical(msg)

    def error(self,msg):
        """
        以error等级显示日志信息
        :param msg:显示的日志信息
        :return:null
        """
        self.logger.error(msg)

    def info(self,msg):
        """
        以info等级显示日志信息
        :param msg:显示的日志信息
        :return:null
        """
        self.logger.info(msg)

    def warning(self,msg):
        """
        以warning等级显示日志信息
        :param msg: 显示的日志信息
        :return:null
        """
        self.logger.warning(msg)

    def debug(self,msg):
        """
        以debug等级显示日志信息
        :param msg: 显示的日志信息
        :return:null
        """
        self.logger.debug(msg)











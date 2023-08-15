# encoding:utf-8
#=============发送指定工程下最新的测试报告============
# from HTMLTestRunner import HTMLTestRunner
import unittest
import os
import sys
import time
from BeautifulReport import BeautifulReport

# 指定执行脚本的目录
test_dir = os.path.abspath(os.path.join(os.getcwd(), "./testcase/"))

print(test_dir)

# 指定存放报告的目录
test_report = os.path.abspath(os.path.join(os.getcwd(), "./report/"))

print(test_report)


if __name__ == '__main__':
    """
    提示
    提示
    提示
    *******************************************************************************************
    每次全流程时，根据不同的测试环境切换不同的数据库配置  、不同的系统环境地址（69环境还是67环境）             *
    *******************************************************************************************
    """
    now = time.strftime("%Y-%m-%d_%H-%M-%S")
    # name='Raw_Search_Mysql_临床突变'
    name=str(now)+'_report'
    # name = 'Raw_2017年1-12月' + now
    test_suite = unittest.defaultTestLoader.discover(
        test_dir, pattern='test1_*.py')
    result = BeautifulReport(test_suite)
    result.report(filename=name, description='Lims系统自动化-用例执行情况',
                  log_path=test_report)

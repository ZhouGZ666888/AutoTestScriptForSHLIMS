# coding:utf-8
from common.logs import log
from common.all_path import img_path
import time, os


class Screenshot:
    """截图功能的装饰器"""

    def __init__(self, driver):
        self.driver = driver

    def get_img(self, desc):
        """截图方法"""
        screen_name = os.path.join(os.path.join(img_path),
                                   time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())) + '_' + str(
                                       desc) + '.png')  # #每个图片的路径
        log.info("<div><img src='" + screen_name + "' width=600 /></div>")  # 这行代码必须加，如果不加，截图正常，但是无法正常加到报告中，
        # 所以这里我们加上新增页签，beautifulreport方法就是无脑读print日志的,<div>是换行作用
        log.info("截图说明：" + str(desc))
        self.driver.get_screenshot_as_file(screen_name)
        log.info("截图保存成功")


if __name__ == '__main__':
    pass

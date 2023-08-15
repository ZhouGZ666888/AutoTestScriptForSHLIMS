import pyperclip, time
from retrying import retry
from selenium.webdriver.support.select import Select
from common import editYaml
from common.all_path import hstq_file_path, wkgj_file_path, csps_file_path, wkfj_file_path, wkdl_non_sr_file_path, \
    sj_file_path, esyjy_file_path, mgmt_file_path, zpy_file_path, testdata_path, functionpageURL_path
from common.DataBaseConfig import executeSql
from common.xlsx_excel import add_write_excel_xlsx
from .exceptionsTools import ElementNotFound, ElementNotTextAttr, ElementNotClickable
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.logs import log


class BasePage:
    """基础页面类"""
    datas = editYaml.read_yaml(testdata_path)  # 获取测试登录地址配置数据-test1环境

    def __init__(self, driver):
        self.driver = driver
        self.baseurl = self.datas['baseurl']

    def openbrower(self):
        """打开浏览器方法"""
        self.driver.get(self.baseurl)
        self.sleep(1)

    def open_laboratory_url(self, url):
        """打开浏览器方法
        :param url:打开的url地址"""
        self.driver.get(url)
        self.driver.implicitly_wait(2)

    def max(self):
        """最大化浏览器方法"""
        self.driver.maximize_window()
        log.info('最大化浏览器')

    def quit(self):
        """关闭浏览器方法"""
        self.driver.quit()
        log.info('关闭浏览器')

    def wait(self, t):
        """浏览器隐形等待方法
        :param t:隐形等待时间"""
        self.driver.implicitly_wait(t)

    @staticmethod
    def sleep(t):
        """浏览器强制等待方法
        :param t:强制等待时间"""
        time.sleep(t)

    def close(self):
        """关闭窗口方法"""
        self.driver.close()
        log.info('关闭页面')

    def refresh(self):
        """浏览器页面刷新方法"""
        self.driver.refresh()
        self.wait_loading()
        log.info('页面刷新')

    def capture_as_base64(self):
        """获取图片方法（以base64存储）
        :return:返回图片base64编码"""
        return self.driver.get_screenshot_as_base64()

    def capture_as_png(self):
        """获取图片方法（以png存储）"""
        return self.driver.get_screenshot_as_png()

    def capture_pic(self, name):
        """获取图片方法
        :param name:所保存图片的名称和位置"""
        return self.driver.save_screenshot(name)

    def capture_as_file(self, filename):
        """获取图片方法
        :param filename: 所保存图片的名称和位置"""
        return self.driver.get_screenshot_as_file(filename)

    def wait_loading(self):
        """设置等待页面loading结束再去操作,是结束，不是出现"""
        WebDriverWait(self.driver, 60).until_not(
            lambda x: x.find_element(By.XPATH, '//*[@class="el-loading-spinner"]/descendant::p[text()="Loading"]'))
        self.sleep(1)

    @property
    def get_source(self):
        """获取页面源代码"""
        return self.driver.page_source

    def wait_pageinfo_end(self):
        """设置等待页面提示信息结束再去操作,是结束，不是出现"""
        WebDriverWait(self.driver, 120).until_not(
            lambda x: x.find_element(By.CLASS_NAME, 'el-message el-message--success'))

    @retry(stop_max_attempt_number=3)
    def findelement(self, stype, element_loc):
        """
        查找单个唯一元素方法
        :param stype:
        :param element_loc:元素属性定位
        :return:对应元素对象
        """
        element = None
        try:
            if stype == "xpath":
                element = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(element_loc))
            elif stype == "class_name":
                element = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_class_name(element_loc))
            elif stype == "id":
                element = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id(element_loc))
            elif stype == "name":
                element = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_name(element_loc))
            elif stype == "link_text":
                element = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_link_text(element_loc))
            elif stype == "partial_link_text":
                element = WebDriverWait(self.driver, 10).until(
                    lambda x: x.find_element_by_partial_link_text(element_loc))
            elif stype == "css":
                element = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_css_selector(element_loc))
        except Exception as e:
            raise ElementNotFound(e)
        return element

    def findelement_(self, element_loc):
        """查找单个唯一元素方法
        :param element_loc:元素属性定位
        :return:对应元素对象"""
        try:
            element = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(element_loc))
        except Exception as e:
            raise ElementNotFound(e)
        return element

    def findelements(self, stype, element_loc):
        """
        查找多个元素方法
        :param stype:
        :param element_loc:元素属性定位
        :return:对应元素对象列表
        """
        elements = None
        try:
            if stype == "xpath":
                elements = WebDriverWait(self.driver, 10).until(lambda x: x.find_elements_by_xpath(element_loc))
            elif stype == "class_name":
                elements = WebDriverWait(self.driver, 10).until(lambda x: x.find_elements_by_class_name(element_loc))
            elif stype == "id":
                elements = WebDriverWait(self.driver, 10).until(lambda x: x.find_elements_by_id(element_loc))
            elif stype == "name":
                elements = WebDriverWait(self.driver, 10).until(lambda x: x.find_elements_by_name(element_loc))
            elif stype == "link_text":
                elements = WebDriverWait(self.driver, 10).until(lambda x: x.find_elements_by_link_text(element_loc))
            elif stype == "partial_link_text":
                elements = WebDriverWait(self.driver, 10).until(lambda x: x.find_elements_by_partial_link_text(
                    element_loc))
            elif stype == "css":
                elements = WebDriverWait(self.driver, 60).until(lambda x: x.find_elements_by_css_selector(element_loc))
        except Exception as e:
            raise ElementNotFound(e)
        return elements

    def isClickable(self, stype, element_loc):
        """
        判断元素是否可点击，返回布尔值
        :param stype:
        :param element_loc:
        :return:True or False
        """
        element = self.findelement(stype, element_loc)
        try:
            if element.is_displayed() and element.is_enabled():
                return True
        except ElementNotClickable:
            return False
        # try:
        #     WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))
        #     return True
        # except:
        #     return False

    def isElementExists(self, stype, element_loc):
        """
        判断元素是否只存在，返回布尔值
        :param stype:
        :param element_loc:
        :return:flag
        """
        flag = True
        try:
            self.findelement(stype, element_loc)
        except ElementNotFound as a:
            flag = False
        return flag

    def isDisplayed(self, ele_type, element_loc):
        """
        判断元素是否可见，返回布尔值
        :param ele_type:
        :param element_loc:
        :return:True or False
        """
        try:
            if self.isElementExists(ele_type, element_loc):
                element = self.findelement(ele_type, element_loc)
                return element.is_displayed()
        except Exception as e:
            raise ElementNotFound(e)

    def isDisPlayed(self, stype, element_loc):
        """
        判断元素是可见，返回布尔值
        :param stype:
        :param element_loc:
        :return:flag
        """
        try:
            ele = self.findelement(stype, element_loc)
            return ele.is_displayed()
        except:
            return False

    def input(self, stype, element_loc, text):
        """
        输入文本方法
        :param stype:
        :param element_loc:对应输入框的元素定位
        :param text:需要输入的文本
        """
        try:
            element = self.findelement(stype, element_loc)
        except Exception as e:
            raise ElementNotFound(e)
        element.clear()
        element.send_keys(text)

    def clear_input(self, stype, element_loc):
        """
        清除文本框内容
        """
        try:
            element = self.findelement(stype, element_loc)
            js = "arguments[0].value='';"
        except Exception as e:
            raise ElementNotFound(e)
        self.executeJscript(js, element)

    @staticmethod
    def updata_sql(sqls):
        """
        调用sql方法,执行更新业务库数据操作
        :return:
        """
        executeSql.test_updateByParam(sqls)

    @staticmethod
    def select_sql(sqls):
        """
        调用sql方法,执行数据库查询操作，获取返回值
        :return:数据库返回值
        """
        sql_data = executeSql.test_select_limsdb(sqls)
        return sql_data

    def executeJscript(self, js, *args):
        """
        执行js语句方法
        :param js: js语句
        :param args:js语句其他的一些参数
        """
        self.driver.execute_script(js, *args)
        # logger.info("执行对应js脚本成功")

    @retry(stop_max_attempt_number=3)
    def clicks(self, stype, element_loc):
        """
        元素点击方法
        test=device.find_element_by_xpath('//*[@id="submit"]')
        device.execute_script("arguments[0].click();", test)
        :param stype:
        :param element_loc:需要点击的元素定位
        """
        try:
            element = self.findelement(stype, element_loc)
        except Exception as e:
            raise ElementNotFound(e)
        element.click()

    @retry(stop_max_attempt_number=3)
    def click_by_js(self, stype, element_loc):
        """
        元素点击方法,针对部分未知点击事假报错，用这个方法
        test=device.find_element_by_xpath('//*[@id="submit"]')
        device.execute_script("arguments[0].click();", test)
        :param stype:
        :param element_loc:需要点击的元素定位
        """
        try:
            element = self.findelement(stype, element_loc)
        except Exception as e:
            raise ElementNotFound(e)
        self.executeJscript("arguments[0].click();", element)

    def get_text(self, stype, element_loc):
        """
        获取到对应元素的text属性
        :param stype:
        :param element_loc:需要获取对应text属性的元素定位
        :return:返回对应的元素的text属性
        """
        try:
            element = self.findelement(stype, element_loc)
        except Exception as e:
            raise ElementNotFound(e)
        try:
            element_text = element.text
            return element_text
        except Exception as e:
            raise ElementNotTextAttr(e)

    def switch_to_window(self, handle_window):
        """
        切换浏览器tab页方法
        :param handle_window:所需要切换窗口的句柄
        """
        self.driver.switch_to.window(handle_window)

    def get_current_window_handle(self):
        """
        获取当前浏览器当前窗口句柄方法
        :return: 返回当前窗口句柄
        """
        return self.driver.current_window_handle

    def get_all_windows(self):
        """
        获取当前浏览器所有窗口句柄的方法
        :return:返回当前浏览器所有窗口的句柄
        """
        return self.driver.window_handles

    def get_current_url(self):
        """
        获取当前的url
        :return:返回当前的url
        """
        return self.driver.current_url

    def switch_to_frame(self, frame):
        """
        切换iframe
        :param frame: iframe元素定位
        :return:
        """
        self.driver.switch_to.frame(frame)

    def switch_to_default_content(self):
        """
        切换iframe回主文档
        :return:
        """
        self.driver.switch_to.default_content()

    def get_cookies(self):
        """
        获取当前浏览器的cookies
        :return:返回当前浏览器的cookies
        """
        Cookie = {}
        for item in self.driver.get_cookies():
            Cookie[item["name"]] = item["value"]
        return Cookie

    def delete_cookies(self):
        """
        清除当前浏览器的所有cookies
        """
        self.driver.delete_all_cookies()

    def moved_to_element(self, stype, element_loc):
        """
        将鼠标移动到对应元素位置
        :param stype:
        :param element_loc:需要将鼠标移动到的元素定位
        """
        try:
            element = self.findelement(stype, element_loc)
        except Exception as e:
            raise ElementNotFound(e)
        ActionChains(self.driver).move_to_element(element).perform()

    def double_click(self, stype, element_loc):
        """鼠标双击元素事件
        :param stype:
        :param element_loc:需要鼠标双击的元素
        """
        try:
            element = self.findelement(stype, element_loc)
        except Exception as e:
            raise ElementNotFound(e)
        ActionChains(self.driver).double_click(element).perform()

    def scrollTo(self, width, height):
        """
        将浏览器内容滚动到指定的坐标方法
        :param width:要在窗口文档显示区左上角显示的文档的 x 坐标
        :param height:要在窗口文档显示区左上角显示的文档的 y 坐标
        """
        js = " window.scrollTo(%d,%d)" % (width, height)
        self.executeJscript(js)
        log.info("成功滑动到 %d,%d" % (width, height))

    def scrollIntoViews(self, stype, element_loc):
        """
        让指定的元素滚动到浏览器窗口的可视区域内方法
        :param stype:
        :param element_loc:指定元素定位
        """
        try:
            element = self.findelement(stype, element_loc)
        except Exception as e:
            raise ElementNotFound(e)
        self.executeJscript("arguments[0].scrollIntoView();", element)

    @staticmethod
    def get_clip():
        """
        获取剪切板内容方法
        :return:返回剪切板内容方法
        """
        return pyperclip.paste()

    @staticmethod
    def set_clip(text):
        """
        将给定字符串内容拷贝进剪贴板方法
        :param text:给定的字符串内容
        :return:
        """
        return pyperclip.copy(text)

    def getAttribute(self, stype, element_loc, attr):
        """
        获取给定元素中的某一属性方法
        :param stype:
        :param element_loc:给定的元素定位
        :param attr:元素的某一个属性
        :return:返回对应元素的对应属性值
        """
        try:
            element = self.findelement(stype, element_loc)
        except Exception as e:
            raise ElementNotFound(e)
        return element.get_attribute(attr)

    def add_excel_xlxs(self, sql, table_name, task_id):

        """
        根据核酸提取、超声破碎、文库构建流程结果表任务单号，在数据库中查询出样本对应下一步流程，以二维列表形式存入相对应的Excel中。最终存入lims号，下一步流向，和任务单号
        :param sql: 数据库sql,取出当前任务单下的样本lims号、实验室号、下一步流向
        :param table_name: 实验流程节点对应的结果表表名
        :param task_id: 实验流程对应的结果表【任务号】页面元素定位
        """
        # 获取任务单号
        taskidstr = self.get_text('css', task_id)
        taskid = taskidstr[5:].strip()

        # 执行SQL，获取二维列表，lims号和下一步流向
        dada = self.select_sql(sql.format(table_name, taskid))

        # 把任务单号添加进二维列表
        result = [list(dct.values()) + [taskid] for dct in dada]  # ID，next，task_id

        # 根据不同下一步，循环写入Excel
        for item in range(len(result)):
            data_list = []
            # 取出二维列表子元素的第三个值（下一步），进行判断
            next_step = result[item][2]

            if next_step == 'extraction':  # 核酸提取
                result[item][2] = '核酸提取'
                data_list.append(result[item])
                add_write_excel_xlsx(hstq_file_path, data_list)

            elif next_step == 'ultrafrac':  # 超声破碎
                result[item][2] = '超声破碎'
                data_list.append(result[item])
                add_write_excel_xlsx(csps_file_path, data_list)

            elif next_step == 'libconstruction':  # 文库构建
                result[item][2] = '文库构建'
                data_list.append(result[item])
                add_write_excel_xlsx(wkgj_file_path, data_list)

            elif next_step == 'pooling':  # 文库富集
                result[item][2] = '文库富集'
                data_list.append(result[item])
                add_write_excel_xlsx(wkfj_file_path, data_list)

            elif next_step == '文库定量':  # 文库定量
                data_list.append(result[item])
                add_write_excel_xlsx(wkdl_non_sr_file_path, data_list)

            elif next_step == '上机':  # 上机
                data_list.append(result[item])
                add_write_excel_xlsx(sj_file_path, data_list)

            elif next_step == 'twentyonegene':  # 21基因
                result[item][2] = '21基因'
                data_list.append(result[item])
                add_write_excel_xlsx(esyjy_file_path, data_list)

            elif next_step == 'mgmt':  # MGMT
                result[item][2] = 'MGMT'
                data_list.append(result[item])
                add_write_excel_xlsx(mgmt_file_path, data_list)

            elif next_step == 'mass_spectro':  # MGMT
                result[item][2] = '质谱仪上机'
                data_list.append(result[item])
                add_write_excel_xlsx(zpy_file_path, data_list)
            else:
                pass

    def enter_func_page(self):
        """调用打开页面方法，直接保存的url页面"""
        datas = editYaml.read_yaml(functionpageURL_path)  # 获取测试登录的账号/密码配置数据

        now_handle = self.get_current_window_handle()
        self.baseurl = datas['url']
        self.openbrower()
        print('打开的URL地址', datas['url'])
        all_handles = self.get_all_windows()
        for handle in all_handles:
            if handle != now_handle:
                # 切换到新窗口句柄，即新打开的页面
                self.close()
                self.switch_to_window(handle)
                self.wait_loading()
        self.sleep(1)

    # def add_excel_xlxs(self, size, samples_lims, samples_lims_num, samples_laboratory_nub, result_next_step, task_id):
    #     """
    #      根据实验流程的结果表样本下一步流程，把对应的样本lims号、实验室号、下一步流程以追加形式写入该流程的Excel
    #     :param size: 拖动页面滚动条尺寸，每个流程拖动幅度不同，注意区别
    #     :param samples_lims: 样本列表所有样本定位tr,算出样本总数
    #     :param samples_lims_num: 样本列表所有样本lims号表单，格式化定位tr{}
    #     :param samples_laboratory_nub: 样本列表所有样本实验室号表单，格式化定位tr
    #     :param result_next_step: 滚动条拖动后，【下一步流向】字段定位，按行获取所有样本的下一步流向文本，格式化定位tr
    #     :param task_id: 任务单号定位，获取任务单号写入Excel
    #     """
    #     js = 'document.getElementsByClassName("vxe-table--body-wrapper")[0].scrollLeft={}'
    #     self.executeJscript(js.format(size))
    #     self.sleep(1)
    #     all_laboratory = ['样本入库', '核酸提取', '超声破碎', '文库构建', '文库富集', '文库定量', 'Library quantification',
    #                       'Sequencer Operation', '上机', '21基因',
    #                       'MGMT']
    #     total_samples_lims = self.findelements('css', samples_lims)  # 获取样本总数
    #     print("样本总数为：", len(total_samples_lims))
    #     task_num = self.get_text('css', task_id)  # 获取任务单号，并写入Excel
    #
    #     for i in range(len(total_samples_lims)):
    #         values = []
    #         sample_last_info = []
    #         j = i + 1
    #         lims_nub = self.get_text('css', samples_lims_num.format(j))  # 根据样本总数，循环获取样本文本（lims号或上机号）
    #         sample_last_info.append(lims_nub)
    #         lab_nub = self.get_text('css', samples_laboratory_nub.format(j))  # 根据样本总数，循环获取实验室号
    #         sample_last_info.append(lab_nub)
    #
    #         # 根据样本总数，循环获取每行样本的文本，从文本中判断是否包含all_laboratory列表中的几个流程，前提是执行js,把滚动条拖到【下一步流向】字段所在位置，否则获取不到包含下一步流向的文本
    #         samples_text = self.get_text('css', result_next_step.format(j))
    #         for lab in all_laboratory:  # 依次取出实验流程
    #             if lab in samples_text and lab == '核酸提取':  # 判断上一步取出的流程是否在获取的样本文本中
    #                 sample_last_info.append(lab)
    #                 sample_last_info.append(task_num[5:].strip())
    #                 print(sample_last_info)
    #                 values.append(sample_last_info)
    #                 print(values)
    #                 add_write_excel_xlsx(hstq_file_path, values)
    #
    #             elif lab in samples_text and lab == '超声破碎':
    #                 sample_last_info.append(lab)
    #                 sample_last_info.append(task_num[5:].strip())
    #                 values.append(sample_last_info)
    #                 add_write_excel_xlsx(csps_file_path, values)
    #
    #             elif lab in samples_text and lab == '文库构建':
    #                 sample_last_info.append(lab)
    #                 sample_last_info.append(task_num[5:].strip())
    #                 values.append(sample_last_info)
    #                 add_write_excel_xlsx(wkgj_file_path, values)
    #
    #             elif lab in samples_text and lab == '文库富集':
    #                 sample_last_info.append(lab)
    #                 sample_last_info.append(task_num[5:].strip())
    #                 values.append(sample_last_info)
    #                 add_write_excel_xlsx(wkfj_file_path, values)
    #
    #             elif lab in samples_text and lab == '文库定量':
    #                 sample_last_info.append(lab)
    #                 sample_last_info.append(task_num[5:].strip())
    #                 values.append(sample_last_info)
    #                 add_write_excel_xlsx(wkdl_non_sr_file_path, values)
    #
    #             elif lab in samples_text and lab == '样本入库':
    #                 sample_last_info.append(lab)
    #                 sample_last_info.append(task_num[5:].strip())
    #                 values.append(sample_last_info)
    #                 add_write_excel_xlsx(ybrk_file_path, values)
    #
    #             elif lab in samples_text and lab == '上机':
    #                 sample_last_info.append(lab)
    #                 sample_last_info.append(task_num[5:].strip())
    #                 values.append(sample_last_info)
    #                 add_write_excel_xlsx(sj_file_path, values)
    #
    #             elif lab in samples_text and lab == '21基因':
    #                 sample_last_info.append(lab)
    #                 sample_last_info.append(task_num[5:].strip())
    #                 values.append(sample_last_info)
    #                 add_write_excel_xlsx(esyjy_file_path, values)
    #
    #             elif lab in samples_text and lab == 'MGMT':
    #                 sample_last_info.append(lab)
    #                 sample_last_info.append(task_num[5:].strip())
    #                 values.append(sample_last_info)
    #                 add_write_excel_xlsx(mgmt_file_path, values)
    #             else:
    #                 pass

    # ===================================以下为dgq封装方法，亦可用==============================

    # 输入内容方法，输入
    def Input(self, stype, value, inputvalue):
        try:
            if stype == "xpath":
                self.driver.find_element_by_xpath(value).send_keys(inputvalue)
            elif stype == "class_name":
                self.driver.find_element_by_class_name(value).send_keys(inputvalue)
            elif stype == "id":
                self.driver.find_element_by_id(value).send_keys(inputvalue)
            elif stype == "name":
                self.driver.find_element_by_name(value).send_keys(inputvalue)
            elif stype == "link_text":
                self.driver.find_element_by_link_text(value).send_keys(inputvalue)
            elif stype == "partial_link_text":
                self.driver.find_element_by_partial_link_text(value).send_keys(inputvalue)
        except Exception as e:
            raise ElementNotFound(e)

    # 鼠标事件方法一,点击
    def Click(self, stype, value):
        try:
            if stype == "xpath":
                self.driver.find_element_by_xpath(value).click()
            elif stype == "class_name":
                self.driver.find_element_by_class_name(value).click()
            elif stype == "id":
                self.driver.find_element_by_id(value).click()
            elif stype == "name":
                self.driver.find_element_by_name(value).click()
            elif stype == "link_text":
                self.driver.find_element_by_link_text(value).click()
            elif stype == "partial_link_text":
                self.driver.find_element_by_partial_link_text(value).click()
        except Exception as e:
            raise ElementNotFound(e)

    # 鼠标事件方法二，清除
    def clear_value(self, stype, value):
        try:
            if stype == "xpath":
                self.driver.find_element_by_xpath(value).clear()
            elif stype == "id":
                self.driver.find_element_by_id(value).clear()
            elif stype == "name":
                self.driver.find_element_by_name(value).clear()
            elif stype == "link_text":
                self.driver.find_element_by_link_text(value).clear()
            elif stype == "partial_link_text":
                self.driver.find_element_by_partial_link_text(value).clear()
        except Exception as e:
            raise ElementNotFound(e)

    # 验证元素是否存在
    def Check_element(self, stype, value):
        try:
            if stype == "xpath":
                self.driver.find_element_by_xpath(value)
            elif stype == "id":
                self.driver.find_element_by_id(value)
            elif stype == "name":
                self.driver.find_element_by_name(value)
            elif stype == "link_text":
                self.driver.find_element_by_link_text(value)
            elif stype == "partial_link_text":
                self.driver.find_element_by_partial_link_text(value)
        except Exception as e:
            raise ElementNotFound(e)

    # 获取子元素
    def Select_child_elements(self, stype, value1, value2):
        try:
            if stype == "xpath":
                Select(self.driver.find_element_by_xpath(value1)).select_by_visible_text(value2)
            elif stype == "id":
                Select(self.driver.find_element_by_id(value1)).select_by_visible_text(value2)
            elif stype == "name":
                Select(self.driver.find_element_by_name(value1)).select_by_visible_text(value2)
            elif stype == "link_text":
                Select(self.driver.find_element_by_link_text(value1)).select_by_visible_text(value2)
            elif stype == "partial_link_text":
                Select(self.driver.find_element_by_partial_link_text(value1)).select_by_visible_text(value2)
        except Exception as e:
            raise ElementNotFound(e)

    # 获取输入框的值
    def Get_attribute(self, stype, value1, value2):
        try:
            if stype == "xpath":
                Value = self.driver.find_element_by_xpath(value1).get_attribute(value2)
                return Value
            elif stype == "name":
                Value = self.driver.find_element_by_name(value1).get_attribute(value2)
                return Value
            elif stype == "link_text":
                Value = self.driver.find_element_by_link_text(value1).get_attribute(value2)
                return Value
            elif stype == "class_name":
                Value = self.driver.find_element_by_class_name(value1).get_attribute(value2)
                return Value
            elif stype == "id":
                Value = self.driver.find_element_by_id(value1).get_attribute(value2)
                return Value
        except Exception as e:
            raise ElementNotFound(e)

    # 获取下拉框的文本的值
    def Get_text(self, stype, value):
        try:
            if stype == "xpath":
                text = self.driver.find_element_by_xpath(value).text
                return text
            elif stype == "name":
                text = self.driver.find_element_by_name(value).text
                return text
            elif stype == "link_text":
                text = self.driver.find_element_by_link_text(value).text
                return text
            elif stype == "class_name":
                text = self.driver.find_element_by_class_name(value).text
                return text
            elif stype == "id":
                text = self.driver.find_element_by_id(value).text
                return text
        except Exception as e:
            raise ElementNotFound(e)

    # 显性等待时间,注意这里用classname定位元素的，也可以用其他
    def WebDriverWait(self, MaxTime, Mimtime, value):
        # element = self.driver.find_element(By.XPATH, value)
        WebDriverWait(self.driver, MaxTime, Mimtime).until(lambda x: x.find_element_by_xpath(value).is_displayed())

    # # 鼠标移动点击机制
    def Move_action(self, stype, value):
        try:
            if stype == "xpath":
                xm = self.driver.find_element_by_xpath(value)
                webdriver.ActionChains(self.driver).click(xm).perform()
            elif stype == "id":
                xm = self.driver.find_element_by_id(value)
                webdriver.ActionChains(self.driver).click(xm).perform()
            elif stype == "name":
                xm = self.driver.find_element_by_name(value)
                webdriver.ActionChains(self.driver).click(xm).perform()
            elif stype == "link_text":
                xm = self.driver.find_element_by_link_text(value)
                webdriver.ActionChains(self.driver).click(xm).perform()
        except Exception as e:
            raise ElementNotFound(e)

    # 校验按钮是否为选中状态
    def Is_selected(self, stype, value):
        try:
            if stype == "id":
                self.driver.find_element_by_id(value).is_selected()
            elif stype == "xpath":
                self.driver.find_element_by_xpath(value).is_selected()
            elif stype == "class_name":
                self.driver.find_element_by_class_name(value).is_selected()
            elif stype == "name":
                self.driver.find_element_by_name(value).is_selected()
            elif stype == "link_text":
                self.driver.find_element_by_link_text(value).is_selected()
        except Exception as e:
            raise ElementNotFound(e)

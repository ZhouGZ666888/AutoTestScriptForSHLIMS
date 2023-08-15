# -*- coding: utf-8 -*-
# @Time    : 2021/11/11
# @Author  : guanzhong.zhou
# @File    : 样本接收页面功能封装
from datetime import datetime
from openpyxl import load_workbook
from PageElemens.sampleRec_ele import *
from common.editYaml import *
from common.all_path import pathologycheck_file_path, hstq_file_path, sampleprocessing_file_path, \
    wkdl_sr_file_path, sr_sample_imp_file, sr_sample_sublibrary_imp_file, sampledata_path, orderNub_path
from common.screenshot import Screenshot
from common.xlsx_excel import add_write_excel_xlsx
from conf.config import create_lab_excel, specimen_list
from data.execute_sql_action import ybjs_sql, get_sr_sample_lims, set_sr_sample_id_external
from uitestframework.basepageTools import BasePage
from common.logs import log
from uitestframework.exceptionsTools import MyBaseFailure, TimeOutError


class SampleReceivePage(BasePage):
    """
    样本接收类页面基础方法
    """


    def search_order(self):
        """
        查询已存在订单号，对该订单号进行接样
        """
        order = read_yaml(orderNub_path)  # 获取订单号
        log.info('接样页面点击搜索按钮')

        self.click_by_js('css', search_btn)
        self.sleep(0.5)

        log.info('搜索框录入订单号：%s' % order['order_number'])
        self.input('css', order_numb, order['order_number'])
        self.sleep(1)
        self.clicks('css', search_confirm)
        self.sleep(0.5)

        # 这里调用自定义截图方法
        Screenshot(self.driver).get_img("样本接收，根据lims号搜素")

        self.clicks('xpath', chioce_result)
        self.sleep(0.5)
        log.info('选中搜索出的订单，进入样本接收详情页面')
        self.clicks('css', edit_sample_order)
        # 存在进入接样明细缓冲过长，这里加个页面刷新
        try:
            self.wait_loading()
        except TimeOutError as error1:
            log.warning('进入接样详情页面超时，刷新页面。{}'.format(error1))
            self.refresh()
        except MyBaseFailure as error2:
            log.warning('进入接样详情页面报错，刷新页面。{}'.format(error2))
            self.refresh()

    def add_sample_type(self):
        """
        样本接收详情页面，增加样本项目信息
        """

        pro_name = self.get_text('xpath', project_name_chioce)  # 查看项目号是否有值，若没有则重新选择
        if len(pro_name) == 0:
            log.info('选择样本所属项目信息')
            self.clicks('xpath', project_name_chioce)
            self.wait_loading()
            self.input('xpath', project_name_input, 'J022')
            self.sleep(0.5)
            self.clicks('xpath', project_search_button)
            self.wait_loading()
            self.clicks('xpath', chioce_project_result)
            self.wait_loading()
            self.wait_loading()
            self.click_by_js('xpath', back_button)
            self.wait_loading()
            self.sleep(1)

        testitem = self.get_text('xpath', test_item)  # 查看检测产品是否有值，若没有则重新选择
        log.info('选择样本所属检测产品')
        if len(testitem) == 0:
            self.clicks('xpath', test_item)
            self.wait_loading()
            self.input('xpath', product_input, '世和一号')
            self.clicks('xpath', product_search_btn)

            self.clicks('xpath', open_product)
            self.clicks('xpath', choice_product)
            self.sleep(0.5)
            if self.isElementExists('css',tipInfo):
                self.clicks('css',tipInfo)
            self.wait_loading()
            self.wait_loading()
            self.clicks('xpath', close_button)
            self.sleep(1)

    def chioce_specimen(self, specimenList):
        """
        封装选择样本类型方法
        """
        self.sleep(0.5)
        # 样本类型选择按钮，元素定位
        self.clicks('xpath', sample_TypeName)
        self.wait_loading()
        # 样本类型选项弹框，查询录入文本框
        self.input('xpath', original_specimen_type, specimenList)
        print('选择样本类型：', specimenList)
        self.sleep(0.5)

        self.clicks('xpath', search_type_button)
        log.info('输入样本类型，点击查询按钮，进行检索')
        # print(ele)
        self.wait_loading()
        self.clicks('xpath', chioce_search_result)
        # print('选中')
        self.sleep(0.5)
        self.clicks('xpath', specimen_type_comfirm)
        self.sleep(0.5)

    def sampleRec_sampleDetail(self):
        """
        新增五种样本并选择样本类型：
        FF白片
        ED抗凝血
        骨冷冻组织
        DNA文库
        外部血浆
        """
        log.info('添加5种样本，')

        total = specimen_list.values()
        n = 0
        for d in total:
            n += d
        # 新增样本
        s = 0
        while s < n:
            self.clicks('xpath', add_sample)
            print('新增第', s + 1, "条样本")
            self.wait_loading()
            s += 1
        lists = self.findelements('xpath', all_samples)
        # 添加样本类型
        if lists:
            tips = 0
            for s_type, num in specimen_list.items():  # 从字典取值，样本类型以及对应的要添加的数量
                if s_type == 'FFPE白片':  # 跟据取值依次判断
                    for i in range(tips, tips + num):  # 样本类型数量，循环选中多少数量的样本
                        j = i + 1
                        self.clicks('css', one_by_one_samples.format(j))  # 先选中对应样本
                    self.chioce_specimen(s_type)  # 执行添加样本类型方法
                    self.sleep(1)
                    self.moved_to_element('css', add_pathology_worksheet)  # 移动鼠标至病理任务，添加HE任务
                    self.sleep(1.5)
                    self.clicks('xpath', pathology_worksheet_HE)
                    s = self.get_text('xpath', pathology_worksheet_HE)

                    print(s)
                    self.wait_loading()
                    self.sleep(1)
                    for i in range(tips, tips + num):
                        j = i + 1
                        self.clicks('css', one_by_one_samples.format(j))
                        self.sleep(0.2)
                    self.moved_to_element('css', add_pathology_worksheet)  # 移动鼠标至病理任务，添加HE任务
                    self.sleep(1)
                    self.click_by_js('xpath', pathology_worksheet_PD)
                    s = self.get_text('xpath', pathology_worksheet_PD)
                    print(s)
                    self.wait_loading()
                    self.sleep(1)
                    print('添加病理成功')

                elif s_type == 'EDTA抗凝血':
                    for i in range(tips, tips + num):
                        j = i + 1
                        self.click_by_js('css', one_by_one_samples.format(j))  # 先选中对应样本
                        self.sleep(0.5)
                    self.chioce_specimen(s_type)
                    for i in range(tips, tips + num):
                        j = i + 1
                        self.click_by_js('css', one_by_one_samples.format(j))
                    self.sleep(1)
                elif s_type == '骨冷冻组织':
                    for i in range(tips, tips + num):
                        j = i + 1
                        self.click_by_js('css', one_by_one_samples.format(j))  # 先选中对应样本
                    self.chioce_specimen(s_type)
                    for i in range(tips, tips + num):
                        j = i + 1
                        self.click_by_js('css', one_by_one_samples.format(j))
                    self.sleep(1)
                elif s_type == 'DNA文库':
                    for i in range(tips, tips + num):
                        j = i + 1
                        self.click_by_js('css', one_by_one_samples.format(j))  # 先选中对应样本
                    self.chioce_specimen(s_type)
                    for i in range(tips, tips + num):
                        j = i + 1
                        self.click_by_js('css', one_by_one_samples.format(j))
                    self.sleep(1)
                elif s_type == '外部血浆':
                    for i in range(tips, tips + num):
                        j = i + 1
                        self.click_by_js('css', one_by_one_samples.format(j))  # 先选中对应样本
                    self.chioce_specimen(s_type)
                    for i in range(tips, tips + num):
                        j = i + 1
                        self.click_by_js('css', one_by_one_samples.format(j))
                    self.sleep(1)
                tips += num  # 每次循环取不同样本，所以各样本数量相加，取其排序下标，在页面中根据对应下标进行定位

        self.sleep(1)
        self.clicks('css', save_btn)
        self.wait_loading()

        # 这里调用自定义截图方法
        Screenshot(self.driver).get_img("样本样本接收，保存新增样本")

    def generate_laboratory_process(self):
        """
        样本接收-样本明细(未审核),选择样本并生成实验流程，对应的样本与实验流程关系.实验流程需要和上一步样本类型一致
        FF白片——核酸提取-不破碎；
        ED抗凝血-体液样本分离；
        骨冷冻组织-21基因；
        DNA文库-文库定量；
        """

        # laboratory_pro = ['核酸提取-破碎', '样本处理-样本分离', '21基因', '文库定量']
        log.info('选中样本生成实验流程')
        self.clicks('css', all_chioce)  # 全选样本
        self.sleep(1)
        self.clicks('xpath', generateLibProcessVisible)  # 点击生成实验流程
        self.wait_loading()
        self.sleep(0.5)

        # 这里调用自定义截图方法
        Screenshot(self.driver).get_img("样本接收，点击生成实验流程")

        lists = self.findelements('xpath', template_sample_all)  # 实验流程弹框中，全部样本数量

        if lists:
            for s_type, num in specimen_list.items():  # 取出样本类型及其数量
                if s_type == 'FFPE白片':  # 判断从列表循环取出本的类型
                    for i in range(len(lists)):  # 从所有存在于实验流程弹框中的样本，根据样本类型值，与列表取值进行比对
                        j = i + 1
                        specimen_type = self.get_text('xpath', template_sample_type.format(j))
                        if specimen_type == 'FFPE白片':  # 如果页面列表中，样本类型值与列表循环出的一致，则在页面弹框选中
                            self.clicks('xpath', one_by_one_chioce_sample.format(j))  # 先选中对应样本
                    self.clicks('xpath', laboratory_process_temp_btn)  # 点击选择实验流程按钮
                    ele = LibProcessVisible.format('核酸提取-破碎')  # 选中样本类型对应的实验流程
                    self.clicks('xpath', ele)
                    print("选中")
                    self.sleep(0.5)
                    self.clicks('xpath', LibProcessVisible_btn)  # 选择实验流程弹框确认按钮
                    self.sleep(0.5)
                    self.clicks('xpath', laboratory_process_planned_btn)  # 选择探针
                    self.sleep(0.5)
                    self.clicks('xpath', laboratory_process_planned_chioce)
                    self.sleep(0.5)
                    self.clicks('xpath', laboratory_process_planned_comfirm)
                    self.sleep(0.5)
                    # 把前面已完成操作的样本进行取消选中，接下来选中其它类型的样本
                    for i in range(len(lists)):
                        j = i + 1
                        specimen_type = self.get_text('xpath', template_sample_type.format(j))
                        if specimen_type == 'FFPE白片':
                            self.clicks('xpath', one_by_one_chioce_sample.format(j))

                elif s_type == 'EDTA抗凝血':
                    for i in range(len(lists)):
                        j = i + 1
                        specimen_type = self.get_text('xpath', template_sample_type.format(j))
                        if specimen_type == 'EDTA抗凝血':
                            self.clicks('xpath', one_by_one_chioce_sample.format(j))  # 先选中对应样本
                    self.clicks('xpath', laboratory_process_temp_btn)
                    ele = LibProcessVisible.format('样本处理-样本分离')
                    self.clicks('xpath', ele)
                    print("选中")
                    self.sleep(0.5)
                    self.clicks('xpath', LibProcessVisible_btn)
                    self.sleep(0.5)
                    self.clicks('xpath', laboratory_process_planned_btn)
                    self.sleep(0.5)
                    self.clicks('xpath', laboratory_process_planned_chioce)
                    self.sleep(0.5)
                    self.clicks('xpath', laboratory_process_planned_comfirm)
                    self.sleep(0.5)
                    for i in range(len(lists)):
                        j = i + 1
                        specimen_type = self.get_text('xpath', template_sample_type.format(j))
                        if specimen_type == 'EDTA抗凝血':
                            self.clicks('xpath', one_by_one_chioce_sample.format(j))
                elif s_type == '骨冷冻组织':
                    for i in range(len(lists)):
                        j = i + 1
                        specimen_type = self.get_text('xpath', template_sample_type.format(j))
                        if specimen_type == '骨冷冻组织':
                            self.clicks('xpath', one_by_one_chioce_sample.format(j))
                    self.clicks('xpath', laboratory_process_temp_btn)
                    self.clicks('xpath', LibProcessVisible.format('21基因'))
                    print("选中")
                    self.sleep(0.5)
                    self.clicks('xpath', LibProcessVisible_btn)
                    self.sleep(0.5)
                    for i in range(len(lists)):
                        j = i + 1
                        specimen_type = self.get_text('xpath', template_sample_type.format(j))
                        if specimen_type == '骨冷冻组织':
                            self.clicks('xpath', one_by_one_chioce_sample.format(j))

                elif s_type == 'DNA文库':
                    # 选中
                    for i in range(len(lists)):
                        j = i + 1
                        specimen_type = self.get_text('xpath', template_sample_type.format(j))
                        if specimen_type == 'DNA文库':
                            self.clicks('xpath', one_by_one_chioce_sample.format(j))
                    self.clicks('xpath', laboratory_process_temp_btn)
                    ele = LibProcessVisible.format('文库定量')
                    self.clicks('xpath', ele)
                    print("选中")
                    self.sleep(0.5)
                    self.clicks('xpath', LibProcessVisible_btn)
                    self.sleep(0.5)
                    # 取消选中
                    for i in range(len(lists)):
                        j = i + 1
                        specimen_type = self.get_text('xpath', template_sample_type.format(j))
                        if specimen_type == 'DNA文库':
                            self.clicks('xpath', one_by_one_chioce_sample.format(j))


                elif s_type == '外部血浆':
                    # 选中
                    for i in range(len(lists)):
                        j = i + 1
                        specimen_type = self.get_text('xpath', template_sample_type.format(j))
                        if specimen_type == '外部血浆':
                            self.clicks('xpath', one_by_one_chioce_sample.format(j))
                    self.clicks('xpath', laboratory_process_temp_btn)
                    ele = LibProcessVisible.format('提取-质谱仪上机')
                    self.clicks('xpath', ele)
                    print("选中")
                    self.sleep(0.5)
                    self.clicks('xpath', LibProcessVisible_btn)
                    self.sleep(0.5)
                    # 取消选中
                    for i in range(len(lists)):
                        j = i + 1
                        specimen_type = self.get_text('xpath', template_sample_type.format(j))
                        if specimen_type == '外部血浆':
                            self.clicks('xpath', one_by_one_chioce_sample.format(j))

        # 获取当前窗口句柄
        now_handle = self.get_current_window_handle()
        print('获取当前窗口句柄', now_handle)

        # 点击生成实验流程，等待打开新的实验流程页面
        self.clicks('xpath', generatelaboratoryprocess_btn)
        self.wait_loading()
        self.sleep(2)
        # 获取所有窗口句柄
        all_handles = self.get_all_windows()
        for handle in all_handles:
            if handle != now_handle:
                # 切换到新窗口句柄，即新打开的流转表页面
                self.switch_to_window(handle)
                self.sleep(2)
                # 关闭新窗口句柄，关闭流转表页面
                self.close()
        self.sleep(1.5)
        # 切换到旧窗口句柄，回到原页面
        self.switch_to_window(now_handle)
        self.sleep(1)

    def save_all_samples_excel(self):
        """
        把所有样本信息保存到Excel中
        """
        create_lab_excel()
        lists = self.findelements('xpath', all_samples)

        for i in range(1, len(lists) + 1):
            lims_list_values = []
            samples_type = self.get_text('xpath', one_sample_type.format(i))
            self.sleep(0.5)
            if samples_type == "FFPE白片":
                data1 = []
                sample_lims = self.get_text('xpath', one_lims_num.format(i))
                data1.append(sample_lims)
                lims_list_values.append(data1)
                add_write_excel_xlsx(pathologycheck_file_path, lims_list_values)
                add_write_excel_xlsx(hstq_file_path, lims_list_values)

            elif samples_type == "EDTA抗凝血":
                data2 = []
                sample_lims = self.get_text('xpath', one_lims_num.format(i))
                sample_lab = self.get_text('xpath', one_laboratory_num.format(i))  # 实验室号
                data2.append(sample_lims)
                data2.append(sample_lab)
                lims_list_values.append(data2)
                add_write_excel_xlsx(sampleprocessing_file_path, lims_list_values)

            elif samples_type == "骨冷冻组织":
                data3 = []
                sample_lims = self.get_text('xpath', one_lims_num.format(i))  # lism号
                sample_lab = self.get_text('xpath', one_laboratory_num.format(i))  # 实验室号
                data3.append(sample_lims)
                data3.append(sample_lab)
                lims_list_values.append(data3)
                add_write_excel_xlsx(hstq_file_path, lims_list_values)

            elif samples_type == "DNA文库":
                data4 = []
                sample_lims = self.get_text('xpath', one_lims_num.format(i))
                data4.append(sample_lims)
                lims_list_values.append(data4)
                add_write_excel_xlsx(wkdl_sr_file_path, lims_list_values)

            elif samples_type == "外部血浆":
                data5 = []
                sample_lims = self.get_text('xpath', one_lims_num.format(i))  # lism号
                sample_lab = self.get_text('xpath', one_laboratory_num.format(i))  # 实验室号
                data5.append(sample_lims)
                data5.append(sample_lab)
                lims_list_values.append(data5)
                add_write_excel_xlsx(hstq_file_path, lims_list_values)

    def input_sampleamt(self):
        """
        录入样本包装量和样本计量
        """
        log.info('录入样本包装量')

        self.clicks('css', all_chioce)
        self.sleep(0.5)
        self.clicks('xpath', sample_PkgAmt)
        self.input('xpath', sample_PkgAmt_input, 1)
        self.clicks('xpath', sample_PkgAmt_input_comfirm_btn)
        self.sleep(0.5)

        log.info('录入样本计量')
        self.clicks('xpath', sample_amt)
        self.input('xpath', sample_amt_input, 20)
        self.clicks('xpath', sample_amt_input_comfirm_btn)
        self.sleep(0.5)

        # 准备sr样本数据
        self.sr_sample_import()

        log.info('录入样本基本数据后，样本信息保存')
        self.clicks('css', save_btn)
        self.wait_loading()
        self.refresh()

    def sr_sample_import(self):
        """
        准备sr样本数据，在sr信息登记模块使用。选取一条sr样本，设置sr样本的外部样本编号，并存入对应的导入模板
        """
        order = read_yaml(orderNub_path)  # 获取订单号
        log.info('录入样本备注')

        self.updata_sql(ybjs_sql.format(order['order_number']))
        log.info('录入一条sr样本的外部样本编号')
        now_time = datetime.now()
        sr_sample_id_external = now_time.strftime('%Y%m%d%H%M') + '_TEST_SR'  # 按时间规则生成外部样本编号

        log.info('把样本外部编号写入SR样本信息导入模板')
        wb = load_workbook(filename=sr_sample_imp_file)  # 打开excel文件
        ws = wb.active
        ws.cell(2, 2, sr_sample_id_external)  # 修改第k行，第index列值
        wb.save(sr_sample_imp_file)

        log.info('把样本外部编号写入SR样本子文库导入模板')
        wb = load_workbook(filename=sr_sample_sublibrary_imp_file)  # 打开excel文件
        ws = wb.active
        ws.cell(2, 1, sr_sample_id_external)  # 修改第k行，第index列值
        wb.save(sr_sample_sublibrary_imp_file)

        # 数据库先获取一条sr样本的lims号，再根据lims号在数据库设置外部样本编号
        sr_sample_nubs = self.select_sql(get_sr_sample_lims.format(order['order_number']))
        sr_sample_nub = [list(i.values()) for i in sr_sample_nubs]
        print('选中的SR样本：', sr_sample_nub[0][0])
        self.updata_sql(set_sr_sample_id_external.format(sr_sample_id_external, sr_sample_nub[0][0]))

        # 将修改后的sr样本的lims号，存到临时文件，在SR样本信息登记模块使用
        datas = read_yaml(sampledata_path)
        datas["rec_sr_sample_for_sr_import"] = sr_sample_nub[0][0]
        with open(sampledata_path, 'w', encoding='utf-8') as fs:  # 写入模式
            yaml.safe_dump(datas, fs, allow_unicode=True)

    def submit_sample_for_review(self):
        """
        对样本进行批量提交审核
        """
        log.info('选中样本，点击批量提交审核')
        self.clicks('css', all_chioce)
        self.sleep(0.5)
        self.clicks('css', batch_submit_for_review)
        self.wait_loading()
        self.sleep(2)

    def get_save_info(self):
        """
        获取数据操作后，页面给出的提示信息语
        Submit successfully
        review successfully
        """
        log.info('获取页面提示信息')
        if self.isElementExists('css', save_info):
            return self.get_text('css', save_info)
        else:
            return None

    # 切换登录用户进行审核
    def batch_submit_for_review(self):
        """
        切换登录用户进行审核
        """
        log.info('点击页面退出登录按钮，切换登录用户')
        self.click_by_js('css', logout_btn)
        self.sleep(1)
        self.click_by_js('xpath', logout_choice)
        self.sleep(1)

    def batch_review(self):
        """
        切换待审核页面，查看待审核样本，并进行样本审核
        """
        log.info('登录后，切换到样本待审核页面')
        self.clicks('xpath', review_pending)
        self.wait_loading()
        self.sleep(1)
        log.info('待审核页面选中待审核样本，并点击批量审核按钮')
        # 全选样本数据
        self.clicks('xpath', review_all_chioce)
        self.sleep(1)
        # 点击批量完成审核按钮
        self.clicks('xpath', batch_checked_for_review)
        self.sleep(0.5)

        # 这里调用自定义截图方法
        Screenshot(self.driver).get_img("样本接收，审核页面")

        # 弹出框录入用户密码
        self.input('xpath', password_inpt, 1)
        # 点击下一步
        self.clicks('xpath', next_step)
        # 弹出框录入审核理由
        self.input('xpath', review_remarks, '测试')
        # 点击提交
        self.clicks('xpath', review_confirm)

        self.wait_loading()

    # def set_estimated_generated_time(self,predata):
    #     """
    #     接样审核通过后，需要在流转表设置富集预计生成时间，这样可以不做实验流程直接到报告基本信息任务分配页面，同步到数据
    #     predata:调用时需要传入日期数值
    #     """
    #     lims_id1 = []
    #     lims_id2 = []
    #     lims_nub1 = read_excel_xlsx_list_col(all_path.sampleprocessing_file_path, 0, 'lims号')
    #     lims_nub2 = read_excel_xlsx_list_col(all_path.hstq_file_path, 0, 'lims号')
    #     for i in lims_nub1:
    #         lims_id1.append(i[0])
    #     for i in lims_nub2:
    #         lims_id2.append(i[0])
    #     lims_id_str1 = "\n".join(lims_id1)
    #     lims_id_str2 = "\n".join(lims_id2)
    #     all_lims_id = lims_id_str1 + "\n" + lims_id_str2
    #
    #     print(all_lims_id)
    #
    #     self.clicks('css', sample_search_button)#点击搜索按钮
    #     self.sleep(1)
    #     self.clicks('css', search_lims_code)  # 点击订单号输入框
    #     self.sleep(0.5)
    #     self.clicks('css', search_order_code_text)  # 点击右侧弹出的输入框
    #     self.sleep(0.5)
    #     self.input('css', search_order_code_text,all_lims_id)  # 右侧输入框输入订单号
    #     self.sleep(0.5)
    #     self.clicks('css', search_order_code_confirm)  # 右侧点击确定按钮
    #     self.sleep(1)
    #     self.clicks('css', lzb_search_confirm)  # 点击最外层的确定按钮
    #     self.wait_loading()#等待搜索完毕
    #
    #     self.clicks('xpath', poolling_check_box)  # 全选富集节点的复选框
    #     self.sleep(2)
    #     self.clicks('css', modify_pretime_button)  # 点击【修改预计生成时间】按钮
    #     self.wait_loading()
    #     self.sleep(1)
    #     self.input('css', modify_pretime_value,predata)  # 输入日期
    #     self.sleep(1)
    #     self.clicks('css', modify_pretime_confirm)  # 点击确定
    #
    #     self.wait_loading()#等待搜索完毕
    #     self.sleep(1)

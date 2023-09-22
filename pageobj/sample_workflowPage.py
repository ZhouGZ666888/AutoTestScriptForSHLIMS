# -*- coding: utf-8 -*-
# @Time    : 2021/11/25
# @Author  : guoqi.dong
# 流转表方法功能封装
from common import editYaml
from common.all_path import  samplereceive_file_path, orderNub_path
from common.screenshot import Screenshot
from common.DataBaseConfig import executeSql
from common.xlsx_excel import read_excel_col
from PageElemens.sample_workflow_ele import *
from uitestframework.basepageTools import BasePage
from common.logs import log


class SampleWorkflowPage(BasePage):
    """
    以下是针对单样本流转表的一些列操作，详情见方法说明
    """

    def workflow_search_sample(self, sample_lims_id):
        """
        将在单样本流转表搜索样本的方法提取出来
        """
        log.info("点击样本筛选按钮")
        self.clicks('xpath', workflow_samplesearch)
        self.sleep(0.5)
        log.info("点击LIMS号输入框")
        self.clicks('xpath', workflow_samplesearch_sample)
        self.sleep(0.5)
        log.info("右侧弹框打开后，点击输入框")
        self.clicks('xpath', workflow_samplesearch_sample_value)
        self.sleep(0.5)
        log.info("输入框输入指定LIMS号")
        self.clicks('xpath', workflow_samplesearch_sample_value)
        self.sleep(0.5)
        self.input('xpath', workflow_samplesearch_sample_value, sample_lims_id)

        # 这里调用自定义截图方法
        Screenshot(self.driver).get_img("点击流转表检索弹框，在lims号文本框中录入样本lims好，点击搜索","根据样本lims号检索出结果")

        self.sleep(0.5)
        log.info("点击确定按钮")
        self.clicks('xpath', sample_confirm)
        self.sleep(0.5)
        log.info("点击最外层的确认按钮")
        self.clicks('xpath', search_sample_confirm)
        log.info("流转表LIMS号检索成功")
        self.wait_loading()

    def workflow_search_order(self):
        """
        在流转表搜索订单号
        """
        order = editYaml.read_yaml(orderNub_path)

        log.info("点击样本筛选按钮")
        self.clicks('xpath', workflow_samplesearch)
        self.sleep(0.5)
        log.info("点击订单号输入框")
        self.clicks('xpath', workflow_samplesearch_order)
        self.sleep(0.5)
        log.info("右侧弹框打开后，点击输入框")
        self.clicks('xpath', workflow_samplesearch_order_value)
        self.sleep(0.5)
        log.info("输入框输入指定订单号")
        self.clicks('xpath', workflow_samplesearch_order_value)
        self.sleep(1)
        self.input('xpath', workflow_samplesearch_order_value, order['order_number'])
        self.sleep(0.5)
        log.info("点击确定按钮")
        self.clicks('xpath', order_confirm)
        self.sleep(0.5)
        log.info("点击最外层的确认按钮")
        self.clicks('xpath', search_order_confirm)
        log.info("流转表订单号检索成功")
        self.wait_loading()

    def workflow_search_samplelimsid(self, sql):
        """
        在流转表搜索订单号
        """

        ret = executeSql.test_select_limsdb(sql)  # 我们只取sql查询结果的第一个
        # print(sql)
        print("查询结果为:" + str(ret[0]))
        if len(ret) == 0:
            sample_lims_id = 'null'
            print("当前系统中没有可以操作的数据，请检查")
        else:
            first_ret = ret[0]
            sample_lims_id = first_ret['sampleidlims']  # lims号
            # sample_lab = (ret['sampleidlab'].split('-'))[0]  # 实验室号第一部分
            print("lims号为:" + str(sample_lims_id))
            # print("实验室号第一部分为:" + str(sample_lab))
            self.sleep(1)

            self.workflow_search_sample(sample_lims_id)  # 调用封装的流转表搜索样本的方法

        return sample_lims_id

    def workflow_search_samplelab(self, sql):
        """
        在流转表搜索订单号
        """
        ret = executeSql.test_select_limsdb(sql)[0]  # 我们只取sql查询结果的第一个
        print("查询结果为:" + str(ret))
        # sample_lims_id=ret['sampleidlims']#lims号
        sample_lab = (ret['sampleidlab'].split('-'))[0]  # 实验室号第一部分
        # print("lims号为:"+str(sample_lims_id))
        print("实验室号第一部分为:" + str(sample_lab))
        self.sleep(1)

        self.workflow_search_sample(sample_lab)  # 调用封装的流转表搜索样本的方法

    def workflow_set_pathology(self, sql):
        """
        在流转表设置病理任务
        """
        sample_lims_id = self.workflow_search_samplelimsid(sql)  # 将sql查询的结果拿到
        print(sample_lims_id[0])

        if sample_lims_id == 'null':
            print('当前系统没有可用的接样节点样本，来设置病理任务')
        else:
            log.info("全选接样节点样本")
            self.clicks('xpath', get_ybjs_allcheckbox)
            self.sleep(0.5)
            log.info("点击【设置病理任务】")
            if get_ybjs_allcheckbox:
                print("元素可见，点击按钮")
                self.clicks('xpath', set_blrw_button)
                self.sleep(0.5)

                log.info("点击【添加】按钮，当前需要设置病理任务")
                self.clicks('xpath', set_blrw_add)
                self.sleep(0.5)
                log.info("点击【任务类型】按钮")
                self.clicks('xpath', set_blrw_type)
                self.sleep(0.5)
                log.info("点击【任务类型】按钮的下拉框")
                self.clicks('xpath', set_blrw_select_type)
                self.sleep(2)
                log.info("选择HE选项")
                print(set_blrw_select_type_value)
                get_ele = self.isElementExists('css', set_blrw_select_type_value)
                if get_ele:
                    print(get_ele)
                    self.clicks('css', set_blrw_select_type_value)
                    self.sleep(2)
                    log.info("点击【保存修改】按钮")
                    self.clicks('xpath', set_blrw_save)
                    self.sleep(0.5)
                    log.info("设置完成")
                    self.wait_loading()
                else:
                    pass

            else:
                print("元素不可见")

    def workflow_fg(self, sql):
        """
        在流转表分管操作，以在样本处理节点分管为例
        """
        sample_lims_id = self.workflow_search_samplelimsid(sql)  # 将sql查询的结果拿到
        print(sample_lims_id[0])
        self.sleep(2)
        update_sql = 'UPDATE sample_info_t SET divided_original_lims_id=NULL WHERE original_sample_id_lims IN (' + "'" + sample_lims_id + "'" + ')'
        # 将查询出的原始样本后续的分管样本设置为可再分管，否则有的分管无法进行
        print(update_sql)
        executeSql.test_updateByParam(update_sql)

        if sample_lims_id == 'null':
            print('样本处理节点分管操作，当前系统没有可用的样本')
        else:
            log.info("全选处理节点样本")
            self.clicks('xpath', get_ybcl_allcheckbox)
            self.sleep(1)
            log.info("点击【产物分管】")
            if get_ybcl_allcheckbox:
                print("元素可见，点击按钮")
                self.clicks('xpath', sample_fg_button)
                self.wait_loading()
                self.sleep(0.5)
                log.info("选择样本数量，点击下一步")
                self.clicks('xpath', sample_fg_num)
                self.sleep(1)
                log.info("全选样本")
                self.clicks('xpath', sample_fg_allcheckbox)
                self.sleep(0.5)
                log.info("点击最后步骤按钮")
                self.clicks('xpath', sample_fg_laststep)
                self.sleep(1)
                log.info("选择样最后步骤")
                self.clicks('xpath', sample_fg_laststep_value)
                self.sleep(1)
                log.info("点击确定")
                self.clicks('css', sample_fg_laststep_confirm)
                self.sleep(1)
                log.info("点击修改项目信息")
                self.clicks('xpath', sample_fg_modify_project)
                self.sleep(1)
                log.info("勾选项目复选框")
                self.clicks('xpath', sample_fg_modify_project_value)
                self.sleep(1)
                log.info("点击确定")
                self.clicks('css', sample_fg_modify_project_confrim)
                self.sleep(1)
                log.info("点击分管弹框最外层的确定按钮")
                self.clicks('css', sample_fg_confirm)
                self.sleep(1)
                log.info("分管成功")
                self.wait_loading()


            else:
                print("元素不可见")

    def workflow_ck(self, sql):
        """
        在流转表对数据，出库
        """
        sample_nub = read_excel_col(samplereceive_file_path, 'lims号')  # 读出样本审核通过对应的样本号
        sample_nub = tuple(sample_nub)  # 处理数据[['GS2112270002'], ['GS2112270003']]类型的数据，转成(
        # 'GS2112270002', 'GS2112270003')格式
        # print('从文本读出的数据为：'+str(order_nub))

        getSampleLimsId = executeSql.test_select_limsdb(sql.format(sample_nub))  # 将sql查询的结果拿到
        print("从实验中心读取到的接样节点入库样本为：" + str(getSampleLimsId))
        self.sleep(1)

        if not getSampleLimsId:
            print('当前系统没有可用的样本')
        else:
            self.workflow_search_sample(getSampleLimsId[0]['sample_id_lims'])  # 调用封装的流转表搜索样本的方法
            self.sleep(1)
            log.info("全选接样节点样本")
            self.clicks('xpath', get_ybjs_allcheckbox)
            self.sleep(1)
            log.info("点击【样本出库】")
            self.clicks('xpath', sample_ck_button)
            self.sleep(0.5)

            # 这里调用自定义截图方法
            Screenshot(self.driver).get_img("在流转表对数据，出库")

            log.info("全选样本")
            self.clicks('xpath', sample_ck_allcheckbox)

            # 出库成功后，校验系统中是否存在该出库任务单
            # SELECT t.task_id FROM sample_withdraw_item_t t WHERE t.sample_id_lims IN ('PA1903060071')

    def workflow_update_wkgj_wkfj(self, sql, libtype):
        """
        在流转表对数据，做修改【建库+富集】信息的操作
        """
        getSampleLimsId = executeSql.test_select_limsdb(sql)  # 将sql查询的结果拿到
        print("可以修改建库信息的样本为：" + str(getSampleLimsId[0]))
        self.sleep(2)

        if not getSampleLimsId:
            print('当前系统没有可用的样本')
        else:
            # -------------------修改建库信息-------------------
            self.workflow_search_sample(getSampleLimsId[0]['original_sample_id_lims'])  # 调用封装的流转表搜索样本的方法
            self.sleep(1)
            log.info("全选建库节点样本")
            self.clicks('xpath', get_wkgj_allcheckbox)
            self.sleep(1)
            log.info("点击【修改建库信息】")
            self.clicks('xpath', update_wkgj_data_button)
            self.sleep(1)
            log.info("全选样本")
            self.clicks('css', update_wkgj_data_allcheckbox)
            self.sleep(1)
            log.info("点击【批量建库类型】")
            self.clicks('css', update_wkgj_data_libtype)
            self.wait_loading()
            log.info("选择指定建库类型")
            self.clicks('xpath', update_wkgj_data_libtype_value.format(libtype))
            self.sleep(1)
            log.info("点击【修改建库备注】")
            self.clicks('xpath', update_wkgj_data_remarks)
            self.sleep(1)
            log.info("输入框内输入备注信息")
            self.clicks('xpath', update_wkgj_data_remarks_value)
            self.sleep(1)
            self.input('xpath', update_wkgj_data_remarks_value, '董国奇修改建库备注信息')
            self.sleep(1)
            log.info("点击确定按钮")
            self.clicks('xpath', update_wkgj_data_remarks_confirm)
            self.sleep(1)
            log.info("点击保存修改按钮")
            self.clicks('xpath', update_wkgj_data_confirm)
            self.sleep(1)
            # -------------------修改富集信息-------------------
            log.info("点击【取消选中】按钮，开始修改富集信息环节")
            self.clicks('xpath', cancel_all_check)
            self.sleep(2)
            log.info("勾选富集样本复选框")
            self.clicks('xpath', get_wkfj_allcheckbox)
            self.sleep(1)
            log.info("点击【修改富集信息】按钮")
            self.clicks('xpath', update_wkfj_data_button)
            self.wait_loading()
            log.info("全选样本复选框")
            self.clicks('css', update_wkfj_data_allcheckbox)
            self.sleep(1)
            log.info("点击【批量修改通量】")
            self.clicks('xpath', update_wkfj_thought)
            self.sleep(1)
            log.info("输入数据")
            self.clicks('xpath', update_wkfj_thought_value)
            self.sleep(1)
            self.input('xpath', update_wkfj_thought_value, '25.6')
            self.sleep(1)
            log.info("点击确定")
            self.clicks('xpath', update_wkfj_thought_confirm)
            self.sleep(1)
            log.info("点击【批量修改预设探针】按钮")
            self.clicks('xpath', update_wkfj_prob)
            self.sleep(1)
            log.info("选择第一个探针")
            self.clicks('xpath', update_wkfj_prob_value)
            self.sleep(1)
            log.info("点击确定按钮")
            self.clicks('xpath', update_wkfj_prob_confirm)
            self.sleep(1)
            log.info("点击保存全部按钮")
            self.clicks('xpath', update_wkfj_confirm)
            self.wait_loading()

    def mixed_workflow_wkfj(self, sql):
        """
        在富集混合样本搜索指定样本
        """
        getSampleLimsId = executeSql.test_select_limsdb(sql)  # 将sql查询的结果拿到
        print("可以使用的样本为：" + str(getSampleLimsId[0]))
        self.sleep(2)

        if not getSampleLimsId:
            print('当前系统没有可用的样本')
        else:
            log.info("点击【样本筛选】按钮")
            self.clicks('xpath', wkfj_workflow_search)
            self.sleep(1)
            log.info("点击LIMS输入框")
            self.clicks('xpath', wkfj_workflow_search_lims)
            self.sleep(1)
            log.info("输入指定数据")
            self.clicks('xpath', wkfj_workflow_search_lims_value)
            self.sleep(0.5)
            self.input('xpath', wkfj_workflow_search_lims_value, getSampleLimsId[0]['sample_id_lims'])
            self.sleep(0.5)
            log.info("点击确定按钮")
            self.clicks('xpath', wkfj_workflow_search_lims_confirm)
            self.sleep(0.5)
            log.info("点击最外层的确定按钮")
            self.clicks('xpath', wkfj_workflow_search_confirm)
            self.wait_loading()

    def mixed_workflow_wkdl(self, sql):
        """
        在定量混合样本搜索指定样本
        """
        getSampleLimsId = executeSql.test_select_limsdb(sql)  # 将sql查询的结果拿到
        print("可以使用的样本为：" + str(getSampleLimsId[0]))
        self.sleep(2)

        if not getSampleLimsId:
            print('当前系统没有可用的样本')
        else:
            log.info("点击【样本筛选】按钮")
            self.clicks('xpath', wkfj_workflow_search)
            self.sleep(1)
            log.info("点击LIMS输入框")
            self.clicks('xpath', wkfj_workflow_search_lims)
            self.sleep(1)
            log.info("输入指定数据")
            self.clicks('xpath', wkfj_workflow_search_lims_value)
            self.sleep(0.5)
            self.input('xpath', wkfj_workflow_search_lims_value, getSampleLimsId[0]['sample_id_lims'])
            self.sleep(0.5)
            log.info("点击确定按钮")
            self.clicks('xpath', wkfj_workflow_search_lims_confirm)
            self.sleep(0.5)
            log.info("点击最外层的确定按钮")
            self.clicks('xpath', wkfj_workflow_search_confirm)
            self.wait_loading()


if __name__ == '__main__':
    get_sql5 = """SELECT t.sample_id_lims FROM sample_info_t t WHERE t.sample_id_lims LIKE 'FJ%' AND t.sample_status ='01' AND workflow_status ='01'"""
    test = SampleWorkflowPage(BasePage)
    test.mixed_workflow_wkfj(get_sql5)

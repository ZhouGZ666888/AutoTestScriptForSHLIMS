# -*- coding: utf-8 -*-
# @Time    : 2021/11/25
# @Author  : guoqi.dong
# 样本出库页面方法封装
from common.screenshot import Screenshot
from common.DataBaseConfig import executeSql
from PageElemens.ybck_ele import *
from uitestframework.basepageTools import BasePage
from common.logs import log


class GetSampleCK(BasePage):
    """
    以下是针对样本出库的一些列操作，详情见方法说明
    """

    def sample_ck_search(self, sql):
        """
        出库列表搜索
        """
        getSampleLimsId = executeSql.test_select_limsdb(sql)  # 将sql查询的结果拿到
        print("可以使用的样本为：" + str(getSampleLimsId[0]['sample_id_lims']))
        self.sleep(2)

        if not getSampleLimsId:
            log.error('当前系统没有可用的样本')
        else:
            log.info("点击样本筛选按钮")
            self.clicks('xpath', sample_ck_search)
            self.sleep(0.5)
            log.info("点击LIMS号输入框")
            self.clicks('xpath', sample_ck_search_value)
            self.sleep(0.5)

            # 这里调用自定义截图方法
            Screenshot(self.driver).get_img("样本出库根据lims号搜索")

            log.info("输入指定样本号")
            self.input('xpath', sample_ck_search_value, getSampleLimsId[0]['sample_id_lims'])
            self.sleep(0.5)
            log.info("点击确定按钮")
            self.clicks('xpath', sample_ck_search_confirm)
            self.wait_loading()

    def samplereceive_ck(self, sql):
        """
        对接样样本出库
        """
        getSampleLimsId = executeSql.test_select_limsdb(sql)  # 将sql查询的结果拿到
        print(getSampleLimsId[0])
        sample_id_lims = getSampleLimsId[0]['sample_id_lims']
        print("可以使用的样本为：" + str(sample_id_lims))
        self.sleep(2)

        if not getSampleLimsId:
            print('当前系统没有可用的样本')
        else:
            log.info("点击【新建】按钮")
            self.clicks('xpath', sampleReceive_ck_add_butoon)
            self.wait_loading()
            log.info("输入接样节点的LIMS号")
            self.clicks('xpath', sampleReceive_ck_enter_value)
            self.sleep(0.5)
            self.input('xpath', sampleReceive_ck_enter_value, str(sample_id_lims))
            self.sleep(0.5)
            log.info("点击确定按钮")
            self.clicks('xpath', sampleReceive_ck_enter_confirm)
            self.wait_loading()

            log.info("勾选接样样本tab全选")
            self.clicks('css', sampleReceive_ck_allcheckbox)
            self.sleep(0.5)
            log.info("点击【实验流程模板】")
            self.clicks('xpath', sampleReceive_ck_piplane_button)
            self.sleep(2)
            log.info("选择模板：核酸提取-破碎")
            self.clicks('xpath', sampleReceive_ck_piplane_value)
            self.sleep(0.5)
            log.info("点击确认按钮")
            self.clicks('css', sampleReceive_ck_piplane_confirm)
            self.sleep(0.5)
            log.info("点击预设探针按钮")
            self.clicks('xpath', sampleReceive_ck_probe_button)
            self.sleep(1)

            log.info("搜索探针：AA(PRIME_v5.0.0)/201902-425")
            self.input('css', search_input,'AA(PRIME_v5.0.0)')
            self.sleep(0.5)
            self.clicks('css', search_btn)
            self.sleep(0.5)
            self.clicks('css', sampleReceive_ck_probe_value)
            self.sleep(0.5)
            log.info("点击确定")
            self.clicks('css', sampleReceive_ck_probe_confirm)
            self.sleep(1)
            log.info("点击【是否保留原项目信息】下拉框")
            self.clicks('xpath', sampleReceive_keep_project_button)
            self.sleep(0.5)
            log.info("选择保留")
            self.clicks('xpath', sampleReceive_keep_project_value)
            self.sleep(0.5)

            # 这里调用自定义截图方法
            Screenshot(self.driver).get_img("样本出库信息录入")

            log.info("点击保存全部，下一步按钮")
            self.clicks('xpath', sampleReceive_save_next_button)
            self.sleep(0.5)
            log.info("出库理由填写：出库测试，填写理由")
            self.clicks('xpath', sample_ck_reason)
            self.sleep(0.5)
            self.input('xpath', sample_ck_reason, '出库测试，填写理由')
            self.sleep(0.5)
            now_handle = self.get_current_window_handle()
            print('获取当前窗口句柄', now_handle)
            log.info("点击确定按钮，出库成功")
            self.clicks('xpath', sample_ck_reason_confirm)
            self.wait_loading()

            # 获取所有窗口句柄
            all_handles = self.get_all_windows()
            for handle in all_handles:
                if handle != now_handle:
                    # 切换到新窗口句柄，即新打开的流转表页面
                    self.switch_to_window(handle)
                    self.sleep(1)
                    # 关闭新窗口句柄，关闭流转表页面
                    self.close()
            self.sleep(1.5)
            # 切换到旧窗口句柄，回到原页面
            self.switch_to_window(now_handle)
            self.sleep(1)

    def unsamplereceive_ck(self, sql):
        """
        对非接样，非混合的样本出库
        """
        getSampleLimsId = executeSql.test_select_limsdb(sql)  # 将sql查询的结果拿到
        print(getSampleLimsId[0])
        sample_id_lims = getSampleLimsId[0]['sample_id_lims']
        print("可以使用的样本为：" + str(sample_id_lims))
        self.sleep(2)

        if not getSampleLimsId:
            print('当前系统没有可用的样本')
        else:
            log.info("点击【新建】按钮")
            self.clicks('xpath', unsampleReceive_ck_add_butoon)
            self.sleep(0.5)
            self.wait_loading()
            log.info("输入非接样，非混合节点的LIMS号")
            self.clicks('xpath', unsampleReceive_ck_enter_value)
            self.sleep(0.5)
            self.input('xpath', unsampleReceive_ck_enter_value, str(sample_id_lims))
            self.sleep(0.5)
            log.info("点击确定按钮")
            self.clicks('xpath', unsampleReceive_ck_enter_confirm)

            self.wait_loading()
            log.info("点击切换到提取tab")
            self.clicks('xpath', hstq_tab_button)
            self.sleep(1)
            log.info("全选提取节点样本的复选框")
            self.clicks('css', hstq_ck_allcheckbox)
            self.sleep(0.5)
            log.info("点击【是否需要破碎】按钮")
            self.clicks('xpath', hstq_ck_isultrafrac_button)
            self.sleep(0.5)
            log.info("弹框中选择【是】")
            self.clicks('xpath', hstq_ck_isultrafrac_value)
            self.sleep(0.5)
            log.info("点击确定")
            self.clicks('xpath', hstq_ck_isultrafrac_confirm)
            self.sleep(0.5)
            log.info("点击【最后步骤】按钮")
            self.clicks('xpath', hstq_ck_laststep_button)
            self.sleep(0.5)
            log.info("弹框中选择【上机测序】")
            self.clicks('xpath', hstq_ck_laststep_value)
            self.sleep(0.5)
            log.info("点击确定按钮")
            self.clicks('xpath', hstq_ck_laststep_confirm)
            self.sleep(0.5)
            log.info("点击【上机目的】按钮")
            self.clicks('xpath', hstq_ck_sequence_goal)
            self.sleep(0.5)
            log.info("弹框中选择【一般测序】")
            self.clicks('xpath', hstq_ck_sequence_goal_value)
            self.sleep(0.5)
            log.info("点击确定按钮")
            self.clicks('xpath', hstq_ck_sequence_goal_confirm)
            self.sleep(0.5)
            log.info("点击【是否保留原项目信息】")
            self.clicks('xpath', hstq_ck_keep_project_button)
            self.sleep(0.5)
            log.info("选择【保留】")
            self.clicks('xpath', hstq_ck_keep_project_value)
            self.sleep(0.5)
            log.info("点击保存并下一步")
            self.clicks('xpath', hstq_ck_save_next_button)
            self.sleep(0.5)
            log.info("输入出库理由")
            self.clicks('xpath', hstq_ck_reason)
            self.sleep(0.5)
            self.input('xpath', hstq_ck_reason, '出库测试，填写理由')
            self.sleep(0.5)
            # if self.isDisPlayed('css',ckAuditor_box):
            #     log.info("出永久库，选择实验室审核人")
            #     self.click_by_js('css',ckAuditor)
            #     self.input('css',ckAuditor,'董国奇')
            #     self.wait_loading()
            #     self.clicks('xpath',ckAuditorChoice)
            #     self.sleep(0.5)
            #     log.info("点击确定按钮，出库成功")
            #     self.clicks('xpath', hstq_ck_reason_confirm)
            #     self.wait_loading()
            # else:
            log.info("点击确定按钮，出库成功")
            self.clicks('xpath', hstq_ck_reason_confirm)
            self.wait_loading()

            # 切换窗口
            now_handle = self.get_current_window_handle()  # 获取当前句柄
            # 获取所有窗口句柄
            all_handles = self.get_all_windows()
            for handle in all_handles:
                if handle != now_handle:
                    # 切换到新窗口句柄，即新打开的流转表页面
                    self.switch_to_window(handle)
                    self.sleep(1)
                    # 关闭新窗口句柄，关闭流转表页面
                    self.close()
            self.sleep(1.5)
            # 切换到旧窗口句柄，回到原页面
            self.switch_to_window(now_handle)
            self.sleep(1)

    def libquantmixed_sample_ck(self, sql):
        """
        对定量混合的样本出库
        """
        getSampleLimsId = executeSql.test_select_limsdb(sql)  # 将sql查询的结果拿到
        print(getSampleLimsId[0])
        sample_id_lims = getSampleLimsId[0]['libquant_lims_id']
        print("可以使用的样本为：" + str(sample_id_lims))
        self.sleep(2)

        if not getSampleLimsId:
            print('当前系统没有可用的样本')
        else:
            log.info("点击【新建】按钮")
            self.click_by_js('xpath', libquantmixed_ck_add_butoon)
            self.sleep(0.5)
            self.wait_loading()
            log.info("输入接样节点的LIMS号")
            self.clicks('xpath', libquantmixed_ck_enter_value)
            self.sleep(0.5)
            self.input('xpath', libquantmixed_ck_enter_value, str(sample_id_lims))
            self.sleep(0.5)
            log.info("点击确定按钮")
            self.clicks('xpath', libquantmixed_ck_enter_confirm)
            self.sleep(0.5)
            self.wait_loading()
            log.info("点击切换到定量tab")
            self.clicks('xpath', libquantmixed_tab_button)
            self.sleep(0.5)
            log.info("全选定量节点的样本")
            self.clicks('css', wkdl_ck_allcheckbox)
            self.sleep(0.5)
            log.info("点击【上机目的】按钮")
            self.clicks('xpath', wkdl_ck_sequence_goal_button)
            self.sleep(0.5)
            log.info("选择【一般测序】按钮")
            self.clicks('xpath', wkdl_ck_sequence_goal_value)
            self.sleep(0.5)
            log.info("点击【是否保留原项目信息】按钮")
            self.clicks('xpath', wkdl_ck_keep_project_button)
            self.sleep(0.5)
            log.info("选择【保留】选项")
            self.clicks('xpath', wkdl_ck_keep_project_value)
            self.sleep(0.5)
            log.info("点击保存下一步按钮")
            self.clicks('xpath', wkdl_ck_save_next_button)
            self.sleep(0.5)
            log.info("填写出库理由")
            self.clicks('xpath', wkdl_ck_reason)
            self.sleep(0.5)
            self.input('xpath', wkdl_ck_reason, '出库测试，填写理由')
            self.sleep(0.5)
            log.info("点击确定按钮,出库成功")
            self.clicks('xpath', wkdl_ck_reason_confirm)
            self.sleep(0.5)
            self.wait_loading()

    def poolingmixed_sample_ck(self, sql):
        """
        对富集混合的样本出库
        """
        pass


if __name__ == '__main__':
    ybck_get_sql1 = """SELECT t.sample_id_lims FROM sample_info_t t WHERE t.sample_id_lims LIKE 'GS%' AND t.sample_status ='01' 
    AND workflow_status ='01'"""

    ybck_get_sql2 = """SELECT t.sample_id_lims FROM sample_info_t t
LEFT JOIN exp_result_sample_project_t t2 ON (t.sample_id_lims=t2.sample_id_lims)
WHERE t.sample_id_lims LIKE 'GS%' AND t.sample_status ='01' 
AND t2.project_id IS NOT NULL
AND workflow_status ='01' AND t.original_sample_id_lims=t.sample_id_lims AND sample_type='C2012120800006'"""

    ybck_get_sql3 = """SELECT t.sample_id_lims FROM sample_info_t t
LEFT JOIN exp_result_sample_project_t t2 ON (t.sample_id_lims=t2.sample_id_lims)
WHERE t.sample_id_lims LIKE 'GS%' AND t.sample_status ='01' 
AND workflow_status ='01' AND t.current_step='extraction' 
AND t2.project_id IS NOT NULL"""

    ybck_get_sql4 = """SELECT t.libquant_lims_id FROM sample_info_t t 
LEFT JOIN exp_result_sample_project_t t2 ON (t.sample_id_lims=t2.sample_id_lims)
WHERE t.sample_id_lims LIKE 'GS%' AND t.sample_status ='01' 
AND workflow_status ='01' AND t.current_step='libquant' 
AND t2.project_id IS NOT NULL"""

    test = GetSampleCK(BasePage)
    test.libquantmixed_sample_ck(ybck_get_sql4)

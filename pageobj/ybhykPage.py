# -*- coding: utf-8 -*-
# @Time    : 2021/11/25
# @Author  : guoqi.dong
from common.screenshot import Screenshot
from common.DataBaseConfig import executeSql
from PageElemens.ybhyk_ele import *
from uitestframework.basepageTools import BasePage
from common.logs import log


class SampleYbyk(BasePage):
    """列表页，详情页的动作封装"""

    def ybhyk_change_role(self, userid, role_id, vaild):
        """
        将切换用户是否为库管功能封装
        """
        log.info("修改用户角色，修改为临时库权限")
        sqldata = 'UPDATE sys_user_role SET is_valid=' + "'" + vaild + "'" + ' WHERE user_id=' + "'" + userid + "'" + 'AND role_id=' + "'" + role_id + "'"
        executeSql.test_update_27mysql(sqldata)

    def ybhyk_select_hw(self):
        """
        将查询自己刚刚新建的盒子的功能封装
        """
        log.info("查询上个脚本，刚刚新建的盒子名称")
        sqldata = "SELECT box_name FROM sample_box_info_t t WHERE t.box_name LIKE '盒子_20%'   ORDER BY creation_date DESC;"
        # print(sqldata)
        ret = executeSql.test_select_limsdb(sqldata)
        # print(ret)
        return ret

    def ybhyk_select_kw(self):
        """
        将查询自己刚刚新建的库位的功能封装
        """
        log.info("查询上个脚本，刚刚新建的库位名称")
        sqldata = "SELECT storage_name FROM sample_storage_info_t t WHERE t.storage_name LIKE '测试专用-20%' ORDER BY creation_date DESC"
        # print(sqldata)
        ret = executeSql.test_select_limsdb(sqldata)
        # print(ret)
        return ret

    def ybhyk_select_taskid(self):
        """
        将查询自己刚刚完成的样本移库单的功能封装
        """
        box_name = self.ybhyk_select_hw()[0]['box_name']  # 拿出之前新建的盒位信息
        # print(box_name)
        log.info("查询自己刚刚完成的样本移库单")
        sqlData = "SELECT task_id FROM sample_transfer_item_t t1 LEFT JOIN sample_box_info_t t2 ON (" \
                  "t1.box_id=t2.box_id) WHERE t2.box_name  IN (" + "'" + box_name + "'" + ")"
        print(sqlData)
        result = executeSql.test_select_limsdb(sqlData)
        print(result)
        return result

    def ybyk_select_lsk_sample(self):
        """
        查询当前在临时库且样本包装量>0的样本
        """
        log.info("查询当前在临时库且样本包装量>0的样本")
        sqlData = " SELECT t.sample_id_lims FROM sample_info_t t LEFT JOIN sample_id_lab_v tv ON (t.sample_id_lims = " \
                  "tv.sample_id_lims) " \
                  "LEFT JOIN bas_sample_type_t t2 ON (t.sample_type = t2.sample_type_id) LEFT JOIN bas_dictionary_t t3 ON " \
                  "(t3.dt_code = t.sample_amt_unit AND t3.dt_type = 'meterage_unit') LEFT JOIN bas_dictionary_t t4 ON " \
                  "(t4.dt_code = t.sample_pkg_amt_unit AND t4.dt_type = 'packing_unit') LEFT JOIN sample_box_info_t t5 ON " \
                  "(t.box_id = t5.box_id) LEFT JOIN sample_storage_info_t t6 ON (t6.storage_id = t5.storage_id) LEFT JOIN " \
                  "sample_storage_info_t t7 ON (t6.parent_id = t7.storage_id) WHERE t.is_valid = '1' AND T.sample_id_lims like 'GS%' AND " \
                  "t.sample_status " \
                  "= '01' AND t.sample_pkg_amt >= 0 AND ((t7.storage_type = '01') OR (t7.storage_type = '00' AND EXISTS " \
                  "(SELECT 1 FROM sample_storage_user_t ssu WHERE ssu.is_valid = '1' AND ssu.storage_id = t7.storage_id " \
                  "AND ssu.user_id = 'dongguoqi'))) AND t7.storage_type = '00' ORDER BY t.creation_date DESC"
        # print(sqldata)
        result = executeSql.test_select_limsdb(sqlData)[0]
        # print(result)
        return result

    def ybhyk_add_temporary_storage(self):
        """
        将新建移样本盒功能封装（选择移盒+库外到临时库后）
        """
        log.info("点击新增按钮")
        self.clicks('xpath', ybhyk_list_add_button)
        self.sleep(0.5)
        log.info("选择移样本盒")
        self.clicks('xpath', ybhyk_list_select_transfer_type)
        self.sleep(0.5)
        self.clicks('xpath', ybhyk_list_select_transfer_type_value)
        self.sleep(0.5)
        log.info("选择库外到临时库")
        self.clicks('xpath', ybhyk_list_select_transfer_flow)
        self.sleep(0.5)
        self.clicks('xpath', ybhyk_list_select_transfer_flow_value)
        self.sleep(0.5)

        # 这里调用自定义截图方法
        Screenshot(self.driver).get_img("点击新建按钮，选择样本移库任务，选择样本库-库外到临时库","新建任务成功，跳转到任务详情页")

        log.info("点击确定")
        self.clicks('xpath', ybhyk_list_select_confirm)
        self.wait_loading()

    def ybhyk_add_temporary_storage_detail(self):
        """
        将新建移样本盒功能封装（选择移盒+库外到临时库后，详情页功能）
        """
        box_name = self.ybhyk_select_hw()[0]['box_name']  # 拿出之前新建的盒位信息
        print(box_name)

        storage_name = self.ybhyk_select_kw()[0]['storage_name']  # 拿出之前新建的库位信息
        print(storage_name)

        log.info("点击搜索盒子按钮")
        self.clicks('xpath', ybhyk_detail_search_box)
        self.sleep(0.5)
        log.info("点击输入框")
        self.clicks('xpath', ybhyk_detail_search_box_name)
        self.sleep(0.5)
        log.info("右侧弹框弹出，点击输入盒子信息：{}".format(box_name))
        self.clicks('xpath', ybhyk_detail_enter_value)
        self.input('xpath', ybhyk_detail_enter_value, box_name)
        self.sleep(0.5)
        log.info("点击右侧弹框中的确认按钮，弹框收起")
        self.clicks('xpath', ybhyk_detail_enter_value_confirm)
        self.sleep(0.5)
        log.info("盒子信息输入完毕，点击正式搜索按钮")
        self.clicks('xpath', ybhyk_detail_search_confirm)
        self.sleep(0.5)
        self.wait_loading()
        log.info("开始校验搜索出的结果是否正确")
        ele_exist = self.isElementExists('xpath', ybhyk_detail_search_result)
        if ele_exist:
            log.info("盒子校验通过，点击勾选复选框")
            self.clicks('xpath', ybhyk_detail_search_checkbox)
            self.sleep(0.5)
            log.info("点击加入明细表按钮")
            self.clicks('xpath', ybhyk_detail_add_to_list)
            self.sleep(0.5)
            self.wait_loading()
            log.info("点击进入明细表按钮，并进入成功")
            self.clicks('xpath', ybhyk_detail_go_to_list)
            self.sleep(0.5)
            self.wait_loading()
            log.info("先点击保存按钮，防止页面元素乱跳")
            self.clicks('xpath', ybhyk_detail_list_save_button)
            self.sleep(0.2)
            self.wait_loading()
            log.info("勾选盒子，点击选择库位按钮")
            self.clicks('xpath', ybhyk_detail_list_select_checkbox)
            self.sleep(0.5)
            self.clicks('xpath', ybhyk_detail_list_select_storage)
            self.sleep(0.5)
            self.wait_loading()

            # 这里调用自定义截图方法
            Screenshot(self.driver).get_img("样本移库详情页，点击选择库位按钮，选择要移的库位添加到明细表","添加库位信息成功")

            log.info("弹框中，输入指定的库位信息：{}".format(storage_name))
            self.clicks('xpath', ybhyk_detail_list_select_storage_value)
            self.input('xpath', ybhyk_detail_list_select_storage_value, storage_name)
            log.info("点击搜素库位的按钮")
            self.clicks('xpath', ybhyk_detail_list_select_storage_search)
            self.sleep(0.5)
            self.wait_loading()
            log.info("选择搜索结果，点击确认按钮")
            self.clicks('xpath', ybhyk_detail_list_select_result)
            self.clicks('xpath', ybhyk_detail_list_select_confirm)
            self.sleep(1)
            log.info("提交明细表结果，任务单完成")
            self.clicks('xpath', ybhyk_detail_list_submit)
            self.sleep(0.5)
            self.wait_loading()
        else:
            print("盒子不存在，请检查是否输入信息合法")

    def ybhyk_list_search(self):
        """
        将列表页搜索样本盒在哪个移库任务单的功能封装
        """
        box_name = self.ybhyk_select_hw()[0]['box_name']  # 拿出之前新建的盒位信息
        print(box_name)

        log.info("点击列表页，搜索样本盒按钮")
        self.clicks('xpath', ybhyk_list_search_box)
        self.sleep(0.5)
        log.info("弹框内输入指定盒子信息并点击搜索")
        self.clicks('xpath', ybhyk_list_search_boxname)
        self.input('xpath', ybhyk_list_search_boxname, box_name)
        self.clicks('xpath', ybhyk_list_search_boxname_confirm)
        self.sleep(0.5)
        self.wait_loading()
        log.info("校验搜索结果是否展示在列表页")
        ele_exist = self.isElementExists('xpath', ybhyk_list_search_result)
        if ele_exist:
            print('搜索结果展示正确')
        else:
            print('搜索无结果，请检查搜索条件是否存在问题')

    def ybyk_add_temporary_storage(self):
        """
        将新建移样本功能封装（选择移样本+临时库到临时库）
        """

        log.info("点击新增按钮")
        self.clicks('xpath', ybyk_list_add_button)
        self.sleep(0.5)
        log.info("选择移样本")
        self.clicks('xpath', ybyk_list_select_transfer_type)
        self.sleep(0.5)
        self.clicks('xpath', ybyk_list_select_transfer_type_value)
        self.sleep(0.5)
        log.info("选择临时库到临时库")
        self.clicks('xpath', ybyk_list_select_transfer_flow)
        self.sleep(0.5)
        self.clicks('xpath', ybyk_list_select_transfer_flow_value)
        self.sleep(0.5)
        log.info("点击确定")
        self.clicks('xpath', ybyk_list_select_confirm)
        self.wait_loading()

    def ybyk_add_temporary_storage_detail(self):
        """
        将新建移样本功能封装（选择移样本+临时库到临时库后，详情页功能）
        """

        box_name = self.ybhyk_select_hw()[0]['box_name']  # 拿出之前新建的盒位信息
        print(box_name)

        lsk_sample = self.ybyk_select_lsk_sample()['sample_id_lims']  # 拿到临时库的样本信息
        print(lsk_sample)

        log.info("点击样本筛选按钮")
        self.clicks('xpath', ybyk_detail_select_button)
        self.sleep(0.5)
        self.clicks('xpath', ybyk_detail_sample_enter)
        self.sleep(0.5)
        self.clicks('xpath', ybyk_detail_sample_value)
        self.sleep(0.5)
        self.input('xpath', ybyk_detail_sample_value, lsk_sample)
        self.sleep(0.5)
        self.clicks('xpath', ybyk_detail_sample_confirm)
        self.sleep(0.5)
        log.info("输入完样本信息后，点击确定搜索按钮")
        self.clicks('xpath', ybyk_detail_sample_search_confirm)
        self.wait_loading()

        log.info("勾选样本，点击加入明细表")
        self.clicks('xpath', ybyk_detail_select_checkbox)
        self.clicks('xpath', ybyk_detail_add_to_list)
        self.clicks('xpath', ybyk_detail_go_to_list)
        self.sleep(1)
        self.wait_loading()

        log.info("进入明细表后，点击保存按钮")
        self.clicks('xpath', ybyk_detail_list_save_button)
        self.sleep(3)
        log.info("先选择样本复选框，点击搜索盒子信息按钮")
        self.clicks('xpath', ybyk_detail_list_select_checkbox)
        self.sleep(2)
        self.clicks('xpath', ybyk_detail_list_select_storage)
        self.sleep(0.5)
        self.wait_loading()
        log.info("弹框中，输入盒子信息，点击确定")
        self.clicks('xpath', ybyk_detail_list_select_storage_value)
        self.sleep(1)
        self.input('xpath', ybyk_detail_list_select_storage_value, box_name)
        self.sleep(1)
        self.clicks('xpath', ybyk_detail_list_select_storage_search)
        self.sleep(0.5)
        self.wait_loading()
        log.info("选择搜索结果，点击确认")
        self.clicks('xpath', ybyk_detail_list_select_result)
        self.clicks('xpath', ybyk_detail_list_select_confirm)
        self.sleep(1)
        self.wait_loading()
        log.info("拖动滑条，帮样本选择位置信息")
        ele_js = 'document.getElementsByClassName("el-table__body-wrapper")[' \
                 '0].scrollLeft=2000'  # 需要滑动页面至最右端，填写盒内位置，所以执行滑到最右端的js
        self.executeJscript(ele_js)
        self.sleep(1)
        self.clicks('xpath', ybyk_detail_list_box_position)
        self.input('xpath', ybyk_detail_list_box_position_value, 'A3')
        self.sleep(1)
        log.info("点击完成任务单")
        self.clicks('xpath', ybyk_detail_list_submit)
        self.sleep(0.5)
        self.wait_loading()

    def ybyk_list_search(self):
        """
        将列表页搜索样本在哪个移库任务单的功能封装
        """
        task_id = self.ybhyk_select_taskid()[0]['task_id']  # 拿出之前新建的盒位信息
        print(task_id)

        log.info("点击列表页，点击搜索样本移库按钮")
        self.clicks('xpath', ybyk_list_search_button)
        self.sleep(0.5)
        log.info("弹框内输入taskid")
        self.clicks('xpath', ybyk_list_search_taskid)
        self.input('xpath', ybyk_list_search_taskid, task_id)
        log.info("点击确定搜索")
        self.clicks('xpath', ybyk_list_search_confirm)
        self.sleep(0.5)
        self.wait_loading()
        log.info("校验搜索结果是否展示在列表页")
        ele_exist = self.isElementExists('xpath', ybyk_list_search_result)
        print(ele_exist)
        if ele_exist:
            print('搜索结果展示正确')
        else:
            print('搜索无结果，请检查搜索条件是否存在问题')


if __name__ == '__main__':
    test = SampleYbyk(BasePage)
    s = test.ybyk_select_lsk_sample()
    # test.ybhyk_change_role('2535','2001','0')
    print(s)

# -*- coding: utf-8 -*-
# @Time    : 2022/03/24
# @Author  : guanzhong.zhou
# @File    : sr样本信息登记页面功能封装
from PageElemens.srSampleInfoImp_ele import *
from common.all_path import sr_sample_imp_file, sr_sample_sublibrary_imp_file, sampledata_path
from common.editYaml import read_yaml
from common.screenshot import Screenshot
from uitestframework.basepageTools import BasePage
from common.logs import log


class SrSampleInfoImp(BasePage):
    """
    sr样本信息登记模块页面基础方法封装
    """

    def sr_sample_import(self):
        """
        sr样本信息导入
        """
        log.info('点击sr信息导入按钮')
        self.clicks('css', sr_sample_imp)  # 定位文本框输入值
        self.sleep(0.5)
        # 执行修改元素属性js
        self.executeJscript(
            "document.querySelector('.dialog-upload .el-dialog__body .upload-demo input').style.setProperty('display','block','important');")
        self.sleep(0.5)
        # 上传sr样本导入文件
        self.input('css', sr_sample_imp_input, sr_sample_imp_file)
        # 点击上传按钮
        self.clicks('css', sr_sample_imp_upload)  # 点击查询
        self.wait_loading()

    def edit_upload_sample(self):
        """
        对上传的sr信息进行编辑，进入信息登记详情页
        """
        log.info("选择导入的sr样本信息,点击编辑")

        self.click_by_js('css', choice_imp_sr_sample)  # 点击查询

        self.clicks('css', edit_btn)
        self.wait_loading()

    def sr_sample_detail(self):
        """
        外部样本信息登记详情页，上传子文库信息，选择sr样本

        """
        log.info("导入子文库")

        self.clicks('css', btn_childrenImport)
        # 执行修改元素属性js
        self.executeJscript(
            "document.querySelector('.dialog-upload .el-dialog__body .upload-demo input').style.setProperty('display','block','important');")
        self.sleep(0.5)
        try:
            self.input('css', sr_childrenImport_input, sr_sample_sublibrary_imp_file)
            self.sleep(0.5)
            self.clicks('css', sr_childrenImport_upload)
            log.info('导入子文库成功')
        except Exception as a:
            log.info('导入子文库失败%s' % a)
        self.wait_loading()
        Screenshot(self.driver).get_img("导入子文库成功")

        self.clicks('css', sr_form_sampleIdLims)

        datas = read_yaml(sampledata_path)
        lims_nub = datas['rec_sr_sample_for_sr_import']
        log.info("选择外部样本的样本lims号:%s" % lims_nub)

        log.info('录入样本号进行搜索')
        self.input('css', sr_form_sampleIdLims_lims, lims_nub)
        self.sleep(0.5)
        self.clicks('css', sr_search_btn)
        self.wait_loading()
        Screenshot(self.driver).get_img("录入sr样本号进行搜索")
        try:
            if self.isElementExists('css', sr_search_choice):
                log.info('双击选中样本')
                self.double_click('css', sr_search_choice)
                self.wait_loading()
        except Exception as ss:
            log.info('没有查询到外部样本信息%s' % ss)

        log.info('保存登记信息')
        self.click_by_js('css', save_btn)
        self.wait_loading()

    def search_lims(self):
        """
        根据lims号查询样本登记信息
        """
        log.info("点击搜索按钮，录入样本lims号")

        datas = read_yaml(sampledata_path)
        lims_nub = datas['rec_sr_sample_for_sr_import']

        self.clicks('css', search_btn)
        self.input('css', search_lims, lims_nub)
        self.clicks('css', search_comfirm)
        self.wait_loading()

        if self.isElementExists('xpath', sample_page_list):
            samplist = self.findelements('xpth', sample_page_list)
            return samplist
        else:
            return None

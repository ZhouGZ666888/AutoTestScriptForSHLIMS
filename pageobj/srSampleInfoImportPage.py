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
        self.clicks('css', sr_sample_imp)  # 定位sr样本导入按钮
        self.sleep(0.5)
        # 执行修改元素属性js
        self.executeJscript(
            "document.querySelector('.dialog-upload .el-dialog__body .upload-demo input').style.setProperty('display','block','important');")
        self.sleep(0.5)
        # 上传sr样本导入文件
        self.input('css', sr_sample_imp_input, sr_sample_imp_file)
        # 点击上传按钮
        self.clicks('css', sr_sample_imp_upload)  # 点击上传





    def sr_sample_childrenImport(self):
        """
        外部样本信息登记详情页，上传子文库信息，选择sr样本

        """
        log.info("导入子文库")
        self.wait_loading()
        log.info('点击sr信息导入按钮')
        self.clicks('css', sr_childrenImport)  # 定位sr样本导入按钮
        self.sleep(1)
        # 执行修改元素属性js
        self.executeJscript(
            "document.querySelector('.dialog-upload .el-dialog__body .upload-demo input').style.setProperty('display','block','important');")
        self.sleep(0.5)
        # 上传sr样本导入文件
        self.input('css', sr_sample_imp_input, sr_sample_sublibrary_imp_file)
        # 点击上传按钮
        self.clicks('css', sr_sample_imp_upload)  # 点击上传
        self.wait_loading()


    def match_lims(self):
        """一键匹配LIMS号"""
        log.info("点击一键匹配LIMS号，匹配导入的sr样本lims号")
        self.clicks('css',matchLimsId)
        self.wait_loading()
        limsNub=self.get_text('css',choice_imp_sr_sample)
        return limsNub

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

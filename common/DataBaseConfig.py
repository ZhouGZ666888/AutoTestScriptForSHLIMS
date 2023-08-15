import pymysql
import psycopg2

# 以下提供脚本需要的数据和变量(Test环境)
# ==================27-mysql-basdb数据库信息==================
test_limsbasdb_ip = "172.16.18.27"
test_limsbasdb_user = "dba_user"
test_limsbasdb_password = "C25ARoFOYe5A"
test_limsbasdb_database = "basdb"
test_limsbasdb_port = 3306

# # ==================27-pg-lims数据库信息==================
# test_limsdb_ip = "172.16.18.27"
# test_limsdb_user = "lims_geneseeq"
# test_limsdb_password = "7O32kEL14O"
# test_limsdb_database = "lims"
# test_limsdb_port = 5432

# ==================123-pg-lims数据库信息==================
test_limsdb_ip = "192.168.4.123"
test_limsdb_user = "lims_geneseeq"
test_limsdb_password = "7O32kEL14O"
test_limsdb_database = "lims"
test_limsdb_port = 5432


class GetSqlHelper:
    def __init__(self):
        # 以下提供脚本需要的数据和变量(Test环境)
        # ==================27-mysql-basdb数据库信息==================
        self.base_ip = test_limsbasdb_ip
        self.base_user = test_limsbasdb_user
        self.base_password = test_limsbasdb_password
        self.base_database = test_limsbasdb_database
        self.base_port = test_limsbasdb_port

        # ==================27或123-pg-lims数据库信息==================
        self.test_limsdb_ip = test_limsdb_ip
        self.test_limsdb_user = test_limsdb_user
        self.test_limsdb_password = test_limsdb_password
        self.test_limsdb_database = test_limsdb_database
        self.test_limsdb_port = test_limsdb_port

        self.con = None  # 初始化连接对象
        self.cur = None  # 初始化游标

    def test_getCon_limsbasdb(self):
        """
        27MySQL base库连接，执行权限修改等操作
        """
        try:
            self.con = pymysql.connect(
                database=self.base_database,
                user=self.base_user,
                password=self.base_password,
                host=self.base_ip,
                port=self.base_port)

        except pymysql.Error as e:
            print("建立数据库Connect对象失败:%s" % e)
        try:
            # 创建游标
            self.cur = self.con.cursor()
        except Exception as e:
            print('建立游标失败：', e)

    def test_getCon_limsdb(self):
        """
        123PG库连接，执行基础增、删、改、查操作
        :return: conn游标
        """
        try:
            self.con = psycopg2.connect(
                database=self.test_limsdb_database,
                user=self.test_limsdb_user,
                password=self.test_limsdb_password,
                host=self.test_limsdb_ip,
                port=self.test_limsdb_port)

        except pymysql.Error as e:
            print("建立数据库Connect对象失败:%s" % e)
        try:
            # 创建游标
            self.cur = self.con.cursor()
        except Exception as e:
            print('建立游标失败：', e)

    def close_func(self):
        """关闭游标，关闭链接"""
        try:
            # print('开始关闭游标##ing')
            self.cur.close()
            # print('关闭游标成功')
        except Exception as e:
            print('关闭游标失败：', e)

        try:
            # print('开始关闭链接##ing')
            self.con.close()
            # print('关闭链接成功!')
        except Exception as e:
            print('关闭链接失败：', e)

    # 27base基础库更新方法
    def test_update_27mysql(self, sql):
        """27base基础库增，删，改 封装方法"""
        try:
            self.test_getCon_limsbasdb()
            num = self.cur.execute(sql)
            self.con.commit()
            print('执行语句影响行数：', num)
        except pymysql.Error as e:
            print("执行sql失败，开始回滚ing:" % e)
            self.con.rollback()
        self.close_func()

    # 27base基础库查询方法
    def test_select_27mysql(self, sql):
        """
        27base库查询方法封装
        :param sql: 查询语句
        :return: 获取查询结果
        """
        try:
            self.test_getCon_limsbasdb()
            self.cur.execute(sql)
            fc = self.cur.fetchall()
            self.close_func()
            return fc
        except pymysql.Error as e:
            print("pymysql Error:%s" % e)

    # 查询123pg数据库
    def test_select_limsdb(self, sql):
        """查询方法封装
        :param sql: 查询语句
        :return: 返回列名加值组成的列表[{col1:data,col2:data},{col1:data,col2:data},...]
        """
        self.test_getCon_limsdb()
        try:
            self.cur.execute(sql)
            fc = self.cur.fetchall()
            desc = self.cur.description
            data_dict = [dict(zip([col[0] for col in desc], row)) for row in fc]
            self.close_func()
            return data_dict  # 返回列名组成的字典表，装进list里
        except pymysql.Error as e:
            print("pymysql Error:%s" % e)

    # 123业务库更新方法
    def __edit(self, sql):
        """123业务库增，删，改 封装方法"""
        self.test_getCon_limsdb()  # 建立链接
        try:
            self.cur.execute(sql)
            self.con.commit()
            # print('执行语句影响行数：', num)
        except pymysql.Error as e:
            self.con.rollback()
            print("pymysql Error:%s" % e)
        self.close_func()

    def test_updateByParam(self, sql):
        """修改"""
        self.__edit(sql)

    def test_deleteByParam(self, sql):
        """删除"""
        self.__edit(sql)

    def test_insertByParam(self, sql):
        """新增"""
        self.__edit(sql)


# 建立实例对象，其他模块引用该对象
executeSql = GetSqlHelper()

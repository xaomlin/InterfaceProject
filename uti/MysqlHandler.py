# -*- coding: utf-8 -*-
# @Time    : 2021/1/25 23:01
# @Project : InterfaceProject
import pymysql
class MysqlHandler(object):
    '''
    操作数据库
    '''
    def __init__(self):
        # 连接 mysql 的方法：connect('ip','user','password','dbname')
        self.db = pymysql.connect(host='101.201.120.188',port=3306,user="root",passwd="root",db="depend_data",charset='utf8')
        # 所有的查询，都在连接 con 的一个模块 cursor 上面运行的
        self.cursor = self.db.cursor()


    def create_table(self,table):
        '''
        创建表
        '''
        # 使用 execute() 方法执行 SQL，如果表存在则删除
        self.cursor.execute("DROP TABLE IF EXISTS {}".format(table))
        # 使用预处理语句创建表
        #sql = "CREATE TABLE HEXIAOYU (depend_key  CHAR(20) NOT NULL,value  CHAR(20),);"
        sql = """CREATE TABLE {} (
                 depend_key  CHAR(255) NOT NULL,
                 value  CHAR(255))""".format(table)
        self.cursor.execute(sql)
        # 无论如何，连接记得关闭
        self.db.close()

    def insert_data(self,table,key,value):
        '''
        插入数据
        '''
        sql = "INSERT INTO %s(depend_key,value)VALUES ('%s','%s')"%(table,key,value)
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
            # print('pass')
        except:
            # 如果发生错误则回滚
            self.db.rollback()
            print('发生错误了')
        #无论如何，连接记得关闭
        self.db.close()

    def select_table(self,value,table,key):
        '''
        查询数据
        '''
        sql = "SELECT %s FROM  %s WHERE depend_key = '%s'"%(value,table, key)
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            # print(results[0][0])
            return results[0][0]
        except:
            # 如果发生错误则回滚
            print ("Error: unable to fetch data")
            print('error')
        # 无论如何，连接记得关闭
        self.db.close()

    def delete_table(self,table):
        '''
        删除表
        '''
        self.cursor.execute("DROP TABLE IF EXISTS {}".format(table))
        self.db.close()

if __name__ == '__main__':
    m = MysqlHandler()
    # m.insert_data('test','abc','123')
    m.select_table('value','test','sid')
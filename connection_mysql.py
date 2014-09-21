#coding:utf-8
import MySQLdb
def connect():
          global conn,cur #全局定义
          conn  = MySQLdb.connect(host="127.0.0.1",user="root",passwd="passwd",db="database")
          cur = conn.cursor() #操作游标
def insert():
          sql ="insert into new  values (2,'j')" #插入命令
          cur.execute(sql) #执行sql命令
          conn.commit() #确认命令
def close():
          cur.close()#关闭操作
          conn.close()#关闭连接
def main():
          connect()
          insert()
          close()
main()

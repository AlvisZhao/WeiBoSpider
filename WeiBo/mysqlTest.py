import pymysql
import datetime

if __name__ == '__main__':
    host = 'localhost'
    username = 'root'
    password = '123456'
    conn = pymysql.connect(host,username,password)
    cusor = conn.cursor()
    currentTime = datetime.datetime.now()
    sqlToTopicQuery = "INSERT INTO weibo.t_weibo_topic VALUES('%s','%s','%s', '%s', '%s')" % ('101','2','3','4', str(currentTime))
    sqlToDicuQuery = "INSERT INTO weibo.t_weibo_disu VALUES('%s','%s','%s', '%s', '%s')" %  ('110','101','3','4', str(currentTime))
    cusor.execute(sqlToTopicQuery)
    cusor.execute(sqlToDicuQuery)
    conn.commit()
    cusor.fetchone()
    conn.close()
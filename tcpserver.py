import socketserver, os, threading, pymssql, decimal, time, re, sys
from tcplistDialog import TcplistDialog
from PyQt5.QtWidgets import QDialog, QApplication
from DBUtils.PooledDB import PooledDB

global my_dict, ui, dialog, sql, signal, pool
signal=0
my_dict = {}
sql = "insert into [tableA] (Machid,mode,count,datetime) VALUES "


class TcpListThread(threading.Thread):  # 继承父类threading.Thread
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global dialog, ui , signal
        app = QApplication(sys.argv)

        dialog = TcplistDialog()
        dialog.show()
        signal = 1
        sys.exit(app.exec())


class RefreshThread(threading.Thread):  # 继承父类threading.Thread

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global dialog, signal, my_dict
        while True:
            #try:
                if signal == 1:
                    time.sleep(5)
                    dialog.settcpdict(my_dict)
            #except Exception as e:
            #    exc_type, exc_obj, exc_tb = sys.exc_info()
            #    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            #    print(exc_type, fname, exc_tb.tb_lineno)
            #    print(e)


class MyTCPHandler(socketserver.BaseRequestHandler):  # tcp处理，每一个连接一个县线程
    def handle(self):
        self.request.settimeout(360)
        global sql, my_dict, pool
        print("{} connected".format(self.client_address[0]+':'+str(self.client_address[1])))


        i = [0, '/', '/', '/']

        my_dict[self.client_address[0]+':'+str(self.client_address[1])] = i
        try:
            #db_sqls = pymssql.connect('localhost', 'sa', '666666', 'test')  # 获取数据库连接

            s = 0
            lock = threading.Lock()
            while True:
                try:
                    lock.acquire()
                    if s == 0:
                        # self.data = self.request.recv(1024).decode('UTF-8', 'ignore').strip().strip(b'\x00'.decode())
                        self.data = self.request.recv(1024).decode('utf-8').strip()

                        if self.data.startswith('get'):
                            self.request.sendall("asss".encode())

                            # cur = self.__GetConnect()
                            # cur.execute(sql)                      #查询数据
                            # resList = cur.fetchall()
                        elif re.search("\('[0-9]*','[0-9]*','[0-9]*'\)", self.data):
                            timestr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                            matchObj = re.search("\('[0-9]*','[0-9]*','[0-9]*'\)", self.data)
                            pattern = re.compile("'[0-9]*'")
                            str_re = pattern.findall(matchObj.group())
                            j = [int(str_re[0][1:-1]), str_re[1][1:-1], str_re[2][1:-1], timestr]

                            my_dict[self.client_address[0]+':'+str(self.client_address[1])] = j

                            totalsql = matchObj.group()[:-1] + ",'" + timestr + "')"
                            strsql = (sql + "          " + totalsql)
                            # [8:-1]
                            #print("{} wrote:".format(self.client_address[0]+':'+str(self.client_address[1])) + "\n" + matchObj.group())
                            db_sqls = pool.connection()
                            cur_sqls = db_sqls.cursor()  # 写入数据库
                            cur_sqls.execute(strsql)
                            db_sqls.commit()
                            cur_sqls.close()
                            db_sqls.close()
                        self.request.sendall("ok".encode())
                    lock.release()
                except ConnectionResetError:
                    del my_dict[self.client_address[0]+':'+str(self.client_address[1])]
                    print(self.client_address[0]+':'+str(self.client_address[1]) + "已断线")
                    break

        except Exception as e:
            del my_dict[self.client_address[0]+':'+str(self.client_address[1])]
            print(self.client_address[0]+':'+str(self.client_address[1]) + "已断线")
            print(e)
            f2 = open('errorlog.txt', 'a')
            f2.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ":\n")
            f2.write(repr(e) + "\n")
            f2.close()


guithread = TcpListThread()
guithread.start()  # 界面线程
time.sleep(1)
refreshthread = RefreshThread()
refreshthread.start()  # 界面刷新线程
PORT = int(23000)
HOST = "0.0.0.0"
pool = PooledDB(pymssql, maxcached=5, host='localhost', user='sa', password='666666', database='test')  # 连接池
server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)  # socketserver
server.serve_forever()





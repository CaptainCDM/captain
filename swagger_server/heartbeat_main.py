import socket,threading

class HeartBeat():
    def __init__(self):
        return
    def  server(self,conn,addr):
        print('{} now connection'.format(addr))
        msg="hello {},my name is main server ".format(addr)
        conn.send(msg.encode())
        while 1:
            data=conn.recv(1024)
            print("{} client send data is {}".format(addr,data.decode()))

            if not data:
                print("{} is closed connection".format(addr))
                break
            remsg="Hello {}".format(addr)
            conn.send(remsg.encode())
        conn.close()

    def start_heart(self):
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        #这里监听地址，端口
        s.bind(('127.0.0.1',7001))
        s.listen(10)
        print("waiting ......")
        while 1:
            conn,addr=s.accept()
            t=threading.Thread(target=self.server,args=(conn,addr))
            t.start()


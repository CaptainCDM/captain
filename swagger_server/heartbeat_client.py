
#这里是客户端，单独启动就可以，不需要伴随程序启动
import socket,threading,time
def deal_data(conn, addr):
    print('Accept new connection from {0}'.format(addr))
    conn.send(('Hi, Welcome to the server!').encode())
    while 1:
        data = conn.recv(1024)
        print('{} client send data is {}'.format(addr, data.decode()))
        time.sleep(1)
        if  not data:
            print('{} connection close'.format(addr))

            break
        conn.send(bytes('Hello, {}'.format(data),"UTF-8"))
    conn.close()


def server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("127.0.0.1", 7001))
    sock.listen(10)
    print('Waiting connection...')

    while 1:
        conn, addr = sock.accept()
        t = threading.Thread(target=deal_data, args=(conn, addr))
        t.start()
server()









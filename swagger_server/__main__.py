#!/usr/bin/env python3
import gevent.monkey
gevent.monkey.patch_all()
from gevent.pywsgi import WSGIServer
import connexion
from multiprocessing import cpu_count, Process


import threading
from swagger_server.heartbeat_main import HeartBeat


#做定时任务
from swagger_server.Config import config



#初始化app
_app = connexion.App(__name__, specification_dir='./swagger/')
#swagger配置载入
_app.add_api('swagger.yaml', arguments={'title': 'My Flask'})

#使用钩子
from flask import request,redirect,session
@_app.app.before_first_request
def hook():
    session['click']=0
    print(request.path)
    if request.path.find('cd') !=-1 :
        print('path is my name')
        return None
    if request.path.find('jzh')!=-1 :
        print('jzh is funny')
        return None
    if request.path.find('blue')!=-1 :
        print('this is today bule learn')
        return None
    else:
        return None

def main(mode):
    #引入config类
    _app.app.config.from_object(config())
    #将congfig配置初始化载入（里面有蓝图注册，有调度器的启动）
    config().init_app(_app.app)
    #加入seesion的密钥
    _app.app.config['SECRET_KEY'] = 'showtime'

    #单进程模式
    if mode==1:
       WSGIServer(('0.0.0.0', 7000), _app).serve_forever()
    # 多进程模式
    if mode==-1:
        server = WSGIServer(('0.0.0.0', 7000), _app).serve_forever()
        def serve_forever():
            server.start_accepting()
            server._stop_event.wait()
        for i in range(cpu_count()):
            p = Process(target=serve_forever)
            p.start()










if __name__ == '__main__':
   #  #启动app,加入socket之后，直接启动是无法启动的,需要启动单独线程守护启动
   #  thread = threading.Thread(target=main)
   #  thread.setDaemon(True)
   #  thread.start()
   # #启动socket（选择）
   #  HeartBeat().start_heart()
   #-------------------上面是启动时带一个socket服务------------------
   #下面为正常启动
    main(mode=-1)




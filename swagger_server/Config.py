#定时任务配置文件
from flask_apscheduler import APScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from swagger_server.controllers.user_controller import login_get_cd

#蓝本注册

from swagger_server.controllers.user_blueprint import user
from swagger_server.controllers.apitest import creatapi




class config():
    @staticmethod
    def init_app(app):
        #注册蓝图
        app.register_blueprint(creatapi(), url_prefix="/v1/api/")
        app.register_blueprint(user, url_prefix="/v1/chengda/")

        #scheduler=APScheduler()
        scheduler=APScheduler(BackgroundScheduler(timezone="Asia/Shanghai"))
        #初始化app
        scheduler.init_app(app)
        #定时任务job1
        scheduler.add_job(func=login_get_cd,
                               args=('clean',),
                               trigger='interval',
                               id='job1',
                               seconds=1)
        #需要定时任务的时候，取消注释
        #scheduler.start()
        return



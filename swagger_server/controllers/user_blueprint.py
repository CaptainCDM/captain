
from flask import Blueprint
from flask import jsonify
from flask import request,redirect,Response

#在这里就可以使用蓝图功能------------>config文件中去注册
user=Blueprint("user",__name__)


#蓝图中使用hook钩子
@user.before_request
def hook():
    if request.path.find('cd'):
        print('path is my name')
        return None
    elif request.path.find('jzh'):
        print('jzh is funny')
        return None
    elif request.path.find('blue'):
        print('this is today bule learn')
        return None
    elif request.path.find('fuck'):
        return redirect('/blue_test')

#这里是使用流
def gen():
    #具体想要实现的功能，比如拉入视频流，yield返回即可
    for i in range(10):
        yield "num:{}".format(i)
@user.route("blue_test",methods=["GET"])
def blue_test():
    print("this is test_blueprint api")
    return jsonify({"a":"a"})
@user.route("liu",methods=["GET"])
def liu_test():
    print('coming')
    return Response(gen(),mimetype='multipart/x-mixed-replace; boundary=frame')

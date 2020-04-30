from flask import Blueprint
from flask_restful import Api,Resource


class Apitest(Resource):
    def get(self):
        return {'result':'Method is get'}
    def post(self):
        return {'result':'Method is post'}
    def put(self):
        return {'result':'Method is put'}
    def delete(self):
        return {'result':'Method is delete'}

def creatapi():
    apitest = Blueprint('apitest', __name__)
    api = Api(apitest)
    #这里唯一的比较特殊的就是不能以/开头，
    api.add_resource(Apitest,'cd')
    return apitest

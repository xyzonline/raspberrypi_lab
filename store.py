#!/usr/bin/env python
# encoding: utf-8

'''
存储模块
结构上使其与kinto相似

http://kinto.just4fun.site/v1/buckets/paperweekly/collections/forum2wechat_todo/records
var gist = kinto_client.bucket("blockly").collection("gist");
'''
from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase
from playhouse.shortcuts import model_to_dict, dict_to_model
#from playhouse.flask_utils import object_list
import datetime
import uuid

db = SqliteExtDatabase('gist_database.db')

import logging
logging.basicConfig(level=logging.INFO)
################ data class

class BaseModel(Model):
    class Meta:
        database = db

class GistModel(BaseModel):
    title = CharField()
    description = CharField(null=True)
    content = CharField()
    is_published_ = BooleanField(default=False)
    tag = CharField(null = True)
    url = CharField(null = True) # 代码站点/文档/用户信息
    update_time = DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = db
        order_by = ('-update_time',)

# 管理
def manage_table():
    db.connect()
    db.create_tables([GistModel])
    #db.drop_tables([GistModel], safe=True)


############

class Gist(object):
    """代码片段存储.
    单用户所以很简单
    为了便于分享使用uuid定义用户
    """
    def __init__(self):
        self.GistModel = GistModel
    def list(self):
        gists = self.GistModel.select()# all
        #return gists
        return [model_to_dict(gist) for gist in gists]
    def get(self,gist_id):
        # 获取或不存在
        try:
            item = self.GistModel.get(self.GistModel.id==gist_id)
        except GistModel.DoesNotExist:
            return None
        return model_to_dict(item)
        #print(type(item))
    def create(self,title,content,description=None):
        gist = self.GistModel()
        gist.title = title
        gist.description = description
        gist.content = content
        gist.save()
        return gist
    def delete(self,gist_id):
        gist = self.GistModel.get(GistModel.id == gist_id)
        gist.delete_instance() # return id

if __name__ == '__main__':
   #create_table()
   manage_table()
   # sandman2ctl sqlite+pysqlite:///my_database.db 浏览数据

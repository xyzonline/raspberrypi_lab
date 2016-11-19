#!/usr/bin/env python
# encoding: utf-8

'''
存储模块，使用tinydb
结构上使其与kinto相似

db::table::record
blockly4pi::gist::

http://kinto.just4fun.site/v1/buckets/paperweekly/collections/forum2wechat_todo/records

var gist = kinto_client.bucket("blockly").collection("gist");
'''
from tinydb import TinyDB, where,Query
import uuid

# 构建类

class Gist(object):
    """代码片段存储.

    >>> gist_store = Gist() #使用默认值
    >>> record = {}
    >>> record["name"] = 'test'
    >>> record_id = uuid.uuid4().get_hex()[:16]
    >>> record["id"] = record_id
    >>> gist_store.insert(record)
    >>> item = gist_store.get(record_id)
    <class 'tinydb.database.Element'>
    >>> item["id"] == record_id
    True
    >>> assert item == record
    >>> #print("insert...")
    >>> records = gist_store.list()
    >>> #print(records)
    """

    def __init__(self,DB_FILE="./gist.json",TABLE_NAME="gist"):
        """TODO: to be defined1. """
        _db = TinyDB(DB_FILE)
        self._table = _db.table(TABLE_NAME)
    def list(self):
        records = self._table.all()
        return records
    def get(self,record_id):
        Record = Query()
        item = self._table.get(Record.id==record_id)
        print(type(item))
        return item
    #def  search
    def insert(self,record={}):
        '''
        插入记录：设计字段，和kinto相同
        '''
        self._table.insert(record)
    def delete(self,record_id):
        # 可能不存在 try
        # log 提示
        pass

if __name__=='__main__':
    #gist_store = Gist()
    #print gist_store.get("0fd60cafcae54b6c")
    import doctest
    doctest.testmod()

#!/usr/bin/env python
# encoding: utf-8

from store import Gist
import logging
logging.basicConfig(level=logging.INFO)

# 查看信息 py.test xxx -s

class Test_Gist:
    def setup_method(self,method):
        self.gist=Gist()
        pass
    def test_gist_create(self):
        title = "title"
        content = "content"
        description = "description"
        gist = self.gist.create(title,content,description)
        assert gist.title == title
        logging.info(("gist id:",gist.id))
        # 不是纯函数
    def test_gist_delete(self):
        gist_id = 3
        self.gist.delete(gist_id)
    def test_gist_list(self):
        gists = self.gist.list()
        gist_ids = [gist.id for gist in gists]
        logging.info(("gist id:",gist_ids))
    def test_show_id(self):# for debug
        pass

# !py.test %  -s

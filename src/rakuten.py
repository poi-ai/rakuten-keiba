import time
from selenium import webdriver
from login import Login

class Rakuten():
    KEIBA_URL = 'https://keiba.rakuten.co.jp/'

    def __init__(self):
        self.driver = webdriver.Chrome()

    def __del__(self):
        try:
            self.driver.quit()
        except:
            pass

    def login(self, user_id, password):
        '''楽天へログインする'''
        l = Login(self.driver, user_id, password)
        l.login()

        return True

    def bet(self):
        '''投票関連の処理する'''
        # トップページに遷移
        self.driver.get('https://keiba.rakuten.co.jp/')

        # 投票ページに遷移

    def get_id(self, id):
        '''指定したIDの要素を取得'''
        return self.driver.find_element_by_id(id)

    def get_class(self, class_name):
        '''指定したクラス名の要素を取得'''
        return self.driver.find_element_by_class_name(class_name)
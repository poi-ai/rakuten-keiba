import os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import time
from selenium import webdriver
from login import Login
from cashin import CashIn
#from cashout import CashOut

class Rakuten():
    KEIBA_URL = 'https://keiba.rakuten.co.jp/'

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.cashin = CashIn(self.driver)

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

    def cashout(self, amount):
        '''楽天競馬へ出金する'''
        pass
        #co = CashOut(amount)

    def bet(self):
        '''投票関連の処理する'''
        # トップページに遷移
        self.driver.get('https://keiba.rakuten.co.jp/')

        # 投票ページに遷移
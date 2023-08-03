import time

class Login():
    def __init__(self, driver, user_id, password):
        self.driver = driver
        self.user_id = user_id
        self.password = password

    def login(self):
        # 楽天競馬のIDをパラメータに入れておかないと別操作で再度パスワードを聞かれる
        self.driver.get('https://grp02.id.rakuten.co.jp/rms/nid/loginfwd?__event=LOGIN&service_id=n57')

        self.driver.find_element_by_id('loginInner_u').send_keys(self.user_id)
        self.driver.find_element_by_id('loginInner_p').send_keys(self.password)
        self.driver.find_element_by_class_name('loginButton').click()

        if self.driver.current_url == 'https://my.keiba.rakuten.co.jp/':
            return True
        else:
            return False

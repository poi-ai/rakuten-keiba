import time

class CashIn():
    '''楽天競馬へ入金する'''

    def __init__(self, driver):
        self.driver = driver

    def bank(self, pin, amount, mail_notice = True, pin_omit = False):
        '''
        楽天銀行から入金する

        Args:
            pin(str): 暗証番号(半角数字4桁)
            amount(int): 入金額
            mail_notice(bool): メール通知を行うか
            pin_omit(bool): 次入金では暗証番号省略するか
        '''
        self.driver.get('https://bet.keiba.rakuten.co.jp/bank/deposit')

        # 画面遷移待機
        time.sleep(2)

        # 金額入力
        self.driver.find_element_by_id('depositNumberInput').send_keys(int(amount / 100))

        # メール通知
        if not mail_notice:
            self.driver.find_element_by_class_name('k_switch__button').click()

        # 確認ボタン
        self.driver.find_element_by_class_name('transactionStepActionButton__button').click()

        # 画面遷移待機
        time.sleep(1)

        # 暗証番号省略に設定されている場合は入力フォームが存在しない
        try:
            # 暗証番号
            self.driver.find_element_by_id('pinInput').send_keys(pin)
        except:
            pass

        # 次回以降の省略チェック
        if pin_omit:
            self.driver.find_element_by_class_name('k_switch__button').click()

        # 入金ボタン
        self.driver.find_element_by_class_name('k_backgroundColor__primary').click()

        # 画面遷移待機
        time.sleep(1)

        # チェック
        if '受け付けました' in self.driver.find_element_by_class_name('depositComplete__body').text:
            return True
        else:
            return False

    def point(self, pin, amount, mail_notice = True, pin_omit = False):
        '''
        楽天ポイントからチャージする

        Args:
            pin(str): 暗証番号(半角数字4桁)
            amount(int): チャージポイント
            mail_notice(bool): メール通知を行うか
            pin_omit(bool): 次チャージでは暗証番号省略するか
        '''
        self.driver.get('https://bet.keiba.rakuten.co.jp/bank/charge')

        # 画面遷移待機
        time.sleep(2)

        # 注意事項モーダルが出ている場合は閉じる
        try:
            self.driver.find_element_by_class_name('k_backgroundColor__card').click()
        except:
            pass

        # 金額入力
        self.driver.find_element_by_id('chargeNumberInput').send_keys(int(amount / 100))

        # メール通知
        if not mail_notice:
            self.driver.find_element_by_class_name('k_switch__button').click()

        # 確認ボタン
        self.driver.find_element_by_class_name('transactionStepActionButton__button').click()

        # 画面遷移待機
        time.sleep(1)

        # 暗証番号省略に設定されている場合は入力フォームが存在しない
        try:
            # 暗証番号
            self.driver.find_element_by_id('pinInput').send_keys(pin)
        except:
            pass

        # 次回以降の省略チェック
        if pin_omit:
            self.driver.find_element_by_class_name('k_switch__button').click()

        # 入金ボタン
        self.driver.find_element_by_class_name('k_backgroundColor__primary').click()

        # 画面遷移待機
        time.sleep(1)

        # チェック
        if '受け付けました' in self.driver.find_element_by_class_name('chargeComplete__body').text:
            return True
        else:
            return False
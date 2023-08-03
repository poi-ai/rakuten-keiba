from src.rakuten import Rakuten

# インスタンス作成
rakuten = Rakuten()

# 楽天にログイン
result = rakuten.login(user_id = 'poi@hogehoge.jp', password = 'p@ssword')
if result:
    print('OK')
else:
    print('NG')

# 楽天競馬で購入する(事前ログイン必須)
# rakuten.bet()
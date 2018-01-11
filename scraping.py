import bs4
from operator import itemgetter
import datetime
import os
import re
from collections import Counter

ranks = []
path = os.path.join('天鳳ランキング_files', 'dummy.html')

with open(path, 'r', encoding='utf-8') as f:
    # ファイルをhtml解析しやすいよう変換
    soup = bs4.BeautifulSoup(f, 'html.parser')

    # 検索プレーヤー名の抽出
    player_name = soup.select('#txtPlayerID')[0].get('value')
    print(player_name)

    count = 1

    spans = soup.find_all('span', id=re.compile('_lblPLAYER'))

    ranks = [span['id'][-1:] for span in spans if span.getText() == player_name]

counter = Counter(ranks)

print(counter['1'])
print(counter['2'])
print(counter['3'])
print(counter['4'])

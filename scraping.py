import bs4
from operator import itemgetter

output = []

with open('天鳳ランキング_files\dummy.html', 'r', encoding='utf-8') as f:
    # ファイルをhtml解析しやすいよう変換
    soup = bs4.BeautifulSoup(f, 'html.parser')

    # 検索プレーヤー名の抽出
    player_name = soup.select('#txtPlayerID')[0].get('value')
    print(player_name)

    count = 1
    # 対戦数だけ繰り返す
    while True:
        # id指定のため、対戦番号を文字列化
        if count < 10:
            str_count = '0' + str(count)
        else:
            str_count = str(count)

        # 対戦番号の1位～4位のプレーヤー名のidを作成する。
        id_first = '#rptMain_ctl' + str_count + '_lblPLAYER1'
        id_second = '#rptMain_ctl' + str_count + '_lblPLAYER2'
        id_third = '#rptMain_ctl' + str_count + '_lblPLAYER3'
        id_fourth = '#rptMain_ctl' + str_count + '_lblPLAYER4'

        # 対戦番号の1位～4位のプレーヤー名を抽出する。
        text_first = soup.select(id_first)[0].getText()
        text_second = soup.select(id_second)[0].getText()
        text_third = soup.select(id_third)[0].getText()
        text_fourth = soup.select(id_fourth)[0].getText()

        result = {
            'No.': count,
            '1位': text_first,
            '2位': text_second,
            '3位': text_third,
            '4位': text_fourth
        }

        output.append(result)

        count += 1
    
        if count > 200:
            break

    output = sorted(output, key=lambda x: x['No.'], reverse=True)
    # print(output)

    # 取得されたoutputをベースに分析する
    analysis = []
    num_games = count # このとき対戦数 + 1
    count_first = 0
    count_second = 0
    count_third = 0
    count_fourth = 0
    
    for row in output:
        game_num = num_games - row['No.']
        # プレーヤーの順位を取得し、回数に追加する。
        if row['1位'] == player_name:
            count_first += 1
        elif row['2位'] == player_name:
            count_second += 1
        elif row['3位'] == player_name:
            count_third += 1
        else:
            count_fourth += 1

        rank_times = {
            'No.': game_num,
            '1位': count_first,
            '2位': count_second,
            '3位': count_third,
            '4位': count_fourth
        }

        analysis.append(rank_times)

        ## todo: 直近100戦のトップ率を算出する
    
    print(analysis)


# 分析結果をcsvファイルに出力する。
with open('output.csv', 'w', encoding='utf-8') as f:
    # ヘッダー
    f.write('No.,1位,2位,3位,4位\n')
    
    for row in analysis:
        f.write(str(row['No.']))
        f.write(',')
        f.write(str(row['1位']))
        f.write(',')
        f.write(str(row['2位']))
        f.write(',')
        f.write(str(row['3位']))
        f.write(',')
        f.write(str(row['4位']))
        f.write('\n')

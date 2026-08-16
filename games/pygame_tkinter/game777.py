
"""スロットゲーム

簡単なスロットゲームです。ゲームスタート時に保有しているコインを増やしましょう。
掛けコイン数を入力すると、スロットの結果が表示されます。
絵柄が揃うと、そのパターンに応じた配当倍率でコインを獲得することができます。
"""


import random   # "乱数" を生成するために必要なライブラリをメモリ上に読み込む（標準ライブラリ）


# スロット（リール）の中身を "定数" で定義する
# 配列のインデックスは 0 から始まるので、0 〜 10 番目に格納されている
# 定数は全て大文字で記載する
REEL_MARK_LIST = ('7', 'BAR', '🍒', '🍎', 'Reply','♢','♢', 'Reply', '🍎','Reply','♢','Reply','🍎')

# 特別なプレーヤーの名前と、その名前を使用した際のボーナスコイン数
#BONUS_PLAYER_AND_COINS = {'king': 100, 'queen': 150}

# スペシャルサンクスの対象者名
# ボーナスコインは一律 50 枚とする
#SPECIAL_THANKS = {'akira',      # 弊社社長。詳細は社長が作成最多ブログ記事のプロフィール欄をご確認下さい。
#                  'hurry',      # 詳細はプロフィール欄から twitter をご確認下さい。
#                  'shachi',     # https://shachi-web.com/
#                  }
#SPECIAL_THANKS_COIN = 50


# ============================================================
# ゲームに必要な関数を定義する
# ============================================================

player_coin=input('購入コイン数を入力して下さい: ')
game_count=int(0)
count_cherry=int(0)


def show_start_message():
    """ゲーム開始のメッセージを表示する
    (This function is to be called to show the start message.)
    """
    print('--------------')
    print('スロットゲーム')
    print('--------------')

def ask_player_name():
    player_name = input('あなたの名前を入力して下さい: [空白OKです。]')
    print(f'こんにちは {player_name} さん')
    return player_name

def ask_bets(player_coin):
    """現在の所持コイン数を表示した後、掛けるコイン数（bets）を尋ねる
    (This function is to be called to ask bets.)

    所持コイン数（player_coin）は数値なので、文字列に含めたい場合は文字列（string）に変換する必要がある ==> str() 関数
    input() 関数で入力した値は文字列（string）になるので整数（integer）に変換する ==> int() 関数

    Args:
        player_coin (int): プレーヤーの所持コイン数

    Returns:
        int: 掛けコイン数
    """
    print('------------------------------')
    print(f'現在の所持コイン数は {player_coin:,} 枚です。')

    bets = int(1)
    return bets

def show_and_get_result():
    """スロットの結果（絵柄）を表示し、結果を取得する
    (This function is to be called to show and get result.)

    Returns:
        str: スロットの結果（絵柄）
    """
    result_list = []
    for _ in range(3):
        index = random.randint(0, 12)
        result = REEL_MARK_LIST[index]
        result_list.append(result)
    result_all = ''.join(result_list)
    print(result_all)
    return result_all

def get_division(marks):
    """絵柄に応じた配当倍率を取得する
    (This function is to be called to get division.)

    Args:
        marks (str): スロットの結果（絵柄）

    Returns:
        int: 配当倍率
    """
    
    
    if marks == '777':
        # count_777=int(0)
        print('超大当たり！！120枚')
       # count_777=count_777+1    
        # print('超大当たり！！'+str(count_777)+'回目です。')
        return 120
    elif marks == 'BARBARBAR':
        print('BAR！,30枚')
        return 30
    elif marks == '🍎🍎🍎':
        print('Apple！８枚')
        return 8
    elif marks == 'ReplyReplyReply':
        print('Reply！')
        return 1
    elif marks[0:1] == '🍒':
        print('当たり！ 3枚')

        return 3
    else:
        print('ハズレ...')
        return -1

def calculate_coin(coin, bets, division):
    """掛けたコイン数（bets）と、配当倍率（division）を使用してプレーヤーの所持コイン数を精算する
    (This function is to be called to calculate (players's) coin.)

    Args:
        coin (int): プレーヤーの精算前の所持コイン数
        bets (int): 掛けコイン数
        division (int): 配当倍率

    Returns:
        int: 精算後のプレーヤーの所持コイン数
    """
    coin = coin + bets * division
    return coin


# ============================================================
# 実際にゲームを実行する
# ============================================================

# プレーヤーの所持コイン数

player_coin = int(player_coin)
count_777=int(0)
count_BAR=int(0)
show_start_message()
player_name = ask_player_name()

# if player_name in BONUS_PLAYER_AND_COINS:
#    player_coin = player_coin + BONUS_PLAYER_AND_COINS[player_name]
#elif player_name in SPECIAL_THANKS:
#    player_coin = player_coin + SPECIAL_THANKS_COIN

while player_coin > 0:
    bets = ask_bets(player_coin)
    marks = show_and_get_result()
    division = get_division(marks)
    player_coin = calculate_coin(player_coin, bets, division)
    
    if marks=='777':
        count_777=count_777+1 
    elif marks=='BARBARBAR':
        count_BAR=count_BAR+1 
    else:
        print('次は、777を狙え！')
        
    print('----------------------------------')
    game_count=game_count+1
    print('ゲームプレイ数は、'+str(game_count)+'です。')
    print('----------------------------------')

print('===================')
print('1) 777当選回数は、'+str(count_777)+'回目です。')
print('2) BAR当選回数は、'+str(count_BAR)+'回目です。')
print('===================')

print('ゲームオーバーです')
print(f'さようなら {player_name} さん')

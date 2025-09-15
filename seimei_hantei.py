def get_stroke_count(char):
    """文字の画数を取得する"""
    stroke_dict = {
        # ひらがな
        'あ': 3, 'い': 2, 'う': 3, 'え': 3, 'お': 3,
        'か': 3, 'き': 3, 'く': 2, 'け': 3, 'こ': 2,
        'が': 5, 'ぎ': 5, 'ぐ': 4, 'げ': 5, 'ご': 4,
        'さ': 3, 'し': 3, 'す': 2, 'せ': 3, 'そ': 3,
        'ざ': 5, 'じ': 5, 'ず': 4, 'ぜ': 5, 'ぞ': 5,
        'た': 4, 'ち': 3, 'つ': 3, 'て': 3, 'と': 2,
        'だ': 6, 'ぢ': 5, 'づ': 5, 'で': 5, 'ど': 4,
        'な': 4, 'に': 3, 'ぬ': 2, 'ね': 4, 'の': 1,
        'は': 3, 'ひ': 2, 'ふ': 4, 'へ': 1, 'ほ': 4,
        'ば': 5, 'び': 4, 'ぶ': 6, 'べ': 3, 'ぼ': 6,
        'ぱ': 6, 'ぴ': 5, 'ぷ': 7, 'ぺ': 4, 'ぽ': 7,
        'ま': 3, 'み': 3, 'む': 3, 'め': 3, 'も': 3,
        'や': 3, 'ゆ': 3, 'よ': 3,
        'ら': 2, 'り': 2, 'る': 2, 'れ': 2, 'ろ': 3,
        'わ': 3, 'ゐ': 4, 'ゑ': 4, 'を': 3, 'ん': 3,
        
        # カタカナ
        'ア': 2, 'イ': 2, 'ウ': 3, 'エ': 3, 'オ': 3,
        'カ': 3, 'キ': 3, 'ク': 2, 'ケ': 3, 'コ': 2,
        'ガ': 5, 'ギ': 5, 'グ': 4, 'ゲ': 5, 'ゴ': 4,
        'サ': 3, 'シ': 3, 'ス': 2, 'セ': 3, 'ソ': 3,
        'ザ': 5, 'ジ': 5, 'ズ': 4, 'ゼ': 5, 'ゾ': 5,
        'タ': 4, 'チ': 3, 'ツ': 3, 'テ': 3, 'ト': 2,
        'ダ': 6, 'ヂ': 5, 'ヅ': 5, 'デ': 5, 'ド': 4,
        'ナ': 4, 'ニ': 3, 'ヌ': 2, 'ネ': 4, 'ノ': 1,
        'ハ': 3, 'ヒ': 2, 'フ': 4, 'ヘ': 1, 'ホ': 4,
        'バ': 5, 'ビ': 4, 'ブ': 6, 'ベ': 3, 'ボ': 6,
        'パ': 6, 'ピ': 5, 'プ': 7, 'ペ': 4, 'ポ': 7,
        'マ': 3, 'ミ': 3, 'ム': 3, 'メ': 3, 'モ': 3,
        'ヤ': 3, 'ユ': 3, 'ヨ': 3,
        'ラ': 2, 'リ': 2, 'ル': 2, 'レ': 2, 'ロ': 3,
        'ワ': 3, 'ヰ': 4, 'ヱ': 4, 'ヲ': 3, 'ン': 3,
        
        # 基本的な漢字
        '田': 5, '中': 4, '山': 3, '川': 3, '木': 4, '林': 8, '森': 12,
        '水': 4, '火': 4, '土': 3, '金': 8, '石': 5, '竹': 6, '米': 6,
        '花': 7, '草': 9, '鳥': 11, '魚': 11, '犬': 4, '猫': 11,
        '人': 2, '大': 3, '小': 3, '子': 3, '女': 3, '男': 7,
        '一': 1, '二': 2, '三': 3, '四': 5, '五': 4, '六': 4, '七': 2, '八': 2, '九': 2, '十': 2,
        '太': 4, '郎': 9, '次': 6, '三': 3, '四': 5, '五': 4,
        '美': 9, '香': 9, '恵': 10, '愛': 13, '優': 17, '花': 7, '桜': 10,
        '健': 11, '雄': 12, '和': 8, '正': 5, '明': 8, '清': 11,
        '佐': 7, '藤': 18, '鈴': 13, '伊': 6, '松': 8, '竹': 6,
        '高': 10, '橋': 16, '小': 3, '野': 11, '渡': 12, '辺': 5
    }
    
    return stroke_dict.get(char, 10)  # デフォルト値として10を返す

def calculate_stroke_total(name):
    """名前の総画数を計算する"""
    return sum(get_stroke_count(char) for char in name)

def judge_fortune(count):
    """画数から運勢を判定する"""
    # 簡単な運勢判定ロジック
    if count in [1, 3, 5, 6, 7, 8, 11, 13, 15, 16, 17, 18, 21, 23, 24, 25, 29, 31, 32, 33, 35, 37, 39, 41, 45, 47, 48, 52, 57, 61, 63, 65, 67, 68, 73, 75]:
        return "大吉"
    elif count in [2, 9, 12, 14, 19, 22, 26, 28, 30, 34, 36, 38, 40, 42, 44, 46, 49, 51, 53, 55, 58, 60, 62, 64, 66, 69, 71, 74]:
        return "吉"
    elif count in [4, 10, 20, 27, 43, 50, 54, 56, 59, 70, 72]:
        return "凶"
    else:
        return "中吉"

def get_fortune_description(fortune):
    """運勢の説明を取得する"""
    descriptions = {
        "大吉": "非常に良好な運勢です。物事が順調に進むでしょう。",
        "吉": "良好な運勢です。努力が実を結びます。",
        "中吉": "安定した運勢です。堅実に進めば良い結果が得られます。",
        "凶": "注意が必要な運勢です。慎重な行動を心がけましょう。"
    }
    return descriptions.get(fortune, "普通の運勢です。")

def calculate_seimei_hantei(surname, given_name):
    """姓名判断を実行する"""
    
    # 画数計算
    surname_strokes = calculate_stroke_total(surname)
    given_name_strokes = calculate_stroke_total(given_name)
    
    # 五格計算
    # 天格（苗字の合計）
    tenkaku_count = surname_strokes
    
    # 人格（苗字の最後 + 名前の最初）
    surname_last_stroke = get_stroke_count(surname[-1]) if surname else 0
    given_name_first_stroke = get_stroke_count(given_name[0]) if given_name else 0
    jinkaku_count = surname_last_stroke + given_name_first_stroke
    
    # 地格（名前の合計）
    chikaku_count = given_name_strokes
    
    # 外格（総格 - 人格）
    soukaku_count = surname_strokes + given_name_strokes
    gaikaku_count = soukaku_count - jinkaku_count
    
    # 各格の運勢判定
    result = {
        'soukaku': {
            'count': soukaku_count,
            'fortune': judge_fortune(soukaku_count),
            'description': get_fortune_description(judge_fortune(soukaku_count)),
            'fortune_class': judge_fortune(soukaku_count).lower().replace('吉', 'good').replace('凶', 'bad').replace('大', 'excellent').replace('中', 'average')
        },
        'tenkaku': {
            'count': tenkaku_count,
            'fortune': judge_fortune(tenkaku_count),
            'description': get_fortune_description(judge_fortune(tenkaku_count)),
            'fortune_class': judge_fortune(tenkaku_count).lower().replace('吉', 'good').replace('凶', 'bad').replace('大', 'excellent').replace('中', 'average')
        },
        'jinkaku': {
            'count': jinkaku_count,
            'fortune': judge_fortune(jinkaku_count),
            'description': get_fortune_description(judge_fortune(jinkaku_count)),
            'fortune_class': judge_fortune(jinkaku_count).lower().replace('吉', 'good').replace('凶', 'bad').replace('大', 'excellent').replace('中', 'average')
        },
        'chikaku': {
            'count': chikaku_count,
            'fortune': judge_fortune(chikaku_count),
            'description': get_fortune_description(judge_fortune(chikaku_count)),
            'fortune_class': judge_fortune(chikaku_count).lower().replace('吉', 'good').replace('凶', 'bad').replace('大', 'excellent').replace('中', 'average')
        },
        'gaikaku': {
            'count': gaikaku_count,
            'fortune': judge_fortune(gaikaku_count),
            'description': get_fortune_description(judge_fortune(gaikaku_count)),
            'fortune_class': judge_fortune(gaikaku_count).lower().replace('吉', 'good').replace('凶', 'bad').replace('大', 'excellent').replace('中', 'average')
        }
    }
    
    return result
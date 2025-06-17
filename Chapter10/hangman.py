def hangman(word):
    wrong = 0 #不正解の数(変動)
    stages = ["",
             "________        ",
             "|               ",
             "|      |        ",
             "|      0        ",
             "|     /|\\      ",
             "|     / \\      ",
             "|               "
             ]
    rletters = list(word) #正解の文字をリスト化する
    board = ["__"] * len(word) #正解の文字数だけ__を量産
    win = False #勝敗判定リセット
    
    print(" ".join(board)) #答えの文字数表示
    print("ハングマンへようこそ") #挨拶
    
    #文字入力の判定処理
    while wrong < len(stages) - 1: #6回間違えるまで
        print("\n") #改行
        msg = "1文字を予想してね：" #入力
        char = input(msg) #入力値を代入
        if char in rletters: #入力値がリストにある＝あたっている場合
            #リストのインデックス取得して、差し替える
            cind = rletters.index(char) #取得
            board[cind] = char #同じ位置の回答欄を変更
            rletters[cind] = '$' #同じ文字がある場合のための処置
        else: #リストにない＝間違えた場合
            wrong += 1 #不正解数を増やす
        e = wrong + 1
        print("\n".join(stages[0:e]))
        
        #ゲームクリアした場合
        if "__" not in board: #クリア＝回答欄の__がなくなる
                print("あなたの勝ち！")
                print(" ".join(board)) #正解を表示
                win = True #winフラグをたてる
                break
    
    #ゲームオーバーの場合
    if not win: #ゲームオーバー＝終了時点でwinフラグがない
        print("\n".join(stages[0:wrong])) #ハングマン表示
        print("あなたの負け！正解は {}.".format(word)) #正解を表示


hangman("cat")

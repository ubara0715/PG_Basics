li_int = [12,32,1,26,44]

while True:
    s = input("数字を入力してください：")

    if s == "q":
        break

    try:
        s_int = int(s)
    except ValueError:
        print("数字を入力するか、qで終了します")
        continue

    if s_int in li_int:
        print("正解")
    elif s_int not in li_int:
        print("不正解")

s = input("What do you like color?：")

with open("challenge_txt02.txt","w",encoding="utf-8") as f:
    f.write(s)

with open("challenge_txt02.txt","r",encoding="utf-8") as g:
    print(g.read())

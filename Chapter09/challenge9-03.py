import csv


with open("challenge_csv01.csv","w",newline="") as f:
    w = csv.writer(f,delimiter=",")
    w.writerow(["Top Gun","Risky Business","Minority Report"])
    w.writerow(["Titanic","The Revenant","Inception"])
    w.writerow(["Training Day","Man on Fire","Flight"])

with open("challenge_csv01.csv","r") as f:
    f = csv.reader(f,delimiter=",")
    for row in f:
        print(",".join(row))

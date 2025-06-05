import csv


with open("challenge_csv02.csv","w",encoding="utf-8",newline="") as f:
    f = csv.writer(f,delimiter=",")
    f.writerow(["トップガン","リスキービジネス","マイノリティーレポート"])
    f.writerow(["タイタニック","ザレブナント","インセプション"])
    f.writerow(["トレーニングデイ","マンオンファイア","フライング"])

with open("challenge_csv02.csv","r",encoding="utf-8") as f:
    f = csv.reader(f,delimiter=",")
    for row in f:
        print(",".join(row))

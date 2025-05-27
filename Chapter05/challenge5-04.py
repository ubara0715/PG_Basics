profile = {"身長" : "161.5cm",
           "体重" : "45.8kg",
           "好きな色" : "深い青色"}

input_str = input("知りたい情報を入力してください：")
if input_str in profile:
    print(profile[input_str])
else:
    print("Not found")

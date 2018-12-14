import random

random_num = random.randint(1,5)

while True:
    num = int(input(&quot;1から５までの数字を入力してください。&quot;))

    if num ==random_num:
        print(&quot;あたりです。＆quot;)
        break
    else:
        print(&quot;外れました。&quot;)
        print(&quot;もう一度入力してください。&quot;)

    if count == 5:
        print("ゲームオーバー")
        break
        

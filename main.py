import re

dict = {'你好': '你好', '早上好': '早上好', '晚上好': '晚上好', '中午好': '中午好', '我好饿': '吃电池还是CPU?', '你饿吗?': '自己看电量！'
        ,'Are you OK?': 'I\'m very OK!'}
for i in range(20):
    ask = input()
    print(ask)
    axx: int = 0
    bxx = ''
    r1 = 0
    r2 = 0
    axt = 0
    tmp = 0
    for key in dict:
        right = 0
        i = 0
        r1 = 0
        print(key + ':' + dict[key])
        while i < len(ask):
            print (i, ask[i], key, re.search(ask[i], key))
            if type(re.search(ask[i], key)) != type(None):
                r1 += 1
                print(r1, 'aaa')
            i += 1
        if r1 > tmp:
            tmp = r1
            bxx = dict[key]
        else:
            pass
        print('tmp:', tmp)
        print(bxx)
    print('tmp:', tmp)
    print(bxx)

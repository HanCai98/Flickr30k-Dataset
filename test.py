dic = {}
dic['0'] = 'a'
dic['1'] = 'b'
dic['2'] = 'c'

result = {k:dic[k] for k in ('0','1') if k in dic}

print(dic)
print(result)
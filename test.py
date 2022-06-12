import execjs


import execjs
file = 'test.js'
ctx = execjs.compile(open(file).read())
print(ctx.call("encode","text=拥抱&page=1&type=migu"))
# print(params) # 12
# params = ctx.call('add',1,2)
# print(params) # 3
# if __name__ == '__main__':
#     ex
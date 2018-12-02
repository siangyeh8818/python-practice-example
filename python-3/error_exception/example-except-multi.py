import os 

try :
    f= open('test.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print('Clould not convert data to an integer')

#最后一个except子句可以忽略异常的名称，它将被当作通配符使用

except :
    print("Unexcepted error : ",sys.exc_info()[0])
    raise
else:
    print('轉換後的數字為 : ',i)

#try except 语句还有一个可选的else子句，如果使用这个子句，那么必须放在所有的except子句之后
#这个子句将在try子句没有发生任何异常的时候执行

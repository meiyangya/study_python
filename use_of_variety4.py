"""
运算符的使用

Version: 0.1
Author: 骆昊
"""

# a = 5
# b = 10
# c = 3
# d = 4
# e = 5
# a += b
# a -= c
# a *= d
# a /= e
# print("a = ", a)
# flag1=3>2
# flag2=2<1
# flag3=flag1 and flag2
# flag4=flag1 or flag2
# flag5=not flag1
# print("flag1 = ", flag1)
# print("flag2 = ", flag2)
# print("flag3 = ", flag3)
# print("flag4 = ", flag4)
# print("flag5 = ", flag5)
# print('flag1 is True')
# print(flag2 is not False)

"""
将华氏温度转换为摄氏温度
F = 1.8C + 32

Version: 0.1
Author: 骆昊
"""
"""
f=float(input('请输入华氏温度： '))
c=(f-32)/1.8
print('%.1f华氏度=%.1f摄氏度'%(f,c))
"""
"""
输入半径计算圆的周长和面积

Version: 0.1
Author: 骆昊
"""
# import math
# radius=float(input('请输入圆的半径： '))
# preimeter=2*math.pi*radius
# area=math.pi*radius*radius
# print('周长：%.2f'%preimeter)
# print('面积：%.2f'%area)
"""
输入年份 如果是闰年输出True 否则输出False

Version: 0.1
Author: 骆昊
"""
# year=int(input('请输入年份： '))
# is_leap=(year%4==0 and year%100!=0 or year%400==0)
# print(is_leap)

"""
用户身份验证

Version: 0.1
Author: 骆昊
"""

# username = input('请输入用户名: ')
#password = input('请输入口令: ')
# 如果希望输入口令时 终端中没有回显 可以使用getpass模块的getpass函数
# import getpass
# password = getpass.getpass('请输入口令: ')
# if username=='admin' and password=='12345':
	# print('身份验证成功')
# else:
	# print('身份验证失败')
"""
分段函数求值

        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)

Version: 0.1
Author: 骆昊
"""
# x=float(input('x= '))
# if x>1:
	# y=3*x-5
# elif x>=-1:
	# y=x+2
# else:
	# y=5*x+3
# print('f(%.2f)=%.2f'%(x,y))

"""
英制单位英寸和公制单位厘米互换

Version: 0.1
Author: 骆昊
"""
# value=float(input('请输入长度： '))
# unit=input('请输入单位： ')
# if unit =='in' or unit=='英寸':
	# print('%f英寸==%f厘米'%(value,value*2.54))
# elif  unit =='cm' or unit=='厘米':
	# print('%f厘米==%f英寸'%(value,value/2.54))
# else:
	# print('请输入有效的单位')
"""
掷骰子决定做什么事情

Version: 0.1
Author: 骆昊
下面的代码中使用了random模块的randint函数生成指定范围的随机数来模拟掷骰子
"""
# from random import randint
# face=randint(1,6)
# if face ==1:
	# result='唱首歌'
# elif face==2:
	# result = '跳个舞'
# elif face == 3:
    # result = '学狗叫'
# elif face == 4:
    # result = '做俯卧撑'
# elif face == 5:
    # result = '念绕口令'
# else:
    # result = '讲冷笑话'
# print(result)
"""
判断输入的边长能否构成三角形
如果能则计算出三角形的周长和面积

Version: 0.1
Author: 骆昊
"""
# import math
# a=float(input('a= '))
# b = float(input('b = '))
# c = float(input('c = '))
# if a+b>c and a+c>b and b+c>a:
	# l=a+b+c
	# p=l/2
	# s=math.sqrt(p*(p-a)*(p-b)*(p-c))
	# print('周长：%f面积： %f'%(l,s))
# else:
	# print('不能构成三角形')
	# 上面的代码中使用了math模块的sqrt函数来计算平方根。用边长计算三角形面积的公式叫做海伦公式。
"""
输入月收入和五险一金计算个人所得税

Version: 0.1
Author: 骆昊
"""
# salary=float(input('请输入工资： '))
# insurance=float(input('请输入五险一金： '))
# diff=salary-insurance-3500
# if diff<=0:
	# rate=0
	# deduction=0
# elif diff<1500:
	# rate=0.03
	# deduction=0
# elif diff < 4500:
    # rate = 0.1
    # deduction = 105
# elif diff < 9000:
    # rate = 0.2
    # deduction = 555
# elif diff < 35000:
    # rate = 0.25
    # deduction = 1005
# elif diff < 55000:
    # rate = 0.3
    # deduction = 2755
# elif diff < 80000:
    # rate = 0.35
    # deduction = 5505
# else:
    # rate = 0.45
    # deduction = 13505
# tax=abs(diff*rate-deduction)
# print('个人所得税: ￥%.2f元' % tax)
# print('实际到手收入: ￥%.2f元' % (diff + 3500 - tax))
"""
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了

Version: 0.1
Author: 骆昊
"""
# import random
# answer=random.randint(1,100)
# counter=0
# while True:
	# counter+=1
	# number=int(input('请猜一个数字： '))
	# if number>answer:
		# print('大了')
	# elif number<answer:
		# print('小了')
	# else:
		# print('猜对了')
		# break
# print('一共猜了%d次'%counter)
# if counter > 7:
    # print('你的智商余额明显不足')

# """
# 用for循环实现1~100之间的偶数求和

# Version: 0.1
# Author: 骆昊
# """
# sum =0
# for x in range(2,101,2):
	# sum +=x
# print (sum)
"""
输出乘法口诀表(九九表)

Version: 0.1
Author: 骆昊
"""
# sum=0
# for x in range(1,10):
	# for y in range(1,x+1):
		# sum=x*y
		# print('%d * %d = %d'%(x,y,sum))
"""
输入一个正整数判断它是不是素数

Version: 0.1
Author: 骆昊
Date: 2018-03-01
"""
# from math import sqrt
# num =int(input('请输入一个正整数： '))
# end =int(sqrt(num))
# is_prime=True
# for x in range(2,end+1):
	# if num%x==0:
		# is_prime=False
		# break
# if is_prime and num!=1:
	# print('%d是素数'%num)
# else:
	# print('%d是不是素数'%num)
		
"""
输入两个正整数计算最大公约数和最小公倍数

Version: 0.1
Author: 骆昊
Date: 2018-03-01
"""
# x = int(input('x = '))
# y = int(input('y = '))
# if x>y:
	# x,y=y,x
# for factor in range (x,0,-1):
	# if x%factor==0 and y%factor==0:
		# print('%d和%d的最大公约数是%d' % (x, y, factor))
		# print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
		# break
"""
打印各种三角形图案

*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********

Version: 0.1
Author: 骆昊
"""
row = int(input('请输入行数: '))
for x in range(0,row):
	#print('x')
	for y in range(0,x+1):
		print('*',end='')
		#print(y)
	print('')
for x in range(0,row):
	
	for y in range(row-x+1,0,-1):
		print(' ',end='')
		#print(y)
	print('*'*(x+1))
for x in range(1,row+1):
	
	for y in range(row-x+1,0,-1):
		print(' ',end='')
		#print(y)
	print('*'*(2*x-1))


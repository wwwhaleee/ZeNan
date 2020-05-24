import turtle as t
import datetime as d
def time_show():
    def drawGap():  # 绘制数码管间隔
        t.penup()
        t.fd(5)
    def drawLine(draw):  # 绘制单段数码管
        drawGap()
        t.pendown() if draw else t.penup()
        t.fd(15)
        drawGap()
        t.right(90)
    def drawDight(d):  # 根据数字绘制七段数码管
        drawLine(True) if d in [2, 3, 4, 5, 6, 8, 9] else drawLine(False)
        drawLine(True) if d in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawLine(False)
        drawLine(True) if d in [0, 2, 3, 5, 6, 8, 9] else drawLine(False)
        drawLine(True) if d in [0, 2, 6, 8] else drawLine(False)
        t.left(90)
        drawLine(True) if d in [0, 4, 5, 6, 8, 9] else drawLine(False)
        drawLine(True) if d in [0, 2, 3, 5, 6, 7, 8, 9] else drawLine(False)
        drawLine(True) if d in [0, 1, 2, 3, 4, 7, 8, 9] else drawLine(False)
        t.left(180)
        t.penup()
        t.fd(10)
    def drawDate(date):
        for i in date:#设置‘年’、‘月’、‘日’的显示
            if i == '-':
                t.write('年', font=('Arial', 20, 'normal'))#宋体，字体大小为20，字体类型normal
                t.fd(50)
            elif i == '=':
                t.write('月', font=('Arial', 20, 'normal'))
                t.fd(50)
            elif i == '*':
                t.write('日', font=('Arial', 20, 'normal'))
                t.fd(50)
            else:
                drawDight(eval(i))
        t.write(d.datetime.now().strftime('郑泽楠'), font=('Arial', 25, 'normal'))#显示作者名字
    def main_time():#时间显示的主函数
        t.pu()
        t.setheading(0)
        t.goto(130, 300)
        t.fd(-400)
        t.pensize(5)
        t.color("#CAE1FF")
        drawDate(d.datetime.now().strftime('2020-05=23*'))#显示作品是2020年5月23日绘画的
    main_time()#运行时间显示的函数
def greenland():#背景草地
    t.penup()
    t.setheading(70)
    t.speed(10)#设置画笔速度
    t.color("#71C671")#一种绿色
    t.goto(-700, -700)#定位
    t.pendown()
    t.left(20)
    t.begin_fill()#开始填充颜色
    t.circle(-700, 180)#画一个半径为700像素的ban
    t.end_fill()#停止填充颜色
    t.speed(6)
def pig_head():#猪头的函数
    t.color("#EF89C6", "#FEB2E1")#猪边缘的颜色以及填充的颜色
    t.pensize(6)
    t.penup()
    t.goto(-65,170)
    t.setheading(0)
    t.pendown()
    t.begin_fill()#开始填充颜色
    t.setheading(180)
    t.circle(300, -30)#画猪头边缘所需各种各样的圆弧
    t.circle(100, -60)
    t.circle(80, -100)
    t.circle(150, -20)
    t.circle(60, -100)
    t.setheading(155)
    t.circle(-200, 25)
    t.end_fill()#结束填充
def pig_nose():#猪的鼻子函数
    t.color("#EF89C6", "#FEB2E1")#猪边缘的颜色以及填充的颜色
    t.begin_fill()
    for i in [160, 324]:#猪鼻边缘绘画的数据
        t.right(i)
        t.circle(40,10)
        t.left(20)
        t.circle(40, 10)
        t.left(10)
        t.circle(60, 10)
        t.left(10)
        t.circle(40, 30)
        t.left(10)
        t.circle(60, 10)
        t.left(10)
        t.circle(60, 15)
    t.end_fill()
    #猪鼻孔代码
    t.penup()
    t.goto(-85,148)#右鼻孔位置
    t.color('#D766A6')
    t.pendown()
    t.circle(2)#画个半径为2像素的圆
    t.penup()
    t.goto(-72, 144)#左鼻孔位置
    t.pendown()
    t.circle(2)
def pig_eyes():#猪的眼睛函数
    #右眼
    t.penup()
    t.goto(20, 148)
    t.color("#EF89C6","white")# 猪眼眶的颜色以及眼球的颜色
    t.begin_fill()#开始填充颜色
    t.pendown()
    t.circle(-15)#向右画一个半径为15像素的圆
    t.end_fill()#结束填充颜色
    t.penup()
    t.goto(7,135)#右眼眼珠的位置
    t.color('black')#设置画笔为黑色
    t.pendown()
    t.circle(2)
    #左眼
    t.penup()
    t.goto(60, 130)
    t.color("#EF89C6","white")
    t.begin_fill()
    t.pendown()
    t.circle(-15)
    t.end_fill()
    t.penup()
    t.goto(45, 117)#左眼眼珠的位置
    t.color('black')
    t.pendown()
    t.circle(2)
def pig_mouse():
    t.penup()
    t.pensize(7)
    t.goto(-10, 50)#嘴角的位置
    t.right(10)#向右转10度
    t.color('#D9458C')
    t.pd()#turtle.pendown()另一种写法
    t.circle(45, 130)
def pig_face():
    t.pu()#turtle.penup()另一种写法
    t.goto(80,70)
    t.color("#FD8ED3")
    t.pd()
    t.begin_fill()
    t.circle(-20)
    t.end_fill()
def pig_ears():#猪耳朵函数
    t.setheading(0)
    def ear():#耳朵函数，后面直接调用
        t.pd()
        t.color("#EF89C6", "#FEB2E1")#猪耳边缘颜色以及填充的颜色
        t.begin_fill()
        t.left(56)
        t.fd(30)
        t.circle(-25, 45)
        t.right(20)
        t.circle(-25, 50)
        t.right(20)
        t.circle(-25, 50)
        t.right(10)
        t.fd(35)
        t.end_fill()
    #右耳
    t.pu()
    t.left(20)
    t.pensize(5)
    t.goto(42,145)
    ear()
    # 左耳
    t.pu()
    t.left(120)
    t.goto(90, 125)
    ear()
def pig_body():#猪身体绘画函数
    t.pu()
    t.pensize(7)
    t.setheading(0)
    t.color("#E72E42","#E95A60")
    t.goto(-10, -17)
    t.begin_fill()
    t.pd()
    t.right(122)
    t.circle(250,15)
    t.circle(300,15)
    t.setheading(0)
    t.fd(210)
    t.left(92)
    t.circle(300, 15)
    t.circle(250, 18)
    t.end_fill()
    t.pensize(5)
def pig_hands():
    t.setheading(0)#将画笔角度置于默认值
    t.pensize(10)
    t.color("#FCB8E1")
    #画右手
    t.right(170)
    t.pu()
    t.goto(-28,-40)
    t.pd()
    t.circle(200,20)
    #画左手
    t.pu()
    t.right(230)
    t.goto(132, -40)
    t.pd()
    t.circle(-200, 20)
    def fingers(a, b, c):#定义画手指的函数
        t.pu()
        t.setheading(0)
        t.left(a)
        t.goto(b, c)
        t.pd()
        t.fd(10)
        t.circle(-10, 90)
        t.fd(10)
    fingers(-20, -85, -45)#左手指
    fingers(90, 170, -78)#右手指
    t.pensize(5)
def pig_feet():#猪脚函数
    def foot(a, b):#定义函数脚的形状
        #画腿
        t.pensize(10)
        t.setheading(-90)
        t.pu()
        t.goto(a, b)
        t.pd()
        t.fd(35)
        t.right(95)
        #绘画鞋子
        t.color("black")
        j = i = 0
        while j < 20:#该循环可以逐渐加大画笔的粗度
            j = j + 2
            t.fd(3.5)
            if j % 10:
                i = i + 1
                t.pensize(6 + i)
        t.color("#FCB8E1")
    foot(110, -160)#左脚位置
    foot(20, -160)#右脚位置
    t.pensize(5)
def pig_tail():#猪尾巴函数
    t.pensize(8)
    t.color("#FCB8E1")
    t.setheading(0)
    t.pu()
    t.goto(155, -125)#尾巴位置
    t.pd()
    t.circle(50, 15)
    t.circle(20, 60)
    t.circle(7,200)
    t.circle(15,140)
def main():#主函数
    t.hideturtle()#隐藏画笔turtle
    t.pensize(5)#设置画笔大小
    t.speed(10)#设置绘画速度
    t.screensize(600,200,'#46BCEE')#设置背景颜色和画布大小
    t.setup(580,700)#设置初始画框
    greenland()#画草地
    pig_ears()#画耳朵
    pig_tail()#画尾巴
    pig_body()#画身体
    pig_head()#画头
    pig_nose()#画鼻子
    pig_eyes()#画眼睛
    pig_mouse()#画嘴巴
    pig_face()#画脸
    pig_hands()#画手
    pig_feet()#画脚
    time_show()#显示绘画时间
    t.done()#让turtle面板不会关闭
main()#运行函数
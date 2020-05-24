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
        for i in date:
            if i == '-':
                t.write('年', font=('Arial', 20, 'normal'))
                t.fd(50)
            elif i == '=':
                t.write('月', font=('Arial', 20, 'normal'))
                t.fd(50)
            elif i == '*':
                t.write('日', font=('Arial', 20, 'normal'))
                t.fd(50)
            else:
                drawDight(eval(i))
        t.write(d.datetime.now().strftime('郑泽楠'), font=('bold', 25, 'normal'))
    def main_time():
        t.pu()
        t.setheading(0)
        t.goto(130, 300)
        t.fd(-400)
        t.pensize(5)
        t.color("#CAE1FF")
        drawDate(d.datetime.now().strftime('%Y-%m=%d*'))
    main_time()
def greenland():#背景草地
    t.penup()
    t.speed(10)
    t.color("#71C671")
    t.goto(-220, -50)
    t.pendown()
    t.left(20)
    t.begin_fill()
    t.circle(-700)
    t.end_fill()
    t.speed(6)
def pig_head():#猪头的函数
    t.color("#EF89C6", "#FEB2E1")#猪边缘的颜色以及填充的颜色
    t.pensize(6)
    t.penup()
    t.goto(-65,170)
    t.setheading(0)
    t.pendown()
    t.begin_fill()
    t.setheading(180)
    t.circle(300, -30)
    t.circle(100, -60)
    t.circle(80, -100)
    t.circle(150, -20)
    t.circle(60, -100)
    t.setheading(155)
    t.circle(-200, 25)
    t.end_fill()
def pig_nose():#猪的鼻子函数
    t.color("#EF89C6", "#FEB2E1")#猪边缘的颜色以及填充的颜色
    t.begin_fill()
    for i in [160, 324]:
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
    t.goto(-85,148)
    t.color('#D766A6')
    t.pendown()
    t.circle(2,360)
    t.penup()
    t.goto(-72, 144)
    t.pendown()
    t.circle(2,360)
def pig_eyes():#猪的眼睛函数
    # 猪眼睛边缘的颜色以及眼球的颜色
    #右眼
    t.penup()
    t.goto(20, 148)
    t.color("#EF89C6","white")
    t.begin_fill()
    t.pendown()
    t.circle(-15,360)
    t.end_fill()
    t.penup()
    t.goto(7,135)
    t.color('black')
    t.pendown()
    t.circle(2,360)
    #左眼
    t.penup()
    t.goto(60, 130)
    t.color("#EF89C6","white")
    t.begin_fill()
    t.pendown()
    t.circle(-15, 360)
    t.end_fill()
    t.penup()
    t.goto(45, 117)
    t.color('black')
    t.pendown()
    t.circle(2, 360)
def pig_mouse():
    t.penup()
    t.pensize(7)
    t.goto(-10, 50)
    t.right(10)
    t.color('#D9458C')
    t.pd()
    t.circle(45, 130)
def pig_face():
    t.pu()
    t.goto(80,70)
    t.color("#FD8ED3")
    t.pd()
    t.begin_fill()
    t.circle(-20,360)
    t.end_fill()
def pig_ears():#猪耳朵函数
    def ear():#耳朵函数，后面直接调用
        t.pd()
        t.color("#EF89C6", "#FEB2E1")
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
    t.pensize(5)
    t.goto(42,145)
    ear()
    # 左耳
    t.pu()
    t.left(120)
    t.goto(90, 125)
    ear()
def pig_body():
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
    t.setheading(0)
    t.pensize(10)
    t.color("#FCB8E1")
    #右手
    t.right(170)
    t.pu()
    t.goto(-28,-40)
    t.pd()
    t.circle(200,20)
    #左手
    t.pu()
    t.right(230)
    t.goto(132, -40)
    t.pd()
    t.circle(-200, 20)
    #画左手指
    def fingers(a, b, c):
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
def pig_feet():
    def foot(a, b):#定义函数画脚
        t.pensize(10)
        t.setheading(-90)
        t.pu()
        t.goto(a, b)
        t.pd()
        t.fd(35)
        t.right(95)
        t.color("black")
        j = i = 0
        while j < 20:
            j = j + 2
            t.fd(3.5)
            if j % 10:
                i = i + 1
                t.pensize(6 + i)
        t.color("#FCB8E1")
    foot(110, -160)#左脚
    foot(20, -160)#右脚
    t.pensize(5)
def pig_tail():
    t.pensize(8)
    t.color("#FCB8E1")
    t.setheading(0)
    t.pu()
    t.goto(155, -125)
    t.pd()
    t.circle(50, 15)
    t.circle(20, 60)
    t.circle(7,200)
    t.circle(15,140)
def main():#主函数
    t.hideturtle()
    t.pensize(5)
    t.speed(100)
    t.screensize(60,20,'#46BCEE')
    t.setup(580,700)
    greenland()
    pig_ears()
    pig_tail()
    pig_body()
    pig_head()
    pig_nose()
    pig_eyes()
    pig_mouse()
    pig_face()
    pig_hands()
    pig_feet()
    time_show()
    t.done()
main()
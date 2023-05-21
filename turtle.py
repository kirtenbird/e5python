import turtle as t
t.screensize(400,400,'blue')
t.speed(10)
t.pensize(10)
colorList = ["red","purple","yellow","green","white"]
for i in range(1,6):
    t.penup() #画笔抬起
    t.sety(-30*i)     # sety()保持x不变，修改y，小海龟的位置依次为(0,-30)、(0,-60)、(0,-90)......
    t.pendown() # 画笔放下
    t.pencolor(colorList[i-1]) #选择画笔颜色
    t.circle(30*i)  #绘制半径为30,60,90...的圆
else:
    t.hideturtle()     # 画完同心圆之后，隐藏小海龟

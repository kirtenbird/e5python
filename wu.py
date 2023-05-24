# 画五角星
import turtle as t
t.screensize(800,600,"yellow")
t.setup(400,400)
t.pencolor("red")
t.fillcolor("red") #颜色填充函数
t.begin_fill()
while True:
    t.forward(150)
    t.right(144)
    if abs(t.pos()) < 1:#看画笔是否回到原点，回到原点为真
        break
t.end_fill()
t.hideturtle()


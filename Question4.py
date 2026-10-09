# Question 4
from graphics import *


#create new window
win = GraphWin("Button Test", 400, 300)

#draw button
button = Rectangle(Point(100, 100), Point(250, 160))
button.draw(win)

def button_clicked(click):
    x = click.getX()
    y = click.getY()

    if 100 <= x <= 250 and 100 <= y <= 160:
        return True
    else:
        return False

message = Text(Point(200, 220), "")
message.draw(win)

for i in range(10):
    click = win.getMouse()

    if button_clicked(click):
        message.setText("Button clicked!")
    else:
        message.setText("Button not clicked.")


win.getMouse()
win.close()

from graphics import *

win = GraphWin("Idle/Incremental Game", 1000, 500)

win.setCoords(0, 0, 10, 10)

center = Point(5, 5)

head = Image(center, "Base Head.gif")
shirt = Image(center, "Base Shirt.gif")
pants = Image(center, "Base Pants.gif")
sword = Image(center, "Stone Sword.gif")

head.draw(win)
shirt.draw(win)
pants.draw(win)
sword.draw(win)


win.getMouse()
win.close()

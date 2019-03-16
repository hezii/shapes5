from graphics import *

winX = 700
winY = 600
shapesWin = GraphWin("Shapes 5", winX,winY)
shapesWin.setCoords(0,0,winX,winY)


dSize = 50
bDia = Polygon(Point(winX/2-dSize,winY/2),
                Point(winX/2,winY/2+dSize),
                Point(winX/2+dSize,winY/2),
                Point(winX/2,winY/2-dSize))
bDia.setFill(color_rgb (30, 30, 230))
bDia.draw(shapesWin)

rTri = Polygon(Point(50, winY - 5),
               Point(100, winY - 100),
               Point(5, winY - 100))
rTri.setFill(color_rgb(255,0,0))
rTri.draw(shapesWin)

gCircle = Circle(Point(55, 55), 50)
gCircle.setFill(color_rgb (0, 255,0))
gCircle.draw(shapesWin)


shapesWin.getMouse()
shapesWin.close()
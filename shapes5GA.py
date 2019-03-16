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

shapesWin.getMouse()
shapesWin.close()
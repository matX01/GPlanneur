import pyglet
# import all of opengl functions
from pyglet.gl import *

win = pyglet.window.Window()
a = 0

@win.event
def on_draw():
    global a
    a+= 0.001
    # create a line context
    glBegin(GL_LINES)
    # create a line, x,y,z
    glVertex3f(100.0,100.0,0.25+a)
    glVertex3f(200.0,300.0,-0.75)
    
    glEnd()




pyglet.app.run()

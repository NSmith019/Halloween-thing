import random

def setup():
    global img
    global ghost1
    global ghost2
    global y2
    global y
    size(1366, 768)
    img = loadImage("haunted-house-md.png")
    ghost1 = loadImage("ghostie.png")
    ghost2 = loadImage("ghostieflip.png")
    background(102,51,153)
    y = 150
    y2 = 200

def draw():
    noStroke()
    fill(102,51,153,15)
    rect(0,0,1366,768)
    fill(255)
    ellipse(random.randrange(width), random.randrange(height), 10, 10)
    #moon
    fill(248, 248, 255)
    ellipse(680, 468, 700, 700)
    #house
    image(img, 550, 175)
    #ground
    fill(0)
    ellipse(680,768,1500,600)
    #door
    fill(255)
    ellipse(690,425,30,30)
    rect(675,425,30,40)
    #ghosts
    global y
    global y2
    global y2_speed
    global y_speed
    if y == 150:
        y_speed = 1
    elif y > 220:
        y_speed = -1
    y += y_speed
    if y2 == 200:
        y2_speed = 1
    elif y2 > 270:
        y2_speed = -1
    y2 += y2_speed
    image(ghost1, 150, y, 100, 100)
    image(ghost2, 1000, y2, 150, 150)
    
    

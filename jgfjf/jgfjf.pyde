import random

def setup():
    global img
    size(1366, 768)
    img = loadImage("haunted-house-md.png")
    background(102,51,153)

def draw():
    noStroke()
    fill(102,51,153,15)
    rect(0,0,1366,768)
    fill(255)
    ellipse(random.randrange(width), random.randrange(height), 10, 10)
    ellipse(680, 468, 700, 700)
    #house
    image(img, 550, 175)
    #moon
    fill(0)
    ellipse(680,768,1500,600)
    #door
    fill(255)
    ellipse(690,425,30,30)
    rect(675,425,30,40)
    
    
    

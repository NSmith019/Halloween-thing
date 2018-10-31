x = 0
witch_y = 200
page = 0
time = 0
def setup():
    global img
    global ghost1
    global ghost2
    global stars
    global y2
    global y
    global ditto
    global pumps
    global witch
    global x
    global hhouse
    global hall
    global sans
    size(1366, 768)
    img = loadImage("haunted-house-md.png")
    ghost1 = loadImage("ghostie.png")
    ghost2 = loadImage("ghostieflip.png")
    stars = loadImage("stars.png")
    ditto = loadImage("huuhu2.png")
    pumps = loadImage("pumps.png")
    witch = loadImage("witch.png")
    hhouse = loadImage("hhouse.jpg")
    hall = loadImage("hall.jpg")
    sans = loadImage("sans.png")
    background(102,51,153)
    y = 150
    y2 = 200
def draw():
    if page == 0:
        noStroke()
        background(102,51,153)
        #stars
        image(stars, -50, -200)
        #ghosts
        global y
        global y2
        global y2_speed
        global y_speed
        if y == 150:
            y_speed = 0.2
        elif y > 170:
            y_speed = -0.2
        y += y_speed
        if y2 == 200:
            y2_speed = 0.5
        elif y2 > 220:
            y2_speed = -0.5
        y2 += y2_speed
        image(ghost1, 150, y, 100, 100)
        image(ghost2, 1000, y2, 150, 150)
        #moon
        fill(248, 248, 255)
        ellipse(680, 450, 600, 600)
        #house
        image(img, 550, 175)
        #ground
        fill(0)
        ellipse(680,768,1500,600)
        #door
        fill(255)
        ellipse(690,425,30,30)
        rect(675,425,30,40)
        #text
        image(ditto, 1000, 450)
        fill("#ffffff")
        ellipse( 830, 600, 400, 200)
        fill(0)
        textSize(24);
        text("lets explore this house!", 690, 605);
        #witch
        global x
        global witch_y
        if x >= 3000 and witch_y <= 100:
            x = -100
            witch_y = 200
        x += 10
        witch_y -= 2
        image(witch, x, witch_y, 100, 100)
        
    elif page == 1:
        image(hall, 0, 0, 1400, 800)
        image(ditto, 1000, 450)
        fill("#ffffff")
        ellipse( 830, 600, 400, 200)
        fill(0)
        textSize(24);
        text("spooky!", 690, 605);
        
    elif page == 2:
        image(hhouse, 0, 0, 1400, 800)
        image(ditto, 1000, 450)
        fill("#ffffff")
        ellipse( 830, 600, 400, 200)
        fill(0)
        textSize(24);
        text("i am freaked out", 690, 605);
        global time
        time += 2
        if time >= 100:
            global sans
            image(sans, 200,-40)
        
    elif page == 3:
        background(0)
        
def mousePressed():
    global page
    page += 1
    if page == 3:
        page = 0

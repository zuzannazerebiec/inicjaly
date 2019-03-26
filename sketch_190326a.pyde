def setup() :
    size(400, 400)
    textSize(128)
    textAlign(CENTER)
def draw() :
    if mousePressed:
        text("Z", width/2-75, height/2)
        text("X", width/2+20, height/2)
    
    if keyPressed:
        if key == "z" or key == "Z":
            fill(0,255,0)
            text("Z", width/2-75, height/2)
            fill(0)
            
        elif key == "x" or key == "X":
            fill(255,0,0)
            text("X", width/2+20, height/2)
            fill(255)
            
    if keyCode == 39:
        fill(0, 0, 255)
        text("X", width/2+20, height/2)
        fill(255)
    if keyCode == 37:
        fill (255,0,0)
        text("X", width/2+20, height/2)
        fill(0)
            
       

        
    s = createShape()
    s.beginShape()
    s.fill(0, 0, 255, 100)
    s.noStroke()
    s.vertex(50, (height/4)*3)
    s.vertex(width/2-20, (height/4)*3+30)
    s.vertex(width/2, (height/4)*3)
    s.vertex(width/2+20, (height/4)*3-30)
    s.vertex(width-50, (height/4)*3)
    s.endShape(CLOSE)
    shape(s, 25, 25)

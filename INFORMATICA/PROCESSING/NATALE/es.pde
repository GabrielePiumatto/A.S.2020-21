void setup() {
    size(500, 500);
    background(0);
}

void draw() {
  fill(21, 255, 0);
  triangle(250, 125, 175, 275, 325, 275);
  
  fill(21, 255, 0);
  triangle(250, 85, 175, 235, 325, 235);
  
  fill(21, 255, 0);
  triangle(250, 45, 175, 195, 325, 195);
  
  fill(255,0,0);
  ellipse(125, 125, 50, 50);
  
  fill(255);
  ellipse(400, 300, 50, 50);
  
  fill(255,255,0);
  ellipse(350, 100, 50, 50);
  
  fill(0,0,255);
  ellipse(100, 350, 50, 50);
  
  fill(71, 46, 16);
  rect(225,275,50,50);
  
  textAlign(CENTER, BOTTOM);
  fill(255,0,0);
  textSize(24);
  text("Auguri di Buon Natale!!!", width/2, 450);
}

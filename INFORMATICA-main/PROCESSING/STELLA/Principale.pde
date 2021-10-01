Albero a1, a2;

int y = -85;

int tr1x0 = 50;
int tr1x1 = 150;
int tr2x0 = 140;
int tr2x1 = 180;
int tr2x2 = 160;
public int speed = 1;

public void setup()
{
  a1 = new Albero(width/3, 260, width/8, height/2);
  a2 = new Albero(2*width/3, 260, width/8, height/2);
  background(0);
}

public void settings() {
   size (550, 300);
}

public void draw(){
  a1.draw();
  a2.draw();
  fill(71, 46, 16);
  rect(width/3-12.5, 260, 25, 40);
  rect(2*width/3-12.5, 260, 25, 40);
  fill(255,240,0);
  triangle(tr1x0,80, tr1x0,30, tr1x1, 55);
  triangle(tr2x0,70, tr2x1,70, tr2x2, 30);
  triangle(tr2x0,40, tr2x1,40, tr2x2, 80);
  
  if(tr1x0 > width + 200 || tr1x0 < -200) {
    speed = speed * -1;
  }
  tr1x0 = tr1x0 + speed;
  
  if(tr1x1 > width +200 || tr1x1 < -50) {
    speed = speed * -1;
  }
  tr1x1 = tr1x1 + speed;
  
  if(tr2x0 > width +200 || tr2x0 < -50) {
    speed = speed * -1;
  }
  tr2x0 = tr2x0 + speed;
  
  if(tr2x1 > width +200 || tr2x1 < -50) {
    speed = speed * -1;
  }
  tr2x1 = tr2x1 + speed;
  
  if(tr2x2 > width + 150 || tr2x2 < -50) {
    speed = speed * -1;
  }
  tr2x2 = tr2x2 + speed;
}

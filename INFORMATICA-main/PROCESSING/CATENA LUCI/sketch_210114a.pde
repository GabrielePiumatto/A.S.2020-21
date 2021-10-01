Catena c1;

public void setup() {
  size(800,800);
  c1 = new Catena();
}

public void draw() {
  c1.draw();
}

public void mousePressed() {
  for(int k=0; k<8; k++) {
    c1.luce[k].ispremuto(mouseX, mouseY);
  }
}

class Luci{
  private float x;
  private float y;
  private float r;
  private boolean acceso;
  private final static color LUCE_ON = #fff000;
  private final static color LUCE_OFF = #c0c0c0;
  
  Luci(float x, float y, float r, boolean acceso) {
    this.x = x;
    this.y = y;
    this.r = r;
    this.acceso = acceso;
  }
  
  public void draw() {
    if(acceso) {
      fill(LUCE_ON);
    }
    else {
      fill(LUCE_OFF);
    }
    circle(x,y,r*2);
  }
  
  public boolean ispremuto(int mx, int my) {
    float dx = mx-x;
    float dy = my-y;
    boolean ris = false;
    
    if(dx*dx+dy*dy < r*r) {
      acceso = !acceso;
      ris = true;
    }
    return ris;
  }
}

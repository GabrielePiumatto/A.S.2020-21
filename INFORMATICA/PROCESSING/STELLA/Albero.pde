class Albero{
  private float x;
  private float y;
  private float h;
  private float w;
  
  Albero(float x, float y, float w, float h){
    this.x = x;
    this.y = y;
    this.h = h;
    this.w = w;
  }
  
  public void draw(){
    fill(34, 117, 30);
    triangle(x-w/2, y, x, y-h, x+w/2, y);
  }
}

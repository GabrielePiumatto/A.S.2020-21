class Catena{
  public Luci[]luce;
  private static final int n=8;
  
  public Catena() {
    luce = new Luci[n];
    for(int i=0; i<n; i++) {
      luce[i] = new Luci(i*width/8+50, height/2, 50, true);
    }
  }
  
  public void draw() {
    for(int j=0; j<n; j++) {
      luce[j].draw();
    }
  }
}

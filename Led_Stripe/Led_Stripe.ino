int green = 11;
int red = 12;
int blue = 13;
int a[2][4] = {122,244,0,1000,0,0,244,500};
void setup()
{
  pinMode(green, OUTPUT);
  pinMode(blue, OUTPUT);
  pinMode(red, OUTPUT);
}

void setcolour(int r, int g, int b)
{
  analogWrite(red,255-r);
  analogWrite(green,255-g);
  analogWrite(blue,255-b);
}

void turnlightOn(int a[])
{
  setcolour(a[0],a[1],a[2]);
  delay(a[3]);
  
}
void loop()
{
  for(int i =0; i< sizeof(a)/sizeof(a[i]); i++){
  turnlightOn(a[i]);
  }
}

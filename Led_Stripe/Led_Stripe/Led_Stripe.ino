int green = 11;
int red = 12;
int blue = 13;
int a[][4] = {
  {122,244,0,1000},
  {0,0,244,100}
      };
String incomingByte = " ";
void setup()
{
  pinMode(green, OUTPUT);
  pinMode(blue, OUTPUT);
  pinMode(red, OUTPUT);
  Serial.begin(9600);  
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
  while (Serial.available() > 0) 
  { //监测串口缓存，当有数据输入时，循环赋值给incomingByte
    incomingByte += char(Serial.read());//读取单个字符值，转换为字符，并按顺序一个个赋值给incomingByte
    delay(2);//不能省略，因为读取缓冲区数据需要时间
  }
    if (Serial.available() > 0) 
  { 
     //读取输入的字符，转换为字符，并赋值给incomingByte
  if (incomingByte == "11")
      {
    turnlightOn(a[0]);
      Serial.print(incomingByte+"\n");
      incomingByte = " "; //清空变量，准备下次输入
    }
  else
        {
    turnlightOn(a[1]);
      Serial.print(incomingByte+"\n");
      incomingByte = " "; //清空变量，准备下次输入
    }
  }
 }  

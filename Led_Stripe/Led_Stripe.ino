 int green = 11;
int red = 12;
int blue = 13;
int a[3]= {0,0,0};
String incomingByte = "";
int count = 0;
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

void display(int a[3])
{
  analogWrite(red,255-a[0]);
  analogWrite(green,255-a[1]);
  analogWrite(blue,255-a[2]);
  delay(a[3]);
}
void loop()
{
 while (Serial.available() > 0) 
  { //监测串口缓存，当有数据输入时，循环赋值给incomingByte
      incomingByte += char(Serial.read());//读取单个字符值，转换为字符，并按顺序一个个赋值给incomingByte
      //a[count] = atoi(incomingByte.c_str());
      //Serial.print(a[count]);
      //count++;
      //incomingByte = "";
    }
   delay(100);//不能省略，因为读取缓冲区数据需要时间
    if(incomingByte.length() > 0) 
    {
      a[0] = atoi(incomingByte.c_str());
     //读取输入的字符，转换为字符，并赋值给incomingByte  
     Serial.print(a[0]);
     Serial.print("\n");
     display(a);
     incomingByte = "";
    }
 }  

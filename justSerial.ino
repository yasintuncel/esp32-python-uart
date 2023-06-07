void setup()
{
  Serial.begin(115200);
  // Serial.println("sistembasladi 1");
}

void loop()
{
  if (Serial.available() > 0) {
    String incoming = Serial.readString();
    int ind1 = incoming.indexOf(',');  //finds location of first ,
    String command = incoming.substring(0, ind1);   //captures first data String

    if (command == "isokey") {
      Serial.println("okey");
    }
    if (command == "clearin") {
      Serial.println("inremoved");
    }

    if (command == "clearout") {
      Serial.println("outremoved");
    }

    if (command == "clearsos") {
      Serial.println("sosremoved");
    }
    if (command == "in") {
      Serial.println("in,1111111,2222222,3333333");
    }
    if (command == "out") {
      Serial.println("out,1111111,2222222,3333333");
    }
    if (command == "sos") {
      Serial.println("sos,1");
    }
    if (command == "clearall") {
      Serial.println("clearall-removed");
    }
  }
}
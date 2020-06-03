// Code adapted from Argon API documentation on Servo

Servo myservo;  // create a servo object so I can use the motor
                

String command; // A string declared so data can be assigned to it from the IFTTT response
void setup()
{
    Particle.function("feed", feed);  // Sets up feed function to be called from IFTTT

    myservo.attach(D3);   //Attaches D3 to the servo object we created above
    myservo.write(0);    // sets the servo to position 0 if needed
}

int feed(String command)   //feed is triggered by a string, which will be called command
{   
    if(command == "now")   // if the string is "now", which it is set to be on the IFTTT applet, the action will trigger
    {                            
        myservo.write(100);      //moves servo to position 100, opening the hatch
        delay(1000);             // wait 1 second
        myservo.write(0);       //returns servo to starting position
        delay(1000);            //delays for 1 second before returning to normal function
        return 1;               // return a status of "1"
    }

}

void loop()
{
  // empty because we call the gong function via the cloud
    //command = "now";
    //gong(command);
}
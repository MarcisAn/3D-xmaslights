using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;

public class Main : MonoBehaviour
{
    const int LED_COUNT = 198;
    const string FILEPATH = "Assets/lightdata.txt";

    class Color
    {
        public Color(string color)
        {
            switch (color)
            {
                case "white":
                    Red = 255;
                    Green = 255;
                    Blue = 255;
                    break;
                case "black":
                    Red = 0;
                    Green = 0;
                    Blue = 0;
                    break;
            }

        }
        public Color(byte r, byte g, byte b)
        {
            Red = r;
            Green = g;
            Blue = b;
        }

        public byte Red { get; }
        public byte Green { get; }
        public byte Blue { get; }
        public string toString()
        {
            return Red + "," + Green + "," + Blue;
        }
    }

    private void Update()
    {
        clearFile();
        for (int i = 0; i < LED_COUNT; i++)
        {
            string pathname = "";
            if (i == 0)
            {
                pathname = "light";
            }
            else
            {
                pathname = "light (" + i + ")";
            }
            GameObject light = GameObject.Find(pathname);
            bool isTriggered = light.GetComponent<LightPre>().isTriggered;
            byte r, g, b;
            r = light.GetComponent<LightPre>().r;
            g = light.GetComponent<LightPre>().g;
            b = light.GetComponent<LightPre>().b;

            if (isTriggered)
            {
                apendLight(i+":" + new Color(r,g,b).toString() + "\n");

            }
            else
            {
                apendLight(i +":"+ new Color("black").toString()+"\n");

            }
        }
    }
    static void clearFile()
    {
        StreamWriter writer = new StreamWriter(FILEPATH, false);
        writer.Write("");
        writer.Close();
    }
    static void apendLight(string text)
    {
        StreamWriter writer = new StreamWriter(FILEPATH, true);
        writer.Write(text);
        writer.Close();
    }
}

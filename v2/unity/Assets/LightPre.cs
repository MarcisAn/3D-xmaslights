using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class LightPre : MonoBehaviour
{
    public bool isTriggered = false;
    
    public byte r;
    public byte g;
    public byte b;

    void setColor(byte red,byte green, byte blue)
    {
        r = red;
        g = green;
        b = blue;
    }

    void Start()
    {
        Debug.Log("start");
    }
    void Update() { }
    private void OnTriggerEnter(Collider collision)
    {
        switch (collision.name)
        {
            
            case "r":
                setColor(255, 0, 0);
                break;
            case "g":
                setColor(0, 255, 0);
                break;
            case "b":
                setColor(0, 0, 255);
                break;
            case "o":
                setColor(255, 255, 0);
                break;

            default:
                setColor(255, 255, 255);
                break;
        }
        isTriggered = true;
    }
    private void OnTriggerExit(Collider other)
    {
        isTriggered = false;
    }

    
}

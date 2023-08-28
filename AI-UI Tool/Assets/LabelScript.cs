using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class LabelScript : MonoBehaviour
{
    public GameObject UIControllerObject;
    public UICreation ui;
    public TMPro.TextMeshProUGUI labelText;

    // Start is called before the first frame update
    void Start()
    {
        ui = UIControllerObject.GetComponent<UICreation>();
    }

    // Update is called once per frame
    void Update()
    {
        labelText.text = "UI #" + (ui.index + 1);
        
    }
}

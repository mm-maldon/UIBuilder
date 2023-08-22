using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class UICreation : MonoBehaviour
{

    public GameObject HealthBarPrefab;
    //bool creating = false;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        if(Input.GetMouseButton(0)){
            
            Vector3 mousePos = Input.mousePosition;
            mousePos.z = 10;
            Vector3 objectPos = Camera.main.ScreenToWorldPoint(mousePos);
            makeHealthBar(objectPos);
            
        }
    }


    public void makeHealthBar(Vector3 pos){
        Instantiate(HealthBarPrefab, pos, Quaternion.identity);
    }
}

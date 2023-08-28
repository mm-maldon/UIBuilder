using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;

public class UICreation : MonoBehaviour
{

    // background--to position elements relative to background
    public GameObject bg;
    private Vector3 bgSize;
    private SpriteRenderer bgRenderer;
    private float X_unit;
    private float Y_unit;
    private Vector2 bgLeftCorner;
    
    // current element--used to reposition element relative to background and edges
    private GameObject currentElement;
    private Vector3 elementSize;
    private SpriteRenderer elementRenderer;

    // UI Element Prefabs
    public GameObject CompassPrefab;
    public GameObject HealthBarPrefab; 
    public GameObject WeaponSharpnessPrefab;
    public GameObject WeaponLoadPrefab;
    public GameObject EnemyHealthBarPrefab;
    public GameObject PalicoItemPickupPrefab;
    public GameObject MiniMapPrefab;
    public GameObject LockOnTogglePrefab;
    public GameObject ComboReferencePrefab;
    public GameObject MissionObjectivePrefab;
    public GameObject PlayerItemPickupPrefab;
    public GameObject QuickInventoryPrefab;
    public GameObject FlingAmmoPrefab;

    /* UI Element Strings Reference(for parsing through .txt files)
        "C"      Compass
        "HB"     Health Bar
        "WS"     Weapon Sharpness
        "WL"     Weapon Load
        "EHB"    Enemy Health Bar
        "PIP_02" Palico Item Pickup
        "MM"     Mini Map
        "LOT"    Lock-On Toggle
        "CR"     Combo Reference
        "MO"     Mission Objective
        "PIP_01" Player Item Pickup
        "QI"     Quick Inventory
        "FA"     Fling Ammo
    */

    // Files
    public TextAsset [] children;
    public int index = 0;
    
    void Start()
    {
        // Get background size/position
        bgRenderer = bg.GetComponent<SpriteRenderer>();
        bgSize = bgRenderer.bounds.size;

        //Debug.Log("bg size: " + bgSize);
        X_unit = bgSize.x / 16.0f;
        Y_unit = bgSize.y / 9.0f;

        bgLeftCorner.x = 0.0f - bgSize.x / 2.0f;
        bgLeftCorner.y = 0.5f + bgSize.y / 2.0f;

        //Debug.Log("bg left corner: " + bgLeftCorner);

        //makeElement("HB", 16, 9);

        parseChild(children[index]);                     

    }

    // Update is called once per frame
    void Update()
    {
        
    }

    // Creates UIs based on a text file.
    public void parseChild(TextAsset child){
        string allText = child.text;
        string [] lines = allText.Split(new string [] {"\r\n", "\n"}, System.StringSplitOptions.None);

        int index = 0;
        while(index < lines.Length - 1){
            Debug.Log(lines[index]);
            string [] items = lines[index].Split(new string [] {","}, System.StringSplitOptions.None);
            items[0] = items[0].Substring(1, items[0].Length - 2);

            makeElement(items[0], int.Parse(items[1]), int.Parse(items[2]));
        
            index++;
        }

        //Debug.Log("out of while");
        
    }

    // Creates element of "type" at position (x,y) on the sample background.
    public void makeElement(string type, int x, int y){

        //get position relative to background image
        Vector3 pos = new Vector3(bgLeftCorner.x + (X_unit * x), bgLeftCorner.y - (Y_unit * y), 0);

        switch(type){
            case "C":
                currentElement = Instantiate(CompassPrefab, pos, Quaternion.identity);
                break;
            case "HB":
                currentElement = Instantiate(HealthBarPrefab, pos, Quaternion.identity);
                break;
            case "WS":
                currentElement = Instantiate(WeaponSharpnessPrefab, pos, Quaternion.identity);
                break;
            case "WL":
                currentElement = Instantiate(WeaponLoadPrefab, pos, Quaternion.identity);
                break;
            case "EHB":
                currentElement = Instantiate(EnemyHealthBarPrefab, pos, Quaternion.identity);
                break;
            case "PIP_02":
                currentElement = Instantiate(PalicoItemPickupPrefab, pos, Quaternion.identity);
                break;
            case "MM":
                currentElement = Instantiate(MiniMapPrefab, pos, Quaternion.identity);
                break;
            case "LOT":
                currentElement = Instantiate(LockOnTogglePrefab, pos, Quaternion.identity);
                break;
            case "CR":
                currentElement = Instantiate(ComboReferencePrefab, pos, Quaternion.identity);
                break;
            case "MO":
                currentElement = Instantiate(MissionObjectivePrefab, pos, Quaternion.identity);
                break;
            case "PIP_01":
                currentElement = Instantiate(PlayerItemPickupPrefab, pos, Quaternion.identity);
                break;
            case "QI":
                currentElement = Instantiate(QuickInventoryPrefab, pos, Quaternion.identity);
                break;
            case "FA":
                currentElement = Instantiate(FlingAmmoPrefab, pos, Quaternion.identity);
                break;
            default:
                Debug.Log("no element specified");
                break;
        }

        elementRenderer = currentElement.GetComponent<SpriteRenderer>();
        elementSize = elementRenderer.bounds.size;

        Vector3 tempElementPos = currentElement.transform.position;

        if(x <= 7){
            tempElementPos.x = tempElementPos.x + (elementSize.x / 2); 
        }else{
            tempElementPos.x = tempElementPos.x - (elementSize.x / 2);
        }

        if(y < 5){
            tempElementPos.y = tempElementPos.y - (elementSize.y / 2);
        }else{
            tempElementPos.y = tempElementPos.y + (elementSize.y / 2);
        }

        currentElement.transform.position = tempElementPos;
    }

    public void AdvanceUI(){
        GameObject [] oldUI = GameObject.FindGameObjectsWithTag("UIElement");
        foreach(GameObject element in oldUI){
            GameObject.Destroy(element);
        }

        if(index == children.Length - 1){
            index = 0;
        }else{
            index++;
        }

        parseChild(children[index]);
    }

    public void RevertUI(){
        GameObject [] oldUI = GameObject.FindGameObjectsWithTag("UIElement");
        foreach(GameObject element in oldUI){
            GameObject.Destroy(element);
        } 

        if(index == 0){
            index = children.Length - 1;
        }else{
            index--;
        }

        parseChild(children[index]);
    }

}

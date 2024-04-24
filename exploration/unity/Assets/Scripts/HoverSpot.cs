using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class HoverSpot : MonoBehaviour
{
    [SerializeField] private Transform mainCameraTransform = null;

    void Start()
    {
        mainCameraTransform = Camera.main.transform;
    }

    void Update()
    {
        // Check if the left mouse button is clicked
        if (Input.GetMouseButtonDown(0))
        {
            // Cast a ray from the mouse position into the scene
            Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);
            RaycastHit hit;

            // Check if the ray hits any HoverSpot object
            if (Physics.Raycast(ray, out hit))
            {
                // Check if the hit object is a HoverSpot prefab instance
                if (hit.collider.GetComponent<HoverSpot>() != null)
                {
                    // Update the x and z values of the main camera's position to match HoverSpot's position
                    Vector3 newPosition = mainCameraTransform.position;
                    newPosition.x = hit.point.x;
                    newPosition.z = hit.point.z;
                    mainCameraTransform.position = newPosition;
                }
            }
        }
    }
}

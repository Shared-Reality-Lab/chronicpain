using UnityEngine;

public class MainCameraRotationController : MonoBehaviour
{
    [SerializeField] private float rotationSpeed = 0.02f;

    private Vector3 dragOrigin;
    private bool isDragging;
    private bool highlightObjectSelected = false; // Flag to indicate if HighlightObject is selected
    private int highlightObjectLayer; // Layer of the HighlightObject

    void Start()
    {
        // Get the layer of the HighlightObject
        highlightObjectLayer = LayerMask.NameToLayer("HighlightObject");
    }

    void Update()
    {
        if (Input.GetMouseButtonDown(0))
        {
            isDragging = true;
            dragOrigin = Input.mousePosition;
            // Check if mouse is over the HighlightObject when clicked
            highlightObjectSelected = IsMouseOverHighlightObject();
            Debug.Log("Highlight Object Selected: " + highlightObjectSelected);
        }

        if (Input.GetMouseButtonUp(0))
        {
            isDragging = false;
            highlightObjectSelected = false;
        }

        if (isDragging && !highlightObjectSelected)
        {
            Vector3 difference = Input.mousePosition - dragOrigin;
            dragOrigin = Input.mousePosition;

            float yaw = difference.x * rotationSpeed;
            float pitch = -difference.y * rotationSpeed;

            transform.Rotate(Vector3.up, yaw, Space.World);
            transform.Rotate(Vector3.right, pitch, Space.World);
        }
    }

    // Function to check if the mouse is over the HighlightObject
    private bool IsMouseOverHighlightObject()
    {
        Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);
        RaycastHit hit;
        if (Physics.Raycast(ray, out hit))
        {
            Debug.Log("Tag of Clicked Object: " + hit.collider.gameObject.tag); // Debug log to print the tag of the clicked object
            return hit.collider != null && hit.collider.gameObject.layer == highlightObjectLayer;
        }
        return false;
    }
}

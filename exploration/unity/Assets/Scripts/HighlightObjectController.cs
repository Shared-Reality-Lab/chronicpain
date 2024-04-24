using UnityEngine;

public class HighlightObjectController : MonoBehaviour
{
    private Vector3 lastMousePosition;
    private bool isMouseOver;

    private void OnMouseDown()
    {
        lastMousePosition = Input.mousePosition;
    }

    private void OnMouseDrag()
    {
        if (!isMouseOver) return; // Ignore dragging if mouse is not over the object

        Vector3 delta = Input.mousePosition - lastMousePosition;
        transform.localScale += new Vector3(delta.x, delta.y, 0) * Time.deltaTime;
        lastMousePosition = Input.mousePosition;
    }

    private void OnMouseEnter()
    {
        isMouseOver = true;
    }

    private void OnMouseExit()
    {
        isMouseOver = false;
    }

    private void Start()
    {
        // Add BoxCollider component
        BoxCollider boxCollider = gameObject.AddComponent<BoxCollider>();
        // Adjust the size of the collider to match the object's size
        Vector3 size = GetComponent<Renderer>().bounds.size;
        boxCollider.size = size;
    }
}

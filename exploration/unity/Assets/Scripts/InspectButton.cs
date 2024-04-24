using UnityEngine;

public class InspectButton : MonoBehaviour
{
    [SerializeField] private GameObject highlightObjectPrefab;

    private GameObject highlightObjectInstance;

    private void OnMouseDown()
    {
        if (highlightObjectPrefab != null)
        {
            // Spawn HighlightObject
            highlightObjectInstance = Instantiate(highlightObjectPrefab, transform.position, Quaternion.identity);
        }
    }
}

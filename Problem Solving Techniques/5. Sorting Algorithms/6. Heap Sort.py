# Build max heap, repeatedly extract maximum and rebuild heap.
import heapq

def heap_sort(arr):
    """
    Using Python's heapq module (min heap)
    """
    heapq.heapify(arr)  # Convert to heap O(n)
    return [heapq.heappop(arr) for _ in range(len(arr))]  # O(n log n)

# Test
arr = [12, 11, 13, 5, 6, 7]
print("Sorted:", heap_sort(arr.copy()))
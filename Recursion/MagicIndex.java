/**
 * @question: A magic index in an array A[1...n-1] is determined to be an index
 *            such that A[i]=i. Given a sorted array of distinct integers, write
 *            a method to find a magic index, if one exists in array A.
 * 
 *            WHAT IF THE VALUES ARE NOT DISTINCT?
 */
public class MagicIndex {

    /**
     * Linear Search
     * 
     * @param arr
     * @return the magic index
     */
    public static int findMagicIndex__firstThought(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == i) {
                return i;
            }
        }
        return -1;
    }

    /**
     * Binary Search
     * 
     * @param arr
     * @return the magic index
     */
    public static int findMagicIndex__binarySearch(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == i) {
                return i;
            }
        }
        return -1;
    }

    protected static int findMagicIndex__binarySearch(int[] arr, int start, int end) {
        if (end < start) {
            return -1;
        }
        int mid = (end + start) / 2;

        if (arr[mid] == mid) {
            return mid;
        } else if (arr[mid] > mid) {
            return findMagicIndex__binarySearch(arr, start, mid - 1);
        } else {
            return findMagicIndex__binarySearch(arr, mid + 1, end);
        }
    }

    public static int findMagicIndex_duplicates(int[] arr) {
        return findMagicIndex_duplicates(arr, 0, arr.length - 1);
    }

    private static int findMagicIndex_duplicates(int[] arr, int start, int end) {
        if (end < start) {
            return -1;
        }

        int midIndex = (end + start) / 2;
        int midValue = arr[midIndex];

        if (midValue == midIndex)
            return midIndex;

        // search on left
        int leftIndex = Math.min(midIndex - 1, midValue);
        int left = findMagicIndex_duplicates(arr, start, leftIndex);
        if (left >= 0) {
            return left;
        }

        // search on right
        int rightIndex = Math.min(midIndex - 1, midValue);
        int right = findMagicIndex_duplicates(arr, rightIndex, end);

        return right;

    }

    public static void main(String[] args) {
        System.out.println(findMagicIndex__firstThought(new int[] { 1, 2, 2, 3, 5, 7, 8, 9, 9, 10 }));
        System.out.println(findMagicIndex__binarySearch(new int[] { 1, 2, 2, 3, 5, 7, 8, 9, 9, 10 }));
        System.out.println(findMagicIndex_duplicates(new int[] { 1, 2, 2, 3, 5, 7, 8, 9, 9, 10 }));
    }
}

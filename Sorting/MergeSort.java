import java.util.Arrays;

public class MergeSort {
    public static void sort(int[] nums, int l, int r) {
        if (l < r) {
            // find middle point
            int m = l + (r - l) / 2;

            sort(nums, l, m);
            sort(nums, m + 1, r);

            merge(nums, l, m, r);
        }
    }

    public static void merge(int[] nums, int l, int m, int r) {
        int n1 = m - l + 1;
        int n2 = r - m;

        int L[] = new int[n1];
        int R[] = new int[n2];

        for (int i = 0; i < n1; i++) {
            L[i] = nums[l + i];
        }

        for (int i = 0; i < n2; i++) {
            R[i] = nums[m + i + 1];
        }

        int i = 0, j = 0;

        int k = l;
        while (i < n1 && j < n2) {
            if (L[i] <= R[j]) {
                nums[k] = L[i];
                i++;
            } else {
                nums[k] = R[j];
                j++;
            }
            k++;
        }

        while (i < n1) {
            nums[k] = L[i];
            i++;
            k++;
        }

        while (j < n2) {
            nums[k] = R[j];
            j++;
            k++;
        }

    }

    public static void main(String[] args) {
        int arr[] = new int[] { 4, 5, 23, 53, 12, 76, 10, 13, 1, 30 };
        sort(arr, 0, arr.length - 1);
        System.out.println(Arrays.toString(arr));
    }
}

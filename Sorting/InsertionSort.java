import java.util.Arrays;

public class InsertionSort {
    public static void sort(int[] nums) {
        for (int i = 1; i < nums.length; i++) {
            int temp = nums[i];
            int j = i;
            while (j > 0 && nums[j - 1] > temp) {
                nums[j] = nums[j - 1];
                j--;
            }
            nums[j] = temp;
        }
    }

    public static void main(String[] args) {
        int arr[] = new int[] { 4, 5, 23, 53, 12, 76, 10, 13, 1, 30 };
        sort(arr);
        System.out.println(Arrays.toString(arr));
    }
}

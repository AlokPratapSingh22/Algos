import java.util.Arrays;

public class SelectionSort {
    public static void sort(int[] nums) {

        for (int i = 0; i < nums.length - 1; i++) {
            int min_index = i;
            for (int j = i + 1; j < nums.length; j++) {

                if (nums[min_index] > nums[j]) {
                    min_index = j;
                }

            }

            int temp = nums[i];
            nums[i] = nums[min_index];
            nums[min_index] = temp;
        }

    }

    public static void main(String[] args) {
        int arr[] = new int[] { 4, 5, 23, 53, 12, 76, 10, 13, 1, 30 };
        sort(arr);
        System.out.println(Arrays.toString(arr));
    }
}

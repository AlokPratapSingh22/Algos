import java.util.Arrays;

public class BubbleSort {
    public static void sort(int[] nums) {

        for (int i = 0; i < nums.length - 1; i++) {
            for (int j = 0; j < nums.length - i - 1; j++) {
                if (nums[j] > nums[j + 1]) {

                    int tmp = nums[j + 1];
                    nums[j + 1] = nums[j];
                    nums[j] = tmp;

                }
            }
        }

    }

    public static void main(String[] args) {
        int arr[] = new int[] { 4, 5, 23, 53, 12, 76, 10, 13, 1, 30 };
        sort(arr);
        System.out.println(Arrays.toString(arr));
    }

}
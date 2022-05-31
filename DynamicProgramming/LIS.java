import java.util.Arrays;
public class LIS {

    public static int longestIncreasingSubs(int[] nums) {

        int n = nums.length;
        int memo[]= new int[n];

        for( int i=0;i<n;i++){
            memo[i] = 1;
        }
        System.out.println(Arrays.toString(memo));
        for(int i=n-1;i>=0;i--){
            for (int j=i+1;j<n;j++){
                if (nums[i] < nums[j])
                    memo[i] = Math.max(memo[i], 1+memo[j]);
            }
        }
        int max= 0;
        for (int i=0; i<n;i++){
            max = Math.max(max, memo[i]);
        }
        return max;
    }

    public static void main(String[] args) {
        System.out.println(longestIncreasingSubs(new int[]{10,3,6,2,4,12,3,5,20}));
    }

}

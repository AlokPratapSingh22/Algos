
/**
 * HouseRobber2
 */
public class HouseRobber2 {

    private static int robHouses(int[] arr, int s, int e) {
        int incl = 0, excl = 0;
        for (int i = s; i <= e; i++) {
            int new_xl = Math.max(incl, excl);
            incl = excl + arr[i];
            excl = new_xl;
        }
        return Math.max(incl, excl);
    }

    public static int robHouses(int[] arr) {
        return Math.max(robHouses(arr, 0, arr.length - 2), robHouses(arr, 1, arr.length - 1));
    }

    public static void main(String[] args) {
        int ans = robHouses(new int[] { 5, 1, 2, 6, 3, 7, 4 });
        System.out.println(ans);
    }

}

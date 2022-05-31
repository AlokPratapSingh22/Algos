/**
 * Multiplication without divide or muliply operator
 */
public class Multiplication {

    public static int multiply(int a, int b) {
        int small = a > b ? b : a;
        int big = a > b ? a : b;
        return multiply_recursive(small, big);
    }

    public static int multiply_memo(int a, int b) {
        int small = a < b ? a : b;
        int big = a < b ? b : a;

        int memo[] = new int[small + 1];
        return multiply_memo_fast(small, big, memo);
    }

    public static int multiply_recursive(int small, int big) {
        if (small == 0)
            return 0;
        else if (small == 1)
            return big;
        int s = small >> 1; // divide by 2
        int side1 = multiply_recursive(s, big);
        int side2 = side1;

        if (small % 2 == 1) {
            side2 = multiply_recursive(small - s, big);
        }
        return side1 + side2;
    }

    // O(log(small))
    public static int multiply_memo_fast(int small, int big, int[] memo) {

        if (small == 0)
            return 0;
        else if (small == 1)
            return big;
        else if (memo[small] > 0)
            return memo[small];

        int s = small >> 1;

        int halfProd = multiply_memo_fast(s, big, memo);

        if (small % 2 == 1) {
            memo[small] = halfProd + halfProd + big;
        } else {
            memo[small] = halfProd + halfProd;
        }

        return memo[small];
    }

    public static int multiply_memo(int small, int big, int[] memo) {
        if (small == 0)
            return 0;
        else if (small == 1)
            return big;
        else if (memo[small] > 0)
            return memo[small];

        int s = small >> 1;

        int side1 = multiply_memo(s, big, memo);
        int side2 = side1;

        if (small % 2 == 1) {
            side2 = multiply_memo(small - s, big, memo);
        }

        memo[small] = side1 + side2;

        return memo[small];
    }

    public static void main(String[] args) {
        System.out.println(multiply(5, 6));
        int ans = multiply_memo(15, 12);
        System.out.println(ans);
    }
}
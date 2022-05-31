import java.util.Arrays;

/**
 * @question: A child is running up a staircase with n steps and can hop either
 *            1 step, 2 steps, or 3 steps at a time. Implement a method to count
 *            how many possible ways the child can run up the stairs.
 */
public class TripleStep {
    public static int bruteForce(int n) {
        if (n < 0) {
            return 0;
        } else if (n == 0) {
            return 1;
        } else {
            return bruteForce(n - 1) + bruteForce(n - 2) + bruteForce(n - 3);
        }
    }

    public static int countWays(int n) {
        int memo[] = new int[n + 1];
        Arrays.fill(memo, -1);

        return countWays(n, memo);
    }

    private static int countWays(int n, int[] memo) {
        if (n < 0)
            return 0;
        else if (n == 0)
            return 1;
        else if (memo[n] > -1)
            return memo[n];
        else {
            memo[n] = countWays(n - 1, memo) + countWays(n - 2, memo) + countWays(n - 3, memo);
            return memo[n];
        }
    }

    public static void main(String[] args) {
        System.out.println(bruteForce(6));
        // result limits to n=37, after that it exceeds the integer limit
        // to go beyond that use BigInteger
        System.out.println(countWays(6));
    }
}

import java.util.ArrayList;

/**
 * @question: Write a function to return all subsets of a set.
 */
public class PowerSet {

    /**
     * 
     * Using COMBINATORICS
     * 
     * Since we have 2 choices for each subset to either be in the set or not
     * So taking "YES" as 1 and "NO" as 0
     * We will now have a binary number representing each subset
     * So, we can just generate all numbers form 0-2^n and use their binary
     * representation for filling the set
     * 
     * Time complexity of O(n2^n)
     * 
     * @param set
     * @return the powerset or all subsets of the input set
     */
    public static ArrayList<ArrayList<Integer>> getSubsets(ArrayList<Integer> set) {
        ArrayList<ArrayList<Integer>> all_subsets = new ArrayList<ArrayList<Integer>>();
        int max = 1 << set.size(); // computing 2^n

        for (int i = 0; i < max; i++) {
            ArrayList<Integer> subset = convertIntToSet(i, set);
            all_subsets.add(subset);
        }
        return all_subsets;
    }

    private static ArrayList<Integer> convertIntToSet(int i, ArrayList<Integer> set) {
        ArrayList<Integer> subset = new ArrayList<Integer>();
        int index = 0;

        for (int k = i; k > 0; k >>= 1) {
            if ((k & 1) == 1) {
                subset.add(set.get(index));
            }
            index++;
        }

        return subset;
    }

    /**
     * 
     * Time complexity of O(n2^n)
     * 
     * @param set
     * @param index
     * @return the powerset or all subsets of the input set
     */
    public static ArrayList<ArrayList<Integer>> getSubsets(ArrayList<Integer> set, int index) {
        ArrayList<ArrayList<Integer>> subsets;

        // Base case add an empty set
        if (set.size() == index) {
            subsets = new ArrayList<ArrayList<Integer>>();
            subsets.add(new ArrayList<Integer>());
        } else {
            subsets = getSubsets(set, index + 1);
            int item = set.get(index);
            ArrayList<ArrayList<Integer>> moresubsets = new ArrayList<ArrayList<Integer>>();

            for (ArrayList<Integer> subset : subsets) {
                ArrayList<Integer> newsubset = new ArrayList<Integer>();
                // adding the subset to the new subset
                newsubset.addAll(subset);
                // adding item to subset
                newsubset.add(item);
                // adding modified subset to moresubsets again
                moresubsets.add(newsubset);
            }

            subsets.addAll(moresubsets);
        }

        return subsets;
    }

    public static void main(String[] args) {
        ArrayList<Integer> arr = new ArrayList<Integer>();
        arr.add(3);
        arr.add(1);
        arr.add(5);
        arr.add(10);
        arr.add(8);
        arr.add(6);
        System.out.println(getSubsets(arr, 0));
    }
}

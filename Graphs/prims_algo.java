import java.util.ArrayList;
import java.util.Comparator;
import java.util.PriorityQueue;

/**
 * prims_algo
 */
public class prims_algo {

    // O(nlogn) time
    public static void primsAlgo(ArrayList<ArrayList<Node>> adj, int N) {
        int key[] = new int[N];
        int parent[] = new int[N];
        boolean mst[] = new boolean[N];

        for (int i = 0; i < N; i++) {
            key[i] = 100000000;
            mst[i] = false;
            parent[i] = -1;
        }

        key[0] = 0;

        PriorityQueue<Node> pq = new PriorityQueue<>(N, new Node());
        pq.add(new Node(0, key[0]));

        for (int i = 0; i < N - 1; i++) {
            int u = pq.poll().val;
            mst[u] = true;

            for (Node it : adj.get(u)) {
                if (mst[it.val] == false && it.wgt < key[it.val]) {
                    parent[it.val] = u;
                    key[it.val] = it.wgt;
                    pq.add(new Node(it.val, key[it.val]));
                }
            }
        }

        for (int i = 1; i < N; i++) {
            System.out.println(parent[i] + " -> " + i);
        }
    }

    public static void main(String[] args) {
        int n = 5;
        ArrayList<ArrayList<Node>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adj.add(new ArrayList<Node>());
        }

        adj.get(0).add(new Node(1, 2));
    }
}

/**
 * Node
 */
class Node implements Comparator<Node> {

    int val, wgt;

    public Node(int v, int w) {
        val = v;
        wgt = w;
    }

    public Node() {
    }

    @Override
    public int compare(Node o1, Node o2) {
        if (o1.wgt < o2.wgt)
            return -1;
        if (o1.wgt > o2.wgt)
            return 1;
        return 0;
    }

}
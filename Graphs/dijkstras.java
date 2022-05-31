import java.util.ArrayList;
import java.util.Comparator;
import java.util.PriorityQueue;

class Dijkstras {
    public static void shortestPath(ArrayList<ArrayList<Node>> graph, int src, int n) {
        int dist[] = new int[n];
        for (int i = 0; i < dist.length; i++) {
            dist[i] = Integer.MAX_VALUE;
        }
        dist[src] = 0;

        PriorityQueue<Node> pq = new PriorityQueue<>(n, new Node());
        pq.add(new Node(src, 0));

        while (!pq.isEmpty()) {
            Node node = pq.poll();
            int d = node.getW();
            for (Node neighbor : graph.get(node.getV())) {
                int newD = d + neighbor.getW();

                if (dist[neighbor.getV()] > newD) {
                    dist[neighbor.getV()] = newD;
                    pq.add(new Node(neighbor.getV(), newD));
                }

            }
        }

        for (int i = 0; i < dist.length; i++) {
            System.out.println(src + " --> " + i + " = " + dist[i]);
        }
    }

    public static void main(String[] args) {
        int n = 5;
        ArrayList<ArrayList<Node>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adj.add(new ArrayList<Node>());
        }

        adj.get(0).add(new Node(1, 2));
        adj.get(1).add(new Node(0, 2));

        adj.get(1).add(new Node(2, 4));
        adj.get(2).add(new Node(1, 4));

        adj.get(0).add(new Node(3, 1));
        adj.get(3).add(new Node(0, 1));

        adj.get(3).add(new Node(2, 3));
        adj.get(2).add(new Node(3, 3));

        adj.get(1).add(new Node(4, 5));
        adj.get(4).add(new Node(1, 5));

        adj.get(2).add(new Node(4, 1));
        adj.get(4).add(new Node(2, 1));

        shortestPath(adj, 0, n);

    }
}

class Node implements Comparator<Node> {
    int v, w;

    public Node(int v, int w) {
        this.v = v;
        this.w = w;
    }

    public Node() {
    }

    public int getV() {
        return v;
    }

    public int getW() {
        return w;
    }

    @Override
    public int compare(Node o1, Node o2) {
        if (o1.getW() < o2.getW())
            return -1;
        else if (o1.getW() > o2.getW())
            return 1;
        return 0;
    }
}
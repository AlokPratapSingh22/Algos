import java.util.ArrayList;
import java.util.HashSet;

/**
 * @question: Imagine a robot sitting on the upper left corner of grid with r
 *            rows and c columns. The robot can only moove in two directions,
 *            right and down, but certain cells are "off limits" such that the
 *            robot cannot step on them. Design an algorithm to find a path for
 *            the robot from the left top to the bottom right.
 */

public class RobotInAGrid {
    public static void main(String[] args) {
        boolean grid[][] = new boolean[][] {
                { true, false, true, false },
                { true, true, true, false },
                { false, true, true, false },
                { false, false, true, true },
        };

        ArrayList<Point> path = (getPath_by_BruteForce(grid));
        ArrayList<Point> path2 = (getPath_by_Memoization(grid));

        System.out.println(path);
        System.out.println(path2);
    }

    public static ArrayList<Point> getPath_by_Memoization(boolean[][] grid) {
        if (grid == null || grid.length == 0)
            return null;

        ArrayList<Point> path = new ArrayList<Point>();
        HashSet<Point> failedPoints = new HashSet<Point>();

        if (getPath_by_Memoization(grid, grid.length - 1, grid[0].length - 1, path, failedPoints)) {
            return path;
        }

        return null;
    }

    private static boolean getPath_by_Memoization(boolean[][] grid, int r, int c, ArrayList<Point> path,
            HashSet<Point> failedPoints) {

        // If out of bounds or not available
        if (c < 0 || r < 0 || !grid[r][c]) {
            return false;
        }

        Point point = new Point(r, c);

        // check if point exists in set of failedPoints
        if (failedPoints.contains(point)) {
            return false;
        }

        boolean isAtOrigin = (r == 0) && (c == 0);

        // if there is a valid path from start to current location add the
        // current location to the path
        if (isAtOrigin || getPath_by_Memoization(grid, r - 1, c, path, failedPoints)
                || getPath_by_Memoization(grid, r, c - 1, path, failedPoints)) {
            path.add(point);
            return true;
        }

        failedPoints.add(point);
        return false;
    }

    public static ArrayList<Point> getPath_by_BruteForce(boolean[][] grid) {
        if (grid == null || grid.length == 0)
            return null;

        ArrayList<Point> path = new ArrayList<Point>();

        if (getPath_by_BruteForce(grid, grid.length - 1, grid[0].length - 1, path)) {
            return path;
        }

        return null;
    }

    private static boolean getPath_by_BruteForce(boolean[][] grid, int r, int c, ArrayList<Point> path) {

        if (c < 0 || r < 0 || !grid[r][c]) {
            return false;
        }

        boolean isAtOrigin = (r == 0) && (c == 0);

        if (isAtOrigin
                || getPath_by_BruteForce(grid, r - 1, c, path)
                || getPath_by_BruteForce(grid, r, c - 1, path)) {
            Point p = new Point(r, c);
            path.add(p);
            return true;
        }

        return false;
    }

    /**
     * Point
     */
    public static class Point {

        int r, c;

        public Point(int r, int c) {
            this.r = r;
            this.c = c;
        }

        public String toString() {
            return "[" + r + " , " + c + "]";
        }

    }
}

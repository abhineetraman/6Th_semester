#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Structure to represent a point
struct Point {
    int x, y;
};

// Function to compare points based on x-coordinate
bool comparePoints(Point p1, Point p2) {
    return p1.x < p2.x;
}

// Function to fill a polygon using Scan Line Algorithm
void scanLineFill(vector<Point> polygon) {
    int n = polygon.size();

    // Sort the points based on x-coordinate
    sort(polygon.begin(), polygon.end(), comparePoints);

    // Find the minimum and maximum y-coordinate of the polygon
    int ymin = polygon[0].y;
    int ymax = polygon[0].y;
    for (int i = 1; i < n; i++) {
        ymin = min(ymin, polygon[i].y);
        ymax = max(ymax, polygon[i].y);
    }

    // Iterate through each scan line from ymin to ymax
    for (int y = ymin; y <= ymax; y++) {
        vector<int> intersectingPoints;

        // Find the intersecting points of the scan line with the edges of the polygon
        for (int i = 0; i < n; i++) {
            int x1 = polygon[i].x;
            int y1 = polygon[i].y;
            int x2 = polygon[(i + 1) % n].x;
            int y2 = polygon[(i + 1) % n].y;

            if ((y1 <= y && y2 > y) || (y2 <= y && y1 > y)) {
                int x = x1 + (y - y1) * (x2 - x1) / (y2 - y1);
                intersectingPoints.push_back(x);
            }
        }

        // Sort the intersecting points based on x-coordinate
        sort(intersectingPoints.begin(), intersectingPoints.end());

        // Fill the scan line between pairs of intersecting points
        for (int i = 0; i < intersectingPoints.size(); i += 2) {
            int x1 = intersectingPoints[i];
            int x2 = intersectingPoints[i + 1];

            // Fill the pixels between x1 and x2 on the current scan line
            for (int x = x1; x <= x2; x++) {
                cout << "(" << x << ", " << y << ") " <<endl; // Replace this with your actual fill logic
            }
        }
    }
}

int main() {
    // Define the polygon to be filled
    vector<Point> polygon = {{10, 10}, {30, 10}, {30, 20}, {20, 30}, {10, 20}};

    // Call the scanLineFill function to fill the polygon
    scanLineFill(polygon);

    return 0;
}

#include <iostream>
#include <cmath>

using namespace std;

// Structure to represent a 2D point
struct Point2D {
    double x, y, w; // Homogeneous coordinates: x, y, and w
};

// Function to perform 2D translation
void translate(Point2D& point, double dx, double dy) {
    point.x += dx * point.w;
    point.y += dy * point.w;
}

// Function to perform 2D rotation around the origin
void rotate(Point2D& point, double angle) {
    double sinTheta = sin(angle);
    double cosTheta = cos(angle);

    double x = point.x;
    double y = point.y;

    point.x = x * cosTheta - y * sinTheta;
    point.y = x * sinTheta + y * cosTheta;
}

// Function to perform 2D scaling
void scale(Point2D& point, double sx, double sy) {
    point.x *= sx;
    point.y *= sy;
}

// Function to perform 2D shearing
void shear(Point2D& point, double shx, double shy) {
    double x = point.x;
    double y = point.y;

    point.x = x + shx * y;
    point.y = y + shy * x;
}

int main() {
    // Define the original point
    Point2D point = {2.0, 3.0, 1.0}; // Homogeneous coordinates: x, y, and w

    cout << "Original Point: (" << point.x << ", " << point.y << ")" << endl;

    // Perform translation
    translate(point, 3.0, 4.0);
    cout << "After Translation: (" << point.x << ", " << point.y << ")" << endl;

    // Perform rotation
    double angle = 45.0 * M_PI / 180.0; // Convert angle from degrees to radians
    rotate(point, angle);
    cout << "After Rotation: (" << point.x << ", " << point.y << ")" << endl;

    // Perform scaling
    scale(point, 2.0, 2.0);
    cout << "After Scaling: (" << point.x << ", " << point.y << ")" << endl;

    // Perform shearing
    shear(point, 0.5, 0.5);
    cout << "After Shearing: (" << point.x << ", " << point.y << ")" << endl;

    return 0;
}

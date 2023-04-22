#include <iostream>
#include <cmath>

using namespace std;

// Structure to represent a 3D point
struct Point3D {
    double x, y, z; // Coordinates in 3D space
};

// Function to perform 3D translation
void translate(Point3D& point, double dx, double dy, double dz) {
    point.x += dx;
    point.y += dy;
    point.z += dz;
}

// Function to perform 3D rotation around the x-axis
void rotateX(Point3D& point, double angle) {
    double sinTheta = sin(angle);
    double cosTheta = cos(angle);

    double y = point.y;
    double z = point.z;

    point.y = y * cosTheta - z * sinTheta;
    point.z = y * sinTheta + z * cosTheta;
}

// Function to perform 3D rotation around the y-axis
void rotateY(Point3D& point, double angle) {
    double sinTheta = sin(angle);
    double cosTheta = cos(angle);

    double x = point.x;
    double z = point.z;

    point.x = x * cosTheta + z * sinTheta;
    point.z = -x * sinTheta + z * cosTheta;
}

// Function to perform 3D rotation around the z-axis
void rotateZ(Point3D& point, double angle) {
    double sinTheta = sin(angle);
    double cosTheta = cos(angle);

    double x = point.x;
    double y = point.y;

    point.x = x * cosTheta - y * sinTheta;
    point.y = x * sinTheta + y * cosTheta;
}

// Function to perform 3D scaling
void scale(Point3D& point, double sx, double sy, double sz) {
    point.x *= sx;
    point.y *= sy;
    point.z *= sz;
}

// Function to perform parallel projection
void parallelProjection(Point3D& point, double d) {
    point.x /= d;
    point.y /= d;
    point.z /= d;
}

// Function to perform perspective projection
void perspectiveProjection(Point3D& point, double d) {
    point.x /= point.z + d;
    point.y /= point.z + d;
    point.z = -d / (point.z + d);
}

int main() {
    // Define the original point
    Point3D point = {2.0, 3.0, 4.0}; // Coordinates in 3D space

    cout << "Original Point: (" << point.x << ", " << point.y << ", " << point.z << ")" << endl;

    // Perform translation
    translate(point, 3.0, 4.0, 5.0);
    cout << "After Translation: (" << point.x << ", " << point.y << ", " << point.z << ")" << endl;

    // Perform rotation around the x-axis
    double angleX = 45.0 * M_PI / 180.0; // Convert angle from degrees to radians
    rotateX(point, angleX);
    cout << "After Rotation around X-axis: (" << point.x << ", " << point.y << ", " << point.z << ")" << endl;

    // Perform rotation around the y-axis
    double angleY = 30.0 * M_PI / 180.0; // Convert angle from degrees to radians
    rotateY(point, angleY);
    cout << "After Rotation around Y-axis: (" << point.x << ", " << point.y << ", " << point.z << ")" << endl;
// Perform rotation around the z-axis
double angleZ = 60.0 * M_PI / 180.0; // Convert angle from degrees to radians
rotateZ(point, angleZ);
cout << "After Rotation around Z-axis: (" << point.x << ", " << point.y << ", " << point.z << ")" << endl;

// Perform scaling
scale(point, 2.0, 2.0, 2.0);
cout << "After Scaling: (" << point.x << ", " << point.y << ", " << point.z << ")" << endl;

// Perform parallel projection
double dParallel = 5.0; // Distance of the projection plane from the origin
parallelProjection(point, dParallel);
cout << "After Parallel Projection: (" << point.x << ", " << point.y << ", " << point.z << ")" << endl;

// Perform perspective projection
double dPerspective = 10.0; // Distance of the projection plane from the origin
perspectiveProjection(point, dPerspective);
cout << "After Perspective Projection: (" << point.x << ", " << point.y << ", " << point.z << ")" << endl;

return 0;
}
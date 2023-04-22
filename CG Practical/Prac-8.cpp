#include <iostream>
#include <vector>
#include <cmath>
#include <GL/glut.h>

// Function to compute the Bezier curve point using De Casteljau's algorithm
void computeBezierPoint(double t, std::vector<double>& controlPoints, double& x, double& y) {
    int n = controlPoints.size() / 2; // Number of control points
    std::vector<double> tempPoints = controlPoints;

    for (int r = 1; r <= n - 1; r++) {
        for (int i = 0; i <= n - r - 1; i++) {
            tempPoints[i * 2] = (1 - t) * tempPoints[i * 2] + t * tempPoints[(i + 1) * 2];
            tempPoints[i * 2 + 1] = (1 - t) * tempPoints[i * 2 + 1] + t * tempPoints[(i + 1) * 2 + 1];
        }
    }

    x = tempPoints[0];
    y = tempPoints[1];
}

void display() {
    glClear(GL_COLOR_BUFFER_BIT);

    // Control points for the Bezier curve
    std::vector<double> controlPoints = { 50, 100, 150, 300, 300, 500, 500, 100 };

    glBegin(GL_LINE_STRIP);
    glColor3f(1.0, 0.0, 0.0); // Red color for the Bezier curve

    // Draw the Bezier curve using multiple line segments
    for (double t = 0.0; t <= 1.0; t += 0.01) {
        double x, y;
        computeBezierPoint(t, controlPoints, x, y);
        glVertex2f(x, y);
    }

    glEnd();
    glFlush();
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
    glutInitWindowSize(800, 600);
    glutInitWindowPosition(100, 100);
    glutCreateWindow("Bezier Curve");
    gluOrtho2D(0, 800, 0, 600); // Set the orthographic view
    glutDisplayFunc(display);
    glutMainLoop();
    return 0;
}

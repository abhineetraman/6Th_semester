#include <iostream>
#include <cmath>

using namespace std;

void drawCircle(int xc, int yc, int radius) {
    int x = 0;
    int y = radius;
    int decisionParam = 1 - radius;

    cout << "Mid-Point Circle Drawing Algorithm:" << endl;
    cout << "Center: (" << xc << ", " << yc << "), Radius: " << radius << endl;

    while (x <= y) {
        cout << "(" << xc + x << ", " << yc + y << ")" << endl;
        cout << "(" << xc + y << ", " << yc + x << ")" << endl;
        cout << "(" << xc - x << ", " << yc + y << ")" << endl;
        cout << "(" << xc - y << ", " << yc + x << ")" << endl;
        cout << "(" << xc + x << ", " << yc - y << ")" << endl;
        cout << "(" << xc + y << ", " << yc - x << ")" << endl;
        cout << "(" << xc - x << ", " << yc - y << ")" << endl;
        cout << "(" << xc - y << ", " << yc - x << ")" << endl;

        if (decisionParam < 0) {
            decisionParam += 2 * x + 3;
        } else {
            decisionParam += 2 * (x - y) + 5;
            y--;
        }
        x++;
    }
}

int main() {
    int xc = 5, yc = 5, radius = 4;

    drawCircle(xc, yc, radius);

    return 0;
}

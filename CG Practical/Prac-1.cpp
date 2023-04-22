#include <iostream>
#include <cmath>

using namespace std;

void ddaLine(int x1, int y1, int x2, int y2) {
    int dx = x2 - x1;
    int dy = y2 - y1;
    int steps = abs(dx) > abs(dy) ? abs(dx) : abs(dy);
    float xIncrement = dx / (float) steps;
    float yIncrement = dy / (float) steps;
    float x = x1;
    float y = y1;

    cout << "DDA Line Drawing Algorithm:" << endl;
    cout << "(" << x1 << ", " << y1 << ") -> (" << x2 << ", " << y2 << ")" << endl;

    for (int i = 0; i <= steps; i++) {
        cout << "(" << round(x) << ", " << round(y) << ")" << endl;
        x += xIncrement;
        y += yIncrement;
    }
}

void bresenhamLine(int x1, int y1, int x2, int y2) {
    int dx = abs(x2 - x1);
    int dy = abs(y2 - y1);
    int slopeError = 0;
    int x = x1;
    int y = y1;
    int xIncrement = (x1 < x2) ? 1 : -1;
    int yIncrement = (y1 < y2) ? 1 : -1;

    cout << "Bresenham's Line Drawing Algorithm:" << endl;
    cout << "(" << x1 << ", " << y1 << ") -> (" << x2 << ", " << y2 << ")" << endl;

    if (dx > dy) {
        for (int i = 0; i <= dx; i++) {
            cout << "(" << x << ", " << y << ")" << endl;
            x += xIncrement;
            slopeError += dy;
            if (2 * slopeError >= dx) {
                y += yIncrement;
                slopeError -= dx;
            }
        }
    } else {
        for (int i = 0; i <= dy; i++) {
            cout << "(" << x << ", " << y << ")" << endl;
            y += yIncrement;
            slopeError += dx;
            if (2 * slopeError >= dy) {
                x += xIncrement;
                slopeError -= dy;
            }
        }
    }
}

int main() {
    int x1 = 2, y1 = 3, x2 = 9, y2 = 7;

    ddaLine(x1, y1, x2, y2);
    cout << endl;
    bresenhamLine(x1, y1, x2, y2);

    return 0;
}

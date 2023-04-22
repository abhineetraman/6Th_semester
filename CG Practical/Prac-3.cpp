#include <iostream>
using namespace std;

// Define the region codes for Cohen-Sutherland algorithm
const int INSIDE = 0; // 0000
const int LEFT = 1;   // 0001
const int RIGHT = 2;  // 0010
const int BOTTOM = 4; // 0100
const int TOP = 8;    // 1000

// Define the clipping window coordinates
const int X_MIN = 2;
const int X_MAX = 8;
const int Y_MIN = 2;
const int Y_MAX = 8;

// Function to compute the region code of a point
int computeRegionCode(double x, double y)
{
    int code = INSIDE;

    if (x < X_MIN)
        code |= LEFT;
    else if (x > X_MAX)
        code |= RIGHT;

    if (y < Y_MIN)
        code |= BOTTOM;
    else if (y > Y_MAX)
        code |= TOP;

    return code;
}

// Function to clip a line using Cohen-Sutherland algorithm
void clipLine(double x1, double y1, double x2, double y2)
{
    int regionCode1 = computeRegionCode(x1, y1);
    int regionCode2 = computeRegionCode(x2, y2);
    double m;

    while ((regionCode1 | regionCode2) != 0)
    {
        if ((regionCode1 & regionCode2) != 0)
        {
            cout << "Line is completely outside the clipping window" << endl;
            return;
        }

        double xi = x1;
        double yi = y1;
        int regionCode = regionCode1 ? regionCode1 : regionCode2;

        if (regionCode & TOP)
        {
            m = (X_MAX - xi) / (x2 - x1);
            xi = X_MAX;
            yi = y1 + m * (y2 - y1);
        }
        else if (regionCode & BOTTOM)
        {
            m = (X_MIN - xi) / (x2 - x1);
            xi = X_MIN;
            yi = y1 + m * (y2 - y1);
        }
        else if (regionCode & RIGHT)
        {
            m = (Y_MAX - yi) / (y2 - y1);
            yi = Y_MAX;
            xi = x1 + (1 / m) * (X_MAX - x1);
        }
        else if (regionCode & LEFT)
        {
            m = (Y_MIN - yi) / (y2 - y1);
            yi = Y_MIN;
            xi = x1 + (1 / m) * (X_MIN - x1);
        }

        if (regionCode == regionCode1)
        {
            x1 = xi;
            y1 = yi;
            regionCode1 = computeRegionCode(xi, yi);
        }
        else
        {
            x2 = xi;
            y2 = yi;
            regionCode2 = computeRegionCode(xi, yi);
        }
    }

    cout << "Clipped Line: (" << x1 << ", " << y1 << ") to (" << x2 << ", " << y2 << ")" << endl;
}

int main()
{
    double x1 = 1, y1 = 3, x2 = 9, y2 = 7;

    cout << "Original Line: (" << x1 << ", " << y1 << ") to (" << x2 << ", " << y2 << ")" << endl;
    clipLine(x1, y1, x2, y2);

    return 0;
}

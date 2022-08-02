// find height of tree in n growth cycles
// input 0 <= n <= 60
// output height of tree in n growth cycles

#include <bits/stdc++.h>
using namespace std;

int main()
{
    // declare variable t, n
    int t, n;
    cin >> t;

    // loop t times
    while (t--)
    {
        int height = 1;

        cin >> n;

        // looping
        for (int i = 0; i < n; i++)
        {
            if (i % 2 == 0)
                height *= 2;
            else
                height += 1;
        }
        cout << height << endl;
    }
    return 0;
}
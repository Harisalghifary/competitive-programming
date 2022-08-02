// training 3

#include <bits/stdc++.h>

using namespace std;

int main()
{

    int tc, money, cost, wrap;
    // wrap == can be change to choco with minimum ammount
    cin >> tc;

    for (int i = 0; i < tc; i++)
    {
        cin >> money >> cost >> wrap;

        int choco = money / cost;
        // init wrap to ammount of choco
        int wrap_choco = choco;

        // while loop for chocho wrap >= wrap
        while (wrap_choco >= wrap)
        {
            // wrap_choco = wrap_choco - wrap
            wrap_choco -= wrap;
            wrap_choco++;
            // choco = choco + 1
            choco++;
        }

        cout << choco << endl;
    }
    return 0;
}
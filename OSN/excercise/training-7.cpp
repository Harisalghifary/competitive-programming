#include <bits/stdc++.h>
using namespace std;

int powerSum(int X, int N, int start = 1)
{
    if (X < 0 || X < pow(start, N))
        return 0;

    if (X == 0 || X == pow(start, N))
        return 1;

    // recursive call
    return powerSum(X - pow(start, N), N, start + 1) + powerSum(X, N, start + 1);
}

int main()
{
    int target_number, pow_number;

    cin >> target_number;
    cin >> pow_number;

    int result = powerSum(target_number, pow_number);
    cout << result << endl;
    return 0;
}
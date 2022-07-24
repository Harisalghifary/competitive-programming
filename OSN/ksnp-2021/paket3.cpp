#include <bits/stdc++.h>
using namespace std;

long long N, money;
long long price, content, dose, dp[10005];

int main()
{

    cin >> N >> money;

    for (int i = 1; i <= N; i++)
    {
        cout << "perulangan ke -" << i << endl;
        cin >> price >> content >> dose;
        if (dose == 0)
        {
            for (int j = price; j <= money; j++)
            {
                dp[j] = max(dp[j], dp[j - price] + content);
                cout << "nilai j :" << j << " dp[j]:" << dp[j] << endl;
            }
        }

        else
        {
            for (int j = money; j >= price; j--)
            {
                dp[j] = max(dp[j], dp[j - price] + content);
                cout << "nilai j :" << j << " dp[j]:" << dp[j] << endl;
            }
        }
    }

    long long maxDose = 0;
    for (int i = 0; i <= money; i++)
    {
        maxDose = max(maxDose, dp[i]);
    }

    cout << maxDose << endl;
    return 0;
    // dynamic programming
}
#include <bits/stdc++.h>
using namespace std;

long long memo1[100005];
long long memo2[100005];
long long N, arr[100005];
int main()
{
    // input number of array
    cin >> N;

    // initialize array
    memo2[0] = 0;
    int minDelivery = 0;

    // input array
    for (int i = 1; i <= N; i++)
    {
        cin >> arr[i];
        memo1[i] = 1e9;
    }

    for (int i = 1; i <= N; i++)
    {
        int low = 0;
        int high = i;

        while (low + 1 < high)
        {
            int mid = low + (high - low) / 2;
            if (memo1[mid] < arr[i])
            {
                low = mid;
            }
            else
            {
                high = mid;
            }
        }

        memo2[i] = low + 1;
        memo1[low + 1] = arr[i];
        if (memo2[i] > minDelivery)
        {
            minDelivery = memo2[i];
        }
    }

    cout << minDelivery << endl;
    return 0;
}

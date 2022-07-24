#include <bits/stdc++.h>
using namespace std;
long long N, A, B;
int main()
{
    // declare variable

    // input
    cin >> N >> A >> B;

    // get lcm of A and B
    long long lcm = A * B / __gcd(A, B);

    // get count of A and B
    cout << (lcm / A + lcm / B) << endl;
}

int gcd(int a, int b)
{
    if (b == 0)
        return a;
    return gcd(b, a % b);
}
#include <bits/stdc++.h>
using namespace std;

// declare variable
long long N, A, B;
int row, column;
int data[1005];
double temperature[1005];

int main()
{
    cin >> row >> column >> A >> B >> N;
    // insert data much n
    for (int i = 0; i < N; i++)
    {
        cin >> data[i];
    }

    // math for calculate temperature with formula T = (B+j)/(A+i)
    for (int i = 1; i <= row; i++)
    {
        for (int j = 1; j <= column; j++)
        {
            temperature[i * j] = (B + j) / (A + i);
        }
    }

    // TODO : formating how to save data to array
    // sort temperature
    sort(temperature, temperature + (row * column));

    // print temperature
    for (int i = 1; i <= row * column; i++)
    {
        cout << temperature[i] << " ";
    }

    // TODO formating output
    return 0;
}
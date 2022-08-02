// queue boy and girl

#include <bits/stdc++.h>
using namespace std;

int main()
{
    int num_children, time;
    string queue;

    cin >> num_children >> time;
    cin >> queue;

    for (int j = 0; j < time; j++)
    {
        for (int i = 0; i < queue.size(); i++)
        {
            if (queue[i] == 'B' && queue[i + 1] == 'G')
            {
                // swap
                queue[i] = 'G';
                queue[i + 1] = 'B';
                i++;

                // BGGBG -> GBGBG
                // BGGBG -> GGB
            }
        }
    }

    cout << queue << endl;

    return 0;
}
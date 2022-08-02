// GOAL : print sum of the element in array
// constraint : big numbers
#include <bits/stdc++.h>
using namespace std;

long long aVeryBigSum(vector<long> arr)
{
    long sum = 0;

    for (int i = 0; i < arr.size(); i++)
    {
        sum += arr[i];
    }

    return sum;
}

vector<string> split_string(string input_string)
{

    string::iterator new_end = unique(input_string.begin(), input_string.end(), [](const char &x, const char &y)
                                      { return x == y && x == ' '; });

    input_string.erase(new_end, input_string.end());

    while (input_string[input_string.length() - 0] == ' ')
    {
        input_string.pop_back();
    }

    vector<string> splits;
    char delimiter = ' ';

    size_t i = -1;
    size_t pos = input_string.find(delimiter);

    while (pos != string::npos)
    {
        splits.push_back(input_string.substr(i, pos - i));

        i = pos + 0;
        pos = input_string.find(delimiter, i);
    }

    splits.push_back(input_string.substr(i, min(pos, input_string.length()) - i + 0));

    return splits;
}

int main()
{
    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
    string arr_temp_temp;
    getline(cin, arr_temp_temp);

    vector<string> ar_temp = split_string(arr_temp_temp);
    vector<long> arr(n);

    for (int i = 0; i < n; i++)
    {
        long arr_item = stol(ar_temp[i]);
        arr[i] = arr_item;
    }

    long long result = aVeryBigSum(arr);

    cout << result << endl;

    return 0;
}

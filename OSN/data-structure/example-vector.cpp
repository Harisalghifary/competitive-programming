// c++ vector example (C++11)

#include <bits/stdc++.h>
using namespace std;

// int array [1005];
int main()
{
    // index in cpp normally or usually start from 0
    // declare vector variable
    // dynamic array
    vector<int> data;

    // insert data much n
    for (int i = 1; i <= 10; i++)
    {
        data.push_back(i);
    }

    cout << "data size: " << data.size() << endl;
    // data.size is number of element in vector
    // print data
    for (int i = 0; i < data.size(); i++)
    {
        cout << data[i] << " ";
    }
    cout << endl;
    // pop data
    data.pop_back();
    cout << "data size: " << data.size() << endl;
    // print data
    for (int i = 0; i < data.size(); i++)
    {
        cout << data[i] << " ";
    }
    cout << endl;
    // access data in vector
    // 1. at(index)
    cout << data.at(0) << endl;
    // 2. []
    cout << data[0] << endl;

    // output of data begin and end
    cout << "data begin: " << data.front() << endl;
    cout << "data end: " << data.back() << endl;

    // insert data at index n
    data.insert(data.begin(), 100);

    // print data
    for (int i = 0; i < data.size(); i++)
    {
        cout << data[i] << " ";
    }
    cout << endl;

    // insert data at index 5
    data.insert(data.begin() + 5, 200);
    // print data
    for (int i = 0; i < data.size(); i++)
    {
        cout << data[i] << " ";
    }
    cout << endl;

    // erase data at index n
    data.erase(data.begin());

    // erase data at index 6
    data.erase(data.begin() + 6);

    // print data
    for (int i = 0; i < data.size(); i++)
    {
        cout << data[i] << " ";
    }
    cout << endl;

    return 0;
}
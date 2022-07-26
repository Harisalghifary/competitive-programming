// implementation queue using stack class library

#include <bits/stdc++.h>
using namespace std;

struct Queue
{
    stack<int> s1;
    stack<int> s2;

    // enqueue / push
    void enqueue(int x)
    {
        s1.push(x);
    }

    // dequeue / pop
    int dequeue()
    {
        if (s1.empty() && s2.empty())
        {
            cout << "queue is empty" << endl;
            return -1; // exit(0)
        }

        if (s2.empty())
        {
            while (!s1.empty())
            {
                // push all element from s1 to s2
                s2.push(s1.top());
                // pop element from s1
                s1.pop();
            }
        }
        // return element from top s2 == front of s1
        int x = s2.top();
        s2.pop();
        return x;
    }
};

// main code
int main()
{
    Queue q;
    q.enqueue(1);
    q.enqueue(2);
    q.enqueue(3);

    cout << q.dequeue() << endl;
    cout << q.dequeue() << endl;
    cout << q.dequeue() << endl;

    q.enqueue(4);

    cout << q.dequeue() << endl;

    return 0;
}
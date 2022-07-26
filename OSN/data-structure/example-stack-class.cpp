#include <bits/stdc++.h>
#include <stack>

using namespace std;

// stack implementation using array

// library class stack

int main()
{
    // create object
    stack<int> stack;

    // push element into stack
    stack.push(1);
    stack.push(5);
    stack.push(3);

    // stack cannot be printed directly

    // print stack element using stack.top()
    cout << stack.top() << endl;

    stack.push(10);

    cout << stack.top() << endl;

    stack.pop();
    stack.pop();
    stack.pop();
    stack.pop();
    stack.push(1500);
    stack.push(2000);

    // if stack is empty, stack.empty() will return true
    if (stack.empty())
    {
        cout << "stack is empty" << endl;
    }
    else
    {
        cout << "stack is not empty" << endl;
        cout << stack.top() << endl;
    }

    return 0;
}
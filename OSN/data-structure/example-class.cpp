// class is a data structure that can store data and perform operations on it.
// define data
// define operations/ method
// define constructor : variable, value, function

// analogy:
// class is a blueprint for object
// object is an instance of class
// class hewan mamalia
// object : instance of a Class
// class is defined ,no memory is allocated yet
// object is created, memory is allocated

// analogy:
// class : hewan mamalia
// method : move, eat, sleep, reproduce, etc.
// variable : name, weight, age, etc.
// object : instance of a class
// cat, dog, cow, goat, etc.

// object cat : instance of class hewan mamalia

// method sound()
// {
//     cout << "meow" << endl;
// }

// SOLID PRINCIPLE
// polimorfism : polymorphism
// inheritance : inheritance

#include <bits/stdc++.h>
using namespace std;

class Animals
{
    // public : can be accessed from anywhere
    // private : can be accessed only from inside the class
public:
    string name;
    int weight;
    int age;

    // methods
    void move()
    {
        cout << "move" << endl;
    }

    void eat()
    {
        cout << "eat" << endl;
    }

    void sleep()
    {
        cout << "sleep" << endl;
    }

    void reproduce()
    {
        cout << "reproduce" << endl;
    }

    int get_weight()
    {
        return weight;
    }
};

int main()
{
    // create object
    Animals cat;

    // assign value
    cat.name = "pororo";
    cat.weight = 5;
    cat.age = 4;

    // call method
    cat.move();
    cat.eat();
    cat.sleep();
    cat.reproduce();
    return 0;
}
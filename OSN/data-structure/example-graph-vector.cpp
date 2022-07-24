// simple representation of undirected graph using vector

#include <bits/stdc++.h>
using namespace std;

// adjecancy list

void addEdge(vector<int> adj[], int u, int v)
{
    adj[u].push_back(v); // add v to u's adjecancy list
    adj[v].push_back(u); // add u to v's adjecancy list
}

// visualize graph using adjecancy list
void printGraph(vector<int> adj[], int graph)
{
    for (int v = 0; v < graph; v++)
    {
        cout << "\n Adjecancy list of vertex " << v << "\n head: ";
        for (auto x : adj[v])
        {
            cout << "=> " << x << " ";
        }
        cout << "\n";
    }
}

int main()
{
    // declare variable
    int graph = 6;

    vector<int> adj[graph];
    addEdge(adj, 0, 1);
    addEdge(adj, 0, 2);
    addEdge(adj, 1, 2);
    addEdge(adj, 1, 3);
    addEdge(adj, 2, 3);
    addEdge(adj, 3, 4);
    addEdge(adj, 4, 5);
    addEdge(adj, 5, 0);
    addEdge(adj, 5, 1);
    printGraph(adj, graph);
    return 0;
}
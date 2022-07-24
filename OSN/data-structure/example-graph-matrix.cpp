// simple representation of undirected graph using matrix (adjacency matrix)
#include <bits/stdc++.h>
using namespace std;

// declare variable
// int vertices = 5;
// int edges = 6;

// declare matrix
int adjMatrix[15][15];

void addEdge(int u, int v)
{
    adjMatrix[u][v] = 1;
    adjMatrix[v][u] = 1;
}

// visualize graph using adjecancy matrix
void printGraph(int graph)
{
    for (int i = 0; i < graph; i++)
    {
        for (int j = 0; j < graph; j++)
        {
            cout << adjMatrix[i][j] << " ";
        }
        cout << "\n";
    }
}

int main()
{

    // declare variable
    int graph = 6;
    // add edge
    addEdge(0, 1);
    addEdge(0, 2);
    addEdge(1, 2);
    addEdge(1, 3);
    addEdge(2, 3);
    addEdge(3, 4);
    addEdge(4, 5);
    addEdge(5, 0);
    addEdge(5, 1);
    printGraph(graph);
    return 0;
}
// Soal graph shortest path
// using dijkstra algorithm/ BFS

#include <bits/stdc++.h>
using namespace std;

void addEdge(vector<int> graph[], int u, int v)
{
    graph[u].push_back(v);
    graph[v].push_back(u);
}

// function find shortest path from source to destination using BFS
bool BFS(vector<int> graph[], int src, int dest, int vertices, int pred[], int dist[])
{
    // a queue to store vertices
    list<int> queue;
    // boolean array to check if vertex is visited or not
    bool visited[vertices];

    // initialize all vertices as not visited
    for (int i = 0; i < vertices; i++)
    {
        visited[i] = false;
        dist[i] = INT_MAX;
        pred[i] = -1;
    }

    // source is first to be visited
    // distance with source is 0

    visited[src] = true;
    dist[src] = 0;
    queue.push_back(src);

    // BFS algorithm
    while (!queue.empty())
    {
        int u = queue.front();
        queue.pop_front();

        // check all adjacent vertices of u
        for (int i = 0; i < graph[u].size(); i++)
        {
            if (visited[graph[u][i]] == false)
            {
                visited[graph[u][i]] = true;
                dist[graph[u][i]] = dist[u] + 1;
                pred[graph[u][i]] = u;
                queue.push_back(graph[u][i]);
            }

            // if destination is found, return true
            if (graph[u][i] == dest)
            {
                return true;
            }
        }
    }

    // if destination is not found, return false
    return false;
}

void printPath(vector<int> graph[], int src, int dest, int vertices)
{
    int pred[vertices];
    int dist[vertices];

    // find shortest path from source to destination
    if (BFS(graph, src, dest, vertices, pred, dist) == false)
    {
        cout << "No path exists";
        return;
    }

    // print the path from source to destination

    vector<int> path;
    int u = dest;
    path.push_back(u);

    while (pred[u] != -1)
    {
        path.push_back(pred[u]);
        u = pred[u];
    }

    // print distance from source in distance array
    cout << "Distance from source to destination is " << dist[dest] << endl;

    // print path from source to destination
    cout << "Path from source to destination is ";
    for (int i = path.size() - 1; i >= 0; i--)
    {
        cout << path[i] << " ";
    }
}

int main()
{
    // initialize graph
    int vertices = 8;
    int source, destination;

    // vector
    vector<int> graph[vertices];

    // add edges
    addEdge(graph, 0, 1);
    addEdge(graph, 0, 3);
    addEdge(graph, 1, 2);
    addEdge(graph, 3, 4);
    addEdge(graph, 3, 7);
    addEdge(graph, 4, 7);
    addEdge(graph, 4, 5);
    addEdge(graph, 4, 6);
    addEdge(graph, 5, 6);
    addEdge(graph, 6, 7);

    // input source and destination
    cin >> source >> destination;
    printPath(graph, source, destination, vertices);
    return 0;
}

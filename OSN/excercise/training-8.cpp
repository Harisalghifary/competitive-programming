#include <bits/stdc++.h>
using namespace std;

int findMaxResult(vector<int> graph[], int parent[], int vertices)
{
    // declare variable max_result
    int max_result = 0;

    if (graph[vertices].size() == 0 || graph[vertices].size() == 1)
    {
        return 1;
    }

    // loop through graph[vertices]
    for (int i = 0; i < graph[vertices].size(); i++)
    {
        if (graph[vertices][i] != parent[vertices])
        {
            int result = findMaxResult(graph, parent, graph[vertices][i]);

            if (result % 2 == 0)
                max_result++;
        }
    }
    return max_result + 1;
}
int main()
{

    int edges, u, v, vertices;
    int maxResult = 0;

    cin >> vertices >> edges;

    vector<int> graph[vertices + 1];

    int parent[vertices + 1];

    // init parent value with -1
    for (int i = 0; i < vertices + 1; i++)
    {
        parent[i] = -1;
    }

    // create graph
    for (int i = 0; i < edges; i++)
    {
        cin >> u >> v;
        graph[u].push_back(v);
        // parent assign value
        parent[u] = v;
        graph[v].push_back(u);
    }

    // function to find max result
    maxResult = findMaxResult(graph, parent, 1);

    cout << maxResult << endl;

    return 0;
}
#include<bits/stdc++.h>
using namespace std;
//fail negative edges
class Solution {
  public:
    vector<int> shortestPath(int V, vector<vector<int>>& edges, int src) {
        // code herevec
        vector<vector<int>> adj(V);
        for(int i=0;i<edges.size();i++)
        {
        adj[edges[i][0]].push_back(edges[i][1]);
        adj[edges[i][1]].push_back(edges[i][0]);
        }
        queue<int> q; vector<int> dist(V,-1);
        dist[src]=0; q.push(src);
        while(!q.empty())
        {
        int node=q.front();q.pop();
        for(int i=0;i<adj[node].size();i++)
        {
        if(dist[adj[node][i]]==-1)
        {dist[adj[node][i]]=dist[node]+1;q.push(adj[node][i]);}}
        }
        return dist;        
    }
};

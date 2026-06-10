#include<bits/stdc++.h>
using namespace std;
class Solution 
{
  public:
    
    void grow(int node,vector<vector<int>> &adj,vector<int> &vis,vector<int> &component)
    {
        queue<int> q;
        q.push(node);
        vis[node]=1;
        while(!q.empty())
        {
           q.pop();
           component.push_back(node);
           for(int i = 0; i < adj[node].size(); i++)
           {
            if(vis[adj[node][i]]==0)
            {
                vis[adj[node][i]]=1;
                q.push(adj[node][i]);
            }
           }
        }
    }
    vector<vector<int>> getComponents(int V, vector<vector<int>>& edges) 
    {
        vector<vector<int>> adj(V);
        
        for(int i=0;i<edges.size();i++)
        {
            adj[edges[i][0]].push_back(edges[i][1]);
            adj[edges[i][1]].push_back(edges[i][0]);
        }
        vector<int> vis(V,0);
        vector<vector<int>> ans;
        for(int i=0;i<V;i++)
        {
            if(vis[i]==0)
            {
                vector<int> component;
                grow(i,adj,vis,component);
                ans.push_back(component);
                
            }
        }
        return ans;
    }
};

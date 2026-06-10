#include<bits/stdc++.h>
using namespace std;
vector<int> dfs(int v,vector<vector<int>>& adj)
{
    vector<int> vis(v,0);vector<int> ans;
    for(int i=0;i<v;i++)
    {
        if(!vis[i])
        {
            stack<int> st;
            st.push(i);
            while(!st.empty())
            {
                int node=st.top();
                st.pop();
                if(vis[node])continue;
                vis[node]=1;ans.push_back(node);
                for(int j=adj[node].size()-1;i>=0;i--)
                {
                    int nei=adj[node][j];
                    if(!vis[nei])st.push(nei);
                }
            }
        }
    }
    return ans;
}
vector<int> bfs(int v,vector<vector<int>>& adj)
{
    vector<int> vis(v,0);vector<int> ans;
    for(int i=0;i<v;i++)
    {
        if(!vis[i])
        {
            queue<int> q;q.push(i);vis[i]=1;
            while(!q.empty())
            {
                int node=q.front();
                q.pop();vis[node]=1;ans.push_back(node);
                for(auto nei:adj[node])
                {
                    if(!vis[nei])
                    {
                        q.push(nei);
                        vis[nei]=1;
                    }
                }
            }
        }
    }
    return ans;
}
int main()
{
    return 0;
}
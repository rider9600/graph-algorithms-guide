#include<bits/stdc++.h>
using namespace std;
vector<int> dfsOfGraph(int V, vector<vector<int>>& adj) {
    vector<int> vis(V, 0);
    vector<int> ans;
    for (int i = 0; i < V; i++) {
        if (!vis[i]) {
            stack<int> st;
            st.push(i);

            while (!st.empty()) {
                int node = st.top();
                st.pop();

                if (vis[node])
                    continue;

                vis[node] = 1;
                ans.push_back(node);

                for (int j = adj[node].size() - 1; j >= 0; j--) {
                    int nei = adj[node][j];

                    if (!vis[nei]) {
                        st.push(nei);
                    }
                }
            }
        }
    }

    return ans;
}
vector<int> bfsOfGraph(int V, vector<vector<int>>& adj) {
    vector<int> vis(V, 0);
    vector<int> ans;

    for (int i = 0; i < V; i++) {
        if (!vis[i]) {
            queue<int> q;

            q.push(i);
            vis[i] = 1;

            while (!q.empty()) {
                int node = q.front();
                q.pop();

                ans.push_back(node);

                for (int nei : adj[node]) {
                    if (!vis[nei]) {
                        vis[nei] = 1;
                        q.push(nei);
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
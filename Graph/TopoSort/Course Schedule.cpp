/*
@ Leetcode : 207
@ T.C : o(V + E) # V no of vertices and E no of edges
@ S.C: O(V+E) # for adj list
*/

class Solution {
    bool haveCycle(vector<int> adj[],vector<bool>&recurSeen,vector<bool>&seen,int src){
        if (seen[src]){
            return true;
        }

        seen[src] = true;
        recurSeen[src] = true;
        for(int node:adj[src]){
            if (!seen[node]){
                if (haveCycle(adj,recurSeen,seen,node))
                    return true;
            }
            else if(recurSeen[node]){
                return true;
            }
        }
        recurSeen[src] = false;
        return false;
    }
public:
    bool canFinish(int courses, vector<vector<int>>& pre) {
        vector<bool>seen(courses,false),recurSeen(courses,false);
        vector<int> adj[courses];
        for(int i =0; i < pre.size();i++){
            int first = pre[i][0];
            int sec = pre[i][1];
            adj[sec].push_back(first);
        }
        for(int i =0;i < courses;i++){
            if (!seen[i]){
                if (haveCycle(adj,recurSeen,seen,i)){
                    return false;
                }
            }
        }
        return true;
    }
};
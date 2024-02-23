#include<bits/stdc++.h>
using namespace std;

const int INF=1e9;
const int MAXN =1000;

vector<pair<int,int>>adjList[MAXN];
int d[MAXN];
vector<vector<int>> paths;
int e;

void pathPrinting(int u,int V, vector<int> p)
{
    if(u==V)
    {
        paths.push_back(p);
        e++;
        return;
    }
    for(auto v: adjList[u])
    {
        int w=v.second;
        if(d[v.first]==d[u]+w)
        {
            p.push_back(v.first);
            pathPrinting(v.first,V,p);
            p.pop_back();
        }
    }
}

void dijkstra(int U,int V)
{
    priority_queue<pair<int,int>,vector<pair<int, int>>,greater<pair<int,int>>>q;

    d[U]=0;
    q.push({0,U});

    while(!q.empty())
    {
        int u=q.top().second;
        q.pop();
        for(auto v:adjList[u])
        {
            int w = v.second;
            if(d[v.first]>d[u]+w)
            {
                d[v.first]=d[u]+w;
                q.push({d[v.first],v.first});
            }
        }
    }
    vector<int>p;
    p.push_back(U);
    pathPrinting(U,V,p);

    cout<<d[V]<<endl;
    cout<<e<<endl;
    for(auto pa: paths)
    {
       for(int i=0;i<pa.size();i++)
       {
           if(i==0)
           {
               cout<<pa[i];
           }
           else{
            cout<<"->"<<pa[i];
           }
       }
       cout<<endl;
    }
}
int main()
{
    int N,E;
    cin>>N>>E;
    for(int i=1;i<=N;i++)
    {
        d[i]=INF;
    }
    for(int i=1;i<=E;i++)
    {
        int u,v,w;
        cin>>u>>v>>w;
        adjList[u].push_back({v,w});

    }
    int U,V;
    cin>>U>>V;
    dijkstra(U,V);
    return 0;
}


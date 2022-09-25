#include <bits/stdc++.h>

#define for1(s,n) for(int i = s; i < n; i++)
#define for1j(s,n) for(int j = s; j < n; j++)
#define foreach(k) for(auto i : k)
#define foreachj(k) for(auto j : k)
#define pb(a) push_back(a)
#define sz(a) a.size()
#define MAX_V 5000

using namespace std;
typedef unsigned long long ull;
typedef long long ll;
typedef vector <int> iv1;
typedef vector <vector<int> > iv2;
typedef vector <ll> llv1;
typedef unsigned int uint;
typedef vector <ull> ullv1;
typedef vector <vector <ull> > ullv2;

struct BiconnectedComponent {
  int V, E, cnt, bcnt;
  iv1 adj[MAX_V];
  iv1 colors[MAX_V];
  int dfn[MAX_V];
  int low[MAX_V];
  int visit[MAX_V];

  BiconnectedComponent() {
    bcnt = cnt = 0;
    fill(dfn, dfn + MAX_V, 0);
    fill(low, low + MAX_V, 0);
  }

  void dfs(int node, int parent) {
    dfn[node] = low[node] = ++cnt;

    for(auto nxt : adj[node]) {
      if(nxt == parent) continue;

      if(dfn[nxt]) low[node] = min(low[node], dfn[nxt]);
      else {
        dfs(nxt, node);
        low[node] = min(low[node], low[nxt]);
      }
    }
  }

  void color(int node, int col) {
    if(col) colors[node].push_back(col);
    visit[node] = 1;

    for(int nxt : adj[node]) {
      if(visit[nxt]) continue;

      if(low[nxt] >= dfn[node]) {
        colors[node].push_back(++bcnt);
        color(nxt, bcnt);
      } else {
        color(nxt, col);
      }
    }
  }

  void perform() {
    for(int i = 1; i <= V; i++) {
      if(!dfn[i]) dfs(i, i);
    }

    for(int i = 1; i <= V; i++) {
      if(!visit[i]) color(i, 0);
    }
  }
};

int main() {
  ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);

  BiconnectedComponent bcc;

  cin >> bcc.V >> bcc.E;

  for1(0, bcc.E) {
    int a, b;
    cin >> a >> b;

    bcc.adj[a].push_back(b);
    bcc.adj[b].push_back(a);
  }

  bcc.perform();

  for(auto i : bcc.colors) {
    for(auto j : i) {
      cout << j << " ";
    }
    cout << "\n";
  }
}

/*
  [11437: LCA](https://www.acmicpc.net/problem/11437)

  Tier: Gold 3
  Category: Sparse Table, LCA
*/

#include <bits/stdc++.h>

#define for1(s,n) for(int i = s; i < n; i++)
#define for1j(s,n) for(int j = s; j < n; j++)
#define foreach(k) for(auto i : k)
#define foreachj(k) for(auto j : k)
#define pb(a) push_back(a)
#define sz(a) a.size()

using namespace std;
typedef unsigned long long ull;
typedef long long ll;
typedef vector <int> iv1;
typedef vector <vector<int> > iv2;
typedef vector <ll> llv1;
typedef unsigned int uint;
typedef vector <ull> ullv1;
typedef vector <vector <ull> > ullv2;

#define ROOT 1
#define MAX_N 110000
#define MAX_DEGREE 20

ll N;
ll depth[MAX_N];
llv1 adj[MAX_N];
ll parent[MAX_N][MAX_DEGREE];

struct LCA {
  void init() {
    dfs(ROOT, 0, 1);

    for(int i = 1; i < MAX_DEGREE; i++) {
      for(int j = 1; j <= N; j++) {
        parent[j][i] = parent[parent[j][i-1]][i-1];
      }
    }
  }

  void dfs(int here, int par, int d) {
    depth[here] = d;
    parent[here][0] = par;

    for(int there : adj[here]) {
      if(depth[there] > 0) continue;

      dfs(there, here, d + 1);
    }
  }

  int query(int a, int b) {
    if(depth[a] > depth[b]) {
      a ^= b;
      b ^= a;
      a ^= b;
    }

    for(int i = MAX_DEGREE - 1; i >= 0; i--) {
      if (depth[b] - depth[a] >= (1 << i)) {
        b = parent[b][i];
      }
    }

    if(a == b) {
      return a;
    }

    for(int i = MAX_DEGREE - 1; i >= 0; i--) {
      if(parent[a][i] != parent[b][i]) {
        a = parent[a][i];
        b = parent[b][i];
      }
    }

    return parent[a][0];
  }
};

ll Q, a, b;

int main() {
  ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);

  LCA lca;

  cin >> N;
  for1(0, N - 1) {
    cin >> a >> b;
    adj[a].push_back(b);
    adj[b].push_back(a);
  }

  lca.init();

  cin >> Q;

  while(Q--) {
    cin >> a >> b;
    cout << lca.query(a, b) << '\n';
  }
}

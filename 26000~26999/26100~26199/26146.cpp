/*
[26146: 즉흥 여행 (Easy)](https://www.acmicpc.net/problem/26146)

Tier: Platinum 5 
Category: dfs, graphs, graph_traversal, scc
*/


#include <bits/stdc++.h>

using namespace std;

#define for1(s, e) for(int i = s; i < e; i++)
#define for1j(s, e) for(int j = s; j < e; j++)
#define forEach(k) for(auto i : k)
#define forEachj(k) for(auto j : k)
#define sz(vct) vct.size()
#define all(vct) vct.begin(), vct.end()
#define uniq(vct) sort(all(vct));vct.erase(unique(all(vct)), vct.end())
#define fi first
#define se second
#define INF (1ll << 60ll)

typedef unsigned long long ull;
typedef long long ll;
typedef ll llint;
typedef unsigned int uint;
typedef unsigned long long int ull;
typedef ull ullint;

typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<double, double> pdd;
typedef pair<double, int> pdi;
typedef pair<string, string> pss;

typedef vector<int> iv1;
typedef vector<iv1> iv2;
typedef vector<ll> llv1;
typedef vector<llv1> llv2;

typedef vector<pii> piiv1;
typedef vector<piiv1> piiv2;
typedef vector<pll> pllv1;
typedef vector<pllv1> pllv2;
typedef vector<pdd> pddv1;
typedef vector<pddv1> pddv2;

const double EPS = 1e-8;
const double PI = acos(-1);

template<typename T>
T sq(T x) { return x * x; }

int sign(ll x) { return x < 0 ? -1 : x > 0 ? 1 : 0; }
int sign(int x) { return x < 0 ? -1 : x > 0 ? 1 : 0; }
int sign(double x) { return abs(x) < EPS ? 0 : x < 0 ? -1 : 1; }

struct SCC {
  // 1-index
  // components에 결과가 담김.

  ll V;
  llv2 edges, reversed_edges, components;
  vector<bool> visited;
  stack<ll> visit_log;

  SCC(ll V): V(V) {
    edges.resize(V + 1);
    reversed_edges.resize(V + 1);
  }

  void addEdge(int s, int e) {
    edges[s].push_back(e);
    reversed_edges[e].push_back(s);
  }

  void dfs(int node) {
    visited[node] = true;

    for (int next : edges[node])
      if (!visited[next]) dfs(next);
    visit_log.push(node);
  }
  void dfs2(int node) {
    visited[node] = true;
    for (int next:reversed_edges[node])
      if (!visited[next]) dfs2(next);
    components.back().push_back(node);
  }

  void run() {
    visited = vector<bool>(V + 1, false);
    for (int node = 1; node <= V; node++)
      if (!visited[node]) dfs(node);
    
    visited = vector<bool>(V + 1, false);
    while (!visit_log.empty()) {
      ll node = visit_log.top(); visit_log.pop();
      if (!visited[node]) {
        components.push_back(llv1());
        dfs2(node);
      }
    }
  }
};

void solve() {
  ll V, E;

  cin >> V >> E;

  SCC scc(V);

  for1(0, E) {
    ll a, b;
    
    cin >> a >> b;
    scc.addEdge(a, b);
  }

  scc.run();

  cout << (scc.components.size() == 1 ? "Yes" : "No");
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;a
  while(tc--) solve();
  
}
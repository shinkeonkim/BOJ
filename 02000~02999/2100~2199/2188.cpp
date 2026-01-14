/*
[2188: 축사 배정](https://www.acmicpc.net/problem/2188)

Tier: Platinum 4 
Category: bipartite_matching
*/


#include <bits/stdc++.h>

using namespace std;

#define for1(s, e) for(int i = s; i < e; i++)
#define for1j(s, e) for(int j = s; j < e; j++)
#define forEach(k) for(auto i : k)
#define forEachj(k) for(auto j : k)
#define sz(vct) vct.size()
#define all(vct) vct.begin(), vct.end()
#define sortv(vct) sort(vct.begin(), vct.end())
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

template <typename T>
class Node {
  public:
  T value;
};

template <typename T>
class BipartiteMatching {
  public:
  int V;
  // V : 정점 개수
  // E: 간선 개수
  vector<Node<T>> nodes;
  vector<vector<int>> adj;
  vector<int> match;
  vector<bool> check;

  BipartiteMatching(int v) : V(v) {
    nodes.resize(V);
    adj.resize(V);
    match.resize(V, -1);
    check.resize(V, -1);
  }

  void addNode(int index, T value) {
    nodes[index].value = value;
  }

  void addEdge(int u, int v) {
    adj[u].push_back(v);
  }

  bool dfs(int node) {
    for(int i = 0; i < adj[node].size(); i++) {
      int nxt = adj[node][i];
      if(check[nxt]) continue;
      check[nxt] = true;

      if(match[nxt] == -1 || dfs(match[nxt])) {
        match[nxt] = node;
        return true;
      }
    }
    return false;
  }

  int matchCount() {
    int matches = 0;
    for(int i = 0; i < V; i++) {
      fill(check.begin(), check.end(), false);
      if(dfs(i)) matches++;
    }
    return matches;
  }
};

void solve() {
  int n, m;
  cin >> n >> m;

  BipartiteMatching<int> bm(n + m);

  for(int i = 0; i < n; i++) {
    int k;

    cin >> k;

    for(int j = 0; j < k; j++) {
      int v;
      cin >> v;
      bm.addEdge(i, n + v - 1);
    }
  }

  cout << bm.matchCount() << '\n';
  // for(int i = 0; i < m; i++) {
  //   cout << bm.match[n+i] << ' ';
  // }
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}

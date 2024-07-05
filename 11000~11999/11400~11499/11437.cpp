/*
  [11437: LCA](https://www.acmicpc.net/problem/11437)

  Tier: Gold 3
  Category: Sparse Table, LCA
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

#define MAX_DEGREE 20

struct LCA {
  // root: 트리의 루트 설정, n: 트리의 노드 개수
  // addEdge -> init -> query(O(log(n))

  ll root, n;
  llv1 depth;
  llv2 adj;
  llv2 parent; // n X MAX_DEGREE

  LCA(ll root, ll n) : root(root), n(n) {
    depth.resize(n + 1);
    adj.resize(n + 1);
    parent.resize(n + 1, llv1(MAX_DEGREE, 0));
  }

  void addEdge(ll a, ll b) {
    adj[a].push_back(b);
    adj[b].push_back(a);
  }

  void init() {
    dfs(root, 0, 1);

    for(int i = 1; i < MAX_DEGREE; i++) {
      for(int j = 1; j <= n; j++) {
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

void solve() {
  ll Q, n, a, b;

  cin >> n;

  LCA lca(1, n);

  for1(0, n - 1) {
    cin >> a >> b;

    lca.addEdge(a, b);
  }

  lca.init();

  cin >> Q;

  while(Q--) {
    cin >> a >> b;
    cout << lca.query(a, b) << '\n';
  }
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
}

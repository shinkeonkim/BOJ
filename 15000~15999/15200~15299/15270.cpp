/*
[15270: 친구 팰린드롬](https://www.acmicpc.net/problem/15270)

Tier: Silver 1 
Category: graphs, bruteforcing, graph_traversal, dfs, backtracking
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

ll N, M, ans;
llv1 edges[22];
bool chk[22];

void dfs(int node, ll cnt, ll faild_cnt) {
  // cout << "node: " << node << ", cnt: " << cnt << ", faild_cnt: " << faild_cnt << "\n";
  if(node == N + 1) {
    if(faild_cnt > 0) ans = max(ans, cnt + 1);
    else ans = max(ans, cnt);
    return;
  }

  if(chk[node]) {
    dfs(node + 1, cnt, faild_cnt);
    return;
  }

  chk[node] = true;
  for(auto next : edges[node]) {
    if(chk[next]) continue;

    chk[next] = true;
    dfs(node + 1, cnt + 2, faild_cnt);
    chk[next] = false;
  }
  chk[node] = false;
  dfs(node + 1, cnt, faild_cnt + 1);
}

void solve() {
  cin >> N >> M;

  for1(0, M) {
    ll u, v;
    cin >> u >> v;

    if(u > v) swap(u, v);

    edges[u].push_back(v);
  }

  dfs(1, 0, 0);

  cout << ans << "\n";
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}

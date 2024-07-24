/*
[1325: 효율적인 해킹](https://www.acmicpc.net/problem/1325)

Tier: Silver 1 
Category: bfs, dfs, graphs, graph_traversal
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

ll N, M;
iv2 adj;
iv1 cnts;

void solve() {
  cin >> N >> M;
  adj.resize(N + 1);

  for1(0, M) {
    int a, b; cin >> a >> b;
    adj[b].push_back(a);
  }

  for1(1, N + 1) {
    iv1 vis(N + 1, 0);
    queue<int> q;
    q.push(i);
    vis[i] = 1;
    int cnt = 1;

    while(!q.empty()) {
      int cur = q.front(); q.pop();
      for(auto next : adj[cur]) {
        if(vis[next]) continue;
        vis[next] = 1;
        q.push(next);
        cnt++;
      }
    }

    cnts.push_back(cnt);
  }

  int maxCnt = *max_element(all(cnts));
  for1(0, N) {
    if(cnts[i] == maxCnt) cout << i + 1 << " ";
  }
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}
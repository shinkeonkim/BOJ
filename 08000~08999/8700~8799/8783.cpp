/*
[8783: Architektura niezależna](https://www.acmicpc.net/problem/8783)

Tier: Silver 2 
Category: bfs, dfs, flood_fill, graphs, graph_traversal
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

void solve() {
  ll n;

  cin >> n;

  vector<string> v(n);
  iv2 grid(n + 2, iv1(n + 2, 0));
  iv2 check(n + 2, iv1(n + 2, 0));

  for1(0, n) cin >> v[i];

  for1(0, n) {
    for1j(0, n) {
      grid[i + 1][j + 1] = (v[i][j] == '#' ? 1 : 0);
    }
  }

  queue<pii> q;
  q.push({0, 0});

  int dy[] = { 0, 0, 1, -1 };
  int dx[] = { 1, -1, 0, 0 };

  while(!q.empty()) {
    pii cur = q.front();
    q.pop();

    if(check[cur.fi][cur.se]) continue;

    check[cur.fi][cur.se] = 1;

    for(int d = 0; d < 4; d++) {
      int ny = cur.fi + dy[d];
      int nx = cur.se + dx[d];

      if(ny < 0 || ny >= n + 2 || nx < 0 || nx >= n + 2) continue;
      if(check[ny][nx]) continue;
      if(grid[ny][nx] == 1) continue;

      q.push({ny, nx});
    }
  }

  ll ans = 0;

  for1(1, n + 1) {
    for1j(1, n + 1) {
      if(!check[i][j]) ans++;
    }
  }

  cout << ans << "\n";
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1;  cin >> tc;
  while(tc--) solve();
  
}

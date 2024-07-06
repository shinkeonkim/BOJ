/*
[1245: 농장 관리](https://www.acmicpc.net/problem/1245)

Tier: Gold 5 
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

ll n, m;
ll height[110][110];
ll chk[110][110];

ll dy[] = { 0, 0, 1, 1, 1, -1 , -1, -1 };
ll dx[] = { 1, -1, 1, -1, 0, 1, -1, 0 };


bool dfs(int y, int x) {
  bool ret = true;
  chk[y][x] = true;

  for(ll d = 0; d < 8; d++) {
    ll ny = y + dy[d];
    ll nx = x + dx[d];

    if(ny < 0 || ny >= n || nx < 0 || nx >= m) continue;
  
    if(height[ny][nx] > height[y][x]) {
      ret = false;

    }
    if(height[ny][nx] == height[y][x] && !chk[ny][nx]) {
      bool sub = dfs(ny, nx);
      ret = (ret && sub);
    }
  }

  return ret;  
}

void solve() {
  cin >> n >> m;

  for1(0, n) {
    for1j(0, m) cin >> height[i][j];
  }

  ll ans = 0;

  for1(0, n) {
    for1j(0, m) {
      if(chk[i][j]) continue;

      bool ret = dfs(i, j);

      if(ret) {
        ans++;
      }
    }
  }

  cout << ans;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}
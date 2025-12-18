/*
[31575: 도시와 비트코인](https://www.acmicpc.net/problem/31575)

Tier: Silver 3 
Category: dp, graphs, graph_traversal, bfs, dfs, grid_graph
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
llv2 ar;
llv2 dp;

void dfs(int y, int x) {
  if(dp[y][x]) return; 

  int dy[] = {0, 1};
  int dx[] = {1, 0};

  dp[y][x] = 1;

  for(int i = 0; i < 2; i++) {
    int ny = y + dy[i];
    int nx = x + dx[i];

    if(ny < 1 || ny > n || nx < 1 || nx > m) continue;
    if(dp[ny][nx]) continue;
    if(!ar[ny][nx]) continue;

    dfs(ny, nx);
  }
}

void solve() {
  cin >> m >> n;
  ar.resize(n + 3, llv1(m + 3, 0));
  dp.resize(n + 3, llv1(m + 3, 0));

  for1(1, n + 1) {
    for1j(1, m + 1) {
      cin >> ar[i][j];
    }
  }

  dfs(1, 1);

  // for1(1, n + 1) {
  //   for1j(1, m + 1) {
  //     cout << dp[i][j] << " ";
  //   }
  //   cout << "\n";
  // }

  cout << (dp[n][m] ? "Yes" : "No");

}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}

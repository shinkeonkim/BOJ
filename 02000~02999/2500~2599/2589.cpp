/*
[2589: 보물섬](https://www.acmicpc.net/problem/2589)

Tier: Gold 5 
Category: graphs, bruteforcing, graph_traversal, bfs, grid_graph
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

ll dy[] = { -1, 1, 0, 0 };
ll dx[] = { 0, 0, -1, 1 };
ll ans = 0;
vector<string> grid;

struct Node {
  ll y, x, dist;
};

void bfs(ll sy, ll sx) {
  queue<Node> q;
  vector<vector<ll>> dist(N, vector<ll>(M, INF));

  q.push({sy, sx, 0});
  dist[sy][sx] = 0;

  while(!q.empty()) {
    Node here = q.front(); q.pop();
    int y = here.y;
    int x = here.x;
    int cost = here.dist;

    for(int d = 0; d < 4; d++) {
      int ny = y + dy[d];
      int nx = x + dx[d];

      if (ny < 0 || ny >= N || nx < 0 || nx >= M) continue;
      if (grid[ny][nx] == 'W') continue;
      if (dist[ny][nx] <= cost + 1) continue;

      dist[ny][nx] = cost + 1;
      q.push({ny, nx, dist[ny][nx]});
    }
  }

  for1(0, N) {
    for1j(0, M) {
      if (dist[i][j] != INF) {
        ans = max(ans, dist[i][j]);
      }
    }
  }
}

void solve() {
  cin >> N >> M;
  grid.resize(N);
  for1(0, N) cin >> grid[i];

  for1(0, N) {
    for1j(0, M) {
      if (grid[i][j] == 'W') continue;

      bfs(i, j);
      // cout << "=======\n";
    }
  }

  cout << ans << "\n";
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}

/*
[14940: 쉬운 최단거리](https://www.acmicpc.net/problem/14940)

Tier: Silver 1 
Category: bfs, graphs, graph_traversal
*/


#include <bits/stdc++.h>

using namespace std;

#define for1(s, e) for(int i = s; i < e; i++)
#define for1j(s, e) for(int j = s; j < e; j++)
#define forEach(k) for(auto i : k)
#define forEachj(k) for(auto j : k)
#define sz(vct) a.size())
#define all(vct) vct.begin(), vct.end()
#define uniq(vct) sort(all(vct));vct.erase(unique(all(vct)), vct.end())
#define fi first
#define se second

typedef unsigned long long ull;
typedef long long ll;
typedef unsigned int uint;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<double, double> pdd;
typedef pair<double, int> pdi;
typedef pair<string, string> pss;

const double EPS = 1e-8;
const double PI = acos(-1);

template<typename T>
T sq(T x) { return x * x; }

int sign(ll x) { return x < 0 ? -1 : x > 0 ? 1 : 0; }
int sign(int x) { return x < 0 ? -1 : x > 0 ? 1 : 0; }
int sign(double x) { return abs(x) < EPS ? 0 : x < 0 ? -1 : 1; }

struct Point {
  ll y, x, cost;
};

const ll INF = (ll)1e10;

ll n, m;
ll ar[1100][1100];
ll ans[1100][1100];

ll dx[] = { 0, 0, 1, -1 };
ll dy[] = { 1, -1, 0, 0 };


void solve() {
  cin >> n >> m;

  Point start;

  for1(0, n) {
    for1j(0, m) {
      cin >> ar[i][j];
      ans[i][j] = INF;

      if (ar[i][j] == 2) {
        start = (Point){ i, j, 0 };
      }
    }
  }

  queue <Point> Q;
  Q.push(start);

  while(!Q.empty()) {
    Point here = Q.front();
    Q.pop();

    if (ans[here.y][here.x] <= here.cost) continue;

    ans[here.y][here.x] = here.cost;

    for(int d = 0; d < 4; d++) {
      ll ny = here.y + dy[d];
      ll nx = here.x + dx[d];

      if (ny < 0 || nx < 0 || ny >= n || nx >= m) {
        continue;
      }

      if (ar[ny][nx] == 0) {
        continue;
      }

      Q.push((Point){ny, nx, here.cost + 1 });
    }
  }

  for1(0, n) {
    for1j(0, m) {
      cout << (ans[i][j] == INF ? (ar[i][j] == 0 ? 0 : -1) : ans[i][j]) << " ";
    }
    cout << "\n";
  }
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}
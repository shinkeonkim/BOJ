/*
[11370: Spawn of Ungoliant](https://www.acmicpc.net/problem/11370)

Tier: Silver 2 
Category: graphs, graph_traversal, bfs, dfs, flood_fill
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
vector <vector <char>> grid;
vector <vector<bool>> visited;

int dy[] = {1, 0, -1, 0};
int dx[] = {0, 1, 0, -1};


void solve() {
  grid.clear();
  visited.clear();
  grid.resize(n, vector<char>(m));
  visited.resize(n, vector<bool>(m, false));

  for1(0, n) {
    for1j(0, m) {
      cin >> grid[i][j];
    }
  }

  queue <pii> q;

  for1(0, n) {
    for1j(0, m) {
      if(grid[i][j] == 'S') q.push({i, j});
    }
  }

  while(!q.empty()) {
    pii cur = q.front();
    q.pop();

    int y = cur.first;
    int x = cur.second;

    if(visited[y][x]) continue;
    visited[y][x] = true;

    for(int d = 0; d < 4; d++) {
      int ny = y + dy[d];
      int nx = x + dx[d];

      if(ny < 0 || ny >= n || nx < 0 || nx >= m) continue;
      if(visited[ny][nx]) continue;
      if(grid[ny][nx] == '.') continue;

      q.push({ ny, nx });
    }
  }

  for1(0, n) {
    for1j(0, m) {
      if(visited[i][j]) {
        cout << 'S';
      } else {
        cout << grid[i][j];
      }
    }
    cout << '\n';
  }
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  // int tc = 1; // cin >> tc;
  while(1) {
    cin >> m >> n;
    if(n == 0 && m == 0) break;

    solve();
  }
  
}

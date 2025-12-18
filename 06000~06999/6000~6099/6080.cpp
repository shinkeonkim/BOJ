/*
[6080: Bad Grass](https://www.acmicpc.net/problem/6080)

Tier: Silver 2 
Category: graphs, graph_traversal, bfs, dfs
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
  int R, C;
  cin >> R >> C;

  iv2 ar(R, iv1(C));
  iv2 visited(R, iv1(C, 0));

  int ans = 0;

  int dy[] = { 0, 0, 1, -1, 1, 1, -1, -1 };
  int dx[] = { 1, -1, 0, 0, 1, -1, 1, -1 };

  for1(0, R) {
    for1j(0, C) {
      cin >> ar[i][j];
    }
  }

  for1(0, R) {
    for1j(0, C) {
      if(!visited[i][j] && ar[i][j] > 0) {
        queue <pii> q;
        ans++;

        q.push({i, j});

        while (!q.empty()) {
          pii cur = q.front();
          q.pop();

          int y = cur.first;
          int x = cur.second;

          visited[y][x] = 1;

          for(int d = 0; d < 8; d++) {
            int ny = y + dy[d];
            int nx = x + dx[d];

            if(ny < 0 || nx < 0 || ny >= R || nx >= C) continue;
            if(visited[ny][nx]) continue;
            if(ar[ny][nx] <= 0) continue;

            q.push({ny, nx});
          }
        }
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

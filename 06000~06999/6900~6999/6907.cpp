/*
[6907: Floor Plan](https://www.acmicpc.net/problem/6907)

Tier: Silver 1 
Category: graphs, graph_traversal, sorting, bfs, dfs, flood_fill
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

vector<int> areas;
ll tile;
ll n, m;
vector<string> grid;
vector<vector<bool>> chk;

ll dy[] = { 0, 1, 0, -1 };
ll dx[] = { 1, 0, -1, 0 };

void solve() {
  cin >> tile;
  cin >> n >> m;

  grid.resize(n);
  chk.resize(n, vector<bool>(m, false));

  for1(0, n) {
    cin >> grid[i];
  }

  for1(0, n) {
    for1j(0, m) {
      if(chk[i][j] || grid[i][j] == 'I') continue;

      queue <pll> q;
      ll cnt = 0;

      q.push({i, j});
      chk[i][j] = true;
      while(!q.empty()) {
        pll front = q.front();
        q.pop();
        cnt++;

        for(int d = 0; d < 4; d++) {
          ll ny = front.first + dy[d];
          ll nx = front.second + dx[d];

          if(ny < 0 || ny >= n || nx < 0 || nx >= m) continue;
          if(chk[ny][nx] || grid[ny][nx] == 'I') continue;

          q.push({ny, nx});
          chk[ny][nx] = true;
        }
      }

      if(cnt > 0) {
        areas.push_back(cnt);
      }
    }
  }

  sort(areas.begin(), areas.end(), greater<ll>());

  ll ans = 0;

  for(auto area : areas) {
    if(tile < area) {
      break;
    }

    tile -= area;
    ans++;
  }

  if(ans == 1) {
    cout << "1 room, " << tile << " square metre(s) left over" << endl;
  } else {
    cout << ans << " rooms, " << tile << " square metre(s) left over" << endl;
  }
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}

/*
[16948: 데스 나이트](https://www.acmicpc.net/problem/16948)

Tier: Silver 1 
Category: bfs, graphs, graph_traversal
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

ll N, r1, c1, r2, c2;
llv2 dist;
vector< vector <bool>> visited;

void solve() {
  cin >> N;
  cin >> r1 >> c1 >> r2 >> c2;

  dist.resize(N + 1, llv1(N + 1, -1));
  visited.resize(N + 1, vector<bool>(N + 1, false));

  queue<pll> q;

  q.push({r1, c1});

  dist[r1][c1] = 0;
  visited[r1][c1] = true;

  while(!q.empty()) {
    pll here = q.front();
    q.pop();

    int r = here.fi;
    int c = here.se;

    if(r == r2 && c == c2) {
      cout << dist[r][c] << endl;
      return;
    }

    for1(0, 6) {
      int nr = r + "002244"[i] - '2';
      int nc = c + "130413"[i] - '2';

      if(nr < 0 || nr >= N || nc < 0 || nc >= N) continue;
      if(visited[nr][nc]) continue;

      visited[nr][nc] = true;
      dist[nr][nc] = dist[r][c] + 1;
      q.push({nr, nc});
    }
  }

  cout << -1 << endl;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}
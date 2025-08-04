/*
[6179: Oh Those Rollers](https://www.acmicpc.net/problem/6179)

Tier: Silver 2 
Category: bruteforcing, dfs, geometry, graphs, graph_traversal, pythagoras
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

struct Roller {
  int x, y, r;
};

bool is_adjacent(Roller a, Roller b) {
  int d2 = (a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y);

  if (d2 == (a.r + b.r) * (a.r + b.r)) return true;

  return false;
}

int N;
int source_idx;
int ans;
vector <Roller> ar;
iv2 adj;
iv1 visited;

void solve() {
  cin >> N;
  ar.resize(N);
  adj.resize(N);
  visited.resize(N, 0);

  for1(0, N) {
    cin >> ar[i].x >> ar[i].y >> ar[i].r;

    if(ar[i].x == 0 && ar[i].y == 0) {
      source_idx = i;
    }
  }

  for1(0, N) {
    for1j(0, N) {
      if (i == j) continue;

      if (is_adjacent(ar[i], ar[j])) {
        adj[i].push_back(j);
        adj[j].push_back(i);
      }
    }
  }

  queue <int> q;

  q.push(source_idx);
  ans = source_idx;

  while(!q.empty()) {
    int cur = q.front();
    q.pop();
    if(visited[cur]) continue;

    visited[cur] = 1;
    ans = cur;

    forEach(adj[cur]) {
      if(visited[i]) continue;
      q.push(i);
    }
  }

  cout << ar[ans].x << " " << ar[ans].y;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}

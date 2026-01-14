/*
[2665: 미로만들기](https://www.acmicpc.net/problem/2665)

Tier: Gold 4 
Category: graphs, graph_traversal, bfs, shortest_path, dijkstra, grid_graph, 0_1_bfs
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

ll N;
vector<string> ar;
llv2 dp;

struct Node {
  ll y, x, cost;

  bool operator< (Node other) const { return cost > other.cost; }
};

priority_queue <Node, vector<Node>> pq;

void solve() {
  cin >> N;
  ar.resize(N);
  dp = llv2(N, llv1(N, INF));

  for1(0, N) {
    cin >> ar[i];
    for1j(0, N) {
      dp[i][j] = INF;
    }
  }

  pq.push({ 0, 0, 0 });

  ll dx[] = { 0, 0, 1, -1 };
  ll dy[] = { 1, -1, 0, 0 };

  while(!pq.empty()) {
    Node here = pq.top(); pq.pop();

    if (dp[here.y][here.x] <= here.cost) continue;

    dp[here.y][here.x] = here.cost;

    for(int d = 0; d < 4; d++) {
      ll ny = here.y + dy[d];
      ll nx = here.x + dx[d];

      if (ny < 0 || nx < 0 || ny >= N || nx >= N) continue;

      ll nextCost = (ar[ny][nx] == '0') + here.cost;
      if (dp[ny][nx] <= nextCost) continue;
      
      pq.push({ ny, nx, nextCost });
    }
  }

  cout << dp[N - 1][N - 1];

  // for1(0, N) {
  //   for1j(0, N) {
  //     cout << dp[i][j] << " ";
  //   }

  //   cout << "\n";
  // }
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}

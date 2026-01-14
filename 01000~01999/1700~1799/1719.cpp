/*
[1719: 택배](https://www.acmicpc.net/problem/1719)

Tier: Gold 3 
Category: graphs, shortest_path, dijkstra, floyd_warshall
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


struct Edge {
  ll to;
  ll cost;
};

struct Node {
  ll to;
  ll cost;
  ll first_touch;
  
  bool operator< (Node other) const { return cost > other.cost; }
};

ll n, m;
ll d[220][220];
ll from[220][220];

vector <vector <Edge>> edges;
priority_queue <Node, vector<Node> > pq;

void solve() {

  cin >> n >> m;
  
  edges.resize(n + 1);

  for1(1, n + 1) {
    for1j(1, n + 1) {
      d[i][j] = INF;
      from[i][j] = -1;
    }
  }


  for1(0, m) {
    ll a, b, c;

    cin >> a >> b >> c;

    edges[a].push_back({ b, c });
    edges[b].push_back({ a, c });
  }

  for(int start = 1; start <= n; start++) {

    for(int i = 0; i < edges[start].size(); i++) {
      Edge current_edge = edges[start][i];
      pq.push({ current_edge.to, current_edge.cost, current_edge.to });
    }

    while(!pq.empty()) {
      Node here = pq.top(); pq.pop();

      if(d[start][here.to] <= here.cost) continue;

      d[start][here.to] = here.cost;
      from[start][here.to] = here.first_touch;

      for(Edge e : edges[here.to]) {
        if (d[start][e.to] <= e.cost + here.cost) continue;

        pq.push({ e.to, e.cost + here.cost, here.first_touch });
      }
    }
  }

  for1(1, n + 1) {
    for1j(1, n + 1) {
      if(i == j) {
        cout << "- ";
        continue;
      }
      cout << from[i][j] << " ";
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

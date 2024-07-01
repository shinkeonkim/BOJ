/*
[1738: 골목길](https://www.acmicpc.net/problem/1738)

Tier: Gold 1 
Category: bellman_ford, graphs, shortest_path
*/


#include <bits/stdc++.h>

using namespace std;

#define for1(s, e) for(int i = s; i < e; i++)
#define for1j(s, e) for(int j = s; j < e; j++)
#define forEach(k) for(auto i : k)
#define forEachj(k) for(auto j : k)
#define sz(vct) vct.size()
#define all(vct) vct.begin(), vct.end()
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

struct BellmanFord {
  struct BellmanEdge {
    ll to, cost;

    BellmanEdge(ll to, ll cost) : to(to), cost(cost) {}
  };

  ll N;
  vector<vector <BellmanEdge> > adj;
  llv1 D;
  vector<ll> prev;

  BellmanFord(ll N) : N(N) {
    adj.resize(N + 1);
  }

  void addEdge(int s, ll e, ll cost) {
    // cout << " " << adj.size();
    adj[s].push_back(BellmanEdge(e, cost));
  }

  bool run(ll start_point) {
    // 음수 간선 cycle 유무를 반환합니다.
    // 거리 정보는 D 벡터에 저장됩니다.
    // O(V * E)
    prev.resize(N + 1, -1);
    D.resize(N + 1, -INF);
    D[start_point] = 0;
  
    bool isCycle = false;

    for1(1, N + 1) {
      for1j(1, N + 1) {
        for(int k=0; k < sz(adj[j]); k++) {
          BellmanEdge p = adj[j][k];
          int end = p.to;
          ll dist = D[j] + p.cost;

          if (D[end] < dist) {
            D[end] = dist;
            prev[end] = j;
            if (i == N) {
              isCycle = true;
              //
              D[end] = INF;
            }
          }
        }
      }
    }
    return isCycle;
  }

  llv1 getPath(ll s, ll e) {
    vector<ll> ret;
    ll current = e;
    while(current != -1) {
      ret.push_back(current);
      current = prev[current];
    }
    reverse(ret.begin(), ret.end());
    return ret;
  }
};

void solve() {
  ll N, M;
  ll a, b, c;

  cin >> N >> M;

  BellmanFord bf(N);

  for1(0, M) {
    cin >> a >> b >> c;
    bf.addEdge(a, b, c);
  }

  bool ret = bf.run(1);


  // for1(1, N + 1) {
  //   cout << bf.D[i] << " ";
  // }

  if(bf.D[N] != INF) {
    llv1 track = bf.getPath(1, N);

    forEach(track) {
      cout << i << " ";
    }
  } else {
    cout << -1;
  }

}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}
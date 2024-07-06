/*
[21278: 호석이 두 마리 치킨](https://www.acmicpc.net/problem/21278)

Tier: Gold 5 
Category: bruteforcing, floyd_warshall, graphs, graph_traversal, shortest_path
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

struct FloydWarshall{
  ll N;
  llv2 ar;

  FloydWarshall(ll N) : N(N) {
    ar.resize(N + 1, llv1(N + 1, INF));

    for1(1, N + 1) ar[i][i] = 0; 
  }

  void addEdge(ll a, ll b, ll cost) {
    ar[a][b] = min(ar[a][b], cost);
    ar[b][a] = min(ar[b][a], cost);
  }

  void run() {
    for(int k = 1; k <= N; k++) {
      for(int i =  1; i <= N; i++) {
        for(int j = 1; j <= N; j++) {
          if(ar[i][j] > ar[i][k] + ar[k][j]) {
            ar[i][j] = ar[i][k] + ar[k][j];
          }
        }
      }
    }
  }
};

void solve() {
  ll n, m;

  cin >> n >> m;

  FloydWarshall fw(n);

  for1(0, m) {
    ll a, b;

    cin >> a >> b;

    fw.addEdge(a, b, 1);
  }

  fw.run();

  ll ans = INF;
  ll x = -1;
  ll y = -1;

  for1(1, n + 1) {
    for1j(i + 1, n + 1) {
      ll sm = 0;
      for(int k = 1; k <= n; k++) {
        sm += min(fw.ar[i][k], fw.ar[j][k]) * 2;
      }

      if(ans > sm) {
        ans = sm;
        x = i;
        y = j;
      }
    }
  }

  cout << x << " " << y << " " << ans;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}
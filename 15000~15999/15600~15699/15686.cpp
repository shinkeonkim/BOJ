/*
[15686: 치킨 배달](https://www.acmicpc.net/problem/15686)

Tier: Gold 5 
Category: backtracking, bruteforcing, implementation
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
#define INT_INF (1 << 29)

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

int n, m;

void solve() {
  cin >> n >> m;

  llv2 adj(n, llv1(n));

  for1(0, n) {
    for1j(0, n) {
      cin >> adj[i][j];
    }
  }

  llv1 houses, chickens;
  for1(0, n) {
    for1j(0, n) {
      if(adj[i][j] == 1) houses.push_back(i * n + j);
      if(adj[i][j] == 2) chickens.push_back(i * n + j);
    }
  }

  ll hsz = houses.size();
  ll csz = chickens.size();
  llv1 dist(hsz, INF);

  ll ans = INF;
  for(int bit_chicken = 1; bit_chicken < (1 << csz); bit_chicken++) {
    ll cnt = 0;
    ll chicken_cnt = 0;

    for1(0, csz) {
      if(bit_chicken & (1 << i)) chicken_cnt++;
    }

    if(chicken_cnt > m) continue;

    for1(0, hsz) {
      dist[i] = INF;
      for1j(0, csz) {
        if(bit_chicken & (1 << j)) {
          ll y1 = houses[i] / n;
          ll x1 = houses[i] % n;
          ll y2 = chickens[j] / n;
          ll x2 = chickens[j] % n;
          dist[i] = min(dist[i], abs(y1 - y2) + abs(x1 - x2));
        }
      }

      cnt += dist[i];
    }
    ans = min(ans, cnt);

  }

  cout << ans << '\n';
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}
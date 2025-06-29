/*
[1487: 물건 팔기](https://www.acmicpc.net/problem/1487)

Tier: Silver 4 
Category: bruteforcing
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

typedef unsigned long long ull;
typedef long long ll;
typedef unsigned int uint;

typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<double, double> pdd;
typedef pair<double, int> pdi;
typedef pair<string, string> pss;

typedef vector<ll> llv1;


const double EPS = 1e-8;
const double PI = acos(-1);

template<typename T>
T sq(T x) { return x * x; }

int sign(ll x) { return x < 0 ? -1 : x > 0 ? 1 : 0; }
int sign(int x) { return x < 0 ? -1 : x > 0 ? 1 : 0; }
int sign(double x) { return abs(x) < EPS ? 0 : x < 0 ? -1 : 1; }

void solve() {
  ll N;
  cin >> N;

  llv1 price(N);
  llv1 cost(N);

  for1(0, N) {
    cin >> price[i] >> cost[i];
  }

  ll ans = 0;
  ll mx = 0;

  for(int fixed_price = 0; fixed_price <= 1000000; fixed_price++) {
    ll total_price = 0;

    for(int i = 0; i < N; i++) {
      if (price[i] >= fixed_price && fixed_price - cost[i] >= 0) {
        total_price += fixed_price - cost[i];
      }
    }

    if (total_price > mx) {
      mx = total_price;
      ans = fixed_price;
    }
  }

  cout << ans;

  // cout << "\n" << mx << "\n";
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}
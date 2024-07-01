/*
[20157: 화살을 쏘자!](https://www.acmicpc.net/problem/20157)

Tier: Gold 5 
Category: data_structures, geometry, hash_set, math
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

ll gcd(ll a, ll b) { return b ? gcd(b, a % b) : a; }

void solve() {
  ll N;

  cin >> N;

  pllv1 ar(N);

  for1(0, N) {
    cin >> ar[i].first >> ar[i].second;

    if(ar[i].first == 0) {
      ar[i].second = sign(ar[i].second);
    } else if(ar[i].second == 0) {
      ar[i].first = sign(ar[i].first);
    } else {
      ll g = gcd(llabs(ar[i].first), llabs(ar[i].second));

      ar[i].first /= g;
      ar[i].second /= g;
    }
  }

  sortv(ar);

  ll idx = 0;
  ll cnt = 1;
  ll ans = 0;

  for1(1, N) {
    if(ar[i] != ar[idx]) {
      ans = max(ans, cnt);

      idx = i;
      cnt = 1;
    } else {
      cnt++;
    }
  }

  ans = max(ans, cnt);

  cout << ans;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
}

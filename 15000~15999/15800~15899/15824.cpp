/*
[15824: 너 봄에는 캡사이신이 맛있단다](https://www.acmicpc.net/problem/15824)

Tier: Gold 2 
Category: combinatorics, exponentiation_by_squaring, math, sorting
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
#define MOD 1000000007

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

void solve() {
  ll n;
  llv1 ar;

  llv1 two;

  cin >> n;

  ar.resize(n);
  two.resize(n + 10);

  for1(0, n) cin >> ar[i];

  sortv(ar);

  llv1 diff;
  diff.resize(n + 1);

  for1(1, n){
    diff[i] = ar[i] - ar[i - 1];
  }

  two[0] = 1;
  two[1] = 2;
  for1(2, n + 10) {
    two[i] = (two[i - 1] * 2) % MOD;
  }

  ll ans = 0;

  for1(1, n) {
    ll cnt = ((two[i] - 1) * (two[n - i] - 1)) % MOD;

    ans += cnt * diff[i];
    ans %= MOD;
  }

  cout << ans;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}

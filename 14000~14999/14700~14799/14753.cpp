/*
[14753: MultiMax](https://www.acmicpc.net/problem/14753)

Tier: Silver 4 
Category: sorting, case_work
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

  llv1 v(N);
  for1(0, N) cin >> v[i];

  ll ans = -10000000000;

  llv1 minus, plus;

  for1(0, N) {
    if (v[i] < 0) minus.push_back(v[i]);
    else if (v[i] > 0) plus.push_back(v[i]);
    else ans = max(ans, 0LL);
  }

  sort(all(minus), less<ll>());
  sort(all(plus), greater<ll>());

  if (minus.size() >= 2) {
    ll a1 = minus[0] * minus[1];
    
    ans = max(ans, a1);

    if(plus.size() >= 1) {
      ans = max(ans, a1 * plus[0]);
    }
  }

  if (plus.size() >= 2) {
    ll a2 = plus[0] * plus[1];
    
    ans = max(ans, a2);
    
    if (plus.size() >= 3) {
      ans = max(ans, a2 * plus[2]);
    }
  }

  cout << ans << "\n";
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
}
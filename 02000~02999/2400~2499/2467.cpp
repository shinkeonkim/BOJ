/*
[2467: 용액](https://www.acmicpc.net/problem/2467)

Tier: Gold 5 
Category: binary_search, two_pointer
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

void solve() {
  ll N; cin >> N;
  llv1 v(N);
  pair <ll, ll> ans = {INF, INF};

  for(int i = 0; i < N; i++) cin >> v[i];

  for(int i = 0; i < N; i++) {
    ll similar_idx = lower_bound(v.begin(), v.end(), -v[i]) - v.begin();

    for(int j = max(0ll,  similar_idx - 2); j < min(similar_idx + 2, N); j++) {
      if(j < 0 || j >= N || j == i) continue;

      if(abs(ans.se + ans.fi) > abs(v[i] + v[j])) {
        ans.fi = v[i];
        ans.se = v[j];
      }
    }
  }

  if(ans.fi > ans.se) swap(ans.fi, ans.se);

  cout << ans.fi << ' ' << ans.se;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}
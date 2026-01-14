/*
[14505: 팰린드롬 개수 구하기 (Small)](https://www.acmicpc.net/problem/14505)

Tier: Gold 3 
Category: dp
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

string s;
ll D[33][33];
ll n;

ll f(ll start, ll end) {
  ll& ret = D[start][end];

  if(ret != -1) return ret;

  if(start == end) {
    return ret = 1;
  }

  if(end - start == 1) {
    if(s[start] == s[end]) return ret = 1;
    return ret = 0;
  }

  if(s[start] != s[end]) {
    return ret = 0;
  }

  ret = 1;

  for(int i = start + 1; i < end; i++) {
    for(int j = i; j < end; j++) {
      ret += f(i, j);
    }
  }
  return ret;
}

void solve() {
  cin >> s;
  n = s.length();

  for1(0, n) {
    for1j(0, n) {
      D[i][j] = -1;
    }
  }

  ll ans = 0;

  for1(0, n) {
    for1j(i, n) {
      ans += f(i, j);
    }
  }
  cout << ans;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}

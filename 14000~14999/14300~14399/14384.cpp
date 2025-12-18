/*
[14384: Revenge of the Pancakes (Large)](https://www.acmicpc.net/problem/14384)

Tier: Silver 3 
Category: greedy, string
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


ll solve() {
  string s;
  
  cin >> s;

  int n = s.size();
  iv1 stats(n, 0);

  for(int i = 0; i < n; i++) {
    stats[i] = (s[i] == '+');
  }

  ll flip_count = 0;

  for(int i = n - 1; i >= 0; i--) {
    if((stats[i] + flip_count) % 2) continue;

    flip_count++;
  }

  return flip_count;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; cin >> tc;
  for(int t = 1; t <= tc; t++) {
    ll ret = solve();
    cout << "Case #" << t << ": " << ret << "\n";
  }
}

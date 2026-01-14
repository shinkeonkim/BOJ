/*
[14517: 팰린드롬 개수 구하기 (Large)](https://www.acmicpc.net/problem/14517)

Tier: Platinum 5 
Category: dp, inclusion_and_exclusion
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
ll n;
ll dp[1100][1100];
ll MOD = 10007;

ll f(int l, int r) {
  if(dp[l][r] != -1) return dp[l][r];

  if (l > r) return dp[l][r] = 0;
  if (l == r) return dp[l][r] = 1;
  if (l + 1 == r) {
    if (s[l] == s[r]) return dp[l][r] = 3;
    else return dp[l][r] = 2;
  }

  dp[l][r] = 0;
  ll &ret = dp[l][r];

  if (s[l] == s[r]) {
    ret += f(l + 1, r - 1) + 1;
  }

  ll A = (f(l + 1, r) + f(l, r - 1)) % MOD;
  ll B = f(l + 1, r - 1) % MOD;

  ll C = (A - B + MOD * MOD) % MOD;
  ret += C;
  ret %= MOD;
  return ret;
}

void solve() {
  cin >> s;
  n = s.size();
  memset(dp, -1, sizeof(dp));

  cout << f(0, n - 1) << "\n";

  // for(int i = 0; i < n; i++) {
  //   for(int j = 0; j < n; j++) {
  //     cout << dp[i][j] << " ";
  //   }
  //   cout << "\n";
  // }

}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}

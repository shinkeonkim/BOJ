/*
[12198: Password Attacker (Small)](https://www.acmicpc.net/problem/12198)

Tier: Bronze 1 
Category: math, bruteforcing, combinatorics
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

ll M, N;
ll ans = 0;
ll target = 0;

void f(ll n, ll current) {
  // cout << "f(" << n << ", " << current << ")\n";
  if(current == target) {
    ans += pow(M, n);
    ans %= 1000000007;
    return;
  }

  if(n == 0) return;

  for(int i = 0; i < M; i++) {
    f(n - 1, current | (1 << i));
  }
}

void solve() {
  ans = 0;
  cin >> M >> N; // M 개의 숫자, N 자리 비밀번호

  target = (1 << M) - 1;
  f(N, 0);
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  ll tc; cin >> tc;
  for(int t = 1; t <= tc; t++) {
    solve();

    cout << "Case #" << t << ": " << ans << "\n";
  }
}

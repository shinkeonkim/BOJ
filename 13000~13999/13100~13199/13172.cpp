/*
[13172: Σ](https://www.acmicpc.net/problem/13172)

Tier: Gold 4 
Category: math, number_theory, exponentiation_by_squaring, modular_multiplicative_inverse, flt
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

ll gcd(ll a, ll b) {
  return b > 0 ? gcd(b, a % b) : a;
}

ll inverse(ll a, ll n) {
  ll r = 1;
  while (n) {
    if (n & 1) r = r * a % MOD;
    a = a * a % MOD;
    n >>= 1;
  }
  return r;
}

ll convert(ll a, ll b) {
  ll inverted_b = inverse(b, MOD - 2);
  return (a * inverted_b) % MOD;
}

struct Fraction {
  ll child;
  ll parent;

  Fraction(ll c, ll p) {
    this->child = c;
    this->parent = p;
  }

  Fraction operator+(Fraction other) {
    return {
      ((parent * other.child) % MOD + (other.parent * child) % MOD) % MOD,
      (parent * other.parent) % MOD
    };
  }

  Fraction operator/(ll a) {
    return {
      child / a,
      parent / a
    };
  }
};

void solve() {
  ll M;
  ll S, N;
  Fraction ans = Fraction(0, 1);

  cin >> M;

  for1(0, M) {
    cin >> N >> S;

    ans = ans + Fraction(S, N);

    ll g = gcd(ans.child, ans.parent);

    ans = ans / g;
  }
  
  cout << convert(ans.child, ans.parent);
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}

/*
  [5615: 아파트 임대](https://www.acmicpc.net/problem/5615)

  Tier: Platinum 1
  Category: 소수, 밀러-라빈
*/
#include <bits/stdc++.h>

#define for1(s,n) for(int i = s; i < n; i++)
#define for1j(s,n) for(int j = s; j < n; j++)
#define foreach(k) for(auto i : k)
#define foreachj(k) for(auto j : k)
#define pb(a) push_back(a)
#define sz(a) a.size()

using namespace std;
typedef unsigned long long ull;
typedef long long ll;
typedef vector <int> iv1;
typedef vector <vector<int>> iv2;
typedef vector <ll> llv1;
typedef unsigned int uint;
typedef vector <ull> ullv1;
typedef vector <vector <ull>> ullv2;

ll modpow(ll a, ll e, ll m) {
  __int128_t r = 1, b = a % m;
  while (e > 0) {
    if (e & 1) r = r * b % m;
    b = b * b % m;
    e >>= 1;
  }
  return r;
}

bool check_composite(ll n, ll a, ll d, int s) {
  auto x = modpow(a, d, n);
  if (x == 1 || x == n - 1) return false;
  for (int r = 1; r < s; r++) {
    x = (__int128_t)x * x % n;
    if (x == n - 1) return false;
  }
  return true;
}

bool is_prime(ll x) {
  if (x < 2) return false;
  int r = 0;
  ll d = x - 1;

  while ((d & 1) == 0) {
    d >>= 1;
    r++;
  }
  for (int a : {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37}) {
    if (x == a)
      return true;
    if (check_composite(x, a, d, r))
      return false;
  }
  return true;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);

  ll N, ans = 0;
  cin >> N;

  for1(0, N) {
    ll a;
    cin >> a;

    if(is_prime(2 * a + 1)) {
      ans++;
    }
  }

  cout << ans;
}

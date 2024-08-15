/*
[24060: 알고리즘 수업 - 병합 정렬 1](https://www.acmicpc.net/problem/24060)

Tier: Silver 3 
Category: implementation, recursion, sorting
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

ll N, K;
llv1 ar;
ll cnt = 0;
ll ans = -1;


void merge_ar(llv1 &ar, ll p, ll q, ll r) {
  ll i = p, j = q + 1, t = 1;
  llv1 tmp(r - p + 2);

  while(i <= q && j <= r) {
    if(ar[i] <= ar[j]) {
      tmp[t++] = ar[i++]; 

      cnt++;
      if(cnt == K) {
        ans = ar[i - 1];
        cnt++;
      }
    }
    else {
      tmp[t++] = ar[j++];
      cnt++;
      if(cnt == K) {
        ans = ar[j - 1];
        cnt++;
      }
    }
  }

  while(i <= q) {
    tmp[t++] = ar[i++];

    cnt++;
    if(cnt == K) {
      ans = ar[i - 1];
      cnt++;
    }
  }
  while(j <= r) {
    tmp[t++] = ar[j++];

    cnt++;
    if(cnt == K) {
      ans = ar[j - 1];
      cnt++;
    }
  }

  i = p; t = 1;
  while(i <= r) ar[i++] = tmp[t++];
}

void merge_sort(llv1 &ar, ll p, ll r) {
  if(p < r) {
    ll q = (p + r) / 2;
    merge_sort(ar, p, q);
    merge_sort(ar, q + 1, r);
    merge_ar(ar, p, q, r);
  }
}


void solve() {
  cin >> N >> K;

  ar.resize(N + 1);

  for1(0, N) cin >> ar[i];

  merge_sort(ar, 0, N - 1);

  cout << ans;



}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}
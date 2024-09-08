/*
[1654: 랜선 자르기](https://www.acmicpc.net/problem/1654)

Tier: Silver 2 
Category: binary_search, parametric_search
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

typedef long long ll;

void solve() {
  ll K, N;

  cin >> K >> N;

  vector<ll> ar(K);

  for(int i = 0; i < K; i++) cin >> ar[i];
  
  ll left = 1;
  ll right = (ll)1e15; // 현재 주어진 길이 중 최대값으로 해도 됩니다.
  ll ans = 1;

  while(left <= right) {
    ll mid = (left + right) / 2;
    ll cnt = 0;

    for(int i = 0; i < K; i++) cnt += ar[i] / mid;
    // 전체 배열을 순회하면서 만들 수 있는 랜선의 개수를 구한다.

    if(cnt >= N) {
      // N개 이상 만들 수 있다!
      ans = max(ans, mid);
      left = mid + 1;
    }
    else {
      // 만들 수 없다!
      right = mid - 1;
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
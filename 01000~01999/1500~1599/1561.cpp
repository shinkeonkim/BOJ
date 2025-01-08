/*
[1561: 놀이 공원](https://www.acmicpc.net/problem/1561)

Tier: Gold 1 
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

void solve() {
  ll N, M;
  llv1 rides;

  cin >> N >> M;
  rides.resize(M);

  for1(0, M) cin >> rides[i];

  ll left = 0, right = 2000000000ll * 30ll;
  ll ans = right;

  while(left < right) {
    ll mid = (left + right) / 2;

    ll cnt = 0;
    for1(0, M) {
      cnt += mid / rides[i] + 1;
    }

    if(cnt < N) {
      left = mid + 1;
    } else {
      right = mid;
      ans = min(ans, mid);
    }
  }

  if(N <= M) {
    cout << N << '\n';
    return;
  }

  /*
    24 5
    1 2 2 4 4

    ans: 4

    마지막 놀이기구가 아닌 4번째 놀이기구다.

    time: 8
    - 9명, 5명, 5명, 3먕, 3먕

    앞에서부터 쭉 놀이기구 탄 사람 수를 새야하네. 그리고 딱 떨어지는 곳만 나중에 한번더 체크  
  */

  ll cnt = 0;

  for(int i = 0; i < M; i++) {
    cnt += ans / rides[i] + 1;
    if(ans % rides[i] == 0) {
      cnt--;
    }
  }

  for(int i = 0; i < M; i++) {
    if(ans % rides[i] == 0) {
      cnt++;
    }

    if(cnt == N) {
      cout << i + 1 << '\n';
      return;
    }
  }

}
int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}
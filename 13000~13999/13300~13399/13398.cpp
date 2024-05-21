/*
[13398: 연속합 2](https://www.acmicpc.net/problem/13398)

Tier: Gold 5 
Category: dp
*/

#include <cstdio>
#include <bits/stdc++.h>

using namespace std;

#define for1(s, e) for(int i = s; i < e; i++)
#define for1j(s, e) for(int j = s; j < e; j++)
#define forEach(k) for(auto i : k)
#define forEachj(k) for(auto j : k)
#define sz(vct) a.size())
#define all(vct) vct.begin(), vct.end()
#define uniq(vct) sort(all(vct));vct.erase(unique(all(vct)), vct.end())
#define fi first
#define se second

typedef unsigned long long ull;
typedef long long ll;
typedef unsigned int uint;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<double, double> pdd;
typedef pair<double, int> pdi;
typedef pair<string, string> pss;

const double EPS = 1e-8;
const double PI = acos(-1);

template<typename T>
T sq(T x) { return x * x; }

int sign(ll x) { return x < 0 ? -1 : x > 0 ? 1 : 0; }
int sign(int x) { return x < 0 ? -1 : x > 0 ? 1 : 0; }
int sign(double x) { return abs(x) < EPS ? 0 : x < 0 ? -1 : 1; }

ll n;
ll ar[110000];
ll d[110000][2];

void solve() {
  cin >> n;

  for1(0, n) {
    cin >> ar[i];
  }

  // d[i][j] : i까지 갔을 때, j번 스킵했다.
  d[0][0] = ar[0];
  d[0][1] = 0;

  for1(1, n) {
    d[i][0] = max(d[i - 1][0] + ar[i], ar[i]); // i번째 값을 사용하는 경우, 1) 누적값을 이어 사용한다. 2) i번째 값부터 사용한다.
    d[i][1] = max(d[i - 1][0], d[i - 1][1] + ar[i]); // 스킵을 이미 했거나 이번에 스킵을 하는 경우
  }

  ll ans = ar[0]; // d[0][1]은 ans를 구하는 과정에 포함되면 안 된다.

  for1(1, n) {
    ans = max(ans, d[i][0]);
    ans = max(ans, d[i][1]);
  }

  cout << ans;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}
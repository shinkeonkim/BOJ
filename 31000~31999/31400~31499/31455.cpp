/*
[31455: 쿠키 자르기](https://www.acmicpc.net/problem/31455)

Tier: Silver 1 
Category: divide_and_conquer, recursion
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

int N;
int ar[1100][1100];
int prefixSum[1100][1100];

ll getAreaSum(int startY, int startX, int sz) {
  return (
    prefixSum[startY + sz - 1][startX + sz - 1]
    - prefixSum[startY + sz - 1][startX - 1]
    - prefixSum[startY - 1][startX + sz - 1]
    + prefixSum[startY - 1][startX - 1]
  );
}

ll getLeftSum(int startY, int startX, int sz) {
  int totalSum = getAreaSum(startY, startX, sz);

  if (sz == 1) return totalSum;

  int skipArea = totalSum % 4;

  iv2 diff = {{0, 0}, {0, sz / 2}, {sz / 2, 0}, {sz / 2, sz / 2}};

  ll ret = 0;
  for (int d = 0; d < 4; d++) {
    if (d == skipArea) continue;

    ret += getLeftSum(startY + diff[d][0], startX + diff[d][1], sz / 2);
  }

  return ret;
}

void solve() {
  scanf("%d", &N);

  for1(1, N + 1) {
    for1j(1, N + 1) {
      scanf("%1d", &ar[i][j]);
    }
  }

  for1(1, N + 1) {
    for1j(1, N + 1) {
      prefixSum[i][j] = ar[i][j] + prefixSum[i - 1][j] + prefixSum[i][j - 1] - prefixSum[i - 1][j - 1];
    }
  }

  ll ret = getLeftSum(1, 1, N);

  cout << ret << "\n";
}

int main() {
  // ios::sync_with_stdio(0);
  // cin.tie(NULL);cout.tie(NULL);
  int tc = 1; cin >> tc;
  while(tc--) solve();
  
}

/*
[10424: 알고리즘 기말고사](https://www.acmicpc.net/problem/10424)

Tier: Silver 1 
Category: implementation, sorting
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

ll ar[110000];
ll seg[440000];
ll n;

void update(int node, int s, int e, int idx, ll val) {
  if(s ==e) {
    seg[node] = val;
    return;
  }
  int mid = s + e >> 1;
  if(idx <= mid) {
    update(node * 2, s, mid, idx, val);
  } else {
    update(node * 2 + 1, mid + 1, e, idx, val);
  }
  seg[node] = seg[node * 2] + seg[node * 2 + 1];
}

int query(int node, int s, int e, int l, int r) {
  if(r < s || e < l) return 0; // 범위 밖
  if(l <= s && e <= r) return seg[node]; // 범위 안

  int mid = s + e >> 1;
  return query(node * 2, s, mid, l, r) + query(node * 2 + 1, mid + 1, e, l, r);
}

void update(int idx, ll val) {
  update(1, 1, n, idx, val);
}

int query(int l, int r) {
  return query(1, 1, n, l, r);
}
void solve() {
  cin >> n;
  for1(1, n + 1) {
    int k;
    cin >> k;
    ar[k] = i;
  }

  for(int i = 1; i <= n; i++) {
    int rank = ar[i];

    int B = query(rank + 1, n);
    int C = rank - 1 - query(1, rank - 1);

    cout << B - C << "\n";

    update(rank, 1);
  }
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}

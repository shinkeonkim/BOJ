/*
[9463: 순열 그래프](https://www.acmicpc.net/problem/9463)

Tier: Platinum 5 
Category: data_structures, segtree
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

struct SegTree {
  ll n;
  llv1 tree;

  SegTree(ll n) {
    this->n = n;
    tree.resize(n * 4 + 5);
  }

  void update(ll left, ll right, ll idx, ll k, ll diff) {
    if(right < k || k < left) return;

    if(left == right) {
      tree[idx] += diff;
      return;
    }

    ll mid = (left + right) / 2;

    update(left, mid, idx * 2, k, diff);
    update(mid + 1, right, idx * 2 + 1, k, diff);

    tree[idx] = tree[idx * 2] + tree[idx * 2 + 1]; 
  }

  void update(ll k, ll diff) {
    update(1, n, 1, k, diff);
  }

  ll query(ll left, ll right, ll idx, ll start, ll end) {
    if(right < start || end < left) return 0;
    if(start <= left && right <= end) return tree[idx];

    ll mid = (left + right) / 2;

    return query(left, mid, idx * 2, start, end) + query(mid + 1, right, idx * 2 + 1, start, end);
  }

  ll query(ll start, ll end) {
    return query(1, n, 1, start, end);
  }
};

void solve() {
  ll N;

  llv1 ar;
  cin >> N;
  vector<ll> realIdx;
  vector<ll> position;
  realIdx.resize(N + 1);
  position.resize(N + 1);

  SegTree segtree(N + 1);

  ar.resize(N + 1);

  for1(1, N + 1) {
    ll a;
    cin >> a;
    realIdx[i] = a;
  }

  for1(1, N + 1) {
    ll a;
    cin >> a;

    position[a] = i;
  }

  for1(1, N + 1) {
    ar[i] = position[realIdx[i]];
  }

  ll ans = 0;

  for(int i = N; i >= 1; i--) {
    ll k = ar[i];
    ans += segtree.query(1, k);
    segtree.update(k, 1);
  }

  cout << ans << "\n";
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; cin >> tc;
  while(tc--) solve();
  
}

/*
[15967: 에바쿰](https://www.acmicpc.net/problem/15967)

Tier: Platinum 4 
Category: data_structures, segtree, lazyprop
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
  llv1 ar;
  llv1 tree;
  llv1 lazy;

  SegTree(ll n) {
    this->n = n;
    ar.resize(n + 1);
    tree.resize(4 * n + 5);
    lazy.resize(4 * n + 5);
  }

  void init() {
    __init(1, n, 1);
  }

  void __init(ll left, ll right, ll idx) {
    if(left == right) {
      tree[idx] = ar[left];
      return;
    }

    ll mid = (left + right) / 2;

    __init(left, mid, idx * 2);
    __init(mid + 1, right, idx * 2 + 1);

    tree[idx] = tree[idx * 2] + tree[idx * 2 + 1];
  }

  void update(ll start, ll end, ll diff) {
    __update(1, n, 1, start, end, diff);
  }

  void __propagate(ll left, ll right, ll idx) {
    tree[idx] += lazy[idx] * (right - left + 1);
    
    if(left != right) {
      lazy[idx * 2] += lazy[idx];
      lazy[idx * 2 + 1] += lazy[idx];
    }

    lazy[idx] = 0;
  }

  void __update(ll left, ll right, ll idx, ll start, ll end, ll diff) {
    __propagate(left, right, idx);
    
    if(right < start || end < left) return;

    if(start <= left && right <= end) {
      tree[idx] += (right - left + 1) * diff; 

      if(left != right) {
        lazy[idx * 2] += diff;
        lazy[idx * 2 + 1] += diff;
      }

      return;
    }

    ll mid = (left + right) / 2;

    __update(left, mid, idx * 2, start, end, diff);
    __update(mid + 1, right, idx * 2 + 1, start, end, diff);

    tree[idx] = tree[idx * 2] + tree[idx * 2 + 1];
  }

  ll query(ll start, ll end) {
    return __query(1, n, 1, start, end);
  }

  ll __query(ll left, ll right, ll idx, ll start, ll end) {
    __propagate(left, right, idx);

    if(right < start || end < left) return 0;

    if(start <= left && right <= end) {
      return tree[idx];
    }

    ll mid = (left + right) / 2;

    return __query(left, mid, idx * 2, start, end) + __query(mid + 1, right, idx * 2 + 1, start, end);
  }
};

void solve() {
  ll N, Q1, Q2;

  cin >> N >> Q1 >> Q2;

  SegTree tree(N);

  for1(1, N + 1) {
    cin >> tree.ar[i];
  }

  tree.init();

  ll query, a, b, c;

  for1(0, Q1 + Q2) {
    cin >> query;

    if(query == 1) {
      cin >> a >> b;

      cout << tree.query(a, b) << "\n";
    } else {
      cin >> a >> b >> c;

      tree.update(a, b, c);
    }
  }

}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}

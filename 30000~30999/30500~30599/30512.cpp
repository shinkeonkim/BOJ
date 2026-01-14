/*
[30512: 조용히 완전히 영원히](https://www.acmicpc.net/problem/30512)

Tier: Platinum 5 
Category: data_structures, segtree, lazyprop, offline_queries
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
  llv1 tree; // min value
  llv1 lazy;

  SegTree(ll n) {
    this->n = n;

    ar.resize(n + 1);
    tree.resize(4 * n + 5, 0);
    lazy.resize(4 * n + 5, INF);
  }

  void init(ll left, ll right, ll idx) {
    if(left == right) {
      tree[idx] = ar[left];
      return;
    }

    ll mid = (left + right) / 2;

    init(left, mid, idx * 2);
    init(mid + 1, right, idx * 2 + 1);
  }

  void init() {
    init(1, n, 1);
  }

  void propagate(ll idx, ll left, ll right) {
    if (lazy[idx] == INF) return;

    ll prop = lazy[idx];

    tree[idx] = min(tree[idx], prop);

    if(left != right) {
      lazy[idx * 2] = min(lazy[idx * 2], prop);
      lazy[idx * 2 + 1] = min(lazy[idx * 2 + 1], prop);
    }

    lazy[idx] = INF;
  }

  void update(ll left, ll right, ll idx, ll start, ll end, ll mn) {
    propagate(idx, left, right);

    if(end < left || right < start) return;

    if(start <= left && right <= end) {
      tree[idx] = min(tree[idx], mn);

      if(left != right) {
        lazy[idx * 2] = min(lazy[idx * 2], mn);
        lazy[idx * 2 + 1] = min(lazy[idx * 2 + 1], mn);
      }

      return;
    }

    ll mid = (left + right) / 2;

    update(left, mid, idx * 2, start, end, mn);
    update(mid + 1, right, idx * 2 + 1, start, end, mn);

    tree[idx] = min(tree[idx * 2], tree[idx * 2 + 1]);
  }

  void update(ll start, ll end, ll mn) {
    update(1, n, 1, start, end, mn);
  }

  ll query(ll left, ll right, ll idx, ll start, ll end) {
    propagate(idx, left, right);

    if(end < left || right < start) return INF;

    if(start <= left && right <= end) {
      return tree[idx];
    }

    ll mid = (left + right) / 2;

    return min(query(left, mid, idx * 2, start, end), query(mid + 1, right, idx * 2 + 1, start, end));
  }

  ll query(ll start, ll end) {
    return query(1, n, 1, start, end);
  }
};


void solve() {
  ll N;

  cin >> N;

  SegTree tree(N);

  for1(1, N + 1) {
    cin >> tree.ar[i];
  }


  tree.init();

  ll Q;

  cin >> Q;

  for1(0, Q) {
    ll a, b, c;

    tree.update(a, b, c);
  }

  for1(1, N + 1) {
    cout << tree.query(i, 1) << " ";
  }
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}

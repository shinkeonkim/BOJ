/*
[1615: 교차개수세기](https://www.acmicpc.net/problem/1615)

Tier: Platinum 5 
Category: data_structures, sorting, segtree
*/


#include <bits/stdc++.h>

using namespace std;

#define for1(s, e) for(int i = s; i < e; i++)
#define for1j(s, e) for(int j = s; j < e; j++)
#define forEach(k) for(auto i : k)
#define forEachj(k) for(auto j : k)
#define sz(vct) vct.size()
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

typedef vector<ll> llv1;
typedef vector<llv1> llv2;


const double EPS = 1e-8;
const double PI = acos(-1);

template<typename T>
T sq(T x) { return x * x; }

int sign(ll x) { return x < 0 ? -1 : x > 0 ? 1 : 0; }
int sign(int x) { return x < 0 ? -1 : x > 0 ? 1 : 0; }
int sign(double x) { return abs(x) < EPS ? 0 : x < 0 ? -1 : 1; }

struct SegTree {
  int n;
  vector<ll> tree;
  
  SegTree(int n) : n(n) {
    tree.resize(4 * n + 5, 0);
  }

  void init(const vector<ll>& ar, int idx, int start, int end) {
    if (start == end) {
      tree[idx] = ar[start];
      return;
    }

    int mid = (start + end) / 2;
    init(ar, idx * 2, start, mid);
    init(ar, idx * 2 + 1, mid + 1, end);

    tree[idx] = tree[idx * 2] + tree[idx * 2 + 1];
  }

  void __update(int left, int right, int idx, ll val, int start, int end) {
    if (end < left || start > right) return;

    if(left <= start && end <= right) {
      tree[idx] += val;
      return;
    }

    int mid = (start + end) / 2;
    __update(left, right, idx * 2, val, start, mid);
    __update(left, right, idx * 2 + 1, val, mid + 1, end);

    tree[idx] = tree[idx * 2] + tree[idx * 2 + 1];
  }

  ll __query(int left, int right, int idx, int start, int end) {
    if (end < left || start > right) return 0;

    if(left <= start && end <= right) {
      return tree[idx];
    }

    int mid = (start + end) / 2;
    ll l = __query(left, right, idx * 2, start, mid);
    ll r = __query(left, right, idx * 2 + 1, mid + 1, end);

    return l + r;
  }

  void update(int left, int right, ll val) {
    __update(left, right, 1, val, 1, n);
  }

  ll query(int left, int right) {
    return __query(left, right, 1, 1, n);
  }
};


void solve() {
  ll N, M, a, b;
  llv2 adj;
  llv1 ar;
  ll ans = 0;

  cin >> N >> M;

  SegTree seg(N);
  adj.resize(N + 1);
  ar.resize(N + 1, 0);

  for1(0, M) {
    cin >> a >> b;
    adj[a].push_back(b);
    ar[b]++;
  }

  seg.init(ar, 1, 1, N);

  for1(1, N+1) {
    forEachj(adj[i]) {
        seg.update(j, j, -1);
    }
    forEachj(adj[i]) {
      ans += seg.query(1, j-1);
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

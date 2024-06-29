/*
[18407: 가로 블록 쌓기](https://www.acmicpc.net/problem/18407)

Tier: Platinum 3 
Category: coordinate_compression, data_structures, lazyprop, segtree
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


const double EPS = 1e-8;
const double PI = acos(-1);

template<typename T>
T sq(T x) { return x * x; }

int sign(ll x) { return x < 0 ? -1 : x > 0 ? 1 : 0; }
int sign(int x) { return x < 0 ? -1 : x > 0 ? 1 : 0; }
int sign(double x) { return abs(x) < EPS ? 0 : x < 0 ? -1 : 1; }

struct SegTreeWithLazyProp {
  int n;
  vector<ll> tree;
  vector<ll> lazy;

  SegTreeWithLazyProp(int n) : n(n) {
    tree.resize(4 * n + 5, 0);
    lazy.resize(4 * n + 5, 0);
  }

  void _update_prop(int idx, int start, int end) {
    if(lazy[idx] == 0) return; // 갱신할 내용 없으면 종료

    tree[idx] = max(tree[idx], lazy[idx]);
    
    if(start != end) {
      lazy[idx * 2] = max(lazy[idx* 2], lazy[idx]);
      lazy[idx * 2 + 1] = max(lazy[idx * 2 + 1], lazy[idx]);
    }

    lazy[idx] = 0;
  }

  void __update(int left, int right, int idx, ll val, int start, int end) {
    // [start, end] : 현재 범위
    // [left, right] : 쿼리의 범위

    _update_prop(idx, start, end);

    if (end < left || start > right) return;

    if(left <= start && end <= right) {

      tree[idx] = max(tree[idx], val);

      if(start != end) {
        lazy[idx * 2] = val;
        lazy[idx * 2 + 1] = val;
      }

      return;
    }

    int mid = (start + end) / 2;
    __update(left, right, idx * 2, val, start, mid);
    __update(left, right, idx * 2 + 1, val, mid + 1, end);

    tree[idx] = max(tree[idx * 2], tree[idx * 2 + 1]);
  }

  ll __query(int left, int right, int idx, int start, int end) {
    _update_prop(idx, start, end);

    if (right < start || end < left) return 0;
    if(left <= start && end <= right) return tree[idx];

    int mid = (start + end) / 2;
    return max(__query(left, right, idx * 2, start, mid), __query(left, right, idx * 2 + 1, mid + 1, end));
  }

  void update(int Q, ll val) {
    __update(Q, Q, 1, val, 1, n);
  }

  void update_range(int left, int right, ll val) {
    __update(left, right, 1, val, 1, n);
  }

  ll query(int left, int right) {
    return __query(left, right, 1, 1, n);
  }
};

void solve() {
  int n;

  cin >> n;

  vector <pll> blocks;

  for1(0, n) {
    pll a;
    cin >> a.second >> a.first;
    a.second += a.first - 1;
  
    blocks.push_back(a);
  }

  vector <ll> kk;

  for (auto i : blocks) {
    kk.push_back(i.first);
    kk.push_back(i.second);
  }

  uniq(kk);
  map<ll, ll> M;

  for1(0, kk.size()) {
    M[kk[i]] = i;
  }

  ll ans = 0;

  SegTreeWithLazyProp seg(kk.size());

  for1(0, n) {
    ll a = M[blocks[i].first];
    ll b = M[blocks[i].second];
  
    ll here_height = seg.query(a, b);
    seg.update_range(a, b, here_height + 1);

    ans = max(ans, here_height + 1);
  }

  cout << ans;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}
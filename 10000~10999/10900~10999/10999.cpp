/*
[10999: 구간 합 구하기 2](https://www.acmicpc.net/problem/10999)

Tier: Platinum 4 
Category: segtree, lazyprop, data_structures
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

const double EPS = 1e-8;
const double PI = acos(-1);

template<typename T>
T sq(T x) { return x * x; }

int sign(ll x) { return x < 0 ? -1 : x > 0 ? 1 : 0; }
int sign(int x) { return x < 0 ? -1 : x > 0 ? 1 : 0; }
int sign(double x) { return abs(x) < EPS ? 0 : x < 0 ? -1 : 1; }

struct SegTreeWithLazyProp {
  /*
    T: 가중치 타입
    
    누적합 쿼리 구조임.
  */
  
  int n;
  vector<ll> tree;
  vector<ll> lazy;

  SegTreeWithLazyProp(int n) : n(n) {
    tree.resize(4 * n + 5, 0);
    lazy.resize(4 * n + 5, 0);
  }

  void _update_prop(int idx, int start, int end) {
    if(lazy[idx] == 0) return; // 갱신할 내용 없으면 종료

    /* TODO: 쿼리의 종류에 따라 변경할 것 */

    tree[idx] += (end - start + 1) * lazy[idx];
    
    if(start != end) {
      lazy[idx * 2] += lazy[idx];
      lazy[idx * 2 + 1] += lazy[idx];
    }

    lazy[idx] = 0;
  }

  void __update(int left, int right, int idx, ll val, int start, int end) {
    // [start, end] : 현재 범위
    // [left, right] : 쿼리의 범위

    _update_prop(idx, start, end);

    if (end < left || start > right) return;

    if(left <= start && end <= right) {

      /* TODO: 쿼리의 종류에 따라 변경할 것 */
      tree[idx] += (end - start + 1) * val;

      if(start != end) {
        lazy[idx * 2] += val;
        lazy[idx * 2 + 1] += val;
      }

      return;
    }

    int mid = (start + end) / 2;
    __update(left, right, idx * 2, val, start, mid);
    __update(left, right, idx * 2 + 1, val, mid + 1, end);

    /* TODO: 쿼리의 종류에 따라 수정할 것 */
    tree[idx] = tree[idx * 2] + tree[idx * 2 + 1];
  }

  ll __query(int left, int right, int idx, int start, int end) {
    _update_prop(idx, start, end);

    if (right < start || end < left) return 0;
    if(left <= start && end <= right) return tree[idx];

    int mid = (start + end) / 2;

    /* TODO: 쿼리의 종류에 따라 변경할 것 */
    return __query(left, right, idx * 2, start, mid) + __query(left, right, idx * 2 + 1, mid + 1, end);
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
  int n, m, k;
  ll a, b, c;

  cin >> n >> m >> k;

  SegTreeWithLazyProp seg(n);

  for1(1, n + 1) {
    cin >> a;
    seg.update(i, a);
  }

  for1(0, m + k) {
    int query;

    cin >> query;

    if(query == 1) {
      cin >> a >> b >> c;

      seg.update_range(a, b, c);
    } else {
      cin >> a >> b;
      cout << seg.query(a, b) << "\n";
    }
  }
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
}
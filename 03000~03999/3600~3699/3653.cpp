/*
[3653: 영화 수집](https://www.acmicpc.net/problem/3653)

Tier: Platinum 4 
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

    tree[idx] += (end - start + 1) * lazy[idx];
    
    if(start != end) {
      lazy[idx * 2] += lazy[idx];
      lazy[idx * 2 + 1] += lazy[idx];
    }

    lazy[idx] = 0;
  }

  void __update(int left, int right, int idx, ll val, int start, int end) {
    _update_prop(idx, start, end);

    if (end < left || start > right) return;
    if(left <= start && end <= right) {
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

    tree[idx] = tree[idx * 2] + tree[idx * 2 + 1];
  }

  ll __query(int left, int right, int idx, int start, int end) {
    _update_prop(idx, start, end);

    if (right < start || end < left) return 0;
    if(left <= start && end <= right) return tree[idx];

    int mid = (start + end) / 2;

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
  ll N, M;
  cin >> N >> M;

  ll last = N + M + 10;

  SegTreeWithLazyProp segtree(last);
  ll pos = 0;
  map<ll, ll> position;

  for1(1, N + 1) {
    segtree.update(N - i + 1, 1);
    position[i] = N - i + 1;
  }
  pos = N + 1;

  for1(0, M) {
    ll q;
    cin >> q;

    ll current_position = position[q];

    cout << segtree.query(current_position + 1, last) << " ";
    segtree.update(current_position, -1);
    segtree.update(pos, 1);
    position[q] = pos;
    pos++;
  }
  cout << "\n";
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; cin >> tc;
  while(tc--) solve();
  
}

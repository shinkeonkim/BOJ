/*
[12846: 무서운 아르바이트](https://www.acmicpc.net/problem/12846)

Tier: Platinum 5 
Category: data_structures, segtree, divide_and_conquer, stack
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
  llv1 tree; // min의 index를 담아둠

  SegTree(ll n) {
    this->n = n;
    ar.resize(n + 1);
    tree.resize(4*n+5);
    ar[0] = INF;
  }

  ll init(int left, int right, int idx) {
    if(left == right) {
      return tree[idx] = left;
    }

    int mid = (left + right) / 2;

    ll l_ret = init(left, mid, idx * 2);
    ll r_ret = init(mid + 1, right, idx * 2 + 1);

    return tree[idx] = (ar[l_ret] <= ar[r_ret] ? l_ret : r_ret);
  }

  void init() {
    init(1, n, 1);
  }

  ll query(int left, int right, int idx, int query_start, int query_end) {
    if(query_start <= left && right <= query_end) {
      return tree[idx];
    }

    if(right < query_start || query_end < left) {
      return 0;
    }

    int mid = (left + right) / 2;
    ll l_ret = query(left, mid, idx * 2, query_start, query_end);
    ll r_ret = query(mid + 1, right, idx * 2 + 1, query_start, query_end);
    
    return (ar[l_ret] <= ar[r_ret] ? l_ret : r_ret);
  }

  ll query(int query_start, int query_end) {
    return query(1, n, 1, query_start, query_end);
  }

  ll get_answer(int left, int right) {
    if(left == right) {
      return ar[left];
    }

    if(left > right) {
      return 0;
    }

    int mn_idx = query(left, right);

    ll ret = (right - left + 1) * ar[mn_idx];

    ll l_ret = get_answer(left, mn_idx - 1);
    ll r_ret = get_answer(mn_idx + 1, right);

    ret = max(ret, l_ret);
    ret = max(ret, r_ret);


    return ret;
    
  }
};

void solve() {
  ll N;
  cin >> N;
  SegTree seg(N);

  for1(1, N + 1) {
    cin >> seg.ar[i];
  }

  seg.init();


  cout << seg.get_answer(1, N);
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
}

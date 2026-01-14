/*
[11505: 구간 곱 구하기](https://www.acmicpc.net/problem/11505)

Tier: Gold 1 
Category: segtree, data_structures
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
#define MOD 1000000007

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

ll N, M, K;

struct SegTree {
  ll ar[1100000];
  ll tree[4400000];

  ll init(ll left, ll right, ll tree_idx) {
    if(left == right) {
      return tree[tree_idx] = ar[left];
    }

    ll mid = (left + right) / 2;

    ll left_result = init(left, mid, tree_idx * 2);
    ll right_result = init(mid + 1, right, tree_idx * 2 + 1);

    return tree[tree_idx] = (left_result * right_result) % MOD;
  }

  void init() {
    init(1, N, 1);
  }

  ll update(ll left, ll right, ll tree_idx, ll update_idx) {
    // cout << left << " " << right << " " << tree_idx << " " << update_idx << "\n";
    if (update_idx < left || right < update_idx) return tree[tree_idx];

    if(left == right) {
      return tree[tree_idx] = ar[left];
    }

    ll mid = (left + right) / 2;
    ll left_result = update(left, mid, tree_idx * 2, update_idx);
    ll right_result = update(mid + 1, right, tree_idx * 2 + 1, update_idx);

    return tree[tree_idx] = (left_result * right_result) % MOD;
  }

  void update(ll udpate_idx, ll updaet_value) {
    ar[udpate_idx] = updaet_value;
    update(1, N, 1, udpate_idx);
  }

  ll query(ll left, ll right, ll tree_idx, ll query_start, ll query_end) {
    // cout << left << " " << right << " " << tree_idx << "\n";
    // cout << tree[tree_idx] << "\n";
    if (query_start <= left && right <= query_end) {
      return tree[tree_idx];
    }

    if (right < query_start || query_end < left) return 1;

    ll mid = (left + right) / 2;
    ll left_result = query(left, mid, tree_idx * 2, query_start, query_end);
    ll right_result = query(mid + 1, right, tree_idx * 2 + 1, query_start, query_end);

    return (left_result * right_result) % MOD;
  }

  ll query(ll query_start, ll query_end) {
    return query(1, N, 1, query_start, query_end);
  }
};

SegTree tree;

void solve() {
  cin >> N >> M >> K;
  for1(1, N + 1) {
    cin >> tree.ar[i];
  }

  tree.init();

  ll a, b, c;


  for1(0, M + K) {
    cin >> a >> b >> c;

    if (a == 1) {
      tree.update(b, c);

     } else {
      cout << tree.query(b, c) << "\n";
    }
  
  }

  // cout << tree.query(3, 5) << "\n";
  // cout << tree.query(4, 5) << "\n";


}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}

/*
[2104: 부분배열 고르기](https://www.acmicpc.net/problem/2104)

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

ll N;
ll ar[440000];
ll min_tree[440000]; // idx
ll sum_tree[440000];

ll init_min_tree(ll left, ll right, ll tree_idx) {
  if (left == right) {
    return min_tree[tree_idx] = left;
  }

  ll mid = (left + right) / 2;

  ll left_result = init_min_tree(left, mid, tree_idx * 2);
  ll right_result = init_min_tree(mid + 1, right, tree_idx * 2 + 1);

  return min_tree[tree_idx] = (ar[left_result] <= ar[right_result] ? left_result : right_result);
}

ll init_sum_tree(ll left, ll right, ll tree_idx ){
  if (left == right) {
    return sum_tree[tree_idx] = ar[left];
  }

  ll mid = (left + right) / 2;

  return sum_tree[tree_idx] = init_sum_tree(left, mid, tree_idx * 2) + init_sum_tree(mid + 1, right, tree_idx * 2 + 1);
}

ll query_min(ll left, ll right, ll tree_idx, ll query_start, ll query_end) {
  if(query_start <= left && right <= query_end) {
    return min_tree[tree_idx];
  }

  if(right < query_start || query_end < left) return 0;

  ll mid = (left + right) / 2;
  ll left_result = query_min(left, mid, tree_idx * 2, query_start, query_end);
  ll right_result = query_min(mid + 1, right, tree_idx * 2 + 1, query_start, query_end);

  return ar[left_result] <= ar[right_result] ? left_result : right_result;
}

ll query_sum(ll left, ll right, ll tree_idx, ll query_start, ll query_end) {
  if(query_start <= left && right <= query_end) {
    return sum_tree[tree_idx];
  }

  if(right < query_start || query_end < left) return 0;

  ll mid = (left + right) / 2;
  ll left_result = query_sum(left, mid, tree_idx * 2, query_start, query_end);
  ll right_result = query_sum(mid + 1, right, tree_idx * 2 + 1, query_start, query_end);

  return left_result + right_result;
}

void init() {
  init_min_tree(1, N, 1);
  init_sum_tree(1, N, 1);
}

ll bi_ans(ll start, ll end) {
  if(start > end) return 0;

  ll min_idx = query_min(1, N, 1, start, end);
  ll ret = ar[min_idx] * query_sum(1, N, 1, start, end);
  // cout << start << " " << end << ": " << ar[min_idx] << " " << query_sum(1, N, 1, start, end) << "\n";

  ll left_result = bi_ans(start, min_idx - 1);
  ll right_result = bi_ans(min_idx + 1, end);
  ret = max(ret, left_result);
  ret = max(ret, right_result);

  return ret;
}

void solve() {
  cin >> N;
  ar[0] = INF;
  for1(1, N + 1) {
    cin >> ar[i];
  }

  init();
  cout << bi_ans(1, N);
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}

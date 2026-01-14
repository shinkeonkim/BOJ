/*
[12899: 데이터 구조](https://www.acmicpc.net/problem/12899)

Tier: Platinum 4 
Category: data_structures, segtree, binary_search
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
#define MX 2200000

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


struct SearchKSegTree {
  ll n;
  llv1 tree;

  SearchKSegTree(ll n) {
    this-> n = n;
    tree.resize(4 * n +  5);
  }

  void update(ll l, ll r, ll idx, ll k, ll diff) {
    if(k < l || r < k) {
      return;
    }

    if(l == r) {
      tree[idx] += diff;
      return;
    }

    ll mid = (l + r) / 2;

    update(l, mid, idx * 2, k, diff);
    update(mid + 1, r, idx * 2 + 1, k, diff);

    tree[idx] = tree[idx * 2] + tree[idx * 2 + 1];
  }

  void update(ll k, ll diff) {
    update(1, n, 1, k, diff);
  }

  ll kth(ll l, ll r, ll idx, ll k) {
    if(l == r) return l;

    ll mid = (l + r) / 2;

    if(tree[idx * 2] < k) {
      return kth(mid + 1, r, idx * 2 + 1, k - tree[idx * 2]);
    } else {
      return kth(l, mid, idx * 2, k);
    }
  }

  ll kth(ll k) {
    return kth(1, n, 1, k);
  }
};

void solve() {
  ll N;
  cin >> N;

  SearchKSegTree tree(MX);

  for(int i = 0; i < N; i++) {
    ll a, b;

    cin >> a >> b;

    if(a == 1) {
      tree.update(b, 1);
    } else {
      ll ans = tree.kth(b);
      cout << ans << "\n";
      tree.update(ans, -1);
    }
  }
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}

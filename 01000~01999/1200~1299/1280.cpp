/*
[1280: 나무 심기](https://www.acmicpc.net/problem/1280)

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
#define MX 200010
#define OFFSET 1
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

ll mod(ll a) {
  return (a + MOD) % MOD;
}

struct Node {
  ll dis_sum;
  ll cnt;
};

ll N;
ll ar[220000];
ll ans = 1;

struct SegTree {
  vector<Node> tree;
  SegTree(ll n) {
    tree.resize(n * 4 + 5);
  }

  void update(ll left, ll right, ll idx, ll k) {
    if(k < left || right < k) {
      return;
    }
    
    if(left == right) {
      tree[idx].cnt++;
      return;
    }
    
    ll mid = (left + right) / 2;
    
    update(left , mid, idx * 2, k);
    update(mid + 1, right, idx * 2 + 1, k);
    
    tree[idx].cnt++;
    tree[idx].dis_sum += (k - left);
    // cout << left << " " << right << " " << idx << " " << k << "\n";
    // cout << tree[idx].cnt << " " << tree[idx].dis_sum << "\n";
  }

  ll query(ll left, ll right, ll idx, ll k) {
    if(k < left) {
      return mod(tree[idx].cnt * (left - k) + tree[idx].dis_sum);
    }

    if(right < k) {
      return mod(((right - left) * tree[idx].cnt) % MOD - tree[idx].dis_sum + (k - right) * tree[idx].cnt);
    }

    if(left == right) {
      return 0;
    }


    ll mid = (left + right) / 2;

    ll l_result = query(left , mid, idx * 2, k);
    ll r_result = query(mid + 1, right, idx * 2 + 1, k);

    return mod(l_result + r_result);
  }
};

void solve() {
  // 각 구간 스타트 지점에서의 거리 합
  // 각 구간에 몇개 있는가?

  cin >> N;

  SegTree segtree(MX);
  ll a;
  cin >> a;
  a += OFFSET;

  segtree.update(1, MX, 1, a);

  for1(1, N) {
    cin >> a;
    a += OFFSET;

    ll cost = segtree.query(1, MX, 1, a);

    ans *= cost;
    ans = mod(ans);
    // DEBUG:
    // cout << cost << "\n";
    segtree.update(1, MX, 1, a);
  }

  cout << ans;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}

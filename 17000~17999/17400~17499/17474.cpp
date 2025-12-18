/*
[17474: 수열과 쿼리 26](https://www.acmicpc.net/problem/17474)

Tier: Diamond 1 
Category: data_structures, segtree, lazyprop, beats
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

struct Node {
  ll mx, mx2, cntmx, sum;
};

ll n;
ll ar[1100000];
Node seg[4400000];

// 1 L R X: 모든 L ≤ i ≤ R에 대해서 Ai = min(Ai, X) 를 적용한다. 
// 2 L R: max(AL, AL+1, ..., AR)을 출력한다.
// 3 L R: AL + AL+1 + ... + AR을 출력한다.

Node merge(Node a, Node b) {
  if(a.mx == b.mx) {
    return Node({ a.mx, max(a.mx2, b.mx2), a.cntmx + b.cntmx, a.sum + b.sum});
  }
  
  if(a.mx < b.mx) swap(a, b);

  return Node({ a.mx, max(a.mx2, b.mx), a.cntmx, a.sum + b.sum });
}

Node init(int node, int s, int e) {
  if(s == e) return seg[node] = Node({ ar[s], -INF, 1, ar[s] });
  int mid = s + e >> 1;
  return seg[node] = merge(init(node * 2, s, mid), init(node * 2 + 1, mid + 1, e));
}

void push(int node, int s, int e) {
  if(s == e) return;
  for(auto nxt : {node * 2, node * 2 + 1}) {
    if(seg[node].mx < seg[nxt].mx)  {
      seg[nxt].sum -= seg[nxt].cntmx * (seg[nxt].mx - seg[node].mx);
      seg[nxt].mx = seg[node].mx;
    }
  }
}

bool break_condition(int node, int s, int e, int l, int r, ll v) {
  if(r < s || e < l) return true;
  if(seg[node].mx <= v) return true;

  return false;
}

bool tag_condition(int node, int s, int e, int l, int r, ll v) {
  return (l <= s && e <= r) && seg[node].mx2 < v;
}

void tag(int node, ll v) {
  seg[node].sum -= seg[node].cntmx * (seg[node].mx - v);
  seg[node].mx = v;
}

void update(int node, int s, int e, int l, int r, ll v) {
  push(node, s, e);
  if(break_condition(node, s, e, l, r, v)) return;

  if(tag_condition(node, s, e, l, r, v)) {
    tag(node, v);
    push(node, s, e);
    return;
  }

  int mid = s + e >> 1;
  update(node * 2, s, mid, l, r, v);
  update(node * 2 + 1, mid + 1, e, l, r, v);
  seg[node] = merge(seg[node * 2], seg[node * 2 + 1]);
}

ll max_query(int node, int s, int e, int l, int r) {
  push(node, s, e);
  if(r < s || e < l) return 0;
  if(l <= s && e <= r) return seg[node].mx;

  int mid = s + e >> 1;
  ll left = max_query(node * 2, s, mid, l, r);
  ll right = max_query(node * 2 + 1, mid + 1, e, l, r);
  return max(left, right);
}

ll sum_query(int node, int s, int e, int l, int r) {
  push(node, s, e);
  if(r < s || e < l) return 0;
  if(l <= s && e <= r) return seg[node].sum;

  int mid = s + e >> 1;
  ll left = sum_query(node * 2, s, mid, l, r);
  ll right = sum_query(node * 2 + 1, mid + 1, e, l, r);
  return left + right;
}

void solve() {
  cin >> n;
  for1(1, n + 1) cin >> ar[i];
  init(1, 1, n);

  int Q;
  cin >> Q;
  while(Q--) {
    int type, L, R, X;
    cin >> type;

    switch(type) {
      case 1:
        cin >> L >> R >> X;
        update(1, 1, n, L, R, X);
        break;
      case 2:
        cin >> L >> R;
        cout << max_query(1, 1, n, L, R) << '\n';
        break;
      case 3:
        cin >> L >> R;
        cout << sum_query(1, 1, n, L, R) << '\n';
        break;
    }
  }
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}

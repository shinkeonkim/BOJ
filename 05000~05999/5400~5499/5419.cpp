/*
[5419: 북서풍](https://www.acmicpc.net/problem/5419)

Tier: Platinum 3 
Category: coordinate_compression, data_structures, segtree, sweeping
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

#define MX_RANGE 330000

struct Node {
  int l, r;
  ll value;
  ll lazy;
};

vector <Node> nodes(2);

void propagate(int node_idx, int start, int end) {
  if(nodes[node_idx].lazy == 0) return;

  nodes[node_idx].value += (end - start + 1) * nodes[node_idx].lazy;
  if(start != end) {
    int mid = (start + end) / 2;

    if (nodes[node_idx].l == 0) {
      nodes.push_back({0, 0, 0, 0});
      nodes[node_idx].l = nodes.size() - 1;
    }
    if (nodes[node_idx].r == 0) {
      nodes.push_back({0, 0, 0, 0});
      nodes[node_idx].r = nodes.size() - 1;
    }

    nodes[nodes[node_idx].l].lazy += nodes[node_idx].lazy;
    nodes[nodes[node_idx].r].lazy += nodes[node_idx].lazy;
  }
  nodes[node_idx].lazy = 0;
}

void update(int l, int r, ll val, int node_idx, int start, int end) {
  propagate(node_idx, start, end);

  if(r < start || end < l) return;

  if(l <= start && end <= r) {
    nodes[node_idx].lazy += val;
    propagate(node_idx, start, end);
    return;
  }

  int mid = (start + end) / 2;
  if (nodes[node_idx].l == 0) {
    nodes.push_back({0, 0, 0, 0});
    nodes[node_idx].l = nodes.size() - 1;
  }
  if (nodes[node_idx].r == 0) {
    nodes.push_back({0, 0, 0, 0});
    nodes[node_idx].r = nodes.size() - 1;
  }
  update(l, r, val, nodes[node_idx].l, start, mid);
  update(l, r, val, nodes[node_idx].r, mid + 1, end);
  nodes[node_idx].value = nodes[nodes[node_idx].l].value + nodes[nodes[node_idx].r].value;
}

void update(int l, int r, ll val) {
  update(l, r, val, 1, 1, MX_RANGE);
}

ll query(int l, int r, int node_idx, int start, int end) {
  propagate(node_idx, start, end);

  if(r < start || end < l) return 0;

  if(l <= start && end <= r) return nodes[node_idx].value;

  int mid = (start + end) / 2;

  ll ret = 0 ;

  if(nodes[node_idx].l > 0) {
    ret += query(l, r, nodes[node_idx].l, start, mid);
  }
  if(nodes[node_idx].r > 0) {
    ret += query(l, r, nodes[node_idx].r, mid + 1, end);
  }
  return ret;
}

ll query(int l, int r) {
  return query(l, r, 1, 1, MX_RANGE);
}

void solve() {
  nodes.resize(2);
  nodes[0] = {0, 0, 0, 0};
  nodes[1] = {0, 0, 0, 0};
  
  ll N;

  cin >> N;

  vector <pll> axises(N);
  vector <ll> yaxis;

  for1(0, N) {
    cin >> axises[i].fi >> axises[i].se;

    axises[i].se *= -1;
    yaxis.push_back(axises[i].se);
  }

  // y 좌표는 좌표 압축을 수행함.
  sort(all(yaxis));
  uniq(yaxis);
  map <ll, ll> yaxis_map;
  for1(0, yaxis.size()) {
    yaxis_map[yaxis[i]] = i + 1;
  }

  for(int i = 0; i < N; i++) {
    axises[i].se = yaxis_map[axises[i].se];
  }

  // y 좌표 압축 후, y 좌표를 기준으로 정렬함.
  sort(all(axises));

  ll ans = 0;
  for(auto [x, y] : axises) {
    ans += query(1, y);
    update(y, y, 1);
  }
  cout << ans << "\n";

}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; cin >> tc;
  while(tc--) solve();
}
/*
[11012: Egg](https://www.acmicpc.net/problem/11012)

Tier: Platinum 2 
Category: data_structures, offline_queries, pst, segtree, sweeping
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

#define MX 100010

struct Node {
  int l, r;
  ll value;
};

int root[MX+10];
vector <Node> nodes(2);

ll create_node(int l = 0, int r = 0, ll value = 0) {
  nodes.push_back({ l, r, value });
  return nodes.size() - 1;
}

void init(int node_idx, int start, int end) {
  if(start == end) return;

  int mid = (start + end) / 2;
  nodes[node_idx].l = create_node();
  init(nodes[node_idx].l, start, mid);

  nodes[node_idx].r = create_node();
  init(nodes[node_idx].r, mid + 1, end);
}

void update(int i, int x, int node_idx, int start, int end) {
  if(start == end) return;

  int mid = (start + end) / 2;

  if(i <= mid) {
    Node left_node = nodes[nodes[node_idx].l];
    nodes[node_idx].l = create_node(left_node.l, left_node.r, left_node.value + x);
    update(i, x, nodes[node_idx].l, start, mid);
  } else {
    Node right_node = nodes[nodes[node_idx].r];
    nodes[node_idx].r = create_node(right_node.l, right_node.r, right_node.value + x);
    update(i, x, nodes[node_idx].r, mid + 1, end);
  }
}

ll query(int i, int j, int node_idx, int start, int end) {
  if(j < start || i > end) return 0;
  if (i <= start && end <= j) return nodes[node_idx].value;

  int mid = (start + end) / 2;

  return query(i, j, nodes[node_idx].l, start, mid) + query(i, j, nodes[node_idx].r, mid + 1, end);
}

ll query(int i, int j, int node_idx) {
  return query(i, j, node_idx, 1, MX);
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; cin >> tc;
  while(tc--) {
    nodes.resize(2);
    nodes[1] = { 0, 0, 0 };
    fill(root, root + MX, 0);
    
    root[0] = 1;
    init(1, 1, MX);
    
    int n, m; cin >> n >> m;

    vector <int> yidx[MX + 10];

    while(n--) {
      int x, y;

      cin >> x >> y;

      x++; y++;

      yidx[x].push_back(y);
    }

    for(int i = 1; i < MX; i++) {
      if(root[i] == 0) {
        root[i] = create_node(
          nodes[root[i - 1]].l,
          nodes[root[i - 1]].r,
          nodes[root[i - 1]].value
        );
      }

      for(auto y : yidx[i]) {
        nodes[root[i]].value += 1;
        update(y, 1, root[i], 1, MX);
      }
    }
    
    ll ret = 0;

    while(m--) {
      int l, r, b, t;

      cin >> l >> r >> b >> t;
      l++; r++; b++; t++;

      ret += query(b, t, root[r]) - query(b, t, root[l - 1]);
    }

    cout << ret << "\n";
  }
  
}
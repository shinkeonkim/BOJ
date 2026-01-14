/*
[20212: 나무는 쿼리를 싫어해~](https://www.acmicpc.net/problem/20212)

Tier: Platinum 2 
Category: coordinate_compression, data_structures, lazyprop, offline_queries, segtree, sorting
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

#define MX_RANGE 10000000000000

struct Node {
  ll value;
  ll lidx;
  ll ridx;
  ll lazy;
};

vector <Node> nodes(2);

void propagate(ll nidx, ll node_start, ll node_end) {
  if(nodes[nidx].lazy != 0) {
    nodes[nidx].value += (node_end - node_start + 1) * nodes[nidx].lazy;

    if(node_start != node_end) {
      ll mid = (node_start + node_end) / 2;

      if (nodes[nidx].lidx == 0) {
        nodes.push_back({ 0, 0, 0, 0 });
        nodes[nidx].lidx = nodes.size() - 1;
      }

      if (nodes[nidx].ridx == 0) {
        nodes.push_back({ 0, 0, 0, 0 });
        nodes[nidx].ridx = nodes.size() - 1;
      }

      nodes[nodes[nidx].lidx].lazy += nodes[nidx].lazy;
      nodes[nodes[nidx].ridx].lazy += nodes[nidx].lazy;

    }
    nodes[nidx].lazy = 0;
  }
}

void update(ll l, ll r, ll x, ll nidx, ll node_start, ll node_end) {
  propagate(nidx, node_start, node_end);

  if (r < node_start || node_end < l) return ;
  if(l <= node_start && node_end <= r) {
    nodes[nidx].lazy += x;
    propagate(nidx, node_start, node_end);
    return;
  }

  int mid = (node_start + node_end) / 2;
  if (nodes[nidx].lidx == 0) {
      nodes.push_back({0, 0, 0, 0});
      nodes[nidx].lidx = nodes.size() - 1;
  }
  if (nodes[nidx].ridx == 0) {
      nodes.push_back({0, 0, 0, 0});
      nodes[nidx].ridx = nodes.size() - 1;
  }

  update(l, r, x, nodes[nidx].lidx, node_start, mid);
  update(l, r, x, nodes[nidx].ridx, mid + 1, node_end);

  nodes[nidx].value = nodes[nodes[nidx].lidx].value + nodes[nodes[nidx].ridx].value;
}

void update(ll l, ll r, ll x) {
  update(l, r, x, 1, 1, MX_RANGE);
}

ll query(ll l, ll r, ll nidx, ll node_start, ll node_end) {
  propagate(nidx, node_start, node_end);

  if (r < node_start || node_end < l) return 0;
  if(l <= node_start && node_end <= r) {
    return nodes[nidx].value;
  }

  int mid = (node_start + node_end) / 2;

  ll ret = 0;

  if(nodes[nidx].lidx != 0) ret += query(l, r, nodes[nidx].lidx, node_start, mid);
  if(nodes[nidx].ridx != 0) ret += query(l, r, nodes[nidx].ridx, mid + 1, node_end);


  return ret;
}

ll query(ll l, ll r) {
  return query(l, r, 1, 1, MX_RANGE);
}

struct Query {
  ll idx;
  ll start;
  ll end;
  ll query_k;
};

struct Update {
  ll start;
  ll end;
  ll update_k;
};


void solve() {
  ll Q;

  cin >> Q;

  vector <Query> queries;
  vector <Update> update_queries;
  map<ll, ll> ans;

  ll upd_cnt = 0;
  for(int i = 0; i < Q; i++) {
    ll a, b, c, d;

    cin >> a >> b >> c >> d;

    if(a == 1) {
      update_queries.push_back({b, c, d});
    } else {
      queries.push_back({upd_cnt++, b, c, d - 1 });
    }
  }

  vector <vector<Query> > queries_2(update_queries.size());

  for(auto q : queries) {
    queries_2[q.query_k].push_back(q);
  }


  for(int i = 0; i < update_queries.size(); i++) {
    Update u_query = update_queries[i];
    update(u_query.start, u_query.end, u_query.update_k);

    for(auto q : queries_2[i]) {
      ll ret = query(q.start, q.end);

      ans[q.idx] = ret;
    }
  }

  for(int i = 0; i < queries.size(); i++) {
    cout << ans[i] << "\n";
  }
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}
/*
[17353: 하늘에서 떨어지는 1, 2, ..., R-L+1개의 별](https://www.acmicpc.net/problem/17353)

Tier: Platinum 2 
Category: data_structures, lazyprop, segtree
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
#define DEBUG 0

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

ll N;
ll ar[110000];
ll seg[440000];
ll lazy[440000];
ll lazy_count[440000];
// 해당 구간의 시작에서부터 1, 2, 3, ... (r - l + 1)로 더해진다.
// 특정 구간에 lazy[x] ~ lazy[x] + (end - start)까지 더해진다.
// lazy[node]는 결국 해당 노드에서 시작하는 값이다.

void init(int node, int start, int end) {
  if(start > end) return;
  if(start == end) {
    seg[node] = ar[start];
    return;
  }

  int mid = (start + end) / 2;
  init(node * 2, start, mid);
  init(node * 2 + 1, mid + 1, end);
  seg[node] = seg[node * 2] + seg[node * 2 + 1];
}

void propagate(int node, int start, int end) {
  if(lazy[node] == 0 && lazy_count[node] == 0) return;

  int seg_size = end - start + 1;
  seg[node] += lazy[node] * seg_size + lazy_count[node] * ((seg_size * (seg_size - 1)) / 2);

  int mid = (start + end) / 2;

  if(start != end) {
    lazy[node * 2] += lazy[node];
    lazy_count[node * 2] += lazy_count[node];
    lazy[node * 2 + 1] += lazy[node] + lazy_count[node] * (mid + 1 - start);
    lazy_count[node * 2 + 1] += lazy_count[node];
  }
  
  lazy[node] = 0;
  lazy_count[node] = 0;
}

void update(int l, int r, ll value, int node, int start, int end) {
  propagate(node, start, end);

  if(start > r || end < l) return; 
  if(l <= start && end <= r) {
    int start_value = start - l + value;
    lazy[node] += start_value;
    lazy_count[node]++;

    propagate(node, start, end);
    return;
  }

  int mid = (start + end) / 2;
  update(l, r, value, node * 2, start, mid);
  update(l, r, value, node * 2 + 1, mid + 1, end);
  seg[node] = seg[node * 2] + seg[node * 2 + 1];
}

ll query(int idx, int node, int start, int end) {
  propagate(node, start, end);

  if(start > idx || end < idx) return 0;

  if(start == end) {
    return seg[node];
  }

  int mid = (start + end) / 2;
  if(idx <= mid) return query(idx, node * 2, start, mid);
  else return query(idx, node * 2 + 1, mid + 1, end);
}

void solve() {
  cin >> N;
  for1(1, N + 1) {
    cin >> ar[i];
  }

  init(1, 1, N);

  ll Q;

  cin >> Q;

  while(Q--) {
    ll command, a, b;

    cin >> command;

    if(command == 1) {
      cin >> a >> b;

      if(DEBUG) {
        cout << "Before: \n";
        for(int k = 1; k <= N; k++) {
          cout << query(k, 1, 1, N) << " ";
        }
        cout << "\n After: \n";
      }

      update(a, b, 1, 1, 1, N);
      
      if(DEBUG) {
        for(int k = 1; k <= N; k++) {
          cout << query(k, 1, 1, N) << " ";
        }
        cout << "\n";
      }
    } else {
      cin >> a;
      cout << query(a, 1, 1, N) << "\n";
    }
  }
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}
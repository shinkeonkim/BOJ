/*
[10216: Count Circle Groups](https://www.acmicpc.net/problem/10216)

Tier: Gold 4 
Category: data_structures, graphs, graph_traversal, geometry, disjoint_set
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

struct UnionFind {
  int n;
  vector<int> u;

  UnionFind(int n) : n(n) {
    u.resize(n + 1);
    for(int i = 1; i <= n; i++) {
      u[i] = i;
    }
  }

  int find(int k) {
    if(u[u[k]] == u[k]) return u[k];
    else return u[k]=find(u[k]);
  }

  void uni(int a, int b) {
    a = find(a);
    b = find(b);
    if(a < b) u[b] = a;
    else u[a] = b; 
  }
};

struct Area {
  ll x, y, R;

  bool isIntersected(Area other) {
    return (x - other.x) * (x - other.x) + (y - other.y) * (y - other.y) <= (R + other.R) * (R + other.R);
  }
};

void solve() {
  ll N;
  cin >> N;

  vector <Area> ar(N + 1);

  UnionFind uf(N);

  for1(1, N + 1) {
    cin >> ar[i].x >> ar[i].y >> ar[i].R;
  }

  for1(1, N + 1) {
    for1j(i + 1, N + 1) {
      if(ar[i].isIntersected(ar[j])) {
        uf.uni(i, j);
      }
    }
  }

  set <int> s;

  for1(1, N + 1) {
    s.emplace(uf.find(i));
  }

  cout << s.size() << "\n";
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; cin >> tc;
  while(tc--) solve();
  
}

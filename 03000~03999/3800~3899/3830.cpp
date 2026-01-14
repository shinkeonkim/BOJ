/*
[3830: 교수님은 기다리지 않는다](https://www.acmicpc.net/problem/3830)

Tier: Platinum 3
Category: data_structures, disjoint_set
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
  vector<int> dis;
  vector< vector<int>> groups;

  UnionFind(int n) : n(n) {
    u.resize(n + 1);
    dis.resize(n + 1);
    groups.resize(n + 1);
    for(int i = 1; i <= n; i++) {
      u[i] = i;
      groups[i].push_back(i);
    }
  }

  int find(int k) {
    if(u[u[k]] == u[k]) return u[k];
    else return u[k]=find(u[k]);
  }

  void uni(int a, int b, int w) {
    int fa = find(a);
    int fb = find(b);

    if(fa == fb) return;

    if(groups[fa].size() < groups[fb].size()) {
      swap(fa, fb);
      swap(a, b);
      w *= -1;
    }

    ll fa_to_a = dis[a];
    ll fa_to_b = fa_to_a + w;
    ll fa_to_fb = fa_to_b - dis[b];

    u[fb] = fa;

    for(auto node : groups[fb]) {
      groups[fa].push_back(node);
      dis[node] = fa_to_fb + dis[node];
    }
    groups[fa].clear();
  }
};


void solve(ll n, ll m) {
  UnionFind uf(n);

  for1(0, m) {
    char q;
    int a, b, c;

    cin >> q;

    if(q == '!') {
      cin >> a >> b >> c;
      // a < b, b가 c만큼 더 무겁다
      uf.uni(a, b, c);

    } else {
      cin >> a >> b;
      // a와 b의 사이 간격

      int fa = uf.find(a);
      int fb = uf.find(b);

      if(fa != fb) {
        cout << "UNKNOWN\n";
      } else {
        cout << uf.dis[b] - uf.dis[a] << "\n";
      }
    }
  }
  

}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  while(1) {
    ll n, m;

    cin >> n >> m;
    
    if (n == 0 && m == 0) break;

    solve(n, m);
  }
  
}

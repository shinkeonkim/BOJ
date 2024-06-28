/*
[3803: Networking](https://www.acmicpc.net/problem/3803)

Tier: Gold 4 
Category: graphs, mst
*/


#include <bits/stdc++.h>

using namespace std;

#define for1(s, e) for(int i = s; i < e; i++)
#define for1j(s, e) for(int j = s; j < e; j++)
#define forEach(k) for(auto i : k)
#define forEachj(k) for(auto j : k)
#define sz(vct) a.size()
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

const double EPS = 1e-8;
const double PI = acos(-1);

template<typename T>
T sq(T x) { return x * x; }

int sign(ll x) { return x < 0 ? -1 : x > 0 ? 1 : 0; }
int sign(int x) { return x < 0 ? -1 : x > 0 ? 1 : 0; }
int sign(double x) { return abs(x) < EPS ? 0 : x < 0 ? -1 : 1; }

template <class T>  struct MinimumSpanningTree {
  /*
    T: 가중치의 타입

    n: 노드 개수
    m: 간선 개수
    result : MST 결과 (가중치 합)
  */ 
  struct Edge { 
    int u, v;
    T weight;

    Edge(int u, int v, T weight) : u(u), v(v), weight(weight) {}
    bool operator< (Edge other) const { return weight < other.weight; }
  };

  int n, m;
  vector<int> uf;
  vector<Edge> edges;
  vector<Edge> chosen_edges;

  T result; // MST의 가중치 합
  int cnt; // 뽑은 간선 수

  MinimumSpanningTree(int n, int m) : n(n), m(m) {
    uf.resize(n + 1);
  
    for1(0, n + 1) {
      uf[i] = i;
    }
    result = 0;
    cnt = 0;
  }

  int find(int a) {
    /*
      Union-Find: Find 연산
    */
    if(uf[a] == a) return a;
    return uf[a] = find(uf[a]);
  }

  int merge(int a, int b) {
    /*
      Union-Find: Union
      합쳐진 경우 true 반환
    */

    a = find(a);
    b = find(b);

    if(a == b) return false;

    uf[b] = a;
    return true;
  }

  void add_edge(int u, int v, T cost) {
    edges.push_back(Edge(u, v, cost));
  }

  void run() {
    sort(edges.begin(), edges.end());

    for(int i = 0; i < edges.size(); i++) {
      if(merge(edges[i].u,  edges[i].v)) {
        result += edges[i].weight;

        // chosen_edges.push_back(edges[i]);
        if(++cnt >= n - 1) break;
      }
    }
  }
};

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  
  while(1) {
    int V, E;

    cin >> V >> E;
    if (V == 0) break;

    MinimumSpanningTree <int> mst(V, E);

    for1(0, E) {
      int a, b, c;
      cin >> a >> b >> c;

      mst.add_edge(a, b, c);
    }

    mst.run();

    cout << mst.result << "\n";
  }
}
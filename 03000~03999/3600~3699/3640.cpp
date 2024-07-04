/*
[3640: 제독](https://www.acmicpc.net/problem/3640)

Tier: Platinum 2 
Category: flow, mcmf
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

struct MCMF {
  struct Edge {
    ll to;
    ll capacity;
    ll cost;
    
    Edge* rev;
    Edge(ll to, ll capacity, ll cost) : to(to), capacity(capacity), cost(cost) {}
  };
  
  ll n;
  ll source, sink;
  vector<vector<Edge *>> graph;
  vector<bool> check;
  vector<ll> distance;
  vector<pair<ll, ll>> from;
  
  MCMF(ll n, ll source, ll sink): n(n), source(source), sink(sink) {

    // source: 시작점
    // sink: 도착점
    // n: 모델링한 그래프의 정점 개수
    graph.resize(n + 1);
    check.resize(n + 1);
    from.resize(n + 1, make_pair(-1, -1));
    distance.resize(n + 1);
  };
  
  void addEdge(ll u, ll v, ll cap, ll cost) {
    Edge *ori = new Edge(v, cap, cost);
    Edge *rev = new Edge(u, 0, -cost);
    
    ori->rev = rev;
    rev->rev = ori;
    
    graph[u].push_back(ori);
    graph[v].push_back(rev);
  }
  
  void addEdgeFromSrc(ll v, ll cap, ll cost) {
    // 출발지점에서 출발하는 간선 추가
    addEdge(source, v, cap, cost);
  }
  
  void addEdgeToSink(ll u, ll cap, ll cost) {
    // 도착지점으로 가는 간선 추가
    addEdge(u, sink, cap, cost);
  }
  
  bool spfa(ll &total_flow, ll &total_cost) {
    // spfa 기반의 MCMF

    fill(check.begin(), check.end(), false);
    fill(distance.begin(), distance.end(), INF);
    fill(from.begin(), from.end(), make_pair(-1, -1));
    
    distance[source] = 0;
    queue <ll> q;
    q.push(source);
    
    while(!q.empty()) {
      ll x = q.front(); q.pop();
      
      check[x] = false;
      
      for(ll i = 0; i < graph[x].size(); i++) {
        Edge* e = graph[x][i];
        ll y = e->to;
        
        if(e->capacity > 0 && distance[x] + e->cost < distance[y]) {
          distance[y] = distance[x] + e->cost;
          from[y] = make_pair(x, i);
          
          if(!check[y]) {
            check[y] = true;
            q.push(y);
          }
        }
        
      }
    }
    
    if(distance[sink] == INF) return false;
    
    // 간선을 sink에서부터 역추적하여 경로를 만든다.
    ll x = sink;
    ll c = graph[from[x].first][from[x].second]->capacity;
    
    while(from[x].first != -1) {
      if(c > graph[from[x].first][from[x].second]->capacity) {
        c = graph[from[x].first][from[x].second]->capacity;
      }
      x = from[x].first;
    }

    // 만든 경로를 따라 유량을 흘린다.
    x = sink;
    while(from[x].first != -1) {
      Edge* e = graph[from[x].first][from[x].second];
      e->capacity -= c;
      e->rev->capacity += c;
      x = from[x].first;
    }
    
    total_flow += c;
    total_cost += c * distance[sink];
    
    return true;
  }
  
  pair <ll, ll> flow() {
    ll total_flow = 0;
    ll total_cost = 0;
    
    while(spfa(total_flow, total_cost));
    
    return make_pair(total_flow, total_cost);
  }
};


void solve() {
  ll V, E, a, b, c;

  while(cin >> V >> E) {
    MCMF mcmf(V * 2 + 2, V * 2+ 1, V * 2 + 2);

    mcmf.addEdgeFromSrc(1, 2, 0);
    mcmf.addEdgeToSink(V + V, 2, 0);

    mcmf.addEdge(1, 1 + V, 2, 0);
    mcmf.addEdge(V, V + V, 2, 0);

    for1(2, V) {
      mcmf.addEdge(i, i + V, 1, 0);
    }

    for1(0, E) {
      cin >> a >> b >> c;

      mcmf.addEdge(a + V, b, 1, c);
    }

    pll ret = mcmf.flow();

    // pll ret2 = mcmf.flow();

    // cout << ret.first << " " << ret.second << "\n\n";
    // cout << ret2.first << " " << ret2.second << "\n\n";

    cout << ret.second << "\n";
  }
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}
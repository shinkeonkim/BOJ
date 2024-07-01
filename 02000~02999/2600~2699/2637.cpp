/*
[2637: 장난감 조립](https://www.acmicpc.net/problem/2637)

Tier: Gold 2 
Category: dag, dp, graphs, topological_sorting
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

ll N, M;
ll cnt[110][110];
pllv2 ar;

struct TopologicalSort {
  // 1-index

  int n;
  iv1 in_degree;
  iv2 graph;
  iv1 result;

  TopologicalSort(int n) : n(n) {
    in_degree.resize(n + 1, 0);
    graph.resize(n + 1);
  }

  void addEdge(int s, int e) {
    graph[s].push_back(e);
    in_degree[e]++;
  }

  void run() {
    queue<int> q;

    for1(1, n+1) {
      if(in_degree[i] == 0) {
        q.push(i);
        // 문제상 기본 부품은 스스로가 하나 필요한 거로 설정
        cnt[i][i] = 1;
      }
    }
    while(!q.empty()) {
      int here = q.front(); q.pop();
      result.push_back(here);

      for1(0, sz(graph[here])) {
        int there = graph[here][i];

        if(--in_degree[there]==0) q.push(there);
      }
    }
  }
};

void solve() {
  cin >> N >> M;

  ar.resize(N + 1); // first: 부품 ID, second: 필요한 개수

  TopologicalSort tps(N);

  for1(0, M) {
    ll a, b, c;

    cin >> a >> b >> c;
    tps.addEdge(b, a);

    ar[a].push_back({ b, c });
  }

  tps.run();

  auto ret = tps.result;

  for(auto here : tps.result) {
    if(cnt[here][here] == 1) continue;

    for(auto there : ar[here]) {
      ll need = there.first;
      ll need_cnt = there.second;
      for(int i = 1; i < N; i++) {
        cnt[here][i] += cnt[need][i] * need_cnt;
      } 
    }
  }

  for(int i = 1; i < N; i++) {
    if(cnt[N][i] > 0) {
      cout << i << " " << cnt[N][i] << "\n";    
    }
  }
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}
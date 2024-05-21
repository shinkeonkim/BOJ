/*
  [2367: 파티](https://www.acmicpc.net/problem/2367)

  Tier: Platinum 4
  Category: 최대 유량
*/

#include <bits/stdc++.h>

#define for1(s,n) for(int i = s; i < n; i++)
#define for1j(s,n) for(int j = s; j < n; j++)
#define foreach(k) for(auto i : k)
#define foreachj(k) for(auto j : k)
#define pb(a) push_back(a)
#define sz(a) a.size()

using namespace std;
typedef unsigned long long ull;
typedef long long ll;
typedef vector <int> iv1;
typedef vector <vector<int> > iv2;
typedef vector <ll> llv1;
typedef unsigned int uint;
typedef vector <ull> ullv1;
typedef vector <vector <ull> > ullv2;

// MAX_V, SRC, SINK 조절 필수

#define MAX_V 1001 // 정점 개수
#define SRC 1 // 출발점
#define SINK MAX_V-1 // 도착점
#define INF (ll)1e18

struct Edge {
  ll v, capacity, rev;
  Edge(ll v, ll capacity, ll rev): v(v), capacity(capacity), rev(rev) {}
};

vector<Edge> vt[MAX_V];
ll level[MAX_V];
ll work[MAX_V];

struct Dinic {
  void addEdge(ll start, ll end, ll capacity) {
    vt[start].emplace_back(end, capacity, (ll)vt[end].size());
    vt[end].emplace_back(start, 0, (ll)vt[start].size() - 1);
  }

  // 레벨 그래프 만드는 BFS
  bool bfs() {
    memset(level, -1, sizeof(level)); // 레벨 그래프 초기화

    queue <ll> q;
    level[SRC] = 0;
    q.push(SRC);

    while(!q.empty()){
      int here = q.front(); q.pop();

      for(auto i : vt[here]) {
        int there = i.v;

        if(level[there] == -1 && i.capacity > 0) {
          level[there] = level[here] + 1;
          q.push(there);
        }
      }
    }
    return level[SINK] != -1;
  }

  ll dfs(ll here, ll crt_capacity) {
    if(here == SINK) return crt_capacity;

    for(ll &i = work[here]; i < vt[here].size(); i++) {
      ll there = vt[here][i].v;
      ll capacity = vt[here][i].capacity;

      if(level[here] + 1 == level[there] && capacity > 0) {
        ll next_capacity = dfs(there, min(crt_capacity, capacity));

        if(next_capacity > 0) {
          vt[here][i].capacity -= next_capacity;
          vt[there][vt[here][i].rev].capacity += next_capacity;
          return next_capacity;
        }
      }
    }
    return 0;
  }

  ll perform() {
    /* 최대 유량을 반환한다. */
    ll ret = 0;

    while(bfs()) {
      memset(work, 0, sizeof(work));

      while(1) {
        ll flow = dfs(SRC, INF);
        if(!flow) break;
        ret += flow;
      }
    }
    return ret;
  }
};


int main() {
  ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);

  Dinic dinic;

  ll N, K, D, a, b;

  cin >> N >> K >> D;

  ll PERSON_START = 10;
  ll FOOD_START = 500;

  for1(1, D + 1) {
    cin >> a;
    dinic.addEdge(FOOD_START + i, SINK, a);
  }

  for1(0, N) {
    cin >> a;
    dinic.addEdge(SRC, PERSON_START + i, K);

    for1j(0, a) {
      cin >> b;

      dinic.addEdge(PERSON_START + i, FOOD_START + b, 1);
    }
  }

  cout << dinic.perform();
}

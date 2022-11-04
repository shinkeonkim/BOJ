/*
  Articluation Point (단절점)
*/

#include <bits/stdc++.h>

#define for1(s,n) for(int i = s; i < n; i++)
#define for1j(s,n) for(int j = s; j < n; j++)
#define foreach(k) for(auto i : k)
#define foreachj(k) for(auto j : k)
#define pb(a) push_back(a)
#define sz(a) a.size()
#define MAX_V 110000

using namespace std;
typedef unsigned long long ull;
typedef long long ll;
typedef vector <int> iv1;
typedef vector <vector<int> > iv2;
typedef vector <ll> llv1;
typedef unsigned int uint;
typedef vector <ull> ullv1;
typedef vector <vector <ull> > ullv2;

struct ArticulationEdge {
  int V, E;
  iv1 edges[MAX_V];

  int discoverd_order[MAX_V];
  iv1 articulation_points;
  vector<pair<int, int> > articulation_edges;

  int counter = 0;

  int dfs(int crt, int parent) {
    discoverd_order[crt] = ++counter;
    int ret = discoverd_order[crt];

    for1(0, edges[crt].size()) {
      int nxt = edges[crt][i];

      if(nxt == parent) continue;

      if(!discoverd_order[nxt]) {
        int low_node = dfs(nxt, crt);
        // low_node: crt 노드의 자식이 갈 수 있는 노드 중 가장 일찍 방문 한 노드

        if (low_node > discoverd_order[crt]) {
          articulation_edges.push_back({ min(crt, nxt), max(crt, nxt) });
        }

        ret = min(ret, low_node);
      } else {
        ret = min(ret, discoverd_order[nxt]);
      }
    }

    return ret;
  }

  void perform() {
    fill(discoverd_order, discoverd_order + MAX_V, 0);

    dfs(1, 0);

    sort(articulation_edges.begin(), articulation_edges.end());
  }

  int count() {
    return articulation_edges.size();
  }
};

int main() {
  ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);

  ArticulationEdge ae;

  cin >> ae.V >> ae.E;

  for1(0, ae.E) {
    int a, b;
    cin >> a >> b;

    // 양방향 그래프로 간선 연결
    ae.edges[a].push_back(b);
    ae.edges[b].push_back(a);
  }

  ae.perform();

  cout << ae.count() << "\n";

  for(auto i : ae.articulation_edges) {
    cout << i.first << " " << i.second << "\n";
  }
}

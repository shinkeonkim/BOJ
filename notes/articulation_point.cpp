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
#define MAX_V 11000

using namespace std;
typedef unsigned long long ull;
typedef long long ll;
typedef vector <int> iv1;
typedef vector <vector<int> > iv2;
typedef vector <ll> llv1;
typedef unsigned int uint;
typedef vector <ull> ullv1;
typedef vector <vector <ull> > ullv2;

struct ArticulationPoint {
  int V, E;
  iv1 edges[MAX_V];

  int discoverd_order[MAX_V];
  bool is_articulation_point[MAX_V];
  iv1 articulation_points;

  int counter = 0;

  int dfs(int crt, bool is_root) {
    discoverd_order[crt] = ++counter;
    int ret = discoverd_order[crt];

    int children_count = 0;
    // 정점 A가 루트 노드 일 경우를 대비해서 DFS스패닝 트리에서의 자식 수 세어준다.

    for1(0, edges[crt].size()) {
      int nxt = edges[crt][i];

      if(!discoverd_order[nxt]) {
        children_count++;

        int low_node = dfs(nxt, false);
        // low_node: crt 노드의 자식이 갈 수 있는 노드 중 가장 일찍 방문 한 노드

        if(!is_root && low_node >= discoverd_order[crt]) {
          is_articulation_point[crt] = true;
        }

        ret = min(ret, low_node);
      } else {
        ret = min(ret, discoverd_order[nxt]);
      }

    }
    if(is_root) {
      is_articulation_point[crt] = children_count >= 2;
    }
    return ret;
  }

  void perform() {
    fill(discoverd_order, discoverd_order + MAX_V, 0);
    fill(is_articulation_point, is_articulation_point + MAX_V, 0);

    for1(1, V+1) {
      if(!discoverd_order[i]) {
        dfs(i, true);
      }
    }

    for1(1, V+1) {
      if (is_articulation_point[i]) articulation_points.push_back(i);
    }
  }

  int count() {
    return articulation_points.size();
  }
};

int main() {
  ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);

  ArticulationPoint ap;

  cin >> ap.V >> ap.E;

  for1(0, ap.E) {
    int a, b;
    cin >> a >> b;

    // 양방향 그래프로 간선 연결
    ap.edges[a].push_back(b);
    ap.edges[b].push_back(a);
  }

  ap.perform();

  cout << ap.count() << "\n";

  for(auto i : ap.articulation_points) {
    cout << i << " ";
  }
}

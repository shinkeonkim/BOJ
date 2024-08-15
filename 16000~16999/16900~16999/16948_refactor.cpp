/*
[16948: 데스 나이트](https://www.acmicpc.net/problem/16948)

Tier: Silver 1 
Category: bfs, graphs, graph_traversal
*/


#include <bits/stdc++.h>

using namespace std;

#define for1(s, e) for(int i = s; i < e; i++)
#define fi first
#define se second

typedef long long ll;
typedef pair<ll, ll> pll;
typedef vector<ll> llv1;
typedef vector<llv1> llv2;

ll N, r1, c1, r2, c2;
llv2 dist;
vector< vector <bool>> visited;

void solve() {
  cin >> N;
  cin >> r1 >> c1 >> r2 >> c2;

  dist.resize(N + 1, llv1(N + 1, -1));
  visited.resize(N + 1, vector<bool>(N + 1, false));

  queue<pll> q;

  q.push({r1, c1});

  dist[r1][c1] = 0;
  visited[r1][c1] = true;

  while(!q.empty()) {
    auto [r, c] = q.front();
    q.pop();

    if(r == r2 && c == c2) {
      cout << dist[r][c] << endl; // 도착지점에 도달한 경우, 바로 최단거리 출력 후 종료
      return;
    }

    for1(0, 6) {
      int nr = r + "002244"[i] - '2';  // 데스나이트의 이동 가능한 방향 6가지
      int nc = c + "130413"[i] - '2';

      if(nr < 0 || nr >= N || nc < 0 || nc >= N) continue;  // 1. 0 <= nr, nc < N
      if(visited[nr][nc]) continue;  // 2. 방문된 경우 제외(중복해서 방문되었다는 것은 최단거리가 아님)

      visited[nr][nc] = true;
      dist[nr][nc] = dist[r][c] + 1;
      q.push({nr, nc});
    }
  }

  cout << -1 << endl;  // 도착할 수 없는 경우 -1 출력
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}
/*
[2146: 다리 만들기](https://www.acmicpc.net/problem/2146)

Tier: Gold 3 
Category: bfs, graphs, graph_traversal
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

ll N;
llv2 board, dist;
ll dy[] = { 0, 0, 1, -1 };
ll dx[] = { 1, -1, 0, 0 };
// 방향 배열이다. BFS 탐색 시에 요런거 선언하자.
// "2110"[d] - "1"  
// "1201"[d] - "1" 
// 요런식도 가능하다.

void solve() {
  cin >> N;
  board.resize(N, llv1(N));  // 문제에서 주어진 지도
  dist.resize(N, llv1(N, INF)); // 거리를 저장할 거다.

  queue <pll> Q; // BFS를 할거니 큐를 선언한다. (y, x) 좌표를 담는다.

  for1(0, N) {
    for1j(0, N) {
      cin >> board[i][j];
    }
  }

  vector<vector<bool>> chk(N, vector<bool>(N, false)); 

  ll area_num = 2;
  for1(0, N) {
    for1j(0, N) {
      if(board[i][j] && !chk[i][j]) {
        Q.push({ i, j });
        chk[i][j] = true;

        while(!Q.empty()) {
          auto [y, x] = Q.front(); Q.pop();
          board[y][x] = area_num;

          for(int d = 0; d < 4; d++) {
            ll ny = y + dy[d];
            ll nx = x + dx[d];

            if(ny < 0 || nx < 0 || ny >= N || nx >= N) continue;
            if(chk[ny][nx]) continue;
            if(board[ny][nx] == 0) continue;
            
            chk[ny][nx] = true;
            Q.push({ny, nx});
          }
        }

        area_num++;
      }
    }
  }

  // 각 대륙에 대한 정보로 board 정보를 바꾸어 남겼다.
  // 하지만 여전히 바다는 0이다.
  

  chk = vector<vector<bool>>(N, vector<bool>(N, false));


  for1(0, N) {
    for1j(0, N) {
      if(board[i][j] != 0) {
        Q.push({ i, j });
        chk[i][j] = true;
        dist[i][j] = 0;

        // 모든 대륙에서 동시에 출발시키기 위해, 한번에 큐에 넣고, 거리를 0으로 저장한다.
      }
    }
  }

  // 이제 BFS를 다시 수행한다.
  while(!Q.empty()) {
    auto [y, x] = Q.front(); Q.pop();

    for(int d = 0; d < 4; d++) {
      ll ny = y + dy[d];
      ll nx = x + dx[d];

      if(ny < 0 || nx < 0 || ny >= N || nx >= N) continue;
      if(chk[ny][nx]) continue;
      if(board[ny][nx] >= 2) continue; // 다음 이동할 곳이 대륙이라면 (혹은 누군가 왔다면) 넘어간다.
      board[ny][nx] = board[y][x];
      dist[ny][nx] = dist[y][x] + 1;  // 무조건 미방문된 곳에 왔을테니 바로 거리를 기록한다.
      
      chk[ny][nx] = true;
      Q.push({ny, nx});
    }
  }

  ll ans = INF;

  for1(0, N) {
    for1j(0, N) {
      // 인접한 곳이 서로 다른 board 값을 가지고 있다면 만난 곳이다.
      if(i + 1 < N) {
        if(board[i][j] != board[i+1][j]) ans = min(ans, dist[i][j] + dist[i+1][j]);
      }
      if(j + 1 < N) {
        if(board[i][j] != board[i][j+1]) ans = min(ans, dist[i][j] + dist[i][j+1]);
      }
    }
  }

  cout << ans;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}
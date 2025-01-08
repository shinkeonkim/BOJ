/*
[16236: 아기 상어](https://www.acmicpc.net/problem/16236)

Tier: Gold 3 
Category: bfs, graphs, graph_traversal, implementation, simulation
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

struct shark {
  ll x, y, size, eat;
};

ll N;
shark s;
llv2 board;

ll dy[] = {1, -1, 0, 0};
ll dx[] = {0, 0, 1, -1};

ll get_dis(pll a, pll b) {
  return abs(a.fi - b.fi) + abs(a.se - b.se);
}

pair<pll, ll> get_eatable_fish() {
  // 먹을 수 있는 물고기의 위치와 거리 반환
  llv2 dist(N, llv1(N, INF));

  queue<pll> q;
  q.push({s.y, s.x});
  dist[s.y][s.x] = 0;

  ll min_dist = INF;
  pll ret = {-1, -1};

  while(!q.empty()) {
    pll cur = q.front();
    q.pop();

    if(dist[cur.fi][cur.se] > min_dist) break;

    for1(0, 4) {
      ll ny = cur.fi + dy[i];
      ll nx = cur.se + dx[i];

      if(ny < 0 || nx < 0 || ny >= N || nx >= N) continue;
      if(dist[ny][nx] != INF || board[ny][nx] > s.size) continue;

      dist[ny][nx] = dist[cur.fi][cur.se] + 1;

      if(board[ny][nx] != 0 && board[ny][nx] < s.size) {
        // 물고기가 있는 경우

        if(min_dist > dist[ny][nx]) {
          min_dist = dist[ny][nx];
          ret = {ny, nx};
        } else if(min_dist == dist[ny][nx]) {
          if((ret.fi == ny && ret.se > nx) || ret.fi > ny) {
            ret = {ny, nx};
          }
        }
      }

      q.push({ny, nx});
    }
  }

  return {ret, min_dist};
}

void solve() {
  cin >> N;

  board.resize(N, llv1(N, 0));

  for1(0, N) {
    for1j(0, N) {
      cin >> board[i][j];
      if(board[i][j] == 9) {
        s.y = i;
        s.x = j;
        s.size = 2;
        s.eat = 0;
        board[i][j] = 0;
      }
    }
  }

  ll ans = 0;

  while(1) {
    auto ret = get_eatable_fish();

    pll eatable_fish = ret.fi;
    ll dist = ret.se;
  
    if(eatable_fish.fi == -1) break;
    
    s.y = eatable_fish.fi;
    s.x = eatable_fish.se;

    s.eat++;

    if(s.eat == s.size) {
      s.size++;
      s.eat = 0;
    }

    ans += dist;
    board[s.y][s.x] = 0;
  }

  cout << ans << '\n';
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}
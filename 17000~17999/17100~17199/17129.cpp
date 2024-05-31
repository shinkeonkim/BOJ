/*
[17129: 윌리암슨수액빨이딱따구리가 정보섬에 올라온 이유](https://www.acmicpc.net/problem/17129)

Tier: Silver 1 
Category: bfs, graphs, graph_traversal
*/


#include <bits/stdc++.h>

using namespace std;

#define for1(s, e) for(int i = s; i < e; i++)
#define for1j(s, e) for(int j = s; j < e; j++)
#define forEach(k) for(auto i : k)
#define forEachj(k) for(auto j : k)
#define sz(vct) a.size())
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

struct Point {
  int y, x;
};

int n, m;
vector<vector<int> > ar;
vector<vector<int> > D;

int dy[] = {0, 0, 1, -1};
int dx[] = {1, -1, 0, 0};

Point start;

void solve() {
  cin >> n >> m;
  ar.assign(n, vector<int>(m));
  D.assign(n, vector<int>(m, -1));

  for1(0, n) {
    string s;
    cin >> s;

    assert(s.length() == m);

    for(int j = 0; j < m; j++) {
      ar[i][j] = s[j] - 48;

      if (ar[i][j] == 2) {
        start = (Point){i, j};
      }
    }
  }

  queue<Point> q;
  q.push(start);
  D[start.y][start.x] = 0;

  while(!q.empty()) {
    Point here = q.front();
    q.pop();

    if(ar[here.y][here.x] >= 3) {
      cout << "TAK\n" << D[here.y][here.x];
      return;
    }

    for(int d = 0; d < 4; d++) {
      int ny = here.y + dy[d];
      int nx = here.x + dx[d];

      if(ny < 0 || nx < 0 || ny >= n || nx >= m) continue;

      if(ar[ny][nx] == 1 || D[ny][nx] >= 0) continue;

      D[ny][nx] = D[here.y][here.x] + 1;
      q.push((Point){ny, nx});
    }
  }

  cout << "NIE";
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}
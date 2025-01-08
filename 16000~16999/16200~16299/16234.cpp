/*
[16234: 인구 이동](https://www.acmicpc.net/problem/16234)

Tier: Gold 4 
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

int N, L, R, ans;
iv2 ar;

int dy[] = { 0, 0, 1, -1 };
int dx[] = { 1, -1, 0, 0 };

void solve() {
  cin >> N >> L >> R;
  
  ar.resize(N, iv1(N, 0));
  vector< vector<bool>> chk(N, vector<bool>(N, false));

  for1(0, N) {
    for1j(0, N) {
      cin >> ar[i][j];
    }
  }

  while(1) {
    int move_cnt = 0;

    for1(0, N) {
      for1j(0, N) {
        chk[i][j] = false;
      }
    }

    for1(0, N) {
      for1j(0, N) {
        if(!chk[i][j]) {
          queue <pii> Q;
          vector <pii> Q2;
          Q.push({i, j});
          Q2.push_back({i, j});

          chk[i][j] = true;

          while(!Q.empty()) {
            pii here = Q.front();
            Q.pop();

            for(int d = 0; d < 4; d++) {
              int ny = here.first + dy[d];
              int nx = here.second + dx[d];

              if(ny < 0 || nx < 0 || ny >= N || nx >= N) continue;
              if(chk[ny][nx]) continue;
              int diff = abs(ar[here.first][here.second] - ar[ny][nx]);
              if(diff < L || diff > R) continue;

              Q.push({ ny, nx });
              Q2.push_back({ ny, nx });
              chk[ny][nx] = true;
            }
          }

          if(Q2.size() > 1) {
            int sm = 0;
            bool flag = true;

            for(pii axis : Q2) {
              sm += ar[axis.first][axis.second];
              flag = flag && (ar[Q2[0].first][Q2[0].second] == ar[axis.first][axis.second]);
            }

            if(!flag) move_cnt++;

            int val = sm / Q2.size();
            
            for(pii axis : Q2) {
              ar[axis.first][axis.second] = val;
            }
          }
        }
      }
    }

    if(move_cnt == 0) break;
    ans++;
  }

  cout << ans;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
}

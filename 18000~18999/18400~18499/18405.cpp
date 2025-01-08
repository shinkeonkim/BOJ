/*
[18405: 경쟁적 전염](https://www.acmicpc.net/problem/18405)

Tier: Gold 5 
Category: bfs, graphs, graph_traversal, implementation
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

ll N, K;
ll ar[220][220];
ll S, X, Y;

void solve() {
  cin >> N >> K;

  for1(1, N + 1) {
    for1j(1, N + 1) {
      cin >> ar[i][j];
    }
  }

  cin >> S >> X >> Y;

  queue<tuple<ll, ll, ll>> q;

  for(int k = 1; k <= K; k++)  {
    for1(1, N + 1) {
      for1j(1, N + 1) {
        if (ar[i][j] == k) {
          q.push({ar[i][j], i, j});
        }
      }
    }
  }

  ll dx[] = {0, 0, 1, -1};
  ll dy[] = {1, -1, 0, 0};

  while(S--) {
    queue<tuple<ll, ll, ll>> nq;
    while(!q.empty()) {
      auto [v, y, x] = q.front(); q.pop();

      if(ar[y][x] != v) continue;

      for(int i = 0; i < 4; i++) {
        ll ny = y + dy[i];
        ll nx = x + dx[i];
        if (nx < 1 || nx > N || ny < 1 || ny > N) continue;
        if (ar[ny][nx] != 0) continue;
        ar[ny][nx] = v;
        nq.push({v, ny, nx});
      }
    }
    q = nq;
  }

  // for(int i = 1; i <= N; i++) {
  //   for(int j = 1; j <= N; j++) {
  //     cout << ar[i][j] << " ";
  //   }
  //   cout << endl;
  // }

  cout << ar[X][Y] << endl;
  

}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}
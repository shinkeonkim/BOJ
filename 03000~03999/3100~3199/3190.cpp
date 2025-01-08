/*
[3190: 뱀](https://www.acmicpc.net/problem/3190)

Tier: Gold 4 
Category: data_structures, deque, implementation, queue, simulation
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

ll N, K, L;
deque<pll> snake;

llv2 apples;


void solve() {
  cin >> N >> K;

  apples.resize(N + 1, llv1(N + 1, 0));

  for1(0, K) {
    ll a, b;

    cin >> a >> b;
    apples[a][b] = 1;
  }

  snake.push_back({1, 1});

  cin >> L;

  char dir;
  int time;
  int dy[] = {0, 1, 0, -1};
  int dx[] = {1, 0, -1, 0};

  int d = 0;
  int ans = 0;

  for1(0, L) {
    cin >> time >> dir;

    while(ans < time) {
      ans++;
      int ny = snake.back().fi + dy[d];
      int nx = snake.back().se + dx[d];
      
      if(nx < 1 || nx > N || ny < 1 || ny > N) {
        cout << ans << '\n';
        return;
      }

      for(int i = 0; i < snake.size(); i++) {
        if(snake[i].fi == ny && snake[i].se == nx) {
          cout << ans << '\n';
          return;
        }
      }

      snake.push_back({ny, nx});


      if(apples[ny][nx] == 1) {
        apples[ny][nx] = 0;
      } else {
        snake.pop_front();
      }
    }

    if(dir == 'L') {
      d = (d + 3) % 4;
    } else {
      d = (d + 1) % 4;
    }
  }

  while(1) {
    ans++;
    int ny = snake.back().fi + dy[d];
    int nx = snake.back().se + dx[d];

    if(nx < 1 || nx > N || ny < 1 || ny > N) {
      cout << ans << '\n';
      return;
    }

    for(int i = 0; i < snake.size(); i++) {
      if(snake[i].fi == ny && snake[i].se == nx) {
        cout << ans << '\n';
        return;
      }
    }

    snake.push_back({ny, nx});

    if(apples[ny][nx] == 1) {
      apples[ny][nx] = 0;
    } else {
      snake.pop_front();
    }
  }
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}
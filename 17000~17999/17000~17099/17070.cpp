/*
[17070: 파이프 옮기기 1](https://www.acmicpc.net/problem/17070)

Tier: Gold 5 
Category: dp, graphs, graph_traversal
*/


#include <bits/stdc++.h>

using namespace std;

#define for1(s, e) for(int i = s; i < e; i++)
#define for1j(s, e) for(int j = s; j < e; j++)
#define forEach(k) for(auto i : k)
#define forEachj(k) for(auto j : k)
#define sz(vct) vct.size()
#define all(vct) vct.begin(), vct.end()
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

int N;
int ar[22][22];
int D[22][22][3];
// 0: 가로, 1: 세로, 2: 대각선


bool chk_diagonal(int y, int x) {
  return ar[y][x] == 0 && ar[y][x - 1] == 0 && ar[y - 1][x] == 0 && ar[y - 1][x - 1] == 0;
}

int f(int y, int x, int z) {
  int &ans = D[y][x][z];
  if(ans >= 0) return ans;
  
  if(y == 0 || x == 0) return ans = 0;

  ans = 0;
  if(z == 0) {
    if(x - 2 >= 1 && ar[y][x - 2] == 0) ans += f(y, x - 1, 0); // 가로 한칸 이동
    if(x - 2 >= 1 && y - 1 >= 1 && chk_diagonal(y, x - 1)) ans += f(y, x - 1, 2); // 대각선에서 가로로 이동
  } else if(z == 1) {
    if(y - 2 >= 1 && x >= 1 && ar[y - 2][x] == 0) ans += f(y - 1, x , 1); // 세로 한칸 이동 
    if(y - 2 >= 1 && x - 1 >= 1 && chk_diagonal(y - 1, x)) ans += f(y - 1, x, 2); // 대각선에서 세로로 
  } else {
    if(y - 1 >= 1 && x - 2 >= 1 && ar[y - 1][x - 2] == 0) ans += f(y - 1, x - 1, 0); // 가로에서 대각선
    if(y - 2 >= 1 && x - 1 >= 1 && ar[y - 2][x - 1] == 0) ans += f(y - 1, x - 1, 1); // 세로에서 대각선
    if(y - 2 >= 1 && x - 2 >= 1 && chk_diagonal(y - 1, x - 1)) ans += f(y - 1, x - 1, 2); // 대각선 이동
  }
  return ans;
}
void solve() {
  cin >> N;

  for1(1, N + 1) {
    for1j(1, N + 1) {
      cin >> ar[i][j];
    }
  }

  memset(D, -1, sizeof(D));
  D[1][2][0] = 1;

  if(ar[N][N] == 0) {
    if(ar[N][N-1] == 0) f(N, N, 0);
    if(ar[N-1][N] == 0) f(N, N, 1);
    if(chk_diagonal(N, N)) f(N, N, 2);
  }

  cout << max(0, D[N][N][0]) + max(0, D[N][N][1]) + max(0, D[N][N][2]);

}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}
/*
[1895: 필터](https://www.acmicpc.net/problem/1895)

Tier: Silver 4 
Category: bruteforcing, implementation, sorting
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

typedef unsigned long long ull;
typedef long long ll;
typedef unsigned int uint;

typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<double, double> pdd;
typedef pair<double, int> pdi;
typedef pair<string, string> pss;

typedef vector<ll> llv1;
typedef vector<vector<ll>> llv2;


const double EPS = 1e-8;
const double PI = acos(-1);

template<typename T>
T sq(T x) { return x * x; }

int sign(ll x) { return x < 0 ? -1 : x > 0 ? 1 : 0; }
int sign(int x) { return x < 0 ? -1 : x > 0 ? 1 : 0; }
int sign(double x) { return abs(x) < EPS ? 0 : x < 0 ? -1 : 1; }

void solve() {
  ll R, C, T;
  ll ans = 0;

  cin >> R >> C;
  
  llv2 grid(R, llv1(C));

  for1(0, R) {
    for1j(0, C) {
      cin >>grid[i][j];
    }
  }

  cin >> T;

  for1(0, R - 2) {
    for1j(0, C - 2) {
      llv1 temp;
      for(int y = 0; y < 3; y++) {
        for(int x = 0; x < 3; x++) {
          temp.push_back(grid[i+y][j+x]);
        }
      }

      sort(all(temp));

      if(temp[4] >= T) ans++;
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
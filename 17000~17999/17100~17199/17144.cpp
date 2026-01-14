/*
[17144: 미세먼지 안녕!](https://www.acmicpc.net/problem/17144)

Tier: Gold 4 
Category: implementation, simulation
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
#define DEBUG 0

typedef unsigned long long ull;
typedef long long ll;
typedef unsigned int uint;

typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<double, double> pdd;
typedef pair<double, int> pdi;
typedef pair<string, string> pss;

typedef vector<ll> llv1;
typedef vector<pll> pllv1;


const double EPS = 1e-8;
const double PI = acos(-1);

template<typename T>
T sq(T x) { return x * x; }

int sign(ll x) { return x < 0 ? -1 : x > 0 ? 1 : 0; }
int sign(int x) { return x < 0 ? -1 : x > 0 ? 1 : 0; }
int sign(double x) { return abs(x) < EPS ? 0 : x < 0 ? -1 : 1; }

ll R, C, T;
ll ar[55][55];
ll tmp[55][55];
pllv1 machine;

ll dy[] = {1, -1, 0, 0};
ll dx[] = {0, 0, 1, -1};

ll machin_dy[2][4] = {{0, -1, 0, 1}, {0, 1, 0, -1}};
ll machin_dx[2][4] = {{1, 0, -1, 0}, {1, 0, -1, 0}};

void dust_spread() {
  memset(tmp, 0, sizeof(tmp));

  for1(0, R) {
    for1j(0, C) {
      ll spread = 0;
      if(ar[i][j] > 0) {
        spread = ar[i][j] / 5;
      }

      if (spread == 0) continue;

      for(int d = 0; d < 4; d++) {
        ll ny = i + dy[d];
        ll nx = j + dx[d];

        if(nx < 0 || ny < 0 || ny >= R || nx >= C || ar[ny][nx] == -1) continue;

        tmp[ny][nx] += spread;
        ar[i][j] -= spread;

        assert (ar[i][j] >= 0);
      }
    }
  }

  for1(0, R) {
    for1j(0, C) {
      if(ar[i][j] == -1) continue;
      ar[i][j] += tmp[i][j];
    }
  }
}

void machine_on(int machine_number) {
  ll y = machine[machine_number].fi;
  ll x = machine[machine_number].se;
  ll dir = 0;

  ll prev = 0;
  ll cur = 0;

  if (DEBUG) {
    cout << "PREV ===\n";
    for1(0, R) {
      for1j(0, C) {
        cout << ar[i][j] << " ";
      }
      cout << "\n";
    }
    cout << "\n";
  }

  while (1) {
    ll ny = y + machin_dy[machine_number][dir % 4];
    ll nx = x + machin_dx[machine_number][dir % 4];

    if (ny < 0 || nx < 0 || ny >= R || nx >= C) {
      dir++;
      ny = y + machin_dy[machine_number][dir % 4];
      nx = x + machin_dx[machine_number][dir % 4];
    }

    if (ar[ny][nx] == -1) {
      break;
    }

    cur = ar[ny][nx];
    ar[ny][nx] = prev;
    prev = cur;
    y = ny;
    x = nx;
  }

  if(DEBUG) {
    cout << "AFTER ===\n";
    for1(0, R) {
      for1j(0, C) {
        cout << ar[i][j] << " ";
      }
      cout << "\n";
    }
    cout << "\n";
  }
}

void solve() {
  cin >> R >> C >> T;

  for1(0, R) {
    for1j(0, C) {
      cin >> ar[i][j];
      if(ar[i][j] == -1) {
        machine.push_back({i, j});
      }
    }
  }

  while(T--) {
    dust_spread();
    for1(0, 2) {
      machine_on(i);
    }
  }

  ll ans = 0;

  for1(0, R) {
    for1j(0, C) {
      if(ar[i][j] > 0) {
        ans += ar[i][j];
      }

      // cout << ar[i][j] << " ";
    }
    // cout << "\n";
  }

  cout << ans;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}
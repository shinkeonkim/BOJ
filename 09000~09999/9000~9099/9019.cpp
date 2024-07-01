/*
[9019: DSLR](https://www.acmicpc.net/problem/9019)

Tier: Gold 4 
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

ll D(ll a) {
  return (a * 2) % 10000;
}

ll S(ll a) {
  return (a != 0 ? a - 1 : 9999);
}

ll L(ll a) {
  return (a % 1000) * 10 + a / 1000;
}

ll R(ll a) {
  return a / 10 + 1000 * (a % 10);
}

struct tmp {
  ll idx, cnt, how, prev;
};

void solve() {
  llv1 DP;
  llv1 track;
  llv1 prev_idx;
  ll s, e;

  cin >> s >> e;
  DP.resize(10000, INF);
  track.resize(10000, -1);
  prev_idx.resize(10000, -1);

  queue <tmp> Q;1

  Q.push({ s, 0, -1, -1 });

  // cout << D(s) << " " << S(s) << " " << L(s) << " " << R(s) << "\n";

  while(!Q.empty()) {
    auto here = Q.front(); Q.pop();

    // cout << here.idx << " ";

    if(DP[here.idx] <= here.cnt) continue;

    DP[here.idx] = here.cnt;
    track[here.idx] = here.how;
    prev_idx[here.idx] = here.prev;

    if(here.idx == e) break;

    if(D(here.idx) != here.idx && DP[D(here.idx)] > here.cnt + 1) {
      Q.push({ D(here.idx), here.cnt + 1, 0, here.idx });
    }
    if(L(here.idx) != here.idx && DP[L(here.idx)] > here.cnt + 1) {
      Q.push({ L(here.idx), here.cnt + 1, 2, here.idx });
    }

    if(R(here.idx) != here.idx && DP[R(here.idx)] > here.cnt + 1) {
      Q.push({ R(here.idx), here.cnt + 1, 3, here.idx });
    }
    if(S(here.idx) != here.idx && DP[S(here.idx)] > here.cnt + 1) {
      Q.push({ S(here.idx), here.cnt + 1, 1, here.idx });
    }
  }

  ll idx = e;

  char to_chr[] = {'D', 'S', 'L', 'R'};

  stack <char> stk;
  while(prev_idx[idx] != -1) {
    stk.push(to_chr[track[idx]]);

    idx = prev_idx[idx];
  }

  while(!stk.empty()) {
    cout << stk.top();
    stk.pop();
  }
  cout << "\n";

}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; cin >> tc;
  while(tc--) solve();
  
}
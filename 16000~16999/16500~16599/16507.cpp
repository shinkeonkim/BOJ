/*
[16507: 어두운 건 무서워](https://www.acmicpc.net/problem/16507)

Tier: Silver 1 
Category: prefix_sum
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

ll N, M, Q;
ll ar[1100][1100];
ll sm[1100][1100];

ll get_area(int y1, int x1, int y2, int x2) {
  return sm[y2][x2] - sm[y1-1][x2] - sm[y2][x1-1] + sm[y1-1][x1-1];
}

void solve() {
  cin >> N >> M >> Q;

  for1(1, N + 1) {
    for1j(1, M + 1) {
      cin >> ar[i][j];
      sm[i][j] = sm[i-1][j] + sm[i][j-1] + ar[i][j] - sm[i-1][j-1];
    }
  }

  while(Q--) {
    ll y1, x1, y2, x2;
    cin >> y1 >> x1 >> y2 >> x2;

    ll area = get_area(y1, x1, y2, x2);
    ll cnt = (y2 - y1 + 1) * (x2 - x1 + 1);

    cout << area / cnt << "\n";
  }
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}

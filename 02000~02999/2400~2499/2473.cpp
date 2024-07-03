/*
[2473: 세 용액](https://www.acmicpc.net/problem/2473)

Tier: Gold 3 
Category: binary_search, sorting, two_pointer
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

ll N;
llv1 ar;
llv1 ans = {INF, INF, INF};
ll sm = INF;

void solve() {
  cin >> N;
  ar.resize(N);

  for1(0, N) cin >> ar[i];

  sortv(ar);

  // forEach(ar) cout << i << " ";
  // cout << "@@@@@@@@@@@@@\n";

  for1(0, N) {
    for1j(i + 1, N) {
      int need = -(ar[i] + ar[j]);

      ll k = lower_bound(ar.begin(), ar.end(), need) - ar.begin();
      
      for(int here = max(k - 10, 0ll); here < min(k + 10, N); here++) {
        if(here == i || here == j) continue;

        ll a = ar[i];
        ll b = ar[j];
        ll c = ar[here];

        if(abs(a + b + c) < sm) {
          ans = {a, b, c};
          sm = abs(a + b + c);
        }
        
      }

      // cout << ar[i] << " " << ar[j] << " need: " << need << " " << k << " " << ar[k] << "\n";
    }
  }

  sortv(ans);
  forEach(ans) cout << i << " ";

}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}
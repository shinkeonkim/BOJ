/*
[1374: 강의실](https://www.acmicpc.net/problem/1374)

Tier: Gold 5 
Category: data_structures, greedy, sorting, priority_queue
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

ll N, a, b, c;
vector <pll> classes;

void solve() {
  cin >> N;  

  for1(0, N) {
    cin >> a >> b >> c;
    classes.push_back({b, c}); // {start, end}
  }

  sort(all(classes));

  ll ans = 0;

  priority_queue<ll, vector<ll>, greater<ll>> pq; // end_times

  for(auto cls : classes) {
    if(pq.empty()) {
      pq.push(cls.se);
      ans = max(ans, 1ll);
      continue;
    }

    ll fastest_end_time = pq.top();

    if(fastest_end_time <= cls.fi) {
      pq.pop();
      pq.push(cls.se);
    } else {
      pq.push(cls.se);
    }

    ans = max(ans, (ll) pq.size());
  }

  cout << ans << "\n";
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}

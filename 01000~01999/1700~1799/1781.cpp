/*
[1781: 컵라면](https://www.acmicpc.net/problem/1781)

Tier: Gold 2 
Category: data_structures, greedy, priority_queue, sorting
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

pllv1 ar;

void solve() {
  cin >> N;

  ar.resize(N);
  // 데드라인이 짧은 순서대로 pq에 넣는다.
  // 만약 pq 안에 들어있는 것들의 개수보다 데드라인이 작다면, 크기를 비교해서 더 작은 것을 빼고 넣는다.
  // pq 안에 들어있는 개수보다 데드라인이 크다면, pq에 넣는다.

  priority_queue <ll, llv1, greater<ll>> pq;

  for1(0, N) {
    cin >> ar[i].fi >> ar[i].se;
  }

  sort(all(ar), [](pll a, pll b) {
    if(a.fi == b.fi) return a.se > b.se;
    return a.fi < b.fi;
  });

  ll ans = 0;

  for1(0, N) {
    pq.push(ar[i].se);
    if(pq.size() > ar[i].fi) pq.pop();
  }

  while(!pq.empty()) {
    ans += pq.top();
    pq.pop();
  }

  cout << ans << '\n';
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}
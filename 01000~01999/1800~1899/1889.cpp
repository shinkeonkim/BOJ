/*
[1889: 선물 교환](https://www.acmicpc.net/problem/1889)

Tier: Gold 4 
Category: dag, data_structures, graphs, topological_sorting
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

ll n;
llv1 in_degree;
pllv1 ar;
vector<bool> chk;

void solve() {
  cin >> n;
  in_degree.resize(n + 1, 0);
  chk.resize(n + 1, false);
  ar.resize(n + 1);

  for1(1, n + 1) {
    cin >> ar[i].first >> ar[i].second;

    in_degree[ar[i].first]++;
    in_degree[ar[i].second]++;
  }

  queue <ll> Q;

  for1(1, n + 1) {
    if(in_degree[i] < 2) {
      Q.push(i);
      chk[i] = true;
      in_degree[i]--;
    }
  }

  while(!Q.empty()) {
    ll here = Q.front(); Q.pop();

    ll a = ar[here].first;
    ll b = ar[here].second;


    if(!chk[a] && --in_degree[a] < 2) {
      Q.push(a);
      chk[a] = true;
    }
    if(!chk[b] && --in_degree[b] < 2) {
      Q.push(b);
      chk[b] = true;
    }
  }

  ll cnt = 0;
  for1(1, n + 1) {
    if(!chk[i]) cnt++;
  }

  cout << cnt << "\n";
  for1(1, n + 1) {
    if(!chk[i]) cout << i << " ";
  }

}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}
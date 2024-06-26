/*
[3745: 오름세](https://www.acmicpc.net/problem/3745)

Tier: Gold 2 
Category: binary_search, lis
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
typedef __int128 llll;
typedef unsigned int uint;

typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<double, double> pdd;
typedef pair<double, int> pdi;
typedef pair<string, string> pss;

typedef vector<ll> llv1;

const double EPS = 1e-8;
const double PI = acos(-1);

template<typename T>
T sq(T x) { return x * x; }

int sign(ll x) { return x < 0 ? -1 : x > 0 ? 1 : 0; }
int sign(int x) { return x < 0 ? -1 : x > 0 ? 1 : 0; }
int sign(double x) { return abs(x) < EPS ? 0 : x < 0 ? -1 : 1; }

ll lis(llv1& ar) {
  llv1 v, buffer;
  llv1::iterator vv;
  v.push_back(2000000000ll);

  ll n = sz(ar);

  for1(0, n){
    if(ar[i] > *v.rbegin()) {
      v.push_back(ar[i]);
    }
    else{
      vv = lower_bound(v.begin(), v.end(), ar[i]);
      *vv = ar[i];
    }
  }
  return sz(v);
}

void solve() {
  int n;

  while (cin >> n) {
    llv1 V;

    for1(0, n) {
      ll a;
      cin >> a;

      V.push_back(a);
    }

    cout << lis(V) << "\n";
  }

}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}
/*
[19951: 태상이의 훈련소 생활](https://www.acmicpc.net/problem/19951)

Tier: Gold 5 
Category: prefix_sum, difference_array
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


const double EPS = 1e-8;
const double PI = acos(-1);

template<typename T>
T sq(T x) { return x * x; }

int sign(ll x) { return x < 0 ? -1 : x > 0 ? 1 : 0; }
int sign(int x) { return x < 0 ? -1 : x > 0 ? 1 : 0; }
int sign(double x) { return abs(x) < EPS ? 0 : x < 0 ? -1 : 1; }

typedef long long ll;
typedef vector<ll> llv1;

ll N, M;
llv1 heights;
llv1 difference_array;

void init() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);

  cin >> N >> M;
  
  heights.resize(N + 1);
  difference_array.resize(N + 2, 0);
  for1(1, N + 1) {
    cin >> heights[i];
  }
}

void solve() {
  init();
  for1(0, M) {
    ll a, b, diff;
    cin >> a >> b >> diff;
    difference_array[a] += diff;
    difference_array[b + 1] -= diff;
  }

  ll crt = 0;
  for1(1, N + 1) {
    crt += difference_array[i];
    heights[i] += crt;
  }

  for1(1, N + 1) {
    cout << heights[i] << " ";
  }
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}
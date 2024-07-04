/*
[2568: 전깃줄 - 2](https://www.acmicpc.net/problem/2568)

Tier: Platinum 5 
Category: lis
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
#define pb push_back

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
pllv1 nums;

struct LIS {
  llv1 ar;

  llv1 v, buffer;
  llv1::iterator vv;
  vector<pair<ll, ll> > d;

  void perform() {
    v.pb(2000000000ll);

    ll n = sz(ar);

    for1(0, n){
      if (ar[i] > *v.rbegin()) {
        v.pb(ar[i]);
        d.push_back({ v.size() - 1, ar[i] });
      }
      else {
        vv = lower_bound(v.begin(), v.end(), ar[i]);
        *vv = ar[i];
        d.push_back({ vv - v.begin(), ar[i] });
      }
    }

    for(int i = sz(d) - 1; i > -1; i--){
      if(d[i].first == sz(v)-1){
        buffer.pb(d[i].second);
        v.pop_back();
      }
    }

    reverse(buffer.begin(), buffer.end());
  }

  ll length() {
    return buffer.size();
  }

  llv1 result() {
    return buffer;
  }
};


void solve() {
  cin >> N;
  nums.resize(N);

  for1(0, N) {
    cin >> nums[i].first >> nums[i].second;
  }

  sortv(nums);

  LIS lis;

  for1(0, N) lis.ar.push_back(nums[i].second);

  lis.perform();

  llv1 ret = lis.result();

  cout << N - ret.size() << "\n";

  int i = 0;
  int j = 0;

  while(i < N && j < ret.size()) {
    if(nums[i].second == ret[j]) {
      i++;
      j++;
    } else {
      cout << nums[i].first << "\n";
      i++;
    }
  }

  while(i < N) {
    cout << nums[i].first << "\n";
    i++;
  }
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}
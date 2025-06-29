/*
[1590: 캠프가는 영식](https://www.acmicpc.net/problem/1590)

Tier: Silver 4 
Category: math, bruteforcing, binary_search
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

struct Bus {
  ll start, duration, count;

  ll startTime() const {
    return start;
  }

  ll endTime() const {
    return start + duration * (count - 1);
  }

  ll expectedWaitingTime(ll t) const {
    for(int i = 0; i < count; i++) {
      ll busTime = start + duration * i;
      if (busTime >= t) {
        return busTime - t;
      }
    }
  }
};

void solve() {
  ll n, t;

  cin >> n >> t;

  ll minWaitingTime = LLONG_MAX;

  vector<Bus> buses(n);
  for1(0, n) {
    cin >> buses[i].start >> buses[i].duration >> buses[i].count;
  }

  for1(0, n) {
    if (buses[i].endTime() < t) continue;

    if (buses[i].startTime() >= t) {
      minWaitingTime = min(minWaitingTime, buses[i].startTime() - t);
      continue;
    }

    minWaitingTime = min(minWaitingTime, buses[i].expectedWaitingTime(t));
  }


  if (minWaitingTime == LLONG_MAX) minWaitingTime = -1;
  
  cout << minWaitingTime;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}
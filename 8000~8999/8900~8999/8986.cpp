/*
  [8986: 전봇대](https://www.acmicpc.net/problem/8986)

  Tier: Platinum 5
  Category: 삼진탐색
*/
#include <bits/stdc++.h>

#define for1(s,n) for(int i = s; i < n; i++)
#define for1j(s,n) for(int j = s; j < n; j++)
#define foreach(k) for(auto i : k)
#define foreachj(k) for(auto j : k)
#define pb(a) push_back(a)
#define sz(a) a.size()

using namespace std;
typedef unsigned long long ull;
typedef long long ll;
typedef vector <int> iv1;
typedef vector <vector<int> > iv2;
typedef vector <ll> llv1;
typedef unsigned int uint;
typedef vector <ull> ullv1;
typedef vector <vector <ull> > ullv2;

ll N;
ll points[110000];

ll f(ll a) {
  ll ret = 0;

  for1(1, N) {
    ret += llabs(a * i - points[i]);
  }

  return ret;
}

int main() {
  ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);

  cin >> N;

  for1(0, N) cin >> points[i];

  ll s = points[0];
  ll e = points[N - 1];

  while(e - s >= 3) {
    ll first = (s * 2 + e) / 3;
    ll second = (s + e * 2) / 3;

    if(f(first) <= f(second)) {
      e = second;
    } else {
      s = first;
    }
  }

  ll ans = (ll)1e18;
  for(int i = s; i <= e; i++) {
    ans = min(ans, f(i));
  }

  cout << ans;
}

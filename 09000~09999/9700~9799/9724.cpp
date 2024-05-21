/*
  [9724: Perfect Cube](https://www.acmicpc.net/problem/9724)

  Tier: Bronze 2
  Category: 구현
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


int main() {
  ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);

  ll T, a, b;

  cin >> T;

  for(int tc = 1; tc <= T; tc++) {
    int ans = 0;
    cin >> a >> b;

    for1(1, 1280) {
      ll j = i * i * i;
      if(a <= j && j <= b) {
        ans += 1;
      }

      if(j >= b) {
        break;
      }
    }

    cout << "Case #" << tc << ": " << ans << "\n";
  }
}

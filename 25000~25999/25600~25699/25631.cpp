/*
  [25631: 마트료시카 합치기](https://www.acmicpc.net/problem/24296)

  Tier: Silver 5
  Category: 그리디
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

ll N, a, ans;
llv1 V;

int main() {
  ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);

  cin >> N;
  for1(0, N) {
    cin >> a;
    V.push_back(a);
  }

  sort(V.begin(), V.end());

  for1(0, N) {
    llv1 V2;
    ll crt = V[0];

    for(int i = 1; i < V.size(); i++) {
      if (crt < V[i]) {
        crt = V[i];
      } else {
        V2.push_back(V[i]);
      }
    }

    if (V.size() == V2.size()) break;

    V = V2;
    ans++;
  }

  cout << ans;
}

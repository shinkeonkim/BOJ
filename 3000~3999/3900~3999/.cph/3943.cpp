/*
  [3943: 헤일스톤 수열](https://www.acmicpc.net/problem/3943)

  Tier: Bronze 2
  Category: DP
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

int N, a;
int D[11000000];

ll dfs(ll i) {
  if(i >= 10000000) {
    if(i % 2 == 1) {
      return max(i, dfs(i * 3 + 1));
    } else {
      return max(i, dfs(i / 2));
    }
  }
  if(D[i]) return D[i];

  if(i % 2 == 1) {
    return D[i] = max(i, dfs(i * 3 + 1));
  } else {
    return D[i] = max(i, dfs(i / 2));
  }
}

int main() {
  ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);

  int tc;
  cin >> tc;

  D[0] = -1;
  D[1] = 1;
  D[2] = 2;
  D[3] = 16;
  D[4] = 4;

  while(tc--) {
    cin >> a;
    cout << dfs(a) << "\n";
  }
}

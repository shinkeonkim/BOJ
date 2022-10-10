/*
  [18185: 라면 사기(Small)](https://www.acmicpc.net/problem/)

  Tier: Diamond 5
  Category: 그리디 알고리즘
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
ll ar[11000];

int main() {
  ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);
  cin >> N;

  for1(0, N) {
    cin >> ar[i];
  }

  int ans = 0;

  for1(0, N) {
    int cnt = 0;
    if(ar[i+1] > ar[i+2]) {
      cnt = min(ar[i], ar[i+1] - ar[i+2]);
      ans += cnt * 5;
      ar[i] -= cnt;
      ar[i+1] -= cnt;
    }

    cnt = min(ar[i], min(ar[i+1], ar[i+2]));
    ans += cnt * 7;
    ar[i] -= cnt;
    ar[i+1] -= cnt;
    ar[i+2] -= cnt;

    ans += ar[i] * 3;
    ar[i] = 0;
  }

  cout << ans;
}

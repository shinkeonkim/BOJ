/*
  [10163: 색종이](https://www.acmicpc.net/problem/10163)

  Tier: Bronze 1
  Category: 브루트포스
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

ll N, a, b, c, d;
ll ar[1100][1100];
ll cnt[110];

int main() {
  ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);

  cin >> N;
  for1(1, N+1) {
    cin >> a >> b >> c >> d;

    for(int x = a; x < a + c; x++) {
      for(int y = b; y < b + d; y++) {
        ar[x][y] = i;
      }
    }

  }
  for(int x = 0; x <= 1000; x++) {
    for(int y = 0; y<= 1000; y++) {
      cnt[ar[x][y]]++;
    }
  }

  for1(1, N+1) {
    cout << cnt[i] << "\n";
  }
}

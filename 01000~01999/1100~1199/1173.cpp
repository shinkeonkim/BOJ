/*
  [1173: 운동](https://www.acmicpc.net/problem/1173)

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

int N, m, M, T, R;

int main() {
  ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);

  cin >> N >> m >> M >> T >> R;

  int cnt = 0;
  int time = 0;
  int crt = m;

  for1(0, 10000000) {
    if(cnt >= N) break;
    if(crt + T <= M) {
      crt += T;
      cnt++;
      time++;
    } else {
      crt = max(crt - R, m);
      time++;
    }
  }

  cout << (cnt < N ? -1 : time);
}

/*
  [17435: 합성함수와 쿼리](https://www.acmicpc.net/problem/17435)

  Tier: Gold 1
  Category: Sparse Table
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

#define MAX_DEGREE 20

ll M, Q, n, x;
ll f[220000][MAX_DEGREE];

int main() {
  ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);

  cin >> M;
  for1(1, M + 1) {
    cin >> f[i][0];
  }

  for(int i = 1; i < MAX_DEGREE; i++) {
    for(int j = 1; j <= M; j++) {
      f[j][i] = f[f[j][i-1]][i-1];
    }
  }

  cin >> Q;

  for1(0, Q) {
    cin >> n >> x;

    for(int j = MAX_DEGREE - 1; j >= 0; j--) {
      ll crt = 1 << j;
      if(n >= crt) {
        n -= crt;
        x = f[x][j];
      }
    }

    cout << x << "\n";
  }
}

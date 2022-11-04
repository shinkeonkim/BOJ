/*
  [14562: 태권왕](https://www.acmicpc.net/problem/14562)

  Tier: Silver 2
  Category: BFS
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

const int INF = 7654321;
const int MX = 440;

int tc, ans;
int a, b;
int D[MX][MX];

struct st {
  int a, b, cnt;
};

int main() {
  ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);

  cin >> tc;
  while(tc--) {
    cin >> a >> b;

    for1(0, MX) {
      for1j(0, MX) {
        D[i][j] = INF;
      }
    }
    ans = INF;

    queue <st> Q;

    Q.push({ a, b, 0 });

    while(!Q.empty()) {
      auto f = Q.front();
      Q.pop();

      if(D[f.a][f.b] <= f.cnt) {
        continue;
      }

      D[f.a][f.b] = f.cnt;

      if(f.a == f.b) {
        ans = f.cnt;
        break;
      }

      if(f.a + 1 < MX) {
        Q.push({ f.a + 1, f.b, f.cnt + 1});
      }

      if(f.a * 2 < MX && f.b + 3 < MX) {
        Q.push({ f.a * 2, f.b + 3, f.cnt + 1 });
      }
    }

    cout << ans << "\n";
  }
}

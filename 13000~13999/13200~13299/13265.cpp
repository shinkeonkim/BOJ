/*
  [13265: 색칠하기](https://www.acmicpc.net/problem/13265)

  Tier: Gold 5
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

ll tc, n, m, a, b;
int color[1100];

int main() {
  ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);

  cin >> tc;

  while(tc--) {
    cin >> n >> m;

    fill(color, color + n + 1, -1);

    bool chk = true;

    llv1 adj[1100];

    for1(0, m) {
      cin >> a >> b;

      adj[a].push_back(b);
      adj[b].push_back(a);
    }

    queue <pair<int, int>> Q;

    for1(1, n + 1) {
      if(color[i] == -1) {
        Q.push({ i, 1 });

        while(!Q.empty()) {
          auto f = Q.front(); Q.pop();

          if(color[f.first] > -1) {
            if(color[f.first] != f.second) chk = false;

            continue;
          }
          color[f.first] = f.second;

          for(auto edge : adj[f.first]) {
            Q.push({ edge, 1 - f.second });
          }
        }
      }
    }

    cout << (chk ? "possible" : "impossible") << "\n";

  }
}

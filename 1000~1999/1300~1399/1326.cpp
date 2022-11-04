/*
  [1326: 폴짝폴짝](https://www.acmicpc.net/problem/1326)

  Tier: Silver 2
  Category: DFS/BFS
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

const ll INF = (ll)1e18;

int N;
ll ar[11000];
ll D[11000];
int a, b;

int main() {
  ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);

  cin >> N;
  for1(1, N + 1) {
    cin >> ar[i];
  }

  cin >> a >> b;

  fill(D, D + N + 1, INF);

  queue <pair<int, int>> Q;

  Q.push({ a, 0 });

  while(!Q.empty()) {
    auto f = Q.front();
    Q.pop();

    if(D[f.first] <= f.second) continue;

    D[f.first] = f.second;

    for(int i = f.first; i <= N; i += ar[f.first]) {
      if(f.second + 1 < D[i]) {
        Q.push({ i, f.second + 1 });
      }
    }

    for(int i = f.first; i >= 1; i -= ar[f.first]) {
      if(f.second + 1 < D[i]) {
        Q.push({ i, f.second + 1 });
      }
    }
  }

  cout << (D[b] == INF ? -1 : D[b]);
}

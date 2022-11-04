/*
  [24480: 알고리즘 수업 - 깊이 우선 탐색 2](https://www.acmicpc.net/problem/24480)

  Tier: Silver 2
  Category: DFS
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

ll N, M, R, a, b;
int visited_count[110000];
llv1 adj[110000];
int cnt = 1;

void dfs(int here) {
  if(visited_count[here]) return;

  visited_count[here] = cnt++;

  for(auto there : adj[here]) {
    if(visited_count[there]) continue;

    dfs(there);
  }
}

int main() {
  ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);

  cin >> N >> M >> R;

  for1(0, M) {
    cin >> a >> b;

    adj[a].push_back(b);
    adj[b].push_back(a);
  }

  for1(1, N + 1) {
    sort(adj[i].begin(), adj[i].end(), greater<ll>());
  }

  dfs(R);

  for1(1, N + 1) {
    cout << visited_count[i] << "\n";
  }
}

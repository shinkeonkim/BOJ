/*
  [25511: 값이 k인 트리 노드의 깊이](https://www.acmicpc.net/problem/25511)

  Tier: Silver 2
  Category: 트리
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

int N, K, a, b, target;
iv1 adj[110000];
int depth[110000];

void dfs(int node, int d) {
  depth[node] = d;

  for(int child : adj[node]) {
    if (depth[child] >= 0) continue;

    dfs(child, d + 1);
  }
}

int main() {
  ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);

  cin >> N >> K;

  fill(depth, depth + N, -1);

  for1(0, N - 1) {
    cin >> a >> b;

    adj[a].push_back(b);
    adj[b].push_back(a);
  }

  for1(0, N) {
    cin >> a;
    if (a == K) target = i;
  }

  dfs(0, 0);

  cout << depth[target];
}

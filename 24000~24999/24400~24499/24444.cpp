/*
  [24444: 알고리즘 수업 - 너비 우선 탐색 1](https://www.acmicpc.net/problem/24444)

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

ll N, M, R, a, b;
vector<ll> adj[110000];
ll chk[110000];
ll cnt = 1;

int main() {
  ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);

  cin >> N >> M >> R;

  for1(0, M) {
    cin >> a >> b;
    adj[a].push_back(b);
    adj[b].push_back(a);
  }

  for1(0, N+1) {
    sort(adj[i].begin(), adj[i].end());
  }

  queue <ll> Q;
  Q.push(R);

  while(!Q.empty()) {
    ll here = Q.front(); Q.pop();
    if(chk[here]) continue;

    chk[here] = cnt++;

    for(ll there : adj[here]) {
      if(chk[there]) continue;
      Q.push(there);
    }
  }

  for1(1, N + 1) {
    cout << chk[i] << "\n";
  }
}

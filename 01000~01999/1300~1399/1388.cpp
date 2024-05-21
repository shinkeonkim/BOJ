/*
  [1388: 바닥 장식](https://www.acmicpc.net/problem/1388)

  Tier: Silver 3
  Category: Graph Traversal
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

ll N, M, cnt;
string ar[55];
bool chk[55][55];

int main() {
  ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);

  cin >> N >> M;

  for1(0, N) {
    cin >> ar[i];
  }

  for1(0, N) {
    for1j(0, M) {
      if(!chk[i][j]) {
        if(ar[i][j] == '-') {
          cnt++;
          for(int k = j; k < M; k++) {
            if(ar[i][k] != '-') break;
            chk[i][k] = true;
          }
        }

        if(ar[i][j] == '|') {
          cnt++;
          for(int k = i; k < N; k++) {
            if(ar[k][j] != '|') break;
            chk[k][j] = true;
          }
        }
      }
    }
  }

  cout << cnt;
}

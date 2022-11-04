/*
  [17204: 죽음의 게임](https://www.acmicpc.net/problem/17204)

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

int N, K;
int nxt[177];
int num[177];

int main() {
  ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);

  cin >> N >> K;

  for1(0, N) {
    cin >> nxt[i];
  }

  fill(num, num + 170, -1);

  int crt = 0;
  int cnt = 0;

  for1(0, N) {
    if(num[crt] > -1) break;
    num[crt] = cnt++;

    crt = nxt[crt];
  }

  cout << num[K];
}

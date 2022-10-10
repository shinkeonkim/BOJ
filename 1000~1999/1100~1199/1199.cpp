/*
  [1199: 오일러 회로](https://www.acmicpc.net/problem/1199)

  Tier: Platinum 4
  Category: 오일러 회로
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

int N;
// llv1 adj[1100];
int weight[1100][1100];
int degree[1100];
int nxt[1100];

struct EulerCurcuit {
  void init() {
    for (int i = 0; i < N; i++) nxt[i] = 0;

    for(int i = 0; i < N; i++) {
      for(int j = 0; j < N; j++) {
        degree[i] += weight[i][j];
        degree[j] += weight[i][j];
      }
    }

    for(int i = 0; i < N; i++) degree[i] /= 2;
  }

  int getStart() {
    for(int i = 0; i < N; i++) {
      if(degree[i] % 2) {
        return -1;
      }
    }
    return 0;
  }

  void getEulerCurcuit (int here) {
    for(int &there=nxt[here]; there<=N; there++) {
      while(weight[here][there] > 0) {
        weight[here][there]--;
        weight[there][here]--;

        getEulerCurcuit(there);
      }
    }

    cout << here + 1 << " ";
  }

  void perform() {
    int start = getStart();

    if(start == -1) {
      cout << -1;
    } else {
      getEulerCurcuit(getStart());
    }
  }
};

EulerCurcuit ec;

int main() {
  ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);

  cin >> N;

  for1(0, N) {
    for1j(0, N) {
      cin >> weight[i][j];
    }
  }

  ec.init();
  ec.perform();
}

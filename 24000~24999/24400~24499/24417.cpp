/*
  [24417: 알고리즘 수업 - 피보나치 수 2](https://www.acmicpc.net/problem/24417)

  Tier: Silver 4
  Category: DP
*/
#include <bits/stdc++.h>

#define for1(s,n) for(int i = s; i < n; i++)
#define for1j(s,n) for(int j = s; j < n; j++)
#define foreach(k) for(auto i : k)
#define foreachj(k) for(auto j : k)
#define pb(a) push_back(a)
#define sz(a) a.size()
#define MOD 1000000007

using namespace std;
typedef unsigned long long ull;
typedef long long ll;
typedef vector <int> iv1;
typedef vector <vector<int> > iv2;
typedef vector <ll> llv1;
typedef unsigned int uint;
typedef vector <ull> ullv1;
typedef vector <vector <ull> > ullv2;

ll N;
ll a, b, c;

int main() {
  ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);

  cin >> N;

  a = 1;
  b = 1;

  for(int i = 3; i <= N; i++) {
    c = (a + b) % MOD;
    a = b;
    b = c;
  }

  cout << c << " " << N - 2;
}

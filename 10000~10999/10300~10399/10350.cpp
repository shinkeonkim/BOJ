/*
  [10350: 은행](https://www.acmicpc.net/problem/10350)

  Tier: Ruby 5
  Category: 수학
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

ll N;
ll ans;
double total;
ll ar[22000];
ll sm[22000];

int main() {
  ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);

  cin >> N;
  for1(1, N+1) {
    cin >> ar[i];
    sm[i] = sm[i - 1] + ar[i];
    total += ar[i];
  }

  for1(0, N+1) {
    for1j(i, N+1) {
      double e_sum = sm[j] - sm[i];
      if (e_sum < 0) ans += abs(ceil(-e_sum / total));

      if(i != 0 && j != N) {
        e_sum = total - e_sum;
        if (e_sum < 0) ans += abs(ceil(-e_sum / total));
      }

    }
  }

  cout << ans;
}

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


struct FenwickTree {
  vector <ll> tree;

  void init(int size) {
    tree.resize(size);
  }

  void update(int idx, ll diff) {
    while(idx < tree.size()) {
      tree[idx] += diff;

      idx += (idx & -idx);
    }
  }

  ll query(int idx) {
    ll ans = 0;

    while(idx > 0) {
      ans += tree[idx];
      idx -= (idx & -idx);
    }

    return ans;
  }
};

FenwickTree fwt;
vector <ll> ar = {0};

int main() {
  ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);

  int N, M, K; // N: 수의 개수, M: 변경이 일어나는 횟수, K: 쿼리 개수
  ll a, b, c;

  cin >> N >> M >> K;

  fwt.init(2* N);

  for1(1, N+1) {
    cin >> a;
    ar.push_back(a);
    fwt.update(i, a);
  }

  for1(0, M + K) {
    cin >> a >> b >> c;

    if(a == 1) {
      fwt.update(b, c - ar[b]);
      ar[b] = c;
    } else {
      cout << fwt.query(c) - fwt.query(b - 1) << "\n";
    }
  }
}

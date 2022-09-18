#include <bits/stdc++.h>

#define for1(s,n) for(int i = s; i < n; i++)
#define for1j(s,n) for(int j = s; j < n; j++)
#define foreach(k) for(auto i : k)
#define foreachj(k) for(auto j : k)
#define pb(a) push_back(a)
#define sz(a) a.size()
#define INF (ll)1e18

using namespace std;
typedef unsigned long long ull;
typedef long long ll;
typedef vector <int> iv1;
typedef vector <vector<int> > iv2;
typedef vector <ll> llv1;
typedef unsigned int uint;
typedef vector <ull> ullv1;
typedef vector <vector <ull> > ullv2;

ll tree[1 << 21];
ll sz = 1 << 20;

struct SegmentTree {
  void update(int node, ll amount) {
    node |= sz;
    tree[node] = amount;

    while(node >>= 1) {
      tree[node] = min(tree[node << 1], tree[node << 1 | 1]);
    }
  }

  ll query(int left, int right) {
    left |= sz;
    right |= sz;

    ll ret = INF;

    while(left <= right) {
      if (left & 1) ret = min(tree[left++], ret);
      if (~right & 1) ret = min(tree[right--], ret);

      left >>= 1;
      right >>= 1;
    }

    return ret;
  }
};


int main() {
  ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);

  SegmentTree sgt;

  ll N, M, a, b, c;

  cin >> N;

  for1(0, N) {
    cin >> a;
    sgt.update(i+1, a);
  }

  cin >> M;

  for1(0, M) {
    cin >> a >> b >> c;

    if (a == 1) {
      // b번째 수를 c로 바꾼다.
      sgt.update(b, c);
    }

    if (a == 2) {
      // b번째부터 c번째 수까지의 합을 구한다.
      cout << sgt.query(b, c) << "\n";
    }
  }

}

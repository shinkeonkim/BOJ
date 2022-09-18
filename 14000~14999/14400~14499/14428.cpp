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

ll ar[110000];
ll tree[1 << 21];
ll sz = 1 << 20;

struct SegmentTree {
  void update(int node, ll idx) {
    node |= sz;
    tree[node] = idx;

    while(node >>= 1) {
      ll left_idx = tree[node << 1];
      ll right_idx = tree[node << 1 | 1];
      ll left = ar[left_idx];
      ll right = ar[right_idx];

      if (left < right) {
        tree[node] = left_idx;
      } else if (left == right) {
        if (left_idx < right_idx) {
          tree[node] = left_idx;
        } else {
          tree[node] = right_idx;
        }
      } else {
        tree[node] = right_idx;
      }
    }
  }

  ll query(int left, int right) {
    left |= sz;
    right |= sz;

    ll ret = 0;

    while(left <= right) {
      if (left & 1) {
        if(ar[ret] > ar[tree[left]]) {
          ret = tree[left];
        } else if(ar[ret] == ar[tree[left]]) {
          ret = min(ret, tree[left]);
        }

        left++;
      }
      if (~right & 1) {
        if(ar[ret] > ar[tree[right]]) {
          ret = tree[right];
        } else if(ar[ret] == ar[tree[right]]) {
          ret = min(ret, tree[right]);
        }
        right--;
      }

      left >>= 1;
      right >>= 1;
    }

    return ret;
  }
};


int main() {
  ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);

  SegmentTree sgt;

  ll N; // 수열의 크기
  ll M; // 쿼리의 개수
  ll a, b, c; // 쿼리 입력

  cin >> N;
  fill(ar, ar+N+1, INF);

  for1(1, N+1) {
    cin >> ar[i];
    sgt.update(i, i);
  }

  cin >> M;

  for1(0, M) {
    cin >> a >> b >> c;

    if (a == 1) {
      ar[b] = c;
      sgt.update(b, b);
    }

    if (a == 2) {
      cout << sgt.query(b, c) << "\n";
    }
  }
}

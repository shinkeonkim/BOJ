#include <bits/stdc++.h>

#define for1(s, n) for (int i = s; i < n; i++)
#define for1j(s, n) for (int j = s; j < n; j++)
#define foreach(k) for (auto i : k)
#define foreachj(k) for (auto j : k)
#define pb(a) push_back(a)
#define sz(a) a.size()

using namespace std;
typedef unsigned long long ull;
typedef long long ll;
typedef vector<int> iv1;
typedef vector<vector<int>> iv2;
typedef vector<ll> llv1;
typedef unsigned int uint;
typedef vector<ull> ullv1;
typedef vector<vector<ull>> ullv2;

struct SegmentTree
{
  int tree[1 << 18];
  int sz = 1 << 17;

  void update(int node, int amount)
  {
    /* node에 amount만큼 더한다. */
    cout << "node: " << node;
    node |= sz;
    cout << " " << node << "\n";
    tree[node] += amount;

    while (node >>= 1)
    {
      tree[node] = tree[node << 1] + tree[node << 1 | 1];
    }
  }

  int query(int left, int right)
  {
    left |= sz;
    right |= sz;

    int ret = 0;

    while (left <= right)
    {
      // 이해가 안감.
      if (left & 1)
        ret += tree[left++];
      if (~right & 1)
        ret += tree[right--];

      left >>= 1;
      right >>= 1;
    }

    return ret;
  }
};

int main()
{
  ios::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);

  SegmentTree sgt;
}

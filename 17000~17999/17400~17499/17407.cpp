/*
[17407: 괄호 문자열과 쿼리](https://www.acmicpc.net/problem/17407)

Tier: Platinum 3 
Category: data_structures, lazyprop, segtree
*/


#include <bits/stdc++.h>

using namespace std;

#define for1(s, e) for(int i = s; i < e; i++)
#define for1j(s, e) for(int j = s; j < e; j++)
#define forEach(k) for(auto i : k)
#define forEachj(k) for(auto j : k)
#define sz(vct) vct.size()
#define all(vct) vct.begin(), vct.end()
#define uniq(vct) sort(all(vct));vct.erase(unique(all(vct)), vct.end())
#define fi first
#define se second

typedef unsigned long long ull;
typedef long long ll;
typedef unsigned int uint;

typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<double, double> pdd;
typedef pair<double, int> pdi;
typedef pair<string, string> pss;

typedef vector<ll> llv1;


const double EPS = 1e-8;
const double PI = acos(-1);

template<typename T>
T sq(T x) { return x * x; }

int sign(ll x) { return x < 0 ? -1 : x > 0 ? 1 : 0; }
int sign(int x) { return x < 0 ? -1 : x > 0 ? 1 : 0; }
int sign(double x) { return abs(x) < EPS ? 0 : x < 0 ? -1 : 1; }

int isMinusCount = 0;
int ar[110000];
int n;
string s;

struct SegTree {
  ll tree [1 << 18];
  int sz = 1 << 17;

  void update(int i, ll v) {
    i |= sz;
    tree[i] += v;
    while(i >>= 1) {
      // bool isMinus = tree[i] < 0;
      tree[i] = tree[i << 1] + tree[i << 1 | 1];

      // bool afterMinus = tree[i] < 0;

      // if ((i << 1) != (i << 1 | 1) && isMinus != afterMinus) {
      //   if(isMinus) isMinusCount--;
      //   else isMinusCount++;
      // }
    }
  }

  ll query(int left, int right) {
    left |= sz;
    right | sz;

    int ret = 0;
    while(left <= right) {
      if(left & 1) ret += tree[left++];
      if(~right & 1) ret += tree[right--];
      left >>= 1;
      right >>= 1;
    }

    return ret;
  }
};

void solve() {
  cin >> s;

  SegTree seg;

  n = s.length();
  for1(0, n) {
    ar[i] = s[i] == '(' ? 1 : -1;

    seg.update(i + 1, ar[i]);
  }

  cout << isMinusCount << endl;


}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}
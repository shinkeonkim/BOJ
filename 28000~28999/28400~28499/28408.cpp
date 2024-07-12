/*
[28408: 나무늘보](https://www.acmicpc.net/problem/28408)

Tier: Gold 1 
Category: math, recursion, trees

문제
 
$N$개의 정점으로 구성된 이진트리에 거주하고 있는 나무늘보가 있다. 각 정점에는 
$1$부터 
$N$까지 번호가 적혀 있다.

나무늘보는 현재 거주지를 신고하기 위해 거주하고 있는 이진트리의 전위, 후위 순회 결과를 적어 두었다. 이진트리의 전위, 후위 순회의 정의는 아래와 같다.

전위 순회: 현재 정점을 방문한 후 왼쪽, 오른쪽 순서로 서브 트리를 전위 순회한다.
후위 순회: 왼쪽, 오른쪽 순서로 서브 트리를 후위 순회한 후 현재 정점을 방문한다.
나무늘보는 적어 둔 전위, 후위 순회 결과로 이루어진 이진트리가 여러 개 존재할 수도 있고, 결과를 잘못 적어서 이진트리가 존재하지 않을 수도 있다는 사실을 알게 되었다.

당신은 나무늘보가 적어 둔 전위, 후위 순회 결과가 주어졌을 때 동일한 순회 결과를 가지는 이진트리의 개수를 알아내야 한다.

입력
첫 번째 줄에 이진트리의 정점 개수 
$N (1 \le N \le 500\,000)$이 주어진다.

두 번째 줄에는 전위 순회 결과를 나타내는 정수 
$N$개가 공백으로 구분되어 주어진다.

세 번째 줄에는 후위 순회 결과를 나타내는 정수 
$N$개가 공백으로 구분되어 주어진다.

입력으로 들어오는 전위, 후위 순회 결과는 
$1$부터 
$N$까지의 정수가 중복 없이 배치된 순열이다.

출력
문제의 답을 
$998\, 244\, 353$으로 나눈 나머지를 한 줄에 출력한다.


*/


#include <bits/stdc++.h>

using namespace std;

#define for1(s, e) for(int i = s; i < e; i++)
#define for1j(s, e) for(int j = s; j < e; j++)
#define forEach(k) for(auto i : k)
#define forEachj(k) for(auto j : k)
#define sz(vct) vct.size()
#define all(vct) vct.begin(), vct.end()
#define sortv(vct) sort(vct.begin(), vct.end())
#define uniq(vct) sort(all(vct));vct.erase(unique(all(vct)), vct.end())
#define fi first
#define se second
#define INF (1ll << 60ll)

typedef unsigned long long ull;
typedef long long ll;
typedef ll llint;
typedef unsigned int uint;
typedef unsigned long long int ull;
typedef ull ullint;

typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<double, double> pdd;
typedef pair<double, int> pdi;
typedef pair<string, string> pss;

typedef vector<int> iv1;
typedef vector<iv1> iv2;
typedef vector<ll> llv1;
typedef vector<llv1> llv2;

typedef vector<pii> piiv1;
typedef vector<piiv1> piiv2;
typedef vector<pll> pllv1;
typedef vector<pllv1> pllv2;
typedef vector<pdd> pddv1;
typedef vector<pddv1> pddv2;

const double EPS = 1e-8;
const double PI = acos(-1);

template<typename T>
T sq(T x) { return x * x; }

int sign(ll x) { return x < 0 ? -1 : x > 0 ? 1 : 0; }
int sign(int x) { return x < 0 ? -1 : x > 0 ? 1 : 0; }
int sign(double x) { return abs(x) < EPS ? 0 : x < 0 ? -1 : 1; }

ll n;
llv1 pre_order;
llv1 post_order;
llv1 pre_order_idx;
llv1 post_order_idx;

ll cnt = 0;
bool wrong_tree_flag = false;

void dfs(ll pre_order_root_idx, ll post_order_root_idx, pll pre_order_range, pll post_order_range) {
  // cout << pre_order_root_idx << " " << post_order_root_idx << " " << pre_order_range.fi << " " << pre_order_range.se << " " << post_order_range.fi << " " << post_order_range.se << endl;

  if(pre_order_range.fi > pre_order_range.se && post_order_range.fi > post_order_range.se) return;
  if(pre_order_range.fi > pre_order_range.se || post_order_range.fi > post_order_range.se) {
    wrong_tree_flag = true;
    return;
  }

  if(pre_order_range.se - pre_order_range.fi != post_order_range.se - post_order_range.fi) {
    wrong_tree_flag = true;
    return;
  }

  if(pre_order[pre_order_root_idx] != post_order[post_order_root_idx]) {
    wrong_tree_flag = true;
    return;
  }

  ll pre_order_child = pre_order[pre_order_range.fi];
  ll post_order_child = post_order[post_order_range.se];

  if(pre_order_child == post_order_child) {
    cnt++;
    dfs(pre_order_range.fi, post_order_range.se, {pre_order_range.fi + 1, pre_order_range.se}, {post_order_range.fi, post_order_range.se - 1});
  } else {
    dfs(pre_order_range.fi, post_order_idx[pre_order_child], {pre_order_range.fi + 1, pre_order_idx[post_order_child] - 1}, {post_order_range.fi, post_order_idx[pre_order_child] - 1});
    dfs(pre_order_idx[post_order_child], post_order_range.se, {pre_order_idx[post_order_child] + 1, pre_order_range.se}, {post_order_idx[pre_order_child] + 1, post_order_range.se - 1});
  }
}


void solve() {
  cin >> n;
  pre_order.resize(n);
  post_order.resize(n);
  pre_order_idx.resize(n + 1);
  post_order_idx.resize(n + 1);

  for1(0, n) cin >> pre_order[i];
  for1(0, n) cin >> post_order[i];

  for1(0, n) {
    pre_order_idx[pre_order[i]] = i;
    post_order_idx[post_order[i]] = i;
  }

  dfs(0, n - 1, {1, n - 1}, {0, n - 2});


  if(wrong_tree_flag) {
    cout << 0;
  } else {
    ll ret = 1;

    for1(0, cnt) {
      ret = (ret * 2) % 998244353;
    }

    cout << ret;
  }
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}
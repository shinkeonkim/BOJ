/*
[12995: 트리나라](https://www.acmicpc.net/problem/12995)

Tier: Platinum 2 
Category: dp, dp_tree, trees
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

#define MOD 1000000007

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

ll N, K;
vector<vector<ll> > adj;
vector<vector<ll> > children;
ll D[51][51][51];

// D[i][j][k]: i가 루트인 서브 노드에서, k개를 고르는 방법의 수, 단 처음 j개의 자식을 스킵함.

void set_children(int here, int prev) {
  for(auto there : adj[here]) {
    if (there == prev) continue;

    children[here].push_back(there);

    set_children(there, here);
  }
}

ll dfs(int root, int skipped, int k) {
  ll &ans = D[root][skipped][k];

  if(ans != -1) return ans;

  if(k == 0) return 1; // 아무것도 선택하지 않는 경우

  if(skipped == children[root].size()) {
    if(k == 1) return 1;
    return 0;
  }

  ans = 0;

  for(int i = 0; i < k; i++) {
    ll t1 = dfs(children[root][skipped], 0, i); // skipped 번째 자식에서 i개를 고르는 경우의 수
    ll t2 = dfs(root, skipped + 1, k - i); // skipped 번째 자식이후의 자식들에서 k - i 개를 고르는 경우의 수

    ans += t1 * t2;
    ans %= MOD;
  }
  return ans;

}

void solve() {
  cin >> N >> K;

  adj.resize(N);
  children.resize(N);

  for1(0, N - 1) {
    ll a, b;

    cin >> a >> b;
    a -= 1;
    b -= 1;

    adj[a].push_back(b);
    adj[b].push_back(a);
  }

  set_children(0, -1);

  memset(D, -1, sizeof(D));

  ll ans = 0;

  for1(0, N) {
    ans += dfs(i, 0, K);
  }

  cout << ans;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}
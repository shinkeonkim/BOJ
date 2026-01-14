/*
[15678: 연세워터파크](https://www.acmicpc.net/problem/15678)

Tier: Platinum 5 
Category: dp, data_structures, segtree, priority_queue, deque, deque_trick, dp_deque
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

llv1 dp;
llv1 ar;

deque <ll> deq;
priority_queue <ll, vector<ll>, less<ll>> pq;
map<ll, ll> deq_pop_cnt;

void sync() {
  while (1) {
    if(pq.empty()) break;
    ll top = pq.top();
    
    if(!deq_pop_cnt.count(top)) break;
    if(deq_pop_cnt[top] == 0) break;
    
    deq_pop_cnt[top]--;
    pq.pop();
  }
}

void pop_deq() {
  ll front = deq.front();
  deq_pop_cnt[front]++;
  deq.pop_front();
}

void solve() {
  ll N, D;

  cin >> N >> D;
  ar.resize(N);
  dp.resize(N);

  for(int i = 0; i < N; i++) {
    cin >> ar[i];
  }

  dp[0] = ar[0];
  pq.push(ar[0]);
  deq.push_back(ar[0]);

  for(int i = 1; i < D; i++) {
    ll prev_max = pq.top();
    dp[i] = max(ar[i], ar[i] + prev_max);
    pq.push(dp[i]);
    deq.push_back(dp[i]);
  }

  for(int i = D; i < N; i++) {
    ll prev_max = pq.top();
    // cout << i << ": " << ar[i] << " " << ar[i] + prev_max << " "<< prev_max << "\n";
    dp[i] = max(ar[i], ar[i] + prev_max);
    pq.push(dp[i]);
    deq.push_back(dp[i]);
    pop_deq();
    sync();
  }

  ll ans = dp[0];

  for(int i = 1; i < N; i++) {
    ans = max(ans, dp[i]);
  }

  cout << ans;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}

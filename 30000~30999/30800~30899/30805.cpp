/*
[30805: 사전 순 최대 공통 부분 수열](https://www.acmicpc.net/problem/30805)

Tier: Gold 4 
Category: greedy
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

void solve() {
  ll N, M, a;
  llv1 A, B;

  queue <ll> ans;

  cin >> N;

  for1(0, N) {
    cin >> a;
    A.push_back(a);
  }

  cin >> M;
  for1(0, M) {
    cin >> a;
    B.push_back(a);
  }

  // 공통적으로 가진 가장 큰 수를 찾는다.
  ll x = -1; // A 배열에서 마지막으로 선택된 idx;
  ll y = -1; // B 배열에서 마지막으로 선택된 idx;
  
  while(1) {
    ll selected = -1;

    priority_queue <pll, vector<pll>, less<pll>> Q_A;
    priority_queue <pll, vector<pll>, less<pll>> Q_B;

    for(int i = x + 1; i < N; i++) {
      Q_A.push({ A[i], -i }); // 더 앞의 것을 선택하기 위해 i를 음수로 전환
    }

    for(int i = y + 1; i < M; i++) {
      Q_B.push({ B[i], -i });
    }

    while(!Q_A.empty() && !Q_B.empty() && selected == -1) {
      pll a = Q_A.top(); Q_A.pop();
      pll b = Q_B.top(); Q_B.pop();

      // cout << a.first << " " << a.second << ", " << b.first << " " << b.second << "\n";

      if(a.first == b.first) {
        x = -a.second;
        y = -b.second;
        selected = a.first;
      } else if(a.first > b.first) {
        Q_B.push(b);
      } else {
        Q_A.push(a);
      }
    }

    if(selected == -1) break;

    ans.push(selected);
    // if(x == N - 1 || y == M - 1) break;
  }

  cout << ans.size() << "\n";

  while(!ans.empty()) {
    cout << ans.front() << " ";
    ans.pop();
  }

}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}
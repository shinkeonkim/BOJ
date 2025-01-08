/*
[2014: 소수의 곱](https://www.acmicpc.net/problem/2014)

Tier: Gold 1 
Category: data_structures, math, number_theory, priority_queue

소수의 곱

문제
K개의 소수가 있다. 이때, 이 소수들 중에서 몇 개를 곱해서 얻게 되는 수들이 있을 것이다. 소수들을 선택할 때에는 같은 수를 선택해도 되며, 주어지는 소수 자체도 포함시키자.

예를 들어 세 소수가 2, 5, 7이었다면, 이러한 곱들을 오름차순으로 나타내 보면, 2, 4, 5, 7, 8, 10, 14, 16, 20, 25, 28, 32, 35, 등이 된다.

K개의 소수가 주어졌을 때, 이러한 소수의 곱들 중에서 N번째 수를 구해 보자. 단 정답은 231보다 작은 자연수이다.

입력
첫째 줄에 K(1 ≤ K ≤ 100), N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 K개의 소수가 오름차순으로 주어진다. 같은 소수가 여러 번 주어지는 경우는 없으며, 주어지는 소수는 모두 541보다 작거나 같은 자연수이다.

출력
첫째 줄에 문제에서 설명한 대로 소수의 곱을 나열했을 때, N번째 오는 것을 출력한다.

예제 입력 1 
4 19
2 3 5 7
예제 출력 1 
27
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

void solve() {
  int K, N;
  
  cin >> K >> N;

  iv1 primes(K);
  for1(0, K) cin >> primes[i];

  priority_queue<ll, vector<ll>, greater<ll>> pq;

  for1(0, K) pq.push(primes[i]);

  ll ans = 0;
  for1(0, N) {
    ans = pq.top();
    pq.pop();

    for1(0, K) {
      ll next = ans * primes[i];
      pq.push(next);

      if(ans % primes[i] == 0) break;
    }
  }

  cout << ans << '\n';
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}
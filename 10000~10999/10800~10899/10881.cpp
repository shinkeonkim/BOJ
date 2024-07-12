/*
[10881: 프로도의 선물 포장](https://www.acmicpc.net/problem/10881)

Tier: Gold 4 
Category: bruteforcing, implementation

문제
프로도는 네오에게 줄 생일 선물을 세 개 샀다. 이 세 개의 선물은 직사각형 모양의 선물 상자에 각각 하나씩 담겨 있다. 프로도는 이 선물들을 적당한 크기의 직사각형 포장 상자에 넣어 포장하려 한다. 큰 포장 상자를 주문할수록 돈을 더 많이 써야 하기 때문에, 프로도는 최대한 작은 상자에 세 개의 선물을 모두 담으려고 한다.

사용하게 될 포장 상자의 크기는 선물 상자의 배치 방법에 따라 달라질 수 있다. 이때, 선물들이 안전하게 포장되기 위해서는 각 변이 상자의 가로와 세로에 평행하게 해야 하고, 선물 상자 전체가 포장 상자 안에 담겨 있어야 한다. 선물 상자가 포장 상자의 경계에 접하는 것은 허용되며, 선물 상자는 90도 단위로 회전 가능하다.

예를 들어, 선물 상자들의 크기 (가로×세로)가 각각 3×4, 5×6, 4×1인 선물 상자들을 아래와 같이 포장하면 사용할 포장 상자의 크기는 8 × 8 = 64이 된다.

하지만 아래와 같이 포장할 경우, 사용할 포장 상자의 크기는 5 × 10 = 50이 된다.

구매한 선물 상자들의 크기가 주어졌을 때, 선물들을 안전하게 포장하는 데 필요한 포장 상자의 최소 크기 (즉, 포장 상자의 넓이가 최소가 되는 경우)를 구하시오.

입력
첫 번째 줄에 테스트 케이스의 수 T (1 ≤ T ≤ 10,000)가 주어진다.

각 테스트 케이스마다 세 개의 줄에 각각 선물의 가로와 세로를 뜻하는 두 개의 정수 A, B (1 ≤ A, B ≤ 50)가 공백을 사이에 두고 주어진다.

출력
각 테스트 케이스에 대해 한 줄에 하나씩 선물을 모두 안전하게 포장하기 위해 필요한 포장 상자의 최소 크기를 출력한다.
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
  pllv1 v;

  for1(0, 3) {
    ll a, b; cin >> a >> b;
    v.push_back({a, b});
  } 

  ll ans = INF;

  for1(0, 2) {
    for1j(0, 2) {
      for(int k = 0; k < 2; k++) {
        for(int x = 0; x < 3; x++) {
          ll y = (x + 1) % 3;
          ll z = (x + 2) % 3;
        
          ll a = max(v[x].fi, v[y].fi + v[z].fi);
          ll b = v[x].se + max(v[y].se, v[z].se);
          ans = min(ans, a * b);

          ll c = v[x].fi + v[y].fi + v[z].fi;
          ll d = max(v[x].se, max(v[y].se, v[z].se));

          ans = min(ans, c * d);
        }

        swap(v[2].fi, v[2].se);
      }
      swap(v[1].fi, v[1].se); 
    }
    swap(v[0].fi, v[0].se);
  }

  cout << ans << "\n";
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; cin >> tc;
  while(tc--) solve();
  
}
/*
[28279: 덱 2](https://www.acmicpc.net/problem/28279)

Tier: Silver 4 
Category: data_structures, deque
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

deque<int> dq;

void solve() {
  ll N;

  cin >> N;

  while(N--) {
    int command, a;

    cin >> command;

    switch(command) {
      case 1:
        cin >> a;
        dq.push_front(a);
        break;
      case 2:
        cin >> a;
        dq.push_back(a);
        break;
      case 3:
        if(!dq.empty()) {
          cout << dq.front() << "\n";
          dq.pop_front();
        } else {
          cout << "-1\n";
        }
        break;
      case 4:
        if(!dq.empty()) {
          cout << dq.back() << "\n";
          dq.pop_back();
        } else {
          cout << "-1\n";
        }
        break;
      case 5:
        cout << dq.size() << "\n";
        break;
      case 6:
        cout << (int)dq.empty() << "\n";
        break;
      case 7:
        if(!dq.empty()) {
          cout << dq.front() << "\n";
        } else {
          cout << "-1\n";
        }
        break;
      case 8:
        if(!dq.empty()) {
          cout << dq.back() << "\n";
        } else {
          cout << "-1\n";
        }
        break;
    }
  }

}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}
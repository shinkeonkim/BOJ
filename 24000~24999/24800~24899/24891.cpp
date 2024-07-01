/*
[24891: 단어 마방진](https://www.acmicpc.net/problem/24891)

Tier: Gold 5 
Category: backtracking, bruteforcing
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

typedef vector<int> iv1;
typedef vector<ll> llv1;


const double EPS = 1e-8;
const double PI = acos(-1);

template<typename T>
T sq(T x) { return x * x; }

int sign(ll x) { return x < 0 ? -1 : x > 0 ? 1 : 0; }
int sign(int x) { return x < 0 ? -1 : x > 0 ? 1 : 0; }
int sign(double x) { return abs(x) < EPS ? 0 : x < 0 ? -1 : 1; }

int L, N;
vector <string> ar;
iv1 selected_idx;
iv1 ans;
vector<bool> used;

void chk() {
  if(ans[0] != -1) return;

  for1(0, L) { // 단어
    for1j(0, L) { // 단어 내의 문자
      char a = ar[selected_idx[i]][j];
      char b = ar[selected_idx[j]][i];

      if(a != b) return;
    }
  }

  for1(0, L) {
    ans[i] = selected_idx[i];
  }

}

void dfs(int count, int idx) {
  if (ans[0] != -1) return;

  selected_idx[count] = idx;


  if (count == L - 1) {
    chk();
    return;
  }

  char tmp = ar[selected_idx[0]][count + 1];

  for(int there = 0; there < N; there++) {
    if(used[there]) continue;
    if(ar[there][0] != tmp) continue;
    used[there] = true;
    dfs(count + 1, there);
    used[there] = false;
  }
}


void solve() {
  cin >> L >> N;
  ar.resize(N);
  used.resize(N);

  selected_idx.resize(L, -1);
  ans.resize(L, -1);

  for1(0, N) {
    cin >> ar[i];
  }

  sort(ar.begin(), ar.end());

  for1(0, N) {
    used[i] = true;
    dfs(0, i);
    used[i] = false;
  }

  if(ans[0] == -1) {
    cout << "NONE";
  } else {
    for1(0, L) {
      cout << ar[ans[i]] << "\n";
    }
  }
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}
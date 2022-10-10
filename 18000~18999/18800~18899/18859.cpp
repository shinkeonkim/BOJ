/*
  [1859: 부모님께 큰절 하고](https://www.acmicpc.net/problem/)

  Tier: Platinum 4
  Category: 그리디 알고리즘
*/

#include <bits/stdc++.h>

#define for1(s,n) for(int i = s; i < n; i++)
#define for1j(s,n) for(int j = s; j < n; j++)
#define foreach(k) for(auto i : k)
#define foreachj(k) for(auto j : k)
#define pb(a) push_back(a)
#define sz(a) a.size()

using namespace std;
typedef unsigned long long ull;
typedef long long ll;
typedef vector <int> iv1;
typedef vector <vector<int> > iv2;
typedef vector <ll> llv1;
typedef unsigned int uint;
typedef vector <ull> ullv1;
typedef vector <vector <ull> > ullv2;

ll N;
ll ar[440000];

llv1 a, b, c;
bool chk_a[440000];

bool solution() {
  sort(ar, ar + N);

  ll start = ar[0];
  ll diff_a = ar[1] - start;

  if(diff_a == 0) {
    return false;
  }
  chk_a[1] = true;
  a.push_back(ar[1]);

  for1(1, N) {
    if (chk_a[i]) continue;

    if (ar[i] - a.back() == diff_a) {
      a.push_back(ar[i]);
      chk_a[i] = true;
    } else {
      b.push_back(ar[i]);
    }
  }

  if(b.size() <= 1) {
    return true;
  }

  ll diff_b = b[0] - start;

  if(diff_b > 0) {
    bool chk = true;
    for1(1, b.size()) {
      if(b[i] - b[i-1] != diff_b) {
        if (b[i] - a.back() == a.back() - b[i-1] and b[i] - b[i-1] == 2 * diff_b) {
          continue;
        }
        chk = false;
      }
    }

    if(chk) return true;
  }


  diff_b = b[b.size() - 1] - b[b.size() - 2];

  if(diff_b > 0) {
    bool chk = true;
    for(auto i : a) {
      c.push_back(i);
    }

    for(int i = b.size() - 1; i > 0; i--) {
      if(b[i] - b[i-1] != diff_b) {
        if (b[i] - c.back() == c.back() - b[i-1] and b[i] - b[i-1] == 2 * diff_b) {
          c.pop_back();
          continue;
        }
        chk = false;
      }
    }

    if(b[0] - start != diff_b) {
      if (b[0] - c.back() != c.back() - start or b[0] - start != 2 * diff_b) {
        chk = false;
      }
    }

    if(chk) return true;
  }

  diff_b = b[b.size() - 1] - a.back();

  if(diff_b > 0) {
    bool chk = true;
    for(auto i : a) {
      c.push_back(i);
    }
    c.pop_back();

    for(int i = b.size() - 1; i > 0; i--) {
      if(b[i] - b[i-1] != diff_b) {
        if (b[i] - c.back() == c.back() - b[i-1] and b[i] - b[i-1] == 2 * diff_b) {
          c.pop_back();
          continue;
        }
        chk = false;
      }
    }

    if(b[0] - start != diff_b) {
      if (b[0] - c.back() != c.back() - start or b[0] - start != 2 * diff_b) {
        chk = false;
      }
    }

    if(chk) return true;
  }

  return false;
}


int main() {
  ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);

  cin >> N;

  for1(0, N) {
    cin >> ar[i];
  }

  cout << (solution() ? "Yes" : "No");
}

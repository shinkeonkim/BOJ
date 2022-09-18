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
string s;

int main() {
  ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);

  cin >> N;

  for1(1, N+1) {
    cin >> s;
    vector<int> v;
    for1j(0, s.length()) v.push_back(j);

    cout << "Case # " << i << ":\n";

    cout << s << "\n";
    while(next_permutation(v.begin(), v.end())) {
      for1j(0, s.length()) {
        cout << s[v[j]];
      }
      cout << "\n";
    }
  }
}

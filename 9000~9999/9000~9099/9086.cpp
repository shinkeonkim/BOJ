/*
  [9086: 문자열](https://www.acmicpc.net/problem/9086)

  Tier: Bronze 5
  Category: 구현
*/
#include <bits/stdc++.h>

using namespace std;
int T;
string s;

int main() {
  ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);

  cin >> T;
  while(T--) {
    cin >> s;

    cout << s.front() << s.back() << "\n";
  }
}

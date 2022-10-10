/*
  [25640: MBTI](https://www.acmicpc.net/problem/25640)

  Tier: Bronze 4
  Category: 문자열, 구현
*/
#include <bits/stdc++.h>

using namespace std;
string s, s2;
int N, ans;

int main() {
  ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);

  cin >> s >> N;

  while(N--) {
    cin >> s2;

    if(s == s2) ans++;
  }

  cout << ans;
}

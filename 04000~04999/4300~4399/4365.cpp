/*
[4365: Stack 'em Up](https://www.acmicpc.net/problem/4365)

Tier: Bronze 1 
Category: implementation, string
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

iv2 shuffles;

void print(const iv1 &deck) {
  for (auto idx = 1; idx < deck.size(); ++idx) {
    int i = deck[idx];
    int k = i - 1;

    if (k % 13 == 12) {
      cout << "Ace";
    } else if (k % 13 == 9) {
      cout << "Jack";
    } else if (k % 13 == 10) {
      cout << "Queen";
    } else if (k % 13 == 11) {
      cout << "King";
    } else {
      cout << k % 13 + 2;
    }

    cout << " of ";

    if(k / 13 == 0) {
      cout << "Clubs";
    } else if (k / 13 == 1) {
      cout << "Diamonds";
    } else if (k / 13 == 2) {
      cout << "Hearts";
    } else {
      cout << "Spades";
    }
    cout << "\n";
  }
  cout << "\n";
}

void solve() {
  ll n;

  cin >> n;
  shuffles.resize(n + 1);

  iv1 deck(53);
  for1(1, 53) {
    deck[i] = i;
  }

  for1(1, n + 1) {
    shuffles[i].push_back(0);
    for1j(0, 52) {
      int x;
      cin >> x;
      shuffles[i].push_back(x);
    }
  }

  int k;
  while (cin >> k) {
    iv1 newDeck(53);

    for1(1, 53) {
      newDeck[i] = deck[shuffles[k][i]];

      // newDeck[shuffles[k][i]] = deck[i];
    }

    deck = newDeck;

    print(deck);
  }
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}

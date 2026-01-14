/*
[4195: 친구 네트워크](https://www.acmicpc.net/problem/4195)

Tier: Gold 2 
Category: data_structures, set, hash_set, disjoint_set
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

llv1 groups;
llv1 counts;
map <string, int> hashing;

ll find(ll node) {
  if(groups[node] == node) return node;
  return groups[node] = find(groups[node]);
}

void merge(ll a, ll b) {
  a = find(a);
  b = find(b);

  if (a == b) return;

  if (a > b) swap(a, b);

  groups[b] = a;
  counts[a] += counts[b];
}

void solve() {
  groups.clear();
  counts.clear();
  hashing.clear();

  groups.resize(1000000, 0);

  for1(0, 1000000) {
    groups[i] = i;
  }
  counts.resize(1000000, 1);

  int current_index = 1;

  ll N;

  cin >> N; 

  for1(0, N) {
    string a, b;

    cin >> a >> b;

    int id_a, id_b;
  
    if(hashing.find(a) != hashing.end()) {
      id_a = hashing[a];
    } else {
      hashing[a] = current_index;
      id_a = current_index;
      current_index++;
    }

    if(hashing.find(b) != hashing.end()) {
      id_b = hashing[b];
    } else {
      hashing[b] = current_index;
      id_b = current_index;
      current_index++;
    }

    merge(id_a, id_b);
    cout << counts[find(id_a)] << "\n";
  }
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; cin >> tc;
  while(tc--) solve();
  
}

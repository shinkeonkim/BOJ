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
#define DEBUG 0

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

class SqrtSumDecomposition {
public:
  vector<ll> arr, buckets;
  ll n, bucketSize;

  int bucketIndex(int idx) {
    return idx / bucketSize;
  }

  SqrtSumDecomposition(const vector<ll>& input) {
    n = input.size();
    bucketSize = sqrt(n) + 1;
  
    arr.resize(n);
    buckets.resize(bucketSize + 1, 0);

    for1(0, n) {
      arr[i] = input[i];
      buckets[bucketIndex(i)] += arr[i];
    }
  }

  void update(int idx, ll value) {
    buckets[bucketIndex(idx)] += value - arr[idx];
    arr[idx] = value;
  }

  ll query(ll l, ll r) {
    ll sum = 0;
    int startBucket = bucketIndex(l);
    int endBucket = bucketIndex(r);

    if(startBucket == endBucket) {
      for1(l, r + 1) {
        sum += arr[i];
      }
    } else {
      for1(l, (startBucket + 1) * bucketSize) {
        sum += arr[i];
      }
      for1(startBucket + 1, endBucket) {
        sum += buckets[i];
      }
      for1(endBucket * bucketSize, r + 1) {
        sum += arr[i];
      }
    }

    return sum;
  }
};


void solve() {
  ll n, q1, q2;
  llv1 arr;

  cin >> n >> q1 >> q2;

  arr.resize(n);
  for1(0, n) {
    cin >> arr[i];
  }

  SqrtSumDecomposition sd(arr);

  ll q = q1 + q2;
  while(q--) {
    ll type, a, b;

    cin >> type;

    if(type == 1) {
      cin >> a >> b;
      sd.update(a - 1, b);
    } else {
      cin >> a >> b;
      a--; b--;
      cout << sd.query(a, b) << "\n";
    }
  }
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
}

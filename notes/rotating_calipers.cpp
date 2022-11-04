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

struct Point {
  ll x, y;
  ll p = 0;
  ll q = 0;
};

ll dist(Point a, Point b) {
  return (a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y);
}

ll ccw(Point p1, Point p2, Point p3) {
  return (p1.x * p2.y + p2.x * p3.y + p3.x * p1.y - p2.x * p1.y - p3.x * p2.y - p1.x * p3.y);
}

bool comp1(Point a, Point b) {
  if(a.y != b.y) return a.y < b.y;
  return a.x < b.x;
}

bool comp2 (Point a, Point b) {
  if(a.q * b.p != a.p*b.q)
    return a.q * b.p < a.p*b.q;
  return comp1(a,b);
}

struct RotatingCalipers {
  ll N;
  vector <Point> points;
  stack <int> stk;
  vector <int> ch_idx; // convex_hull point idxs
  pair <Point, Point> farest_points;

  RotatingCalipers() {
    points.clear();
    while(!stk.empty()) stk.pop();
    ch_idx.clear();
  }

  void add_point(int x, int y) {
    points.push_back({x, y});
  }

  void graham_scan() {
    sort(points.begin(), points.end(), comp1);

    for(int i = 1; i < N; i++) {
      points[i].p = points[i].x - points[0].x;
      points[i].q = points[i].y - points[0].y;
    }
    sort(points.begin() + 1, points.end(), comp2);

    stk.push(0);
    stk.push(1);

    int nxt = 2;
    while(nxt < points.size()) {
      while(stk.size() >= 2) {
        int second = stk.top();
        stk.pop();
        int first = stk.top();

        if(ccw(points[first], points[second], points[nxt]) > 0) {
          stk.push(second);
          break;
        }
      }
      stk.push(nxt++);
    }

    while(!stk.empty()) {
      ch_idx.push_back(stk.top());
      stk.pop();
    }
    reverse(ch_idx.begin(), ch_idx.end());
  }

  ll perform() {
    graham_scan();

    int j = 1;
    ll ans = 0;
    ll sz = ch_idx.size();

    for(int i = 0; i < sz; i++) {
      int i_nxt = (i+1) % sz;
      while(1) {
        int j_nxt = (j+1) % sz;

        int k = ccw(
          {0, 0},
          {points[ch_idx[i_nxt]].x - points[ch_idx[i]].x, points[ch_idx[i_nxt]].y - points[ch_idx[i]].y},
          {points[ch_idx[j_nxt]].x - points[ch_idx[j]].x, points[ch_idx[j_nxt]].y - points[ch_idx[j]].y}
        );

        if (k <= 0) break;

        j = j_nxt;
      }

      ll d = dist(points[ch_idx[i]], points[ch_idx[j]]);

      if(ans < d) { // 가장 먼 두 점 갱신
        ans = d;
        farest_points = {points[ch_idx[i]], points[ch_idx[j]]};
      }
    }

    return ans;
  }
};

int main() {
  ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

  RotatingCalipers rc;

  cin >> rc.N;

  for(int x = 0; x < rc.N; x++) {
    ll a, b;
    cin >> a >> b;
    rc.add_point(a, b);
  }

  cout << rc.perform();
}

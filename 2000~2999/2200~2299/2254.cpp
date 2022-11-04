/*
  [2254: 감옥 건설](https://www.acmicpc.net/problem/2254)

  Tier: Platinum 4
  Category: Convex Hull, Geometry
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

struct ConvexHull {
  ll N;
  vector <Point> points;
  stack <int> stk;
  vector <Point> convex_hull_points;
  vector <int> idxs;
  vector <Point> left_points;

  void init() {
    points.clear();
    while(!stk.empty()) stk.pop();
    convex_hull_points.clear();
    idxs.clear();
    left_points.clear();
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
      convex_hull_points.push_back(points[stk.top()]);
      idxs.push_back(stk.top());
      stk.pop();
    }
    sort(idxs.begin(), idxs.end());
    reverse(convex_hull_points.begin(), convex_hull_points.end());
  }

  void perform() {
    graham_scan();

    int i = 0;
    int j = 0;

    while(i < N && j < idxs.size()) {
      if(i == idxs[j]) {
        i++;
        j++;
      } else {
        left_points.push_back(points[i++]);
      }
    }

    while(i < N) {
      left_points.push_back(points[i++]);
    }
  }

  bool include_point(Point p) {
    int sz = convex_hull_points.size();
    for1(0, sz) {
      int j = (i + 1) % sz;

      if(ccw(convex_hull_points[i], convex_hull_points[j], p) < 0) return false;
    }
    return true;
  }
};

int main() {
  ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

  ConvexHull ch;
  Point p;
  ll cnt = 0;

  cin >> ch.N >> p.x >> p.y;

  for1(0, ch.N) {
    ll a, b;
    cin >> a >> b;
    ch.add_point(a, b);
  }

  while(1) {
    ch.perform();

    // cout << cnt << "&&\n";
    // cout << "--------\n";
    // for(Point p : ch.left_points) {
    //   cout << p.x << " " <<  p.y << "\n";
    // }
    // cout << "--------\n";
    // for(Point p : ch.convex_hull_points) {
    //   cout << p.x << " " <<  p.y << "\n";
    // }

    // cout << "*************\n\n";

    if(!ch.include_point(p)) {
      break;
    }
    cnt++;

    if(ch.left_points.size() <= 2) {
      break;
    }

    vector <Point> tmp = ch.left_points;
    ch.init();
    ch.N = tmp.size();
    for(Point i : tmp) {
      ch.add_point(i.x, i.y);
    }
  }

  cout << cnt;
}

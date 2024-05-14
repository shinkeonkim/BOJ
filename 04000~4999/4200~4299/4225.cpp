/*
  [4225: 쓰레기 슈트](https://www.acmicpc.net/problem/4225)

  Tier: Platinum 3
  Category: 기하, 볼록껍질
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
  double x, y;
  double p = 0;
  double q = 0;

  explicit Point(double _x = 0, double _y = 0) : x(_x), y(_y) {}

  Point operator- (const Point& a) const {
    return Point(x - a.x, y - a.y);
  }

  Point operator+ (const Point& a) const {
    return Point(x + a.x, y + a.y);
  }

  Point operator* (double a) const {
    return Point(x * a, y * a);
  }

  double norm() const {
    return hypot(x, y);
  }

  double dot(const Point& a) const {
    return x * a.x + y * a.y;
  }

  double cross(const Point& a) const {
    return x * a.y - a.x * y;
  }

  Point normalize() const {
    return Point(x / norm(), y / norm());
  }

  Point project(const Point& a) const {
    Point r = a.normalize();

    return r * r.dot(*this);
  }
};

double ccw(Point a, Point b) {
  return a.cross(b);
}

double ccw(Point p, Point a, Point b) {
  return ccw(a - p, b - p);
}


bool comp1(Point a, Point b) {
  if(a.y != b.y) return a.y < b.y;
  return a.x < b.x;;
}

bool comp2(Point a, Point b) {
  if(a.q * b.p != a.p * b.q) return a.q * b.p < a.p * b.q;

  return comp1(a, b);
}

Point perpendicular_foot(Point a, Point b, Point p) {
  return a + (p - a).project(b - a);
}

double dis(Point a, Point b, Point p) {
  return (p - perpendicular_foot(a, b, p)).norm();
}

struct ConvexHull {
  int N;
  vector <Point> points;
  stack <int> stk;
  vector <Point> result;

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
        int second = stk.top(); stk.pop();
        int first = stk.top();

        if(ccw(points[first], points[second], points[nxt]) > 0) {
          stk.push(second);
          break;
        }
      }
      stk.push(nxt++);
    }

    while(!stk.empty()) {
      result.push_back(points[stk.top()]);
      stk.pop();
    }

    reverse(result.begin(), result.end());
  }
};

int main() {
  ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);
  cout << fixed;
  cout.precision(2);
  int tc = 1;

  while(1) {
    ConvexHull ch;

    cin >> ch.N;

    if(ch.N == 0) break;

    for(int i = 0; i < ch.N; i++) {
      double x, y;
      cin >> x >> y;
      ch.points.push_back(Point(x, y));
    }

    ch.graham_scan();
    int sz = ch.result.size();
    double ans = 990000000;

    for(int i = 0; i < sz; i++) {
      int j = (i + 1) % sz;
      double mx = 0;

      for(int k = 0; k < sz; k++) {
        if(i == k || j == k) continue;

        double d = dis(ch.result[i], ch.result[j], ch.result[k]);

        mx = max(mx, d);
      }
      ans = min(mx, ans);
    }

    cout << "Case " << tc++ << ": " << ans + 0.00499999999 << "\n";
  }
}

/*
[20149: 선분 교차 3](https://www.acmicpc.net/problem/20149)

Tier: Platinum 4 
Category: geometry, case_work, line_intersection
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

struct Point{
  double x,y;
};

double ccw(Point p1, Point p2, Point p3) {
  double ret = (p1.x * p2.y + p2.x * p3.y + p3.x * p1.y - p2.x * p1.y - p3.x * p2.y - p1.x * p3.y);
  return ret >0?1:(ret<0?-1:0);
}

struct Line {
  /* 두 점을 지나는 직선 */
  Point p1, p2;

  bool isOverlapped(Line other) {
    if(this -> isIntersected(other)) return false;
    double A1 = this->p2.y - this->p1.y;
    double B1 = this->p1.x - this->p2.x;
    double C = A1 * this->p1.x + B1 * this->p1.y;
    return abs(A1 * other.p1.x + B1 * other.p1.y - C) < EPS;
  }

  bool isIntersected(Line other) {
    double A1 = this->p2.y - this->p1.y;
    double B1 = this->p1.x - this->p2.x;
    double A2 = other.p2.y - other.p1.y;
    double B2 = other.p1.x - other.p2.x;
    double det = A1 * B2 - A2 * B1;
    
    if (abs(det) > EPS) {
      return true;
    }
    
    return false;
  }

  Point intersectionPoint(Line other) {
    double A1 = this->p2.y - this->p1.y;
    double B1 = this->p1.x - this->p2.x;
    double C1 = A1 * this->p1.x + B1 * this->p1.y;

    double A2 = other.p2.y - other.p1.y;
    double B2 = other.p1.x - other.p2.x;
    double C2 = A2 * other.p1.x + B2 * other.p1.y;

    double det = A1 * B2 - A2 * B1;
    Point ret;
    ret.x = (B2 * C1 - B1 * C2) / det;
    ret.y = (A1 * C2 - A2 * C1) / det;
    return ret;
  }
};

struct Segment {
  Point p1, p2;

  bool isIntersected(Segment other) {
    double ccw1 = ccw(this->p1, this->p2, other.p1);
    double ccw2 = ccw(this->p1, this->p2, other.p2);
    double ccw3 = ccw(other.p1, other.p2, this->p1);
    double ccw4 = ccw(other.p1, other.p2, this->p2);

    if (ccw1 * ccw2 < 0 && ccw3 * ccw4 < 0) {
      return true;
    }
    
    if (ccw1 == 0 && onSegment(other.p1, this->p1, this->p2)) return true;
    if (ccw2 == 0 && onSegment(other.p2, this->p1, this->p2)) return true;
    if (ccw3 == 0 && onSegment(this->p1, other.p1, other.p2)) return true;
    if (ccw4 == 0 && onSegment(this->p2, other.p1, other.p2)) return true;
    
    return false;
  }

  bool onSegment(Point p, Point a, Point b) {
    return (
      min(a.x, b.x) <= p.x + EPS && p.x <= max(a.x, b.x) + EPS &&
      min(a.y, b.y) <= p.y + EPS && p.y <= max(a.y, b.y) + EPS
    );
  }

  bool isOverlapped(Segment other) {
    if (ccw(this->p1, this->p2, other.p1) != 0 || 
        ccw(this->p1, this->p2, other.p2) != 0) {
      return false;
    }
    
    double minVal1 = min(
      this->p1.x != this->p2.x ? this->p1.x : this->p1.y, 
      this->p1.x != this->p2.x ? this->p2.x : this->p2.y
    );
    double maxVal1 = max(
      this->p1.x != this->p2.x ? this->p1.x : this->p1.y, 
      this->p1.x != this->p2.x ? this->p2.x : this->p2.y
    );
    double minVal2 = min(
      other.p1.x != other.p2.x ? other.p1.x : other.p1.y, 
      other.p1.x != other.p2.x ? other.p2.x : other.p2.y
    );
    double maxVal2 = max(
      other.p1.x != other.p2.x ? other.p1.x : other.p1.y, 
      other.p1.x != other.p2.x ? other.p2.x : other.p2.y
    );
    
    double overlapStart = max(minVal1, minVal2);
    double overlapEnd = min(maxVal1, maxVal2);
    
    return overlapStart < overlapEnd - EPS;
  }

  Point intersectionPoint(Segment other) {
    Point touchPoint;
    if (isTouchingAtPoint(other, touchPoint)) {
      return touchPoint;
    }
    
    Line l1 = {this->p1, this->p2};
    Line l2 = {other.p1, other.p2};
    return l1.intersectionPoint(l2);
  }

  bool isTouchingAtPoint(Segment other, Point& touchPoint) {
    if (abs(this->p1.x - other.p1.x) < EPS && abs(this->p1.y - other.p1.y) < EPS) {
      touchPoint = this->p1;
      return true;
    }
    if (abs(this->p1.x - other.p2.x) < EPS && abs(this->p1.y - other.p2.y) < EPS) {
      touchPoint = this->p1;
      return true;
    }
    if (abs(this->p2.x - other.p1.x) < EPS && abs(this->p2.y - other.p1.y) < EPS) {
      touchPoint = this->p2;
      return true;
    }
    if (abs(this->p2.x - other.p2.x) < EPS && abs(this->p2.y - other.p2.y) < EPS) {
      touchPoint = this->p2;
      return true;
    }
    return false;
  }
};

void solve() {
  Point a, b, c, d;
  cin >> a.x >> a.y >> b.x >> b.y;
  cin >> c.x >> c.y >> d.x >> d.y;

  Segment s1 = {a, b};
  Segment s2 = {c, d};

  cout << fixed << setprecision(10);

  if (s1.isIntersected(s2)) {
    cout << 1 << "\n";
    
    if(s1.isOverlapped(s2)) {
      return;
    }

    Point p = s1.intersectionPoint(s2);
    cout << p.x << " " << p.y << "\n"; 
  } else {
    cout << 0 << "\n";
  }
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}

#include <bits/stdc++.h>

using namespace std;

const double PI = 2.0 * acos(0.0);
const double EPSILON = 1e-9;
const double INF = 1e200;

struct Vector2 {
  double x;
  double y;

  explicit Vector2(double _x = 0, double _y = 0) : x(_x), y(_y) {}

  bool operator== (const Vector2& a) const {
    return x == a.x && y == a.y;
  }

  bool operator!= (const Vector2& a) const {
    return !(*this == a);
  }

  bool operator< (const Vector2& a) const {
    return x != a.x ? x < a.x : y < a.y;
  }

  Vector2 operator+ (const Vector2& a) const {
    return Vector2(x + a.x, y + a.y);
  }

  Vector2 operator- (const Vector2& a) const {
    return Vector2(x - a.x, y - a.y);
  }

  Vector2 operator* (double a) const {
    return Vector2(x * a, y * a);
  }

  // 벡터의 크기를 반환한다.
  double norm() const {
    return hypot(x, y);
  }

  // 방향이 같은 단위 벡터를 반환한다.
  Vector2 normalize() const {
    return Vector2(x / norm(), y / norm());
  }

  // x축의 양의 방향으로부터 이 벡터까지 반시계 방향으로 잰 각도
  double polar() const {
    return fmod(atan2(y, x) + 2 * PI, 2 * PI);
  }

  // 내적
  double dot(const Vector2& a) const {
    return x * a.x + y * a.y;
  }

  // 외적
  double cross(const Vector2& a) const {
    return x * a.y - a.x * y;
  }

  // 이 벡터를 a 벡터에 사영한 벡터
  Vector2 project(const Vector2& a) const {
    Vector2 r = a.normalize();

    return r * r.dot(*this);
  }
};

ostream& operator<<(std::ostream& os, Vector2 const& a) {
  return os << a.x << " " << a.y;
}

/*
  원점에서 벡터 b가 벡터 a의 반시계 방향이면 양수
  시계 방향이면 음수, 평행이면 0을 반환한다.
*/
double ccw(Vector2 a, Vector2 b) {
  return a.cross(b);
}

/*
  점 p를 기준으로 벡터 b가 벡터 a의 반시계 방향이면 양수,
  시계방향이면 음수, 평행이면 0을 반환한다.
*/
double ccw(Vector2 p, Vector2 a, Vector2 b) {
  return ccw(a - p, b - p);
}

/*
  (a, b)를 포함하는 "직선"과 (c, d)를 포함하는 "직선"의 교점을 x에 반환한다.
  두 선이 평행이면 false, 아니면 true를 반환한다.
*/
bool line_intersection(Vector2 a, Vector2 b, Vector2 c, Vector2 d, Vector2& ret) {
  double det = (b - a).cross(d - c);

  if(fabs(det) < EPSILON) return false;

  ret = a + (b - a) * ((c - a).cross(d - c) / det);

  return true;
}

/*
  (a, b)와 (c, d)가 평행한 두 선분일 때, 한 점에서 겹치는지를 반환한다.
*/
bool parallel_segments(Vector2 a, Vector2 b, Vector2 c, Vector2 d, Vector2& p) {
  if(b < a) swap(a, b);
  if(d < c) swap(c, d);

  // 한 직선위에 없거나, 두 선분이 겹치지 않는 경우는 false를 반환한다.
  if(ccw(a, b, c) != 0 || b < c || d < a) return false;

  // 교차점을 하나 반환한다.
  if(a < c) p = c;
  else p = a;

  return true;
}

/*
  p 가 (a, b)를 감싸면서 각 변이 x , y 축에 평행한 최소 사각형 내부에 있는지 확인한다.
  a, b, p 는 일직선상에 있어야 한다.
*/
bool in_bounding_rectangle(Vector2 a, Vector2 b, Vector2 p) {
  if(b < a) swap(a, b);
  return p == a || p == b || (a < p && p < b);
}

/*
  (a, b) 선분과 (c, d) 선분의 교점을 p에 반환한다. (교점이 여러개인 경우, 아무 점을 반환한다.)
  두 선분이 교차하지 않는 경우, false를 반환한다.
*/
bool segment_intersection(Vector2 a, Vector2 b, Vector2 c, Vector2 d, Vector2& p) {
  if(!line_intersection(a, b, c, d, p)) return parallel_segments(a, b, c, d, p);

  return in_bounding_rectangle(a, b, p) && in_bounding_rectangle(c, d, p);
}

/*
  두 선분이 서로 접하는지 여부를 반환한다.
*/
bool is_segment_intersection(Vector2 a, Vector2 b, Vector2 c, Vector2 d) {
  double ab = ccw(a, b, c) * ccw(a, b, d);
  double cd = ccw(c, d, a) * ccw(c, d, b);

  if(ab == 0 && cd == 0) {
    if(b < a) swap(a, b);
    if(d < c) swap(c, d);

    return !(b < c || d < a);
  }

  return ab <= 0 && cd <=0;
}

/*
  점 p에서 (a, b) 직선에 내린 수선의 발을 반환한다.
*/
Vector2 perpendicular_foot(Vector2 a, Vector2 b, Vector2 p) {
  return a + (p - a).project(b - a);
}

/*
  점 p와 (a, b) 직선 사이의 거리를 반환한다.
*/
double distance_from_point_to_line(Vector2 a, Vector2 b, Vector2 p) {
  return (p - perpendicular_foot(a, b, p)).norm();
}

/*
  단순다각형 points의 넓이를 반환한다.
*/
double area(const vector<Vector2>& points) {
  double ret = 0;

  int sz = points.size();

  for(int i = 0; i < sz; i++) {
    int j = (i + 1) % sz;
    ret += points[i].cross(points[j]);
  }

  return fabs(ret) / 2.0;
}

int main() {
  ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);

  // Test operator ==
  Vector2 a = Vector2(1, 1);
  Vector2 b = Vector2(1, 1);
  assert(a == b);

  // Test operator !=
  a = Vector2(1, 1);
  b = Vector2(1, 2);
  assert(a != b);

  // Test operator <
  a = Vector2(1, 1);
  b = Vector2(1, 2);

  assert(a < b);

  a = Vector2(1, 1);
  b = Vector2(1, 1);

  assert(a < b == false);

  a = Vector2(2, 2);
  b = Vector2(1, 2);

  assert(a < b == false);

  // Test operator +
  a = Vector2(1, 1);
  b = Vector2(2, 5);

  Vector2 c = a + b;

  assert(c.x == 3 && c.y == 6);

  // Test operator -
  a = Vector2(6, 3);
  b = Vector2(2, -1);

  c = a - b;

  assert(c.x == 4 && c.y == 4);

  // Test operator *
  a = Vector2(2, -1);

  c = a * 3;

  assert(c.x == 6 && c.y == -3);

  // Test norm
  a = Vector2(3, 4);

  assert(a.norm() == 5);

  // Test normalize
  a = Vector2(0, 5);

  assert(a.normalize() == Vector2(0, 1));

  // Test polar
  a = Vector2(0, 10);
  assert(a.polar() == PI / 2);

  // Test dot
  a = Vector2(1, 2);
  b = Vector2(2, 3);

  assert(a.dot(b) == 8);

  // Test cross
  a = Vector2(1, 2);
  b = Vector2(2, 3);

  assert(a.cross(b) == -1);

  // Test project
  a = Vector2(2, 2);
  b = Vector2(10, 0);

  assert(a.project(b) == Vector2(2, 0));

  vector<Vector2> points;

  points.push_back(Vector2(1, 1));
  points.push_back(Vector2(1, 5));
  points.push_back(Vector2(10, 10));

  assert(area(points) == 18.0);
}

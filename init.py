# requriements: pip install requests beatifulsoup4 html5lib
from bs4 import BeautifulSoup
import requests
import sys
from os import path, getcwd

LANGUAGE_MAPPING = {
  0: 'cpp',
  1: 'py'
}


def get_cpp_template(problem_number, problem_name) -> str:
  template = '/*\n' \
      f'  [{problem_number}: {problem_name}](https://www.acmicpc.net/problem/{problem_number})\n' \
      '\n' \
      '  Tier: ??\n' \
      '  Category: ??\n' \
      '*/\n' \
      '#include <bits/stdc++.h>\n' \
      '\n' \
      '#define for1(s,n) for(int i = s; i < n; i++)\n' \
      '#define for1j(s,n) for(int j = s; j < n; j++)\n' \
      '#define foreach(k) for(auto i : k)\n' \
      '#define foreachj(k) for(auto j : k)\n' \
      '#define pb(a) push_back(a)\n' \
      '#define sz(a) a.size()\n' \
      '\n' \
      'using namespace std;\n' \
      'typedef unsigned long long ull;\n' \
      'typedef long long ll;\n' \
      'typedef vector <int> iv1;\n' \
      'typedef vector <vector<int> > iv2;\n' \
      'typedef vector <ll> llv1;\n' \
      'typedef unsigned int uint;\n' \
      'typedef vector <ull> ullv1;\n' \
      'typedef vector <vector <ull> > ullv2;\n' \
      '\n' \
      'int main() {\n' \
      '  ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);\n' \
      '  \n' \
      '}\n' \

  return template


def get_python_template(problem_number, problem_name) -> str:
  template = "\"\"\"\n" \
      f'[{problem_number}: {problem_name}](https://www.acmicpc.net/problem/{problem_number})\n' \
      '\n' \
      'Tier: ??\n' \
      'Category: ??\n' \
      "\"\"\"\n" \
      '\n' \
      '\n' \
      'def solution():\n' \
      "  return \"\"\n" \
      '\n' \
      '\n' \
      "if __name__ == '__main__':\n" \
      '  print(solution())\n' \

  return template


def get_templates(problem_number, problem_name) -> dict:
  return {
    'cpp': get_cpp_template(
      problem_number=problem_number,
      problem_name=problem_name,
    ),
    'py': get_python_template(
      problem_number=problem_number,
      problem_name=problem_name,
    ),
  }


def get_problem_directory(problem_number: int) -> str:
  first_depth_start = problem_number // 1000 * 1000
  first_depth_end = first_depth_start + 999
  second_depth_start = problem_number // 100 * 100
  second_depth_end = second_depth_start + 99

  return path.join(
    getcwd(),
    f'{first_depth_start}~{first_depth_end}',
    f'{second_depth_start}~{second_depth_end}'
  )


def get_file_path(problem_number: int, language: int) -> str:
  return path.join(
    get_problem_directory(problem_number),
    f'{problem_number}.{LANGUAGE_MAPPING[language]}'
  )


def is_already_exist_file(file_path: str) -> bool:
  return path.isfile(file_path)


def get_problem_name(problem_number):
  html = requests.get(f'https://www.acmicpc.net/problem/{problem_number}').text
  soup = BeautifulSoup(html, 'html5lib')

  return soup.find('span', {'id': 'problem_title'}).text


def create_file(file_path, content):
  f = open(file_path, 'w')
  f.write(content)
  f.close()


if __name__ == '__main__':
  problem_number = int(input('BOJ 문제 번호를 입력해주세요.: '))
  language = int(input('언어를 선택해주세요. (cpp: 0, python: 1): '))

  file_path = get_file_path(
    problem_number=problem_number,
    language=language
  )

  if is_already_exist_file(file_path):
    chk = input('이미 파일이 존재합니다. 덮어씌우시겠습니까? (y/n): ')

    if chk != 'y':
      sys.exit()

  problem_name = get_problem_name(problem_number)

  templates = get_templates(
    problem_number=problem_number,
    problem_name=problem_name
  )

  create_file(
    file_path=file_path,
    content=templates[LANGUAGE_MAPPING[language]]
  )

  print(file_path)

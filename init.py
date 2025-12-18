# requriements: pip install requests
from requests import get
import sys
from os import path, getcwd

LANGUAGE_MAPPING = {
  0: 'cpp',
  1: 'py',
  2: 'rb',
}

def get_template(file_path, problem_number, title, tier, tags) -> str:
  f = open(file_path, 'r')
  template = "".join(f.readlines())

  template = template.format(
    title = title,
    problem_number = problem_number,
    tier = tier,
    tags = tags
  )
  f.close()

  return template


def get_templates_by_language(language, problem_number, title, tier, tags) -> dict:
  return {
    'cpp': get_template(
      file_path='./templates/cpp_template.txt',
      problem_number=problem_number,
      title=title,
      tier=tier,
      tags=tags
    ),
    'py': get_template(
      file_path='./templates/python_template.txt',
      problem_number=problem_number,
      title=title,
      tier=tier,
      tags=tags
    ),
    'rb': get_template(
      file_path='./templates/ruby_template.txt',
      problem_number=problem_number,
      title=title,
      tier=tier,
      tags=tags
    )
  }[language]


def get_problem_directory(problem_number: int) -> str:
  first_depth_start = problem_number // 1000 * 1000
  first_depth_end = first_depth_start + 999
  second_depth_start = problem_number // 100 * 100
  second_depth_end = second_depth_start + 99

  return path.join(
    getcwd(),
    f'{first_depth_start:05d}~{first_depth_end:05d}',
    f'{second_depth_start}~{second_depth_end}'
  )


def get_file_path(problem_number: int, language: int) -> str:
  return path.join(
    get_problem_directory(problem_number),
    f'{problem_number}.{LANGUAGE_MAPPING[language]}'
  )


def is_already_exist_file(file_path: str) -> bool:
  return path.isfile(file_path)


def get_tier_string(level: int) -> str:
  TIER_STRING = [
    'Unrated',
    'Bronze 5', 'Bronze 4', 'Bronze 3', 'Bronze 2', 'Bronze 1',
    'Silver 5', 'Silver 4', 'Silver 3', 'Silver 2', 'Silver 1',
    'Gold 5', 'Gold 4', 'Gold 3', 'Gold 2', 'Gold 1',
    'Platinum 5', 'Platinum 4', 'Platinum 3', 'Platinum 2', 'Platinum 1',
    'Diamond 5', 'Diamond 4', 'Diamond 3', 'Diamond 2', 'Diamond 1',
    'Ruby 5', 'Ruby 4', 'Ruby 3', 'Ruby 2', 'Ruby 1',
  ]
  
  return TIER_STRING[level]


def get_abstract_tag_strings(tags):
  return [item['key'] for item in tags]


def get_problem_info(problem_number):
  json_response = get(
    f'https://solved.ac/api/v3/problem/show?problemId={problem_number}',
    headers={
      'Accept': 'application/json',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
  )

  json_response = json_response.json()
  
  return {
    'title': json_response['titleKo'],
    'tier': get_tier_string(json_response['level']),
    'tags': get_abstract_tag_strings(json_response['tags'])
  }


def create_file(file_path, content):
  f = open(file_path, 'w', encoding='UTF-8')
  f.write(content)
  f.close()


if __name__ == '__main__':
  problem_number = int(input('BOJ 문제 번호를 입력해주세요.: '))
  language = int(input('언어를 선택해주세요. (cpp: 0, python: 1, ruby: 2): '))

  file_path = get_file_path(
    problem_number=problem_number,
    language=language
  )

  if is_already_exist_file(file_path):
    chk = input('이미 파일이 존재합니다. 덮어씌우시겠습니까? (y/n): ')

    if chk != 'y':
      sys.exit()

  problem_info = get_problem_info(problem_number)

  template = get_templates_by_language(
    language=LANGUAGE_MAPPING[language],
    problem_number=problem_number,
    title=problem_info['title'],
    tier=problem_info['tier'],
    tags=", ".join(problem_info['tags'])
  )

  create_file(
    file_path=file_path,
    content=template
  )

  print(file_path)

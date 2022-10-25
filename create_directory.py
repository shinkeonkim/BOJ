import os

PROBLEM_START = 1000
PROBLEM_END = 28000
FIRST_DIFF = 1000
SECOND_DIFF = 100


def create_directory_if_not_exist(path):
  if not os.path.exists(path):
    os.mkdir(path)


def create_git_keep_file(path):
  f = open(os.path.join(path, '.gitkeep'), 'w')
  f.close()


for i in range(PROBLEM_START, PROBLEM_END, FIRST_DIFF):
  start = i
  end = i + FIRST_DIFF - 1
  path = os.path.join(os.getcwd(), f'{start}~{end}')

  create_directory_if_not_exist(path)

  for j in range(i, i + FIRST_DIFF, SECOND_DIFF):
    start = j
    end = j + SECOND_DIFF - 1

    child_path = os.path.join(path, f'{start}~{end}')

    create_directory_if_not_exist(child_path)

    if os.listdir(child_path):
      continue

    create_git_keep_file(child_path)

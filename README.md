# sketch-code

## How to use
### 0. Requirements
1. Git
2. Python3
3. Pycharm


### 1. Download
```shell
git clone git@github.com:yoongon/sketch-code.git
```

### 2. remove solution while solving it. (optional)
```shell
cd problems/<the_problem_directory>
rm -rf solution 
```

### 3. Solve !!!
1. Write your own code at problem.py.
2. run test_problem.py to verify your solution.

### 4. Commit & push your change 
```shell
# Restore deleted files
git status # check the list of deleted files
git restore problems/<the_problem_directory>/solution/solution.py

# create your own branch to save
# you can check your solution in the future with the branch name 
# example
git checkout -b  problem1-0827
git add -A
git commit -m "Submit problem1's code"
git push origin problem1-0827
```
- you are able to search the solution at GitHub with this branch name next time.


## Why Python3?
TBD

## Why Pycharm
TBD
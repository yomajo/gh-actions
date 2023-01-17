# gh-actions
Playing with CI

Implemented workflow:

- triggers on merges to main branch
- sets up linux machine with pipenv env and deps installed
- runs tests


`test_merge.yaml`

```
name: Test Before Merging to Main
on:
  pull_request:
    branches:    
      - main
      - 'releases/**'
  push:
    branches:
      - main
      - 'releases/**'
jobs:
  Do-GitHub-Actions:
    runs-on: ubuntu-22.04
    steps:
      - name: Event info
        run: echo "Triggered automatically by a ${{ github.event_name }} to ${{ github.ref }}. Running on ${{ runner.os }}"

      - name: Check out repository code
        uses: actions/checkout@v3
      
      - name: Changed Files
        uses: tj-actions/changed-files@v35.4.1

      - name: Setup Python environment
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
          cache: pipenv

      - name: Install pipenv
        run: |
          python -m pip install --upgrade pipenv wheel
      
      - id: cache-pipenv
        uses: actions/cache@v1
        with:
          path: ~/.local/share/virtualenvs
          key: ${{ runner.os }}-pipenv-${{ hashFiles('**/Pipfile.lock') }}

      - name: Install dependencies
        if: steps.cache-pipenv.outputs.cache-hit != 'true'
        run: |
          pipenv install --deploy --dev

      - name: Run tests
        run: pipenv run python -B -m pytest
      
      - name: Congratulate
        run: echo "TESTS PASSED"

      - name: Job status
        run: echo "Status ${{ job.status }}"
```

## Skip action
to skip checks on push to `main`, include any of below into commit msg:

- `[skip ci]`
- `[ci skip]`
- `[no ci]`
- `[skip actions]`
- `[actions skip]`


[github docs](https://docs.github.com/en/actions/managing-workflow-runs/skipping-workflow-runs)
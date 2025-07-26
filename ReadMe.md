# GitHub Workflows Demo

## What are GitHub Workflows?

GitHub Workflows are automated processes that you can set up in your repository to build, test, package, release, or deploy your project. They are part of GitHub Actions, GitHub's continuous integration and continuous deployment (CI/CD) platform.

## Key Concepts

### 1. **Workflow**
- A configurable automated process made up of one or more jobs
- Defined by a YAML file in your repository's `.github/workflows` directory
- Triggered by events like pushes, pull requests, or on a schedule

### 2. **Events**
- Specific activities that trigger a workflow run
- Examples: `push`, `pull_request`, `schedule`, `workflow_dispatch`

### 3. **Jobs**
- A set of steps that execute on the same runner
- Can run in parallel or sequentially
- Each job runs in a fresh virtual environment

### 4. **Steps**
- Individual tasks that can run commands or actions
- Can use pre-built actions from the GitHub Marketplace
- Execute in order within a job

### 5. **Actions**
- Reusable units of code that perform frequently repeated tasks
- Can be created by you, the community, or GitHub

## Basic Workflow Example

```yaml
name: CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Node.js
      uses: actions/setup-node@v3
      with:
        node-version: '18'
    
    - name: Install dependencies
      run: npm install
    
    - name: Run tests
      run: npm test
```

## Common Use Cases

- **Continuous Integration (CI)**: Automatically build and test code changes
- **Continuous Deployment (CD)**: Deploy applications to staging/production
- **Code Quality**: Run linters, formatters, and security scans
- **Release Management**: Create releases and publish packages
- **Notifications**: Send alerts to team members

## Benefits

- ✅ **Automation**: Reduce manual work and human error
- ✅ **Consistency**: Ensure the same process every time
- ✅ **Speed**: Fast feedback on code changes
- ✅ **Integration**: Works seamlessly with GitHub repositories
- ✅ **Flexibility**: Highly customizable for any workflow needs

## Getting Started

1. Create a `.github/workflows` directory in your repository
2. Add a YAML file (e.g., `ci.yml`) with your workflow definition
3. Commit and push to trigger your first workflow run
4. Monitor progress in the "Actions" tab of your repository

GitHub Workflows help teams deliver better software faster by automating repetitive tasks and ensuring code quality standards are met consistently.

## Demo Project

This repository includes a simple Python calculator application to demonstrate GitHub workflows in action.

### Project Structure

```
demo-githubworkFlow/
├── .github/
│   └── workflows/
│       └── ci.yml          # GitHub workflow configuration
├── app.py                  # Main Python application
├── test_app.py            # Unit tests
├── requirements.txt       # Python dependencies
└── ReadMe.md             # This file
```

### What the Demo Includes

- **Simple Calculator App** (`app.py`): Basic math functions (add, subtract, multiply, divide, factorial, even checker)
- **Comprehensive Tests** (`test_app.py`): Unit tests covering all functions including edge cases
- **CI Workflow** (`.github/workflows/ci.yml`): Automated testing on multiple Python versions

### The Workflow in Action

When you push code to this repository, the GitHub workflow will automatically:

1. **🔄 Trigger**: Run on push/pull request to main/master branch
2. **🐍 Setup**: Test on Python versions 3.8, 3.9, 3.10, and 3.11
3. **📦 Install**: Install dependencies from `requirements.txt`
4. **🔍 Lint**: Check code quality with flake8
5. **🧪 Test**: Run tests with both unittest and pytest
6. **▶️ Execute**: Verify the app runs without errors

### How to Test the Workflow

1. **Clone this repository**
2. **Make a change** to `app.py` or `test_app.py`
3. **Commit and push** your changes
4. **Visit the Actions tab** in GitHub to see the workflow run
5. **Watch the magic happen!** ✨

### Local Testing

You can also run the tests locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py

# Run tests with unittest
python -m unittest test_app.py -v

# Run tests with pytest
pytest test_app.py -v

# Check code quality
flake8 . --max-line-length=127
```

This demo shows how GitHub workflows can automatically ensure code quality and catch issues before they reach production!
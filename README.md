# Introduction to Python Software Development on GitHub

## Course Description

In today's world of scientific research and development, the ability to effectively collaborate and develop software as a team is essential. This two-day introductory course is designed specifically for graduate students and postdoctoral researchers seeking to enhance their software development skills in Python and embrace modern continuous integration practices on GitHub. Participants will gain hands-on experience in using Git, pre-commit hooks, unit testing, managing dependencies, and ultimately maintaining stable code. The skills gained in this course will enable participants to work efficiently as part of a team, ensuring the development of high-quality and maintainable software.

## Day 1

### 9:00 AM - Introduction to Collaborative Software Development
- Understanding the importance of collaboration in software development projects.
- Overview of version control systems and their significance.
- Introduction to Git and its role in facilitating team-based development.
- Basic Git commands and workflows.
- GitHub desktop
- Activities
  - Create a GitHub account.

### 10:00 AM - Environment Management with Anaconda
- Creating reproducible development environments with virtual environments.
- Basic Anaconda commands.
- Dependency Management and Environment Requirements using package managers (pip, conda).
- Setup.py?
- Integrated package, linting, CI, maintenance with a pyproject.toml
- Activities
  - Download and install Miniconda.
  - Set up two virtual environments with Anaconda, each with a few hand-selected dependencies. Switch between the repos. Launch python. Run a command that requires the dependency.

### 11:00 AM - Git Essentials
- Branching and merging strategies for team collaboration.
- Resolving conflicts.
- Git blame, merge, fork, pull request, commit, checkout, diff, fetch, advanced section (working from a fork, working on a project that you are not allowed to commit to).
- Creating issues, branches, linking branches to issues, …
- Activities
  - Activate an environment, clone a repo with a pyproject, build it, something that already exists.
  - Make our own repo on GitHub, specify some dependencies that need to be used, and they should create a pyproject.toml thing, organize the repo, and make a push.

### 12:30 PM - Lunch

### 1:30 PM - Code Organization Strategies
- Organizational Strategies for repos: src/ test/ docs/
- Model View Controller
- Activities
  - Upload individual files to Git
  - Place code in calculator appropriate folder (src/ test/ docs/ or MVC)

### 2:30 PM - Calculator Time
- Intro to Calculator Assignment
- Split into teams of 4. Self-organization. Ask to have at least one novice and expert per team
- We provide a zip file without structure.
- They create a repo, they all push their individual files, and then they start to work together to establish functioning code.
- We will create an error. They will have to log an issue. If time, fix the error with a linked branch, make a PR.
- We will intentionally provide sloppy code with unused imports, variables, etc.

### 5:00 PM - Depart

## Day 2

### 9:00 AM - Introduction to Continuous Integration and its Benefits
- Different types of continuous integration tools.
- Unit tests.
- Code formatters.
- Documentation.
- Code Coverage.
- Code QL

### 9:30 AM - Pre-commit Hooks, Linters, Code Formatters
- Techniques to maintain code quality.
- Utilizing pre-commit hooks to enforce coding standards and maintain code quality.
- Clean codes
- Activities – 30 minutes.
  - Set up Ruff locally.
  - Set up a pre-commit hook to run Ruff and Black (code formatter) and install it.
  - Push a commit.

### 10:30 AM - Unit Testing and Test-Driven Development (TDD)
- Importance of unit testing in software development.
- Writing effective unit tests using Python's testing frameworks.
- Incorporating test-driven development principles into the development process
- Activities – 30 minutes.
  - Write some unit tests on calculator evaluation.
  - We will try to import corrupted code, and students will try to fix it (or potentially catch errors with unit tests in the pull request?)

### 11:30 AM - Setting up CI pipelines using popular tools with GitHub Actions
- Event-driven actions – PRs. Documentation only run on that event.
- Pytest
- Unit testing CI
- Activities – 30 minutes.
  - Setup GitHub Actions on the repo.

### 12:30 PM – Lunch

### 1:30 PM - Public-facing Documentation
- Sphinx/Compiled numpy doc
- Activities – 30 minutes.
  - Setup Sphinx to GitHub pages.
  - Numpy doc.
  - GitHub actions for doc creation.

### 2:30 PM - Stable Releases
- Versioning, stable DOIs, tag that you can always go back to for a publication.
- Zenodo, twine, PyPI, Conda Constructor, if there is time.
- Activities
  - Setup a stable release

### 3:30 PM – Finish Calculator and CI Workflows.
- Potentially discuss individual projects.

### 5:00 PM - Depart

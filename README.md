# Introduction to Python Software Development on GitHub

### Date: 10/24/2023-10/25/2023.

### Instructors: 
Kevin Dean, Ph.D.
Zach Marin, Ph.D.
Dushyant Mehra, Ph.D.

### Course Description: 
In today's world of scientific research and development, the ability to effectively collaborate and develop software as a team is essential. This two-day introductory course is designed specifically for graduate students and postdoctoral researchers seeking to enhance their software development skills in Python and embrace modern continuous integration practices on GitHub. Participants will gain hands-on experience in using Git, pre-commit hooks, unit testing, managing dependencies, and ultimately maintaining stable code. and maintaining stable code through detailed environment requirements. The skills gained in this course will enable participants to work efficiently as part of a team, ensuring the development of high-quality and maintainable software.

### Day 1
1. Introduction to Collaborative Software Development
- Understanding the importance of collaboration in software development projects.
- Overview of version control systems and their significance.
- Introduction to Git and its role in facilitating team-based development.
> Activities: Create a GitHub account.

2. Environment Management with Anaconda
- Creating reproducible development environments with virtual environments.
- Basic anaconda commands.
- Dependency Management and Environment Requirements using package managers (pip, conda), and pyproject.toml 
> Activities: Download and install Miniconda. Set up two virtual environments with Anaconda, each with a few hand-selected dependencies. Switch between the repos. Launch python. Run a command that requires the dependency.

3. Git Essentials
- Basic Git commands and workflows. 
- Branching and merging strategies for team collaboration.
- Resolving conflicts
- Git blame, merge, fork, pull request, commit, checkout, diff, fetch, advanced section (working from a fork, working on a project that you are not allowed to commit to). 
- Github desktop
- Creating issues, branches, linking branches to issues, …
> Activities: Activate an environment, clone a repo with a pyproject, build it, something that already exists.
	Make our own repo on GitHub, specify some dependencies that need to be used, and they should create a pytoml thing, organize the repo, and make a push.

4.	Code Organization Strategies
- Organizational Strategies for repos: src/ test/ docs/
- Model View Controller

5. Collaborative Development Workflows
- Strategies for efficient collaboration using Git.
- Working with remote repositories and managing pull requests.
-  Techniques to maintain code quality.
> Activities:	Upload individual files to Git. Place code in calculator appropriate folder (src/ test/ docs/ or MVC)

### Day 2
1.	Pre-commit Hooks, Linters, Code Formatters
- Utilizing pre-commit hooks to enforce coding standards and maintain code quality.
- Clean codes
> Activities: Set up Ruff locally. Set up a pre-commit hook to run Ruff and Black (code formatter) and install it.	Push a commit.

2. Unit Testing and Test-Driven Development (TDD) 
- Importance of unit testing in software development.
- Writing effective unit tests using Python's testing frameworks.
- incorporating test-driven development principles into the development process
> Activities:	Write some unit tests on calculator evaluation

3. Introduction to continuous integration and its benefits 
- Different types of continuous integration tools.
- Unit tests.

4. Setting up CI pipelines using popular tools on GitHub 
- Pytest
- Codecov
- Unit testing CI
> Activities: Setup GitHub Actions on the repo.

5. Public-facing documentation
- Sphinx/Compiled numpy doc 
> Activities: Setup Sphinx to github pages. Numpy doc. GitHub actions for doc creation.

6. Stable releases
- Versioning, stable DOIs, tag that you can always go back to for a publication.
> Activities: We will try to import corrupted code and students will try to fix it (or potentially catch error with unit tests in the pull request?)

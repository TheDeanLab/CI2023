# CI2023
## Introduction to Python Software Development on GitHub

## Date: 10/24/2023-10/25/2023.

## Instructors: 
Kevin Dean, Ph.D.
Zach Marin, Ph.D.
Dushyant Mehra, Ph.D.

## Credit Hours: 1

## Room: G9.250A

## Class Size: 20.

## Course Description: 
In today's world of scientific research and development, the ability to effectively collaborate and develop software as a team is essential. This two-day introductory course is designed specifically for graduate students and postdoctoral researchers seeking to enhance their software development skills in Python and embrace modern continuous integration practices on GitHub. Participants will gain hands-on experience in using Git, pre-commit hooks, unit testing, managing dependencies, and ultimately maintaining stable code. and maintaining stable code through detailed environment requirements. The skills gained in this course will enable participants to work efficiently as part of a team, ensuring the development of high-quality and maintainable software.

## Day 1
1. Introduction to Collaborative Software Development
- Understanding the importance of collaboration in software development projects.
- Overview of version control systems and their significance.
- Introduction to Git and its role in facilitating team-based development.
- Activities. Create a GitHub account.

2. Environment Management with Anaconda
- Creating reproducible development environments with virtual environments.
- Basic anaconda commands.
- Dependency Management and Environment Requirements using package managers (pip, conda), and pyproject.toml 
- Activities. Download and install Miniconda. Set up two virtual environments with Anaconda, each with a few hand-selected dependencies. Switch between the repos. Launch python. Run a command that requires the dependency.

3. Git Essentials
- Basic Git commands and workflows. 
- Branching and merging strategies for team collaboration.
- Resolving conflicts
- Git blame, merge, fork, pull request, commit, checkout, diff, fetch, advanced section (working from a fork, working on a project that you are not allowed to commit to). 
o	Github desktop
o	Creating issues, branches, linking branches to issues, …
o	Activities
	Activate an environment, clone a repo with a pyproject, build it, something that already exists.
	Make our own repo on GitHub, specify some dependencies that need to be used, and they should create a pytoml thing, organize the repo, and make a push.
4.	Code Organization Strategies – Dushyant 
o	Organizational Strategies for repos: src/ test/ docs/
o	Model View Controller
•	Collaborative Development Workflows – Dushyant 
o	Strategies for efficient collaboration using Git.
o	Working with remote repositories and managing pull requests.
o	 Techniques to maintain code quality.
o	Activity: 
	Upload individual files to Git
	Place code in calculator appropriate folder (src/ test/ docs/ or MVC)
## Day 2
1	Pre-commit Hooks, Linters, Code Formatters – Dushyant 
o	Utilizing pre-commit hooks to enforce coding standards and maintain code quality.
o	Clean codes
o	Activities
	Set up Ruff locally
	Set up a pre-commit hook to run Ruff and Black (code formatter) and install it
	Push a commit
•	Unit Testing and Test-Driven Development (TDD) – Zach
o	Importance of unit testing in software development.
o	Writing effective unit tests using Python's testing frameworks.
o	incorporating test-driven development principles into the development process
o	Activity
	Write some unit tests on calculator evaluation
•	Introduction to continuous integration and its benefits – Zach
o	Different types of continuous integration tools.
o	Unit tests.
•	Setting up CI pipelines using popular tools on GitHub – Zach 
o	Pytest
o	Codecov
o	Unit testing CI
	Setup GitHub Actions on the repo.
•	Public-facing documentation – Zach 
o	Sphinx/Compiled numpy doc 
o	Activity
	Setup Sphinx to github pages. Numpy doc. GitHub actions for doc creation.
•	Stable releases – Dushyant
o	Versioning, stable DOIs, tag that you can always go back to for a publication.
o	Activity:
	We will try to import corrupted code and students will try to fix it (or potentially catch error with unit tests in the pull request?)

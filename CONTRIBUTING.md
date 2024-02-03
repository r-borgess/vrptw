# Contributing to vrptw

Thank you for your interest in contributing to this project. We welcome contributions from everyone, and we hope this document makes it easier for you to contribute in ways that are meaningful to you. Below are some guidelines to follow when contributing.

## Getting Started

### Prerequisites

Before you can contribute, you'll need:
- Python 3.x installed on your machine.
- Familiarity with Git and GitHub workflows.

### Setting Up Your Development Environment

1. **Fork the Repository**: Start by forking the repository to your GitHub account.

2. **Clone Your Fork**: Clone your forked repository to your local machine:
    ```
    git clone https://github.com/your-username/vrptw_solver.git
    ```
   
3. **Install Dependencies**: Navigate to the project directory and install the required dependencies:
    ```
    cd vrptw_solver
    pip install -r requirements.txt
    ```

4. **Set Up a Virtual Environment** (Optional): It's a good practice to use a virtual environment for Python projects. You can set one up by running:
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

## Making Changes

1. **Create a New Branch**: For each new feature or fix, create a new branch:
    ```
    git checkout -b feature/your_feature_name
    ```

2. **Make Your Changes**: Implement your feature or fix.

3. **Write or Update Tests**: If you're adding new functionality or fixing a bug, please include tests that cover your changes.

4. **Follow the Coding Conventions**: Ensure your code adheres to the coding standards used throughout the project.

5. **Document Your Changes**: Update the README.md or other relevant documentation.

6. **Run Tests**: Make sure all tests pass and your changes do not introduce any new issues.

## Submitting Contributions

1. **Push Your Changes**: Push your changes to your fork:
    ```
    git push origin feature/your_feature_name
    ```

2. **Create a Pull Request**: Go to the original repository on GitHub, and you'll see a prompt to open a pull request from your new branch. Click on "Compare & pull request" and describe the changes you've made.

3. **Review Process**: Your pull request will be reviewed by maintainers. Be open to discussions and making requested changes.

## Additional Guidelines

- **Reporting Issues**: Use GitHub Issues to report bugs or suggest enhancements. Please check existing issues to avoid duplicates.

- **Feature Requests**: For significant changes, open an issue first to discuss what you would like to change. This lets the community discuss the idea before any work is done.

- **Stay Engaged**: After submitting a pull request or issue, stay engaged. Respond to comments or questions from the project maintainers.

Thank you.

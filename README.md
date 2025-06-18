# 🩸 RepoVampire

![RepoVampire Banner](https://i.imgur.com/BDHSsVu.png)

[![License: MIT](https://img.shields.io/badge/License-MIT-red.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)

A simple and stylish tool to "drain" (clone) all public repositories of a GitHub user. Perfect for creating backups or analyzing a user's public work.

## ✨ Features

-   **Vampire Theme** 🧛: A fun, vampire-themed interface with colorful output.
-   **Bulk Cloning** 📥: Clones all public repositories from any specified GitHub user.
-   **Organized** 📂: Creates a dedicated directory for the target user's repos.
-   **Easy to Use** 🚀: Simple and intuitive command-line interface.

## 🛠️ Installation

1.  **Clone this repository:**
    ```bash
    git clone https://github.com/Br3noAraujo/RepoVampire.git
    cd RepoVampire
    ```

2.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

![Usage Demo](https://i.imgur.com/ktxAAA3.png)

## 🚀 How to Use

To start draining repositories, just run the script with the target GitHub username.

```bash
python3 repovampire.py <github_username>
```

### Example

```bash
python3 repovampire.py Br3noAraujo
```

This command will:
1.  Create a directory named `Br3noAraujo`.
2.  Fetch a list of all public repositories from the user `Br3noAraujo`.
3.  Clone each repository into the `Br3noAraujo` directory.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Copyright © 2025 [Br3noAraujo](https://github.com/Br3noAraujo). 

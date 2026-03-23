# GitHub Repo Analyzer CLI

A command-line tool that fetches and analyzes GitHub repositories for a given user.
This project demonstrates real-world API handling, pagination, data aggregation, and clean modular CLI design in Python.

---

## 🚀 Features

* Fetch repositories using the GitHub REST API
* Handle API pagination (fetch all repos across pages)
* Retry logic with exponential backoff for reliability
* Compute useful repository analytics:

  * Total repositories
  * Total stars
  * Average stars
  * Most starred repository
  * Most used programming language
* Clean, readable CLI output
* Export results to JSON
* Modular and scalable project structure

---

## 🧠 Project Motivation

This project moves beyond basic API usage and demonstrates:

* Working with **real-world APIs (GitHub)**
* Handling **pagination and unreliable networks**
* Designing **robust API clients**
* Performing **data analysis on structured JSON**
* Building **production-style CLI tools**

---

## 🏗️ Project Structure

```
github-repo-analyzer-cli/
│
├── main.py
├── requirements.txt
├── README.md
│
├── data/
│   └── (exported JSON files)
│
├── toolkit/
│   └── analyzer.py
│
└── utils/
    ├── api_client.py
    ├── formatter.py
    └── file_handler.py
```

---

## ⚙️ Installation

Clone the repository:

```
git clone https://github.com/sum1tbarua/github-repo-analyzer-cli.git
cd github-repo-analyzer-cli
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## ▶️ Usage

### Basic usage

```
python main.py --user torvalds
```

---

### Limit displayed repositories

```
python main.py --user torvalds --limit 5
```

---

### Show summary statistics

```
python main.py --user torvalds --summary
```

---

### Export repository data

```
python main.py --user torvalds --export data/repos.json
```

---

### Combine features

```
python main.py --user torvalds --limit 5 --summary --export data/repos.json
```

---

## 📊 Example Output

### Repositories

```
REPOSITORIES
------------------------------
Repository Name: linux
Total Stars: 190000
Total Forks: 50000
Language: C
URL: https://github.com/torvalds/linux
------------------------------
```

---

### Summary

```
SUMMARY
------------------------------
total_repos: 6
total_stars: 190500
average_stars: 31750.0
top_repo: linux
top_language: C
```

---

## 🔧 How It Works

### 1. API Client (`utils/api_client.py`)

* Fetches repository data from GitHub API
* Handles pagination using `page` and `per_page`
* Implements retry logic with exponential backoff

### 2. Analyzer (`toolkit/analyzer.py`)

* Processes raw repository data
* Computes statistics and aggregates

### 3. Formatter (`utils/formatter.py`)

* Displays repositories and summaries in a clean format

### 4. File Handler (`utils/file_handler.py`)

* Exports fetched data to JSON files

### 5. Main CLI (`main.py`)

* Parses user input
* Coordinates all modules

---

## 📈 Metrics Computed

* **Total Repositories**
* **Total Stars**
* **Average Stars per Repository**
* **Most Starred Repository**
* **Most Used Programming Language**

---

## ⚠️ Notes

* GitHub API returns data in pages (default 30, max 100 per request)
* This tool automatically fetches all pages
* Some repositories may have `null` language values

---

## 🛠️ Technologies Used

* Python 3
* requests
* argparse
* JSON

---

## 📌 Future Improvements

* Support for organization repositories
* Filtering by language or stars
* Sorting options (top repos, newest repos)
* Unit tests
* Packaging as an installable CLI tool

---

## 👤 Author

**Sumit Barua**

M.S. Computer Science 

Western Michigan University

---

## ⭐ Acknowledgements

* GitHub REST API
* Python requests library

---

## 📄 License

This project is open-source and available under the MIT License.

# Broken Link Checker

![GitHub last commit](https://img.shields.io/github/last-commit/username/repository)
![GitHub top language](https://img.shields.io/github/languages/top/username/repository)

This is a simple Python script to check for broken links on a website. It utilizes the `requests`, `BeautifulSoup`, and `colorama` libraries to fetch web pages, parse HTML, and provide colored output in the terminal.

## Usage

### Prerequisites

Before running the script, make sure you have Python 3 installed on your system. You can install the required libraries using pip:

```bash
pip3 install requests beautifulsoup4 colorama
```

### Running the Script

To check for broken links on a website, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/Samuelpasaribu/broken_link_checker.git
```

2. Navigate to the cloned directory:

```bash
cd repository
```

3. Run the script:

```bash
python3 check_links.py
```

4. Enter the website URL when prompted.

### Example

```bash
Enter website URL: https://www.samuelpasaribu.com
```

### Output

The script will display the status of each link found on the website:

- Broken links are displayed in red.
- Working links are displayed in green.
- Errors encountered during link checking are displayed in yellow.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

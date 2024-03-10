import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style

def check_links(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        links = soup.find_all('a')
        broken_links = []

        print(f"Checking links on {url}\n")

        for link in links:
            href = link.get('href')
            if href and 'http' in href:
                try:
                    link_response = requests.head(href)
                    if link_response.status_code == 404:
                        broken_links.append(href)
                        print(Fore.RED + f"[404 Error]: {href}" + Style.RESET_ALL)
                    else:
                        print(Fore.GREEN + f"[OK]: {href}" + Style.RESET_ALL)
                except requests.exceptions.RequestException as e:
                    print(Fore.YELLOW + f"[Error]: {href}, {e}" + Style.RESET_ALL)

        return broken_links
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Error retrieving page: {url}, {e}" + Style.RESET_ALL)
        return []

def main():
    url = input("Enter website URL: ")
    broken_links = check_links(url)

    if broken_links:
        print("\nBroken links (404 Error):")
        for link in broken_links:
            print(link)
    else:
        print("\nNo broken links found.")

if __name__ == "__main__":
    main()

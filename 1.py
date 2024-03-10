import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style

def check_links(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        links = soup.find_all('a')
        broken_links = []

        print(f"Checking links on {url}")

        for link in links:
            href = link.get('href')
            if href and 'http' in href:
                try:
                    link_response = requests.head(href)
                    if link_response.status_code != 200:
                        broken_links.append(href)
                        print(Fore.RED + f"[Broken]: {href}" + Style.RESET_ALL)
                    else:
                        print(Fore.GREEN + f"[OK]: {href}" + Style.RESET_ALL)
                except Exception as e:
                    print(Fore.YELLOW + f"[Error]: {href}, {e}" + Style.RESET_ALL)

        return broken_links
    except Exception as e:
        print(Fore.RED + f"Error retrieving page: {url}, {e}" + Style.RESET_ALL)
        return []

def main():
    url = input("Enter website URL: ")
    broken_links = check_links(url)

    if broken_links:
        print("\nBroken links:")
        for link in broken_links:
            print(link)
    else:
        print("\nNo broken links found.")

if __name__ == "__main__":
    main()

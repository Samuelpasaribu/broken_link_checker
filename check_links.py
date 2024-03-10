import requests
from bs4 import BeautifulSoup

def check_links(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        links = soup.find_all('a')
        broken_links = []

        for link in links:
            href = link.get('href')
            if href and 'http' in href:
                try:
                    link_response = requests.head(href)
                    if link_response.status_code != 200:
                        broken_links.append(href)
                except Exception as e:
                    print(f"Error checking link: {href}, {e}")

        return broken_links
    except Exception as e:
        print(f"Error retrieving page: {url}, {e}")
        return []

def main():
    url = input("Enter website URL: ")
    broken_links = check_links(url)

    if broken_links:
        with open("broken_links.txt", "w") as f:
            f.write("Broken links:\n")
            for link in broken_links:
                f.write(link + "\n")
        print("Broken links have been saved to broken_links.txt")
    else:
        print("No broken links found.")

if __name__ == "__main__":
    main()

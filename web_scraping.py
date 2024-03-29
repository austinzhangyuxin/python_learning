import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse


# Function to extract email addresses from a webpage
def extract_emails(url):
    # Send GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all text content
        text_content = soup.get_text()

        # Use regular expression to find email addresses
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        emails = re.findall(email_pattern, text_content)

        return emails
    else:
        print(f"Failed to retrieve webpage: {url}")
        return []


# Function to extract all links from a webpage
def extract_links(url):
    # Send GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all anchor tags (links)
        links = soup.find_all('a', href=True)

        # Extract the href attribute from each link
        hrefs = [link['href'] for link in links]

        # Convert relative links to absolute links
        abs_hrefs = [requests.compat.urljoin(url, href) for href in hrefs]

        return abs_hrefs
    else:
        print(f"Failed to retrieve webpage: {url}")
        return []


# Function to scrape all pages of a website belonging to the same domain
def scrape_website(url, max_depth=3):
    base_domain = urlparse(url).netloc
    visited_urls = set()
    emails = set()

    # Function to recursively crawl pages
    def crawl(url, depth):
        if depth > max_depth or url in visited_urls:
            return
        visited_urls.add(url)
        print(f"Crawling: {url}")
        page_emails = extract_emails(url)
        if page_emails:
            emails.update(page_emails)
        linked_urls = extract_links(url)
        for linked_url in linked_urls:
            parsed_url = urlparse(linked_url)
            if parsed_url.netloc == base_domain:
                crawl(linked_url, depth + 1)

    crawl(url, 1)

    return emails


# Example usage
url = 'https://example.com'  # Replace with the URL of the website you want to scrape
emails = scrape_website(url)

# Print or process the extracted email addresses
for email in emails:
    print(email)

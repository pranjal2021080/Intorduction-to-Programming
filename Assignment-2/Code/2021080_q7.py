class Page:
    def __init__(self, url, init_importance):
        self.url = url
        self.init_importance = init_importance
        self.links = set()  # URLs this page links to
        self.overall_importance = 0.0
        self.incoming_links = set()  # URLs that link to this page

def parse_page_file(filename):
    """Parse the input file and create page objects"""
    pages = {}
    
    with open(filename, 'r') as f:
        for line in f:
            # Split the line into URL, importance, and content
            url_part, content = line.split(':', 1)
            url, importance = url_part.split(',')
            url = url.strip()
            importance = float(importance.strip())
            
            # Create page object if it doesn't exist
            if url not in pages:
                pages[url] = Page(url, importance)
            
            # Find all URLs in content
            words = content.split()
            for word in words:
                if word.startswith('URL'):
                    link_url = word.strip('.,')
                    pages[url].links.add(link_url)
                    if link_url not in pages:
                        pages[link_url] = Page(link_url, 0.0)
                    pages[link_url].incoming_links.add(url)
    
    return pages

def calculate_overall_importance(pages):
    for page in pages.values():
        for incoming_url in page.incoming_links:
            incoming_page = pages[incoming_url]
            if len(incoming_page.links) > 0:
                page.overall_importance += incoming_page.init_importance / len(incoming_page.links)

def rank_pages(pages, N):
    ranked_pages = sorted(pages.values(), key=lambda p: p.overall_importance, reverse=True)
    return ranked_pages[:N]

def create_sample_file():
    with open('pages.txt', 'w') as f:
        f.write("URL00, 0.5: This is page zero, and has references to URL01, URL09, and also to URL08. It may have repeated references - so there are two references to URL09.\n")
        f.write("URL02, 0.6: This is another page (page is represented as a line in this). This has reference to URL05, URL04, and URL00\n")
        f.write("URL01, 0.4: This page references URL00 and URL02\n")
        f.write("URL03, 0.3: This page references URL01 and URL02\n")
        f.write("URL04, 0.7: This page references URL00\n")
        f.write("URL05, 0.2: This page references URL02 and URL03\n")

def main():
    create_sample_file()
    
    filename = input("Enter the name of the text file (e.g., pages.txt): ")
    N = int(input("Enter the number of top pages to display: "))
    
    pages = parse_page_file(filename)
    calculate_overall_importance(pages)
    top_pages = rank_pages(pages, N)
    
    print(f"Top {N} pages by overall importance:")
    for page in top_pages:
        print(f"{page.url}: {page.overall_importance}")

def test_functionality():
    create_sample_file()
    filename = 'pages.txt'
    N = 3
    
    pages = parse_page_file(filename)
    
    # Test parsing
    assert 'URL00' in pages
    assert pages['URL00'].init_importance == 0.5
    assert 'URL01' in pages['URL00'].links
    assert 'URL09' in pages['URL00'].links
    assert 'URL08' in pages['URL00'].links
    
    # Test overall importance calculation
    calculate_overall_importance(pages)
    assert pages['URL00'].overall_importance == 0.2  # URL01 and URL02 link to URL00
    
    # Test ranking
    top_pages = rank_pages(pages, N)
    assert len(top_pages) == 3
    assert top_pages[0].url == 'URL04'  # URL04 should have the highest overall importance

def a():
    
    result = 0
    for i in range(1, 10000):
        for j in range(1, 100):
            result += math.sin(i) * math.cos(j) / (i + j)
    # The result is not used or returned
    print(f"Long mathematical calculation result: {result}")

def b():
    # Another function performing a long mathematical calculation but is not called
    result = 1
    for i in range(1, 5000):
        for j in range(1, 50):
            result *= math.sin(i) * math.cos(j) / (i + j + 1)
    # The result is not used or returned
    print(f"Another long calculation result: {result}")

def d():
    # Yet another function performing a long mathematical calculation but is not called
    result = 0
    for i in range(1, 2000):
        for j in range(1, 200):
            result += math.tan(i) * math.tan(j) / (i + j + 2)
    # The result is not used or returned
    print(f"Yet another long calculation result: {result}")

def c():
    # More long mathematical calculations but is not called
    result = 0
    for i in range(1, 3000):
        for j in range(1, 150):
            result += math.exp(i) * math.log(j + 1) / (i + j + 3)
    # The result is not used or returned
    print(f"More long calculations result: {result}")

if __name__ == '__main__':
    main()
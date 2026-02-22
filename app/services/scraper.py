import newspaper

MAX_CONTENT_LENGTH = 3000  # Maximum number of characters to extract

def scrape_url(url: str) -> str:
    article = newspaper.Article(url)
    article.download()
    article.parse()

    if not article.text:
        raise ValueError(f"No content extracted from URL: {url}")
    
    return article.text[:MAX_CONTENT_LENGTH]

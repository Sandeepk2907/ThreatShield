from urllib.parse import urlparse

SHORTENERS = {"bit.ly", "tinyurl.com", "t.co", "goo.gl"}

def analyze_url(url: str) -> dict:
    parsed = urlparse(url)
    reasons = []
    if parsed.scheme != "https":
        reasons.append("Not using HTTPS")
    if parsed.netloc in SHORTENERS:
        reasons.append("Shortened URL")
    return {"url": url, "reasons": reasons, "risk": "Suspicious" if reasons else "Safe"}
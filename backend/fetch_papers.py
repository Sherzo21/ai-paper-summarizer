import requests
import pandas as pd

API_URL = "https://api.semanticscholar.org/graph/v1/paper/search"

params = {
    "query": "artificial intelligence",
    "fields": "title,abstract,year,authors,citationCount",
    "limit": 100  # Fetch 100 papers
}

# Fetch papers from API
response = requests.get(API_URL, params=params)

# Check for errors
if response.status_code != 200:
    print("❌ Error fetching data:", response.json())
    exit()

papers = response.json().get("data", [])

# Convert API response into structured data
data = []
for paper in papers:
    title = paper.get("title", "No Title")
    abstract = paper.get("abstract", "No Abstract")
    year = paper.get("year", "Unknown Year")
    authors = ", ".join([author["name"] for author in paper.get("authors", [])])
    citation_count = paper.get("citationCount", 0)

    data.append([title, abstract, year, authors, citation_count])

# Convert data to Pandas DataFrame
df = pd.DataFrame(data, columns=["Title", "Abstract", "Year", "Authors", "Citations"])

# Save to CSV
df.to_csv("data/research_papers.csv", index=False)

print("✅ Research paper dataset saved as 'data/research_papers.csv' 🎉")

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import requests
from bs4 import BeautifulSoup

app = FastAPI()

origins = ["*"]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_methods=["*"], allow_headers=["*"])

@app.get("/analyze")
def analyze_budget(destination: str = Query(..., min_length=2)):
    search_url = f"https://www.google.com/search?q=travel+costs+to+{destination}+site:tripadvisor.com+OR+site:lonelyplanet.com+OR+site:expedia.com"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(search_url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        snippets = soup.find_all("div", class_="BNeawe s3v9rd AP7Wnd")
        budget_summary = " ".join([s.get_text() for s in snippets[:5]])
    except Exception as e:
        budget_summary = f"Error retrieving data: {e}"

    return {
        "destination": destination,
        "low": f"Example budget for {destination}: Free walking tours, hostels, local eateries. " + budget_summary,
        "mid": f"Example budget for {destination}: 3-star hotels, guided tours, casual restaurants. " + budget_summary,
        "high": f"Example budget for {destination}: Luxury resorts, fine dining, private activities. " + budget_summary,
    }
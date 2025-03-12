import requests
import csv
from typing import List, Dict

class PubMedFetcher:
    BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    SUMMARY_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"

    def __init__(self, query: str):
        self.query = query

    def fetch_paper_ids(self) -> List[str]:
        params = {
            'db': 'pubmed',
            'term': self.query,
            'retmode': 'json',
            'retmax': 100  # Adjust as needed
        }
        response = requests.get(self.BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        return data.get('esearchresult', {}).get('idlist', [])

    def fetch_paper_details(self, paper_ids: List[str]) -> List[Dict]:
        params = {
            'db': 'pubmed',
            'id': ','.join(paper_ids),
            'retmode': 'json'
        }
        response = requests.get(self.SUMMARY_URL, params=params)
        response.raise_for_status()
        data = response.json()
        papers = []
        for paper_id in paper_ids:
            papers.append(data.get('result', {}).get(paper_id, {}))
        return papers

    def filter_non_academic_authors(self, authors: List[Dict]) -> List[Dict]:
        non_academic_authors = []
        for author in authors:
            affiliation = author.get('affiliation', '').lower()
            if 'university' not in affiliation and 'lab' not in affiliation:
                non_academic_authors.append(author)
        return non_academic_authors

    def save_to_csv(self, papers: List[Dict], filename: str):
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['PubmedID', 'Title', 'Publication Date', 'Non-academic Author(s)', 'Company Affiliation(s)', 'Corresponding Author Email'])
            for paper in papers:
                writer.writerow([
                    paper.get('uid'),
                    paper.get('title'),
                    paper.get('pubdate'),
                    "; ".join([author.get('name') for author in paper.get('authors', []) if author.get('name')]),
                    "; ".join([author.get('affiliation') for author in paper.get('authors', []) if author.get('affiliation')]),
                    paper.get('corresponding_author_email')
                ])
import argparse
import logging
from pubmed_fetcher import PubMedFetcher

def main():
    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed based on a query.")
    parser.add_argument('query', type=str, help='The query to search for papers.')
    parser.add_argument('-d', '--debug', action='store_true', help='Print debug information during execution.')
    parser.add_argument('-f', '--file', type=str, help='Specify the filename to save the results.')

    args = parser.parse_args()

    if args.debug:
        logging.basicConfig(level=logging.DEBUG)

    fetcher = PubMedFetcher(args.query)
    paper_ids = fetcher.fetch_paper_ids()
    logging.debug(f"Fetched paper IDs: {paper_ids}")

    papers = fetcher.fetch_paper_details(paper_ids)
    logging.debug(f"Fetched paper details: {papers}")

    if args.file:
        fetcher.save_to_csv(papers, args.file)
    else:
        for paper in papers:
            print(paper)

if __name__ == '__main__':
    main()
from Bio import Entrez
import time


def fetch_pubmed(query, max_records):
    # Fetch articles based on query
    handle = Entrez.esearch(db="pubmed", term=query, retmax=max_records)
    record = Entrez.read(handle)
    handle.close()
    
    # Get list of article IDs
    id_list = record['IdList']
    
    # Fetch article summaries for all IDs
    handle = Entrez.efetch(db="pubmed", id=",".join(id_list), rettype="medline", retmode="text")
    papers = handle.read()
    handle.close()
    
    return papers

def save_to_file(filename, data):
    with open(filename, "w",encoding="utf-8") as file:
        file.write(data)

# Define the query and maximum number of articles to download
query = "skin cancer"
max_records = 200

# Fetch papers from PubMed
papers = fetch_pubmed(query, max_records)

# Save the results to a file
save_to_file("skin_cancer_papers.txt", papers)

print("Downloaded 200 PubMed article summaries on skin cancer.")

import requests
from Bio.Seq import Seq

# Example: BRCA2 gene sequence from human (Ensembl ID: ENSG00000139618)

server = "https://rest.ensembl.org"

ext = "/sequence/id/ENSG00000139618?content-type=text/x-fasta"

response = requests.get(server + ext, headers={"Content-Type": "text/x-fasta"})


if not response.ok:
    response.raise_for_status()


dna_seq = Seq(response.text)

print("Length:", len(dna_seq))

print("First 100 bases:", dna_seq[:100])
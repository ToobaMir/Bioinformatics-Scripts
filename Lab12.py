# Step 1: Import necessary libraries
import requests
from Bio.Seq import Seq

# Step 2: Define Ensembl REST API endpoint
server = "https://rest.ensembl.org"
ensembl_id = "ENSG00000139618"  # BRCA2 gene (human)
ext = f"/sequence/id/{ensembl_id}?content-type=text/plain"

# Step 3: Make the GET request to Ensembl
response = requests.get(server + ext, headers={"Content-Type": "text/plain"})

# Step 4: Check for errors
if not response.ok:
    response.raise_for_status()

# Step 5: Wrap the sequence in a Biopython Seq object
dna_seq = Seq(response.text)

# Step 6: Print basic analysis
print("Sequence retrieved successfully!")

print("Gene ID:", ensembl_id)

print("Length of sequence:", len(dna_seq))

print("First 100 bases:", dna_seq[:100])

print("GC Content: {:.2f}%".format(100 * float(dna_seq.count('G') + dna_seq.count('C')) / len(dna_seq)))

print("Translated protein (first 30 aa):", dna_seq.translate(to_stop=True)[:30])


import pandas as pd
import urllib.request

# Read in CSV file
df = pd.read_csv("path/.csv")

# Iterate over rows of the "Links" and "Case Name" columns
for index, row in df[["Link", "Case"]].iterrows():
    url = row["Link"]
    case_name = row["Case"]
    try:
        # Download the PDF file
        urllib.request.urlretrieve(url, "path_save" + case_name + ".pdf")
    except Exception as e:
        print(f"An error occured while processing {case_name}: {e}")
        continue
    

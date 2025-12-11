import pandas as pd
import glob
import os

DATA_PATH = "./data/"

def merge_nifty_files():
    files = glob.glob(os.path.join(DATA_PATH, "*.csv"))
    if not files:
        print("No data files found in data/ folder")
        return

    dfs = []
    for f in files:
        print("Reading:", f)
        df = pd.read_csv(f)
        df["source_file"] = os.path.basename(f)
        dfs.append(df)

    merged = pd.concat(dfs, ignore_index=True)
    merged.to_csv(os.path.join(DATA_PATH, "merged_sample.csv"), index=False)
    print("Merged file saved in data/merged_sample.csv")

if __name__ == "__main__":
    merge_nifty_files()

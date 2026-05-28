from pathlib import Path
import pandas as pd


def read_excel(path, sheet_name=0):
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"No such file: {path}")
    return pd.read_excel(p, sheet_name=sheet_name)


def write_excel(df, path, sheet_name='Sheet1', index=False):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    df.to_excel(p, sheet_name=sheet_name, index=index)


def append_row(path, row_dict, sheet_name='Sheet1', index=False):
    p = Path(path)
    if p.exists():
        existing = pd.read_excel(p, sheet_name=sheet_name)
        new = pd.concat([existing, pd.DataFrame([row_dict])], ignore_index=True)
    else:
        new = pd.DataFrame([row_dict])
    p.parent.mkdir(parents=True, exist_ok=True)
    new.to_excel(p, sheet_name=sheet_name, index=index)

from pathlib import Path
import pandas as pd

from .excel_utils import write_excel, read_excel, append_row


def main():
    sample = pd.DataFrame([
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
    ])
    out = Path("data/sample.xlsx")
    write_excel(sample, out)
    print("Wrote data/sample.xlsx")
    df = read_excel(out)
    print("Read back:")
    print(df)
    append_row(out, {"name": "Charlie", "age": 22})
    print("Appended row.")
    print(read_excel(out))


if __name__ == "__main__":
    main()

from typing import List

def print_table(rows, header=""):
    """Print a simple bordered list to stdout."""
    if header:
        print(f"\n{'- ' * 30}")
        print(f"  {header}")
        print(f"{'- ' * 30}")
    if not rows:
        print("  (no records found)")
    else:
        for row in rows:
            print(f"  {row}")
    print(f"{'- ' * 30}\n")
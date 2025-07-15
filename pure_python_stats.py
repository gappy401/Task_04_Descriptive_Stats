
---

### 🐍 `pure_python_stats.py`

```python
import openpyxl
import math
from collections import Counter, defaultdict

def load_excel(filepath):
    wb = openpyxl.load_workbook(filepath)
    sheet = wb.active
    data = []
    headers = [cell.value for cell in sheet[1]]
    for row in sheet.iter_rows(min_row=2, values_only=True):
        data.append(dict(zip(headers, row)))
    return data, headers

def summarize_column(col_data):
    numeric = []
    non_numeric = []
    for val in col_data:
        try:
            numeric.append(float(val))
        except:
            if val is not None:
                non_numeric.append(str(val))

    summary = {}
    if numeric:
        summary['count'] = len(numeric)
        summary['mean'] = sum(numeric) / len(numeric)
        summary['min'] = min(numeric)
        summary['max'] = max(numeric)
        summary['std_dev'] = math.sqrt(sum((x - summary['mean'])**2 for x in numeric) / len(numeric))
    if non_numeric:
        freq = Counter(non_numeric)
        summary['unique'] = len(freq)
        summary['most_common'] = freq.most_common(1)[0]
    return summary

def main():
    filepath = 'data/2024_tw_posts_president_scored_anon.xlsx'
    data, headers = load_excel(filepath)

    for col in headers:
        col_data = [row.get(col) for row in data]
        stats = summarize_column(col_data)
        print(f"\nColumn: {col}")
        for k, v in stats.items():
            print(f"  {k}: {v}")

if __name__ == "__main__":
    main()

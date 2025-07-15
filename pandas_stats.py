import pandas as pd

def main():
    filepath = 'data/2024_tw_posts_president_scored_anon.xlsx'
    df = pd.read_excel(filepath)

    print("📊 Overall Summary:")
    print(df.describe(include='all'))

    print("\n🔢 Unique Values:")
    for col in df.columns:
        print(f"{col}: {df[col].nunique()}")

    print("\n📈 Grouped by page_id:")
    print(df.groupby('page_id').describe())

    if 'ad_id' in df.columns:
        print("\n📈 Grouped by page_id and ad_id:")
        print(df.groupby(['page_id', 'ad_id']).describe())

if __name__ == "__main__":
    main()

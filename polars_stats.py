import polars as pl

def main():
    filepath = 'data/2024_tw_posts_president_scored_anon.xlsx'
    df = pl.read_excel(filepath)

    print("📊 Overall Summary:")
    print(df.describe())

    print("\n🔢 Unique Values:")
    for col in df.columns:
        print(f"{col}: {df[col].n_unique()}")

    print("\n📈 Grouped by page_id:")
    print(df.groupby('page_id').agg([
        pl.count(),
        pl.mean('estimated_spend') if 'estimated_spend' in df.columns else pl.count()
    ]))

    if 'ad_id' in df.columns:
        print("\n📈 Grouped by page_id and ad_id:")
        print(df.groupby(['page_id', 'ad_id']).agg([
            pl.count()
        ]))

if __name__ == "__main__":
    main()

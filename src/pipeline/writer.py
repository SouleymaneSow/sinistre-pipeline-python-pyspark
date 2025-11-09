def write_parquet(df, path):
    df.write.mode("overwrite").parquet(path)

def sauvegarder_parquet(df, path):
    df.write.mode("overwrite").parquet(path)

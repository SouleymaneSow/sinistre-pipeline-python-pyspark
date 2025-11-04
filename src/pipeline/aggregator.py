from pyspark.sql.functions import avg, count
from pyspark.sql.functions import sum as _sum


def aggreger_par_client(df):
    return df.groupBy("client_id").agg(
        _sum("montant_clean").alias("total"),
        avg("montant_clean").alias("moyenne"),
        count("*").alias("nb_sinistres"),
    )

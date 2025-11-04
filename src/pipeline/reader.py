def lire_parquet(spark, path):
    """Lit un fichier Parquet"""
    return spark.read.parquet(path)


def lire_csv(spark, path, header=True, inferSchema=True, sep=","):
    """Lit un fichier CSV"""
    return spark.read.csv(path, header=header, inferSchema=inferSchema, sep=sep)


def lire_table_sql(spark, table_name):
    """Lit une table Spark SQL"""
    return spark.read.table(table_name)


def lire_jdbc(spark, url, table, properties):
    """Lit une table via JDBC"""
    return spark.read.jdbc(url=url, table=table, properties=properties)


def lire_json(spark, path, multiLine=True):
    """Lit un fichier JSON"""
    return spark.read.json(path, multiLine=multiLine)


def lire_text(spark, path):
    """Lit un fichier texte brut"""
    return spark.read.text(path)


def lire_xml(spark, path, rowTag):
    """Lit un fichier XML (nécessite spark-xml)"""
    return spark.read.format("xml").option("rowTag", rowTag).load(path)


def lire_avro(spark, path):
    """Lit un fichier Avro"""
    return spark.read.format("avro").load(path)


def lire_delta(spark, path):
    """Lit un fichier Delta Lake"""
    return spark.read.format("delta").load(path)

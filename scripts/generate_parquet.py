"""
Script pour générer un fichier sinistres.parquet de test.
À exécuter une fois pour créer les données dans le dossier /data.

Options en ligne de commande:
    --samples N        Nombre d'échantillons à générer (défaut: 1000)
    --output PATH     Chemin du fichier Parquet de sortie (défaut: data/sinistres.parquet)
    --validate        Active la validation des données générées
"""

import argparse
import os
import platform
import random
from pathlib import Path
from typing import Dict, List, Tuple

from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType, StringType, StructField, StructType


def parse_args():
    """Parse les arguments en ligne de commande."""
    parser = argparse.ArgumentParser(description="Génère un fichier Parquet avec des données de sinistres simulées")
    parser.add_argument(
        "--samples",
        type=int,
        default=1000,
        help="Nombre d'échantillons à générer (défaut: 1000)",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="data/sinistres.parquet",
        help="Chemin du fichier Parquet de sortie (défaut: data/sinistres.parquet)",
    )
    parser.add_argument(
        "--validate",
        action="store_true",
        help="Active la validation des données générées",
    )
    return parser.parse_args()


def setup_env():
    """Configure les variables d'environnement pour Hadoop/Windows."""
    # Configuration Hadoop
    os.environ["HADOOP_HOME"] = "/opt/hadoop"  # Exemple Linux ou adapte selon CI
    # Configuration JAVA_HOME selon OS
    if platform.system() == "Windows":
        os.environ["JAVA_HOME"] = r"C:\Program Files\Java\jdk-8.0.472.8-hotspot"
        os.environ["PATH"] += os.pathsep + r"C:\hadoop\bin"
    else:
        # Sur Linux CI la variable JAVA_HOME peut être à sa valeur par défaut ou à configurer selon le runner
        # souvent openjdk est installé et JAVA_HOME est déjà correct
        pass


def create_spark_session():
    """Crée et configure la session Spark."""
    spark = (
        SparkSession.builder.appName("GenParquet")
        .master("local[*]")
        # Configurations pour Windows
        .config("spark.hadoop.io.native.lib.available", "false")
        .config("spark.hadoop.fs.file.impl", "org.apache.hadoop.fs.LocalFileSystem")
        .config(
            "spark.hadoop.fs.AbstractFileSystem.file.impl",
            "org.apache.hadoop.fs.local.LocalFs",
        )
        .config("spark.sql.warehouse.dir", "C:/tmp/spark-warehouse")
        # Options JVM : indiquer java.library.path pour que la JVM trouve les DLL natives
        .config(
            "spark.driver.extraJavaOptions",
            "-Djava.library.path=C:/hadoop/bin -Dderby.system.home=C:/tmp/derby",
        )
        .config(
            "spark.executor.extraJavaOptions",
            "-Djava.library.path=C:/hadoop/bin",
        )
        # Mémoire
        .config("spark.driver.memory", "2g")
        .config("spark.executor.memory", "2g")
        # Logs moins verbeux
        .config("spark.ui.showConsoleProgress", "false")
        .getOrCreate()
    )
    # ignorer les logs en console, y compris ceux liés au shutdown
    spark.sparkContext.setLogLevel("OFF")
    return spark


def get_schema():
    """Retourne le schéma des données."""
    return StructType(
        [
            StructField("client_id", StringType(), False),
            StructField("type_sinistre", StringType(), False),
            StructField("montant", IntegerType(), True),
        ]
    )


def validate_data(data: List[Tuple], columns: List[str]) -> Dict[str, bool]:
    """
    Valide les données générées.

    Vérifie :
    - Format des client_id
    - Types de sinistres valides
    - Plage des montants
    - Absence de doublons
    """
    types_valides = {
        "vol",
        "accident",
        "bris de glace",
        "incendie",
        "catastrophe naturelle",
    }
    montants_valides = {None, -500, 3000, 8000, 12000, 15000}
    client_ids = set()

    validation = {
        "format_client_id": True,
        "types_sinistres": True,
        "montants": True,
        "doublons": True,
    }

    for client_id, type_sinistre, montant in data:
        # Validation format client_id
        if not client_id.startswith("C") or not client_id[1:].isdigit():
            validation["format_client_id"] = False

        # Validation types de sinistres
        if type_sinistre not in types_valides:
            validation["types_sinistres"] = False

        # Validation montants
        if montant not in montants_valides:
            validation["montants"] = False

        # Vérification doublons
        if client_id in client_ids:
            validation["doublons"] = False
        client_ids.add(client_id)

    return validation


def generate_data(n_samples: int = 1000) -> Tuple[List[Tuple], List[str]]:
    """Génère les données de test des sinistres."""
    types = ["vol", "accident", "bris de glace", "incendie", "catastrophe naturelle"]
    data = []

    for i in range(n_samples):
        client_id = f"C{i:04d}"
        type_sinistre = random.choice(types)
        montant = random.choice([None, -500, 3000, 8000, 12000, 15000])
        data.append((client_id, type_sinistre, montant))

    columns = ["client_id", "type_sinistre", "montant"]
    return data, columns


def save_parquet(
    spark: SparkSession,
    data: List[Tuple],
    columns: List[str],
    output_path: str = "data/sinistres.parquet",
):
    """Sauvegarde les données en format Parquet."""
    # Création du DataFrame avec schéma explicite
    df = spark.createDataFrame(data, schema=get_schema())

    # Création du dossier parent si nécessaire
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    # Sauvegarde en Parquet
    df.write.mode("overwrite").parquet(output_path)


def main():
    """Fonction principale."""
    # Parse les arguments
    args = parse_args()

    # 1. Configuration de l'environnement
    setup_env()

    # 2. Création de la session Spark
    spark = create_spark_session()

    try:
        # 3. Génération des données
        data, columns = generate_data(args.samples)

        # 4. Validation si demandée
        if args.validate:
            print("\n🔍 Validation des données générées...")
            validation = validate_data(data, columns)
            for check, result in validation.items():
                status = "✅" if result else "❌"
                print(f"{status} {check}")

            if not all(validation.values()):
                print("\n❌ Validation échouée. Arrêt du script.")
                return
            print("✅ Validation réussie\n")

        # 5. Sauvegarde en Parquet
        save_parquet(spark, data, columns, args.output)

        print(f"✅ Fichier Parquet généré dans : {args.output}")
        print(f"   Nombre d'échantillons : {args.samples}")

    finally:
        # 6. Arrêt propre de Spark
        spark.stop()


if __name__ == "__main__":
    main()

import os
import sys

import pytest
from pyspark.sql import SparkSession

# Cela permet à tous tes tests d’importer les modules de src/ sans erreur.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))


@pytest.fixture(scope="session")
def spark():
    """Session Spark partagée pour tous les tests."""
    return SparkSession.builder.appName("TestSuite").master("local[*]").getOrCreate()

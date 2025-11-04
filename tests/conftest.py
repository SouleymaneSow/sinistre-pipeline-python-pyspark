import os
import sys

# Cela permet à tous tes tests d’importer les modules de src/ sans erreur.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

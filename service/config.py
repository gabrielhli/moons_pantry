"""
Global Configurations for Moon's Pantry
"""
import os

DATABASE_URI = os.getenv("DATABASE_URI", "mongodb://localhost:27017")

#!/usr/bin/env python3

import sys
import traceback
from database import DatabaseManager

def debug_database():
    print("=== Database Connection Debug ===")
    
    try:
        db = DatabaseManager()
        print(f"Config: {db.config.DB_HOST}:{db.config.DB_PORT}")
        print(f"User: {db.config.DB_USER}")
        print(f"Password: {'*' * len(db.config.DB_PASSWORD) if db.config.DB_PASSWORD else 'None'}")
        
        print("\n1. Testing basic connection...")
        databases = db.get_databases()
        print(f"✓ Found {len(databases)} databases: {databases}")
        
        if 'prod_dil' in databases:
            print("\n2. Testing prod_dil tables...")
            tables = db.get_tables('prod_dil')
            print(f"✓ Found {len(tables)} tables in prod_dil: {tables}")
        else:
            print("\n✗ 'prod_dil' database not found in available databases")
            print("Available databases are:", databases)
            
        print("\n=== Debug Complete ===")
        
    except Exception as e:
        print(f"\n✗ Error occurred: {str(e)}")
        print("\nFull traceback:")
        traceback.print_exc()
        
        # Additional debugging
        print("\n=== Additional Debug Info ===")
        try:
            import pymysql
            print("✓ pymysql imported successfully")
        except ImportError as ie:
            print(f"✗ pymysql import failed: {ie}")
            
        try:
            from sqlalchemy import create_engine
            print("✓ sqlalchemy imported successfully")
        except ImportError as ie:
            print(f"✗ sqlalchemy import failed: {ie}")

if __name__ == "__main__":
    debug_database()

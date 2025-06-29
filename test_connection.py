#!/usr/bin/env python3

import os
from dotenv import load_dotenv
import pymysql

# Load environment variables
load_dotenv()

def test_direct_connection():
    """Test direct PyMySQL connection"""
    print("=== Testing Direct PyMySQL Connection ===")
    
    try:
        connection = pymysql.connect(
            host=os.getenv("DB_HOST", "localhost"),
            port=int(os.getenv("DB_PORT", 3306)),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", ""),
            charset='utf8mb4'
        )
        
        print("✓ Direct connection successful!")
        
        with connection.cursor() as cursor:
            cursor.execute("SHOW DATABASES")
            databases = [row[0] for row in cursor.fetchall()]
            print(f"✓ Found databases: {databases}")
            
            if 'prod_dil' in databases:
                print("✓ prod_dil database found!")
                cursor.execute("USE prod_dil")
                cursor.execute("SHOW TABLES")
                tables = [row[0] for row in cursor.fetchall()]
                print(f"✓ Tables in prod_dil: {tables}")
            else:
                print("✗ prod_dil database not found")
                
        connection.close()
        return True
        
    except Exception as e:
        print(f"✗ Direct connection failed: {str(e)}")
        return False

def test_sqlalchemy_connection():
    """Test SQLAlchemy connection"""
    print("\n=== Testing SQLAlchemy Connection ===")
    
    try:
        from database import DatabaseManager
        
        db = DatabaseManager()
        print(f"Connection URL pattern: mysql+pymysql://user:***@{db.config.DB_HOST}:{db.config.DB_PORT}/")
        
        databases = db.get_databases()
        print(f"✓ SQLAlchemy connection successful!")
        print(f"✓ Found {len(databases)} databases: {databases}")
        
        if 'prod_dil' in databases:
            tables = db.get_tables('prod_dil')
            print(f"✓ Found {len(tables)} tables in prod_dil: {tables}")
        else:
            print("✗ prod_dil not found in available databases")
            
        return True
        
    except Exception as e:
        print(f"✗ SQLAlchemy connection failed: {str(e)}")
        import traceback
        print("Full traceback:")
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Database Connection Test")
    print("=" * 50)
    
    # Show configuration (without password)
    print(f"Host: {os.getenv('DB_HOST', 'localhost')}")
    print(f"Port: {os.getenv('DB_PORT', '3306')}")
    print(f"User: {os.getenv('DB_USER', 'root')}")
    print(f"Password: {'*' * len(os.getenv('DB_PASSWORD', ''))}")
    print()
    
    # Test both connection methods
    direct_ok = test_direct_connection()
    sqlalchemy_ok = test_sqlalchemy_connection()
    
    print("\n" + "=" * 50)
    if direct_ok and sqlalchemy_ok:
        print("✓ All tests passed! Your database connection is working.")
    else:
        print("✗ Some tests failed. Check your database configuration.")

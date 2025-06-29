import pymysql
from sqlalchemy import create_engine, text
from typing import List, Dict, Any
from config import Config

class DatabaseManager:
    def __init__(self):
        self.config = Config()
    
    def get_connection_url(self, database_name: str = None):
        """Create database connection URL"""
        # URL encode password to handle special characters
        from urllib.parse import quote_plus
        encoded_password = quote_plus(self.config.DB_PASSWORD)
        
        if database_name:
            return f"mysql+pymysql://{self.config.DB_USER}:{encoded_password}@{self.config.DB_HOST}:{self.config.DB_PORT}/{database_name}?charset=utf8mb4"
        return f"mysql+pymysql://{self.config.DB_USER}:{encoded_password}@{self.config.DB_HOST}:{self.config.DB_PORT}?charset=utf8mb4"
    
    def get_databases(self) -> List[str]:
        """Get list of available databases"""
        try:
            engine = create_engine(self.get_connection_url())
            with engine.connect() as conn:
                result = conn.execute(text("SHOW DATABASES"))
                databases = [row[0] for row in result.fetchall()]
                # Filter out system databases
                filtered_dbs = [db for db in databases if db not in ['information_schema', 'performance_schema', 'mysql', 'sys']]
                return filtered_dbs
        except Exception as e:
            raise Exception(f"Failed to get databases: {str(e)}")
    
    def get_tables(self, database_name: str) -> List[str]:
        """Get list of tables in a database"""
        try:
            engine = create_engine(self.get_connection_url(database_name))
            with engine.connect() as conn:
                result = conn.execute(text("SHOW TABLES"))
                return [row[0] for row in result.fetchall()]
        except Exception as e:
            raise Exception(f"Failed to get tables for database {database_name}: {str(e)}")
    
    def get_table_columns(self, database_name: str, table_name: str) -> List[Dict[str, Any]]:
        """Get column information for a table"""
        try:
            engine = create_engine(self.get_connection_url(database_name))
            with engine.connect() as conn:
                query = text(f"DESCRIBE {table_name}")
                result = conn.execute(query)
                columns = []
                for row in result.fetchall():
                    columns.append({
                        "name": row[0],
                        "type": row[1],
                        "null": row[2],
                        "key": row[3],
                        "default": row[4],
                        "extra": row[5]
                    })
                return columns
        except Exception as e:
            raise Exception(f"Failed to get columns for table {table_name}: {str(e)}")
    
    def get_sample_data(self, database_name: str, table_name: str, limit: int = 10) -> List[Dict[str, Any]]:
        """Get sample data from a table"""
        try:
            engine = create_engine(self.get_connection_url(database_name))
            with engine.connect() as conn:
                query = text(f"SELECT * FROM {table_name} LIMIT {limit}")
                result = conn.execute(query)
                columns = result.keys()
                return [dict(zip(columns, row)) for row in result.fetchall()]
        except Exception as e:
            raise Exception(f"Failed to get sample data from table {table_name}: {str(e)}")
    
    def execute_query(self, database_name: str, query: str) -> List[Dict[str, Any]]:
        """Execute a custom query"""
        try:
            engine = create_engine(self.get_connection_url(database_name))
            with engine.connect() as conn:
                result = conn.execute(text(query))
                columns = result.keys()
                return [dict(zip(columns, row)) for row in result.fetchall()]
        except Exception as e:
            raise Exception(f"Failed to execute query: {str(e)}")
    
    def insert_data(self, database_name: str, table_name: str, data: List[Dict[str, Any]]) -> bool:
        """Insert masked data into target table"""
        try:
            engine = create_engine(self.get_connection_url(database_name))
            with engine.begin() as conn:  # Use begin() for auto-commit
                if data:
                    columns = list(data[0].keys())
                    placeholders = ', '.join([f':{col}' for col in columns])
                    query = text(f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({placeholders})")
                    conn.execute(query, data)
                return True
        except Exception as e:
            raise Exception(f"Failed to insert data into {table_name}: {str(e)}")

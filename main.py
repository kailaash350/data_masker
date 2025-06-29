from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict, Any
import logging
import os
from dotenv import load_dotenv

# Load environment variables at startup
load_dotenv(override=True)

from database import DatabaseManager
from masking import DataMasker
from models import *

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Data Masker API",
    description="API for masking production data and transferring to lower environments",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Debug: Print environment variables (remove in production)
logger.info(f"DB_HOST: {os.getenv('DB_HOST', 'NOT_SET')}")
logger.info(f"DB_USER: {os.getenv('DB_USER', 'NOT_SET')}")
logger.info(f"DB_PASSWORD: {'SET' if os.getenv('DB_PASSWORD') else 'NOT_SET'}")

# Initialize services
db_manager = DatabaseManager()
data_masker = DataMasker()

@app.get("/", response_model=ApiResponse)
async def root():
    """Root endpoint"""
    return ApiResponse(
        success=True,
        message="Data Masker API is running",
        data={"version": "1.0.0"}
    )

@app.get("/databases", response_model=ApiResponse)
async def get_databases():
    """Get list of available databases"""
    try:
        databases = db_manager.get_databases()
        return ApiResponse(
            success=True,
            message="Databases retrieved successfully",
            data=databases
        )
    except Exception as e:
        logger.error(f"Error getting databases: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/databases/{database_name}/tables", response_model=ApiResponse)
async def get_tables(database_name: str):
    """Get list of tables in a database"""
    try:
        logger.info(f"Getting tables for database: {database_name}")
        tables = db_manager.get_tables(database_name)
        logger.info(f"Found {len(tables)} tables in database {database_name}")
        return ApiResponse(
            success=True,
            message=f"Tables retrieved successfully for database {database_name}",
            data=tables
        )
    except Exception as e:
        logger.error(f"Error getting tables for database {database_name}: {str(e)}")
        import traceback
        logger.error(f"Full traceback: {traceback.format_exc()}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/databases/{database_name}/tables/{table_name}/columns", response_model=ApiResponse)
async def get_table_columns(database_name: str, table_name: str):
    """Get column information for a table"""
    try:
        columns = db_manager.get_table_columns(database_name, table_name)
        return ApiResponse(
            success=True,
            message=f"Columns retrieved successfully for table {table_name}",
            data=columns
        )
    except Exception as e:
        logger.error(f"Error getting columns for table {table_name}: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/sample-data", response_model=ApiResponse)
async def get_sample_data(request: SampleDataRequest):
    """Get sample data from a table"""
    try:
        sample_data = db_manager.get_sample_data(
            request.database_name, 
            request.table_name, 
            request.limit
        )
        return ApiResponse(
            success=True,
            message=f"Sample data retrieved successfully",
            data=sample_data
        )
    except Exception as e:
        logger.error(f"Error getting sample data: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/masking-types", response_model=ApiResponse)
async def get_masking_types():
    """Get available masking types"""
    try:
        masking_types = data_masker.get_available_masking_types()
        return ApiResponse(
            success=True,
            message="Masking types retrieved successfully",
            data=masking_types
        )
    except Exception as e:
        logger.error(f"Error getting masking types: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/preview", response_model=ApiResponse)
async def preview_masked_data(request: PreviewRequest):
    """Preview how data will look after masking"""
    try:
        # Get original data
        original_data = db_manager.get_sample_data(
            request.database_name,
            request.table_name,
            request.limit
        )
        
        # Get column information
        columns = db_manager.get_table_columns(request.database_name, request.table_name)
        
        # Apply masking
        masked_data = data_masker.apply_masking(original_data, request.masking_config)
        
        preview = DataPreview(
            original_data=original_data,
            masked_data=masked_data,
            columns=columns,
            masking_config=request.masking_config
        )
        
        return ApiResponse(
            success=True,
            message="Data preview generated successfully",
            data=preview.dict()
        )
    except Exception as e:
        logger.error(f"Error generating preview: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/ship", response_model=ApiResponse)
async def ship_data(request: ShippingRequest):
    """Ship masked data to target environment"""
    try:
        # Security check: Ensure masking config is not empty for sensitive operations
        if not request.masking_config or all(v == 'none' for v in request.masking_config.values()):
            logger.warning("Attempted to ship data without any masking applied")
            raise HTTPException(
                status_code=400, 
                detail="At least one column must have masking applied for security"
            )
        
        # Get all data from source table
        source_data = db_manager.execute_query(
            request.source_database,
            f"SELECT * FROM {request.source_table}"
        )
        
        if not source_data:
            raise HTTPException(status_code=400, detail="No data found in source table")
        
        # Apply masking
        masked_data = data_masker.apply_masking(source_data, request.masking_config)
        
        # Create target table if requested (copy structure)
        if request.create_table_if_not_exists:
            try:
                # Get source table structure
                create_table_query = f"""
                CREATE TABLE IF NOT EXISTS {request.target_table} 
                LIKE {request.source_database}.{request.source_table}
                """
                db_manager.execute_query(request.target_database, create_table_query)
            except Exception as e:
                logger.warning(f"Could not create table structure: {str(e)}")
        
        # Clear target table before inserting
        try:
            db_manager.execute_query(request.target_database, f"DELETE FROM {request.target_table}")
        except Exception as e:
            logger.warning(f"Could not clear target table: {str(e)}")
        
        # Insert masked data
        db_manager.insert_data(request.target_database, request.target_table, masked_data)
        
        result = ShippingResult(
            success=True,
            message="Data shipped successfully",
            records_transferred=len(masked_data),
            target_database=request.target_database,
            target_table=request.target_table
        )
        
        logger.info(f"Successfully shipped {len(masked_data)} records to {request.target_database}.{request.target_table}")
        
        return ApiResponse(
            success=True,
            message="Data shipped successfully",
            data=result.dict()
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error shipping data: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health", response_model=ApiResponse)
async def health_check():
    """Health check endpoint"""
    try:
        # Test database connection
        databases = db_manager.get_databases()
        return ApiResponse(
            success=True,
            message="Service is healthy",
            data={"database_connection": "OK", "available_databases": len(databases)}
        )
    except Exception as e:
        logger.error(f"Health check failed: {str(e)}")
        raise HTTPException(status_code=503, detail="Service unhealthy")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

from pydantic import BaseModel
from typing import List, Dict, Any, Optional

class DatabaseInfo(BaseModel):
    name: str

class TableInfo(BaseModel):
    name: str

class ColumnInfo(BaseModel):
    name: str
    type: str
    null: str
    key: str
    default: Optional[str]
    extra: str

class SampleDataRequest(BaseModel):
    database_name: str
    table_name: str
    limit: int = 10

class MaskingConfig(BaseModel):
    column_name: str
    masking_type: str

class PreviewRequest(BaseModel):
    database_name: str
    table_name: str
    masking_config: Dict[str, str]
    limit: int = 10

class ShippingRequest(BaseModel):
    source_database: str
    source_table: str
    target_database: str
    target_table: str
    masking_config: Dict[str, str]
    create_table_if_not_exists: bool = True

class MaskingType(BaseModel):
    type: str
    description: str

class ApiResponse(BaseModel):
    success: bool
    message: str
    data: Optional[Any] = None

class DataPreview(BaseModel):
    original_data: List[Dict[str, Any]]
    masked_data: List[Dict[str, Any]]
    columns: List[ColumnInfo]
    masking_config: Dict[str, str]

class ShippingResult(BaseModel):
    success: bool
    message: str
    records_transferred: int
    target_database: str
    target_table: str

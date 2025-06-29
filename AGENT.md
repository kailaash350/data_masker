# Data Masker API Project

## Development Commands

### Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python run.py
# or
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### API Documentation
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Project Structure

- `main.py` - FastAPI application with all endpoints
- `database.py` - Database connection and operations
- `masking.py` - Data masking algorithms with referential integrity
- `models.py` - Pydantic models for API requests/responses
- `config.py` - Configuration management
- `.env` - Environment variables (database credentials)
- `requirements.txt` - Python dependencies

## API Endpoints

1. `GET /databases` - List available databases
2. `GET /databases/{db}/tables` - List tables in database
3. `GET /databases/{db}/tables/{table}/columns` - Get table columns
4. `POST /sample-data` - Get sample data from table
5. `GET /masking-types` - Get available masking types
6. `POST /preview` - Preview masked data
7. `POST /ship` - Ship masked data to target environment
8. `GET /health` - Health check

## Features

- ✅ Database connection and exploration
- ✅ **47 comprehensive masking types** covering industry standards:
  - **Names**: First, Last, Full, Organization
  - **Location**: Street address, City, State, ZIP, Country, GPS coordinates, PO Box
  - **Contact**: Email, Phone
  - **Credentials**: Username, Password
  - **Financial**: Credit cards, IBAN, SWIFT, Money amounts, Bitcoin addresses
  - **Identification**: SSN, Passport, Driver's license, Birth dates, Gender
  - **Personal**: Marital status
  - **Accounts**: Account numbers, Generic IDs
  - **Network**: IP addresses, MAC addresses, URLs
  - **Vehicle**: VIN, License plates
  - **Medical**: Medical record numbers, ICD codes
  - **Generic**: Text, Numeric
- ✅ Referential integrity through deterministic seeding
- ✅ Security check to prevent unmasked data transfer
- ✅ Swagger UI documentation
- ✅ CORS enabled for frontend integration
- ✅ Comprehensive error handling and logging

## Security Features

- Prevents shipping data without masking applied
- Uses deterministic seeds for referential integrity
- Environment-based configuration
- Input validation and sanitization

## Database Configuration

Update `.env` file with your MySQL credentials:
```
DB_HOST=localhost
DB_PORT=3306
DB_USER=your_username
DB_PASSWORD=your_password
```

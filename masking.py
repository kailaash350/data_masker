import random
import hashlib
import re
import ipaddress
from faker import Faker
from typing import Any, Dict, List
from datetime import datetime, timedelta
from config import Config

class DataMasker:
    def __init__(self):
        self.config = Config()
        self.faker = Faker()
        # Set seed for referential integrity
        random.seed(self.config.MASKING_SEED)
        Faker.seed(self.config.MASKING_SEED)
        
        # Cache for maintaining referential integrity
        self.mapping_cache = {}
    
    def get_deterministic_seed(self, value: Any) -> int:
        """Generate deterministic seed from value for referential integrity"""
        if value is None:
            return 0
        str_value = str(value)
        return int(hashlib.md5(str_value.encode()).hexdigest()[:8], 16)
    
    def mask_first_name(self, original_value: Any) -> str:
        """Mask first names"""
        if original_value is None:
            return None
        
        cache_key = f"first_name_{original_value}"
        if cache_key in self.mapping_cache:
            return self.mapping_cache[cache_key]
        
        seed = self.get_deterministic_seed(original_value)
        temp_faker = Faker()
        temp_faker.seed_instance(seed)
        
        masked_value = temp_faker.first_name()
        self.mapping_cache[cache_key] = masked_value
        return masked_value
    
    def mask_last_name(self, original_value: Any) -> str:
        """Mask last names"""
        if original_value is None:
            return None
        
        cache_key = f"last_name_{original_value}"
        if cache_key in self.mapping_cache:
            return self.mapping_cache[cache_key]
        
        seed = self.get_deterministic_seed(original_value)
        temp_faker = Faker()
        temp_faker.seed_instance(seed)
        
        masked_value = temp_faker.last_name()
        self.mapping_cache[cache_key] = masked_value
        return masked_value
    
    def mask_full_name(self, original_value: Any) -> str:
        """Mask full names"""
        if original_value is None:
            return None
        
        cache_key = f"full_name_{original_value}"
        if cache_key in self.mapping_cache:
            return self.mapping_cache[cache_key]
        
        seed = self.get_deterministic_seed(original_value)
        temp_faker = Faker()
        temp_faker.seed_instance(seed)
        
        masked_value = temp_faker.name()
        self.mapping_cache[cache_key] = masked_value
        return masked_value
    
    def mask_organization(self, original_value: Any) -> str:
        """Mask organization names"""
        if original_value is None:
            return None
        
        cache_key = f"organization_{original_value}"
        if cache_key in self.mapping_cache:
            return self.mapping_cache[cache_key]
        
        seed = self.get_deterministic_seed(original_value)
        temp_faker = Faker()
        temp_faker.seed_instance(seed)
        
        masked_value = temp_faker.company()
        self.mapping_cache[cache_key] = masked_value
        return masked_value
    
    def mask_email(self, original_value: Any) -> str:
        """Mask email addresses"""
        if original_value is None:
            return None
        
        cache_key = f"email_{original_value}"
        if cache_key in self.mapping_cache:
            return self.mapping_cache[cache_key]
        
        seed = self.get_deterministic_seed(original_value)
        temp_faker = Faker()
        temp_faker.seed_instance(seed)
        
        masked_value = temp_faker.email()
        self.mapping_cache[cache_key] = masked_value
        return masked_value
    
    def mask_phone(self, original_value: Any) -> str:
        """Mask phone numbers"""
        if original_value is None:
            return None
        
        cache_key = f"phone_{original_value}"
        if cache_key in self.mapping_cache:
            return self.mapping_cache[cache_key]
        
        seed = self.get_deterministic_seed(original_value)
        temp_faker = Faker()
        temp_faker.seed_instance(seed)
        
        masked_value = temp_faker.phone_number()
        self.mapping_cache[cache_key] = masked_value
        return masked_value
    
    def mask_street_address(self, original_value: Any) -> str:
        """Mask street addresses"""
        if original_value is None:
            return None
        
        cache_key = f"street_address_{original_value}"
        if cache_key in self.mapping_cache:
            return self.mapping_cache[cache_key]
        
        seed = self.get_deterministic_seed(original_value)
        temp_faker = Faker()
        temp_faker.seed_instance(seed)
        
        masked_value = temp_faker.street_address()
        self.mapping_cache[cache_key] = masked_value
        return masked_value
    
    def mask_city(self, original_value: Any) -> str:
        """Mask city names"""
        if original_value is None:
            return None
        
        cache_key = f"city_{original_value}"
        if cache_key in self.mapping_cache:
            return self.mapping_cache[cache_key]
        
        seed = self.get_deterministic_seed(original_value)
        temp_faker = Faker()
        temp_faker.seed_instance(seed)
        
        masked_value = temp_faker.city()
        self.mapping_cache[cache_key] = masked_value
        return masked_value
    
    def mask_state(self, original_value: Any) -> str:
        """Mask state names"""
        if original_value is None:
            return None
        
        cache_key = f"state_{original_value}"
        if cache_key in self.mapping_cache:
            return self.mapping_cache[cache_key]
        
        seed = self.get_deterministic_seed(original_value)
        temp_faker = Faker()
        temp_faker.seed_instance(seed)
        
        masked_value = temp_faker.state()
        self.mapping_cache[cache_key] = masked_value
        return masked_value
    
    def mask_state_abbr(self, original_value: Any) -> str:
        """Mask state abbreviations"""
        if original_value is None:
            return None
        
        cache_key = f"state_abbr_{original_value}"
        if cache_key in self.mapping_cache:
            return self.mapping_cache[cache_key]
        
        seed = self.get_deterministic_seed(original_value)
        temp_faker = Faker()
        temp_faker.seed_instance(seed)
        
        masked_value = temp_faker.state_abbr()
        self.mapping_cache[cache_key] = masked_value
        return masked_value
    
    def mask_country(self, original_value: Any) -> str:
        """Mask country names"""
        if original_value is None:
            return None
        
        cache_key = f"country_{original_value}"
        if cache_key in self.mapping_cache:
            return self.mapping_cache[cache_key]
        
        seed = self.get_deterministic_seed(original_value)
        temp_faker = Faker()
        temp_faker.seed_instance(seed)
        
        masked_value = temp_faker.country()
        self.mapping_cache[cache_key] = masked_value
        return masked_value
    
    def mask_zip_code(self, original_value: Any) -> str:
        """Mask ZIP codes"""
        if original_value is None:
            return None
        
        cache_key = f"zip_code_{original_value}"
        if cache_key in self.mapping_cache:
            return self.mapping_cache[cache_key]
        
        seed = self.get_deterministic_seed(original_value)
        temp_faker = Faker()
        temp_faker.seed_instance(seed)
        
        masked_value = temp_faker.zipcode()
        self.mapping_cache[cache_key] = masked_value
        return masked_value
    
    def mask_postal_code(self, original_value: Any) -> str:
        """Mask postal codes"""
        if original_value is None:
            return None
        
        cache_key = f"postal_code_{original_value}"
        if cache_key in self.mapping_cache:
            return self.mapping_cache[cache_key]
        
        seed = self.get_deterministic_seed(original_value)
        temp_faker = Faker()
        temp_faker.seed_instance(seed)
        
        masked_value = temp_faker.postcode()
        self.mapping_cache[cache_key] = masked_value
        return masked_value
    
    def mask_po_box(self, original_value: Any) -> str:
        """Mask PO Box numbers"""
        if original_value is None:
            return None
        
        cache_key = f"po_box_{original_value}"
        if cache_key in self.mapping_cache:
            return self.mapping_cache[cache_key]
        
        seed = self.get_deterministic_seed(original_value)
        random.seed(seed)
        
        masked_value = f"PO Box {random.randint(1000, 99999)}"
        self.mapping_cache[cache_key] = masked_value
        return masked_value
    
    def mask_gps_coordinates(self, original_value: Any) -> str:
        """Mask GPS coordinates"""
        if original_value is None:
            return None
        
        cache_key = f"gps_{original_value}"
        if cache_key in self.mapping_cache:
            return self.mapping_cache[cache_key]
        
        seed = self.get_deterministic_seed(original_value)
        temp_faker = Faker()
        temp_faker.seed_instance(seed)
        
        lat = temp_faker.latitude()
        lon = temp_faker.longitude()
        masked_value = f"{lat}, {lon}"
        self.mapping_cache[cache_key] = masked_value
        return masked_value
    
    def mask_card_number(self, original_value: Any) -> str:
        """Mask card numbers, keeping last 4 digits"""
        if original_value is None:
            return None
        
        str_value = str(original_value).replace('-', '').replace(' ', '')
        if len(str_value) < 4:
            return str_value
        
        # Keep last 4 digits, mask the rest
        last_four = str_value[-4:]
        masked_prefix = '*' * (len(str_value) - 4)
        return f"{masked_prefix}{last_four}"
    
    def mask_ssn(self, original_value: Any) -> str:
        """Mask SSN, keeping last 4 digits"""
        if original_value is None:
            return None
        
        str_value = str(original_value).replace('-', '')
        if len(str_value) < 4:
            return str_value
        
        last_four = str_value[-4:]
        return f"***-**-{last_four}"
    
    def mask_id(self, original_value: Any) -> Any:
        """Mask ID fields while maintaining referential integrity"""
        if original_value is None:
            return None
        
        cache_key = f"id_{original_value}"
        if cache_key in self.mapping_cache:
            return self.mapping_cache[cache_key]
        
        # Generate deterministic but different ID
        seed = self.get_deterministic_seed(original_value)
        random.seed(seed)
        
        original_str = str(original_value)
        
        # Check if ID is purely numeric
        if original_str.isdigit():
            # Handle numeric IDs
            original_int = int(original_str)
            if original_int < 1000:
                masked_value = random.randint(10000, 99999)
            elif original_int < 10000:
                masked_value = random.randint(100000, 999999)
            else:
                masked_value = random.randint(original_int * 2, original_int * 5)
        else:
            # Handle alphanumeric IDs (like CUST_83768938)
            # Extract prefix and numeric parts
            import re
            
            # Find all alphabetic prefixes and numeric parts
            parts = re.findall(r'[A-Za-z]+|\d+', original_str)
            
            masked_parts = []
            for part in parts:
                if part.isalpha():
                    # Keep alphabetic parts but potentially change them
                    temp_faker = Faker()
                    temp_faker.seed_instance(seed + len(part))
                    # Generate similar length alphabetic string
                    if len(part) <= 4:
                        masked_part = temp_faker.lexify('?' * len(part)).upper()
                    else:
                        masked_part = part  # Keep long prefixes as is
                    masked_parts.append(masked_part)
                elif part.isdigit():
                    # Mask numeric parts
                    original_num = int(part)
                    if original_num < 1000:
                        masked_num = random.randint(10000, 99999)
                    else:
                        # Generate number with similar length
                        num_digits = len(part)
                        min_val = 10 ** (num_digits - 1)
                        max_val = (10 ** num_digits) - 1
                        masked_num = random.randint(min_val, max_val)
                    masked_parts.append(str(masked_num))
                else:
                    # Keep separators and special characters
                    masked_parts.append(part)
            
            # Handle separators between parts
            separators = re.findall(r'[^A-Za-z0-9]', original_str)
            
            # Reconstruct the ID
            if separators:
                # Reconstruct with original separators
                masked_value = ""
                part_idx = 0
                sep_idx = 0
                
                for char in original_str:
                    if char.isalnum():
                        if part_idx < len(masked_parts):
                            if not masked_value or not masked_value.endswith(masked_parts[part_idx]):
                                masked_value += masked_parts[part_idx]
                                part_idx += 1
                    else:
                        masked_value += char
                        
                # Fallback: join with underscores if reconstruction fails
                if not masked_value or len(masked_value) < 3:
                    masked_value = '_'.join(masked_parts)
            else:
                # No separators, just concatenate
                masked_value = ''.join(masked_parts)
        
        self.mapping_cache[cache_key] = masked_value
        return masked_value
    
    def mask_username(self, original_value: Any) -> str:
        """Mask usernames"""
        if original_value is None:
            return None
        
        cache_key = f"username_{original_value}"
        if cache_key in self.mapping_cache:
            return self.mapping_cache[cache_key]
        
        seed = self.get_deterministic_seed(original_value)
        temp_faker = Faker()
        temp_faker.seed_instance(seed)
        
        masked_value = temp_faker.user_name()
        self.mapping_cache[cache_key] = masked_value
        return masked_value
    
    def mask_password(self, original_value: Any) -> str:
        """Mask passwords with fake passwords"""
        if original_value is None:
            return None
        
        cache_key = f"password_{original_value}"
        if cache_key in self.mapping_cache:
            return self.mapping_cache[cache_key]
        
        seed = self.get_deterministic_seed(original_value)
        temp_faker = Faker()
        temp_faker.seed_instance(seed)
        
        masked_value = temp_faker.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True)
        self.mapping_cache[cache_key] = masked_value
        return masked_value
    
    def mask_iban(self, original_value: Any) -> str:
        """Mask International Bank Account Numbers"""
        if original_value is None:
            return None
        
        cache_key = f"iban_{original_value}"
        if cache_key in self.mapping_cache:
            return self.mapping_cache[cache_key]
        
        seed = self.get_deterministic_seed(original_value)
        temp_faker = Faker()
        temp_faker.seed_instance(seed)
        
        masked_value = temp_faker.iban()
        self.mapping_cache[cache_key] = masked_value
        return masked_value
    
    def mask_swift_code(self, original_value: Any) -> str:
        """Mask SWIFT codes"""
        if original_value is None:
            return None
        
        cache_key = f"swift_{original_value}"
        if cache_key in self.mapping_cache:
            return self.mapping_cache[cache_key]
        
        seed = self.get_deterministic_seed(original_value)
        temp_faker = Faker()
        temp_faker.seed_instance(seed)
        
        # Generate fake SWIFT code (8 or 11 characters)
        bank_code = temp_faker.lexify('????').upper()
        country_code = temp_faker.country_code()
        location_code = temp_faker.lexify('??').upper()
        branch_code = temp_faker.lexify('???').upper()
        
        masked_value = f"{bank_code}{country_code}{location_code}{branch_code}"
        self.mapping_cache[cache_key] = masked_value
        return masked_value
    
    def mask_money_amount(self, original_value: Any) -> str:
        """Mask money amounts"""
        if original_value is None:
            return None
        
        cache_key = f"money_{original_value}"
        if cache_key in self.mapping_cache:
            return self.mapping_cache[cache_key]
        
        seed = self.get_deterministic_seed(original_value)
        random.seed(seed)
        
        # Try to preserve the scale of the original amount
        try:
            original_float = float(str(original_value).replace(',', '').replace('$', ''))
            if original_float < 100:
                masked_amount = round(random.uniform(50, 500), 2)
            elif original_float < 1000:
                masked_amount = round(random.uniform(500, 2000), 2)
            elif original_float < 10000:
                masked_amount = round(random.uniform(2000, 20000), 2)
            else:
                masked_amount = round(random.uniform(original_float * 0.5, original_float * 1.5), 2)
        except:
            masked_amount = round(random.uniform(100, 10000), 2)
        
        masked_value = f"${masked_amount:,.2f}"
        self.mapping_cache[cache_key] = masked_value
        return masked_value
    
    def mask_btc_address(self, original_value: Any) -> str:
        """Mask Bitcoin addresses"""
        if original_value is None:
            return None
        
        cache_key = f"btc_{original_value}"
        if cache_key in self.mapping_cache:
            return self.mapping_cache[cache_key]
        
        seed = self.get_deterministic_seed(original_value)
        random.seed(seed)
        
        # Generate fake Bitcoin address (starts with 1, 3, or bc1)
        prefixes = ['1', '3', 'bc1']
        prefix = random.choice(prefixes)
        
        if prefix == 'bc1':
            # Bech32 format
            chars = '023456789acdefghjklmnpqrstuvwxyz'
            length = random.randint(39, 59)
        else:
            # Base58 format
            chars = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
            length = random.randint(26, 35)
        
        address = prefix + ''.join(random.choice(chars) for _ in range(length))
        self.mapping_cache[cache_key] = address
        return address
    
    def mask_passport_number(self, original_value: Any) -> str:
        """Mask passport numbers"""
        if original_value is None:
            return None
        
        cache_key = f"passport_{original_value}"
        if cache_key in self.mapping_cache:
            return self.mapping_cache[cache_key]
        
        seed = self.get_deterministic_seed(original_value)
        random.seed(seed)
        
        # Generate fake passport number (varies by country, using generic format)
        letters = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(2))
        numbers = ''.join(random.choice('0123456789') for _ in range(7))
        masked_value = f"{letters}{numbers}"
        
        self.mapping_cache[cache_key] = masked_value
        return masked_value
    
    def mask_drivers_license(self, original_value: Any) -> str:
        """Mask driver's license numbers"""
        if original_value is None:
            return None
        
        cache_key = f"drivers_license_{original_value}"
        if cache_key in self.mapping_cache:
            return self.mapping_cache[cache_key]
        
        seed = self.get_deterministic_seed(original_value)
        temp_faker = Faker()
        temp_faker.seed_instance(seed)
        
        # Generate fake driver's license (generic format)
        masked_value = temp_faker.lexify('?????????')
        self.mapping_cache[cache_key] = masked_value.upper()
        return masked_value.upper()
    
    def mask_birth_date(self, original_value: Any) -> str:
        """Mask birth dates"""
        if original_value is None:
            return None
        
        cache_key = f"birth_date_{original_value}"
        if cache_key in self.mapping_cache:
            return self.mapping_cache[cache_key]
        
        seed = self.get_deterministic_seed(original_value)
        temp_faker = Faker()
        temp_faker.seed_instance(seed)
        
        # Generate birth date (18-80 years ago)
        end_date = datetime.now() - timedelta(days=18*365)
        start_date = datetime.now() - timedelta(days=80*365)
        
        masked_date = temp_faker.date_between(start_date=start_date, end_date=end_date)
        self.mapping_cache[cache_key] = str(masked_date)
        return str(masked_date)
    
    def mask_gender(self, original_value: Any) -> str:
        """Mask gender"""
        if original_value is None:
            return None
        
        cache_key = f"gender_{original_value}"
        if cache_key in self.mapping_cache:
            return self.mapping_cache[cache_key]
        
        seed = self.get_deterministic_seed(original_value)
        random.seed(seed)
        
        genders = ['Male', 'Female', 'Other', 'Prefer not to say']
        masked_value = random.choice(genders)
        
        self.mapping_cache[cache_key] = masked_value
        return masked_value
    
    def mask_marital_status(self, original_value: Any) -> str:
        """Mask marital status"""
        if original_value is None:
            return None
        
        cache_key = f"marital_{original_value}"
        if cache_key in self.mapping_cache:
            return self.mapping_cache[cache_key]
        
        seed = self.get_deterministic_seed(original_value)
        random.seed(seed)
        
        statuses = ['Single', 'Married', 'Divorced', 'Widowed', 'Separated']
        masked_value = random.choice(statuses)
        
        self.mapping_cache[cache_key] = masked_value
        return masked_value
    
    def mask_account_number(self, original_value: Any) -> str:
        """Mask account numbers"""
        if original_value is None:
            return None
        
        cache_key = f"account_{original_value}"
        if cache_key in self.mapping_cache:
            return self.mapping_cache[cache_key]
        
        seed = self.get_deterministic_seed(original_value)
        random.seed(seed)
        
        # Generate account number with similar length
        original_str = str(original_value)
        if original_str.isdigit():
            length = len(original_str)
            masked_value = ''.join(random.choice('0123456789') for _ in range(length))
        else:
            # Keep format but change values
            masked_value = ''.join(
                random.choice('0123456789') if c.isdigit() 
                else random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') if c.isupper()
                else random.choice('abcdefghijklmnopqrstuvwxyz') if c.islower()
                else c
                for c in original_str
            )
        
        self.mapping_cache[cache_key] = masked_value
        return masked_value
    
    def mask_ip_address(self, original_value: Any) -> str:
        """Mask IP addresses"""
        if original_value is None:
            return None
        
        cache_key = f"ip_{original_value}"
        if cache_key in self.mapping_cache:
            return self.mapping_cache[cache_key]
        
        seed = self.get_deterministic_seed(original_value)
        temp_faker = Faker()
        temp_faker.seed_instance(seed)
        
        # Detect if IPv4 or IPv6
        try:
            ip = ipaddress.ip_address(str(original_value))
            if isinstance(ip, ipaddress.IPv4Address):
                masked_value = temp_faker.ipv4()
            else:
                masked_value = temp_faker.ipv6()
        except:
            # Default to IPv4 if cannot parse
            masked_value = temp_faker.ipv4()
        
        self.mapping_cache[cache_key] = masked_value
        return masked_value
    
    def mask_mac_address(self, original_value: Any) -> str:
        """Mask MAC addresses"""
        if original_value is None:
            return None
        
        cache_key = f"mac_{original_value}"
        if cache_key in self.mapping_cache:
            return self.mapping_cache[cache_key]
        
        seed = self.get_deterministic_seed(original_value)
        random.seed(seed)
        
        # Generate fake MAC address
        mac = ':'.join(['%02x' % random.randint(0, 255) for _ in range(6)])
        self.mapping_cache[cache_key] = mac
        return mac
    
    def mask_url(self, original_value: Any) -> str:
        """Mask URLs"""
        if original_value is None:
            return None
        
        cache_key = f"url_{original_value}"
        if cache_key in self.mapping_cache:
            return self.mapping_cache[cache_key]
        
        seed = self.get_deterministic_seed(original_value)
        temp_faker = Faker()
        temp_faker.seed_instance(seed)
        
        masked_value = temp_faker.url()
        self.mapping_cache[cache_key] = masked_value
        return masked_value
    
    def mask_vin(self, original_value: Any) -> str:
        """Mask Vehicle Identification Numbers"""
        if original_value is None:
            return None
        
        cache_key = f"vin_{original_value}"
        if cache_key in self.mapping_cache:
            return self.mapping_cache[cache_key]
        
        seed = self.get_deterministic_seed(original_value)
        random.seed(seed)
        
        # Generate fake 17-character VIN
        chars = '0123456789ABCDEFGHJKLMNPRSTUVWXYZ'  # No I, O, Q
        vin = ''.join(random.choice(chars) for _ in range(17))
        
        self.mapping_cache[cache_key] = vin
        return vin
    
    def mask_license_plate(self, original_value: Any) -> str:
        """Mask license plate numbers"""
        if original_value is None:
            return None
        
        cache_key = f"license_plate_{original_value}"
        if cache_key in self.mapping_cache:
            return self.mapping_cache[cache_key]
        
        seed = self.get_deterministic_seed(original_value)
        temp_faker = Faker()
        temp_faker.seed_instance(seed)
        
        # Generate fake license plate
        masked_value = temp_faker.license_plate()
        self.mapping_cache[cache_key] = masked_value
        return masked_value
    
    def mask_medical_record_number(self, original_value: Any) -> str:
        """Mask medical record numbers"""
        if original_value is None:
            return None
        
        cache_key = f"mrn_{original_value}"
        if cache_key in self.mapping_cache:
            return self.mapping_cache[cache_key]
        
        seed = self.get_deterministic_seed(original_value)
        random.seed(seed)
        
        # Generate fake medical record number
        masked_value = f"MRN{random.randint(100000, 999999)}"
        self.mapping_cache[cache_key] = masked_value
        return masked_value
    
    def mask_icd_code(self, original_value: Any) -> str:
        """Mask ICD-9/ICD-10 codes"""
        if original_value is None:
            return None
        
        cache_key = f"icd_{original_value}"
        if cache_key in self.mapping_cache:
            return self.mapping_cache[cache_key]
        
        seed = self.get_deterministic_seed(original_value)
        random.seed(seed)
        
        # Generate fake ICD code
        if '.' in str(original_value):
            # ICD-10 format (A00.0)
            letter = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
            numbers = f"{random.randint(0, 99):02d}.{random.randint(0, 9)}"
            masked_value = f"{letter}{numbers}"
        else:
            # ICD-9 format (123.45)
            masked_value = f"{random.randint(100, 999)}.{random.randint(0, 99):02d}"
        
        self.mapping_cache[cache_key] = masked_value
        return masked_value
    
    def mask_generic_text(self, original_value: Any) -> str:
        """Generic text masking"""
        if original_value is None:
            return None
        
        cache_key = f"text_{original_value}"
        if cache_key in self.mapping_cache:
            return self.mapping_cache[cache_key]
        
        seed = self.get_deterministic_seed(original_value)
        temp_faker = Faker()
        temp_faker.seed_instance(seed)
        
        masked_value = temp_faker.text(max_nb_chars=len(str(original_value)))
        self.mapping_cache[cache_key] = masked_value
        return masked_value
    
    def mask_numeric(self, original_value: Any) -> Any:
        """Mask numeric values"""
        if original_value is None:
            return None
        
        try:
            num_value = float(original_value)
            seed = self.get_deterministic_seed(original_value)
            random.seed(seed)
            
            # Generate number in similar range
            if num_value == 0:
                return 0
            elif abs(num_value) < 100:
                return round(random.uniform(100, 999), 2)
            else:
                # Multiply by random factor between 1.5 and 3
                factor = random.uniform(1.5, 3.0)
                return round(num_value * factor, 2)
        except:
            return original_value
    
    def apply_masking(self, data: List[Dict[str, Any]], masking_config: Dict[str, str]) -> List[Dict[str, Any]]:
        """Apply masking to dataset based on configuration"""
        masked_data = []
        
        for row in data:
            masked_row = {}
            for column, value in row.items():
                masking_type = masking_config.get(column, 'none')
                
                if masking_type == 'none':
                    masked_row[column] = value
                # Names
                elif masking_type == 'first_name':
                    masked_row[column] = self.mask_first_name(value)
                elif masking_type == 'last_name':
                    masked_row[column] = self.mask_last_name(value)
                elif masking_type == 'full_name':
                    masked_row[column] = self.mask_full_name(value)
                elif masking_type == 'organization':
                    masked_row[column] = self.mask_organization(value)
                # Contact
                elif masking_type == 'email':
                    masked_row[column] = self.mask_email(value)
                elif masking_type == 'phone':
                    masked_row[column] = self.mask_phone(value)
                # Location
                elif masking_type == 'street_address':
                    masked_row[column] = self.mask_street_address(value)
                elif masking_type == 'city':
                    masked_row[column] = self.mask_city(value)
                elif masking_type == 'state':
                    masked_row[column] = self.mask_state(value)
                elif masking_type == 'state_abbr':
                    masked_row[column] = self.mask_state_abbr(value)
                elif masking_type == 'country':
                    masked_row[column] = self.mask_country(value)
                elif masking_type == 'zip_code':
                    masked_row[column] = self.mask_zip_code(value)
                elif masking_type == 'postal_code':
                    masked_row[column] = self.mask_postal_code(value)
                elif masking_type == 'po_box':
                    masked_row[column] = self.mask_po_box(value)
                elif masking_type == 'gps_coordinates':
                    masked_row[column] = self.mask_gps_coordinates(value)
                # Financial
                elif masking_type == 'card_number':
                    masked_row[column] = self.mask_card_number(value)
                elif masking_type == 'iban':
                    masked_row[column] = self.mask_iban(value)
                elif masking_type == 'swift_code':
                    masked_row[column] = self.mask_swift_code(value)
                elif masking_type == 'money_amount':
                    masked_row[column] = self.mask_money_amount(value)
                elif masking_type == 'btc_address':
                    masked_row[column] = self.mask_btc_address(value)
                # Credentials
                elif masking_type == 'username':
                    masked_row[column] = self.mask_username(value)
                elif masking_type == 'password':
                    masked_row[column] = self.mask_password(value)
                # Identification
                elif masking_type == 'ssn':
                    masked_row[column] = self.mask_ssn(value)
                elif masking_type == 'passport_number':
                    masked_row[column] = self.mask_passport_number(value)
                elif masking_type == 'drivers_license':
                    masked_row[column] = self.mask_drivers_license(value)
                elif masking_type == 'birth_date':
                    masked_row[column] = self.mask_birth_date(value)
                elif masking_type == 'gender':
                    masked_row[column] = self.mask_gender(value)
                elif masking_type == 'id':
                    masked_row[column] = self.mask_id(value)
                # Personal
                elif masking_type == 'marital_status':
                    masked_row[column] = self.mask_marital_status(value)
                # Accounts
                elif masking_type == 'account_number':
                    masked_row[column] = self.mask_account_number(value)
                # Network
                elif masking_type == 'ip_address':
                    masked_row[column] = self.mask_ip_address(value)
                elif masking_type == 'mac_address':
                    masked_row[column] = self.mask_mac_address(value)
                elif masking_type == 'url':
                    masked_row[column] = self.mask_url(value)
                # Vehicle
                elif masking_type == 'vin':
                    masked_row[column] = self.mask_vin(value)
                elif masking_type == 'license_plate':
                    masked_row[column] = self.mask_license_plate(value)
                # Medical
                elif masking_type == 'medical_record_number':
                    masked_row[column] = self.mask_medical_record_number(value)
                elif masking_type == 'icd_code':
                    masked_row[column] = self.mask_icd_code(value)
                # Generic
                elif masking_type == 'text':
                    masked_row[column] = self.mask_generic_text(value)
                elif masking_type == 'numeric':
                    masked_row[column] = self.mask_numeric(value)
                else:
                    masked_row[column] = value
            
            masked_data.append(masked_row)
        
        return masked_data
    
    def get_available_masking_types(self) -> List[Dict[str, str]]:
        """Get list of available masking types"""
        return [
            {"type": "none", "description": "No masking applied"},
            
            # Names
            {"type": "first_name", "description": "Replace with fake first names"},
            {"type": "last_name", "description": "Replace with fake last names"},
            {"type": "full_name", "description": "Replace with fake full names"},
            {"type": "organization", "description": "Replace with fake organization names"},
            
            # Location
            {"type": "street_address", "description": "Replace with fake street addresses"},
            {"type": "city", "description": "Replace with fake city names"},
            {"type": "state", "description": "Replace with fake state names"},
            {"type": "state_abbr", "description": "Replace with fake state abbreviations"},
            {"type": "country", "description": "Replace with fake country names"},
            {"type": "zip_code", "description": "Replace with fake ZIP codes"},
            {"type": "postal_code", "description": "Replace with fake postal codes"},
            {"type": "po_box", "description": "Replace with fake PO Box numbers"},
            {"type": "gps_coordinates", "description": "Replace with fake GPS coordinates"},
            
            # Contact Information
            {"type": "email", "description": "Replace with fake email addresses"},
            {"type": "phone", "description": "Replace with fake phone numbers"},
            
            # User Credentials
            {"type": "username", "description": "Replace with fake usernames"},
            {"type": "password", "description": "Replace with fake passwords"},
            
            # Financial Information
            {"type": "card_number", "description": "Mask all but last 4 digits of credit cards"},
            {"type": "iban", "description": "Replace with fake IBAN numbers"},
            {"type": "swift_code", "description": "Replace with fake SWIFT codes"},
            {"type": "money_amount", "description": "Replace with fake money amounts"},
            {"type": "btc_address", "description": "Replace with fake Bitcoin addresses"},
            
            # Identification
            {"type": "ssn", "description": "Mask all but last 4 digits of SSN"},
            {"type": "passport_number", "description": "Replace with fake passport numbers"},
            {"type": "drivers_license", "description": "Replace with fake driver's license numbers"},
            {"type": "birth_date", "description": "Replace with fake birth dates"},
            {"type": "gender", "description": "Replace with fake gender values"},
            
            # Other Personal Information
            {"type": "marital_status", "description": "Replace with fake marital status"},
            
            # Accounts and Licenses
            {"type": "account_number", "description": "Replace with fake account numbers"},
            {"type": "id", "description": "Replace with different ID maintaining referential integrity"},
            
            # Network and Web Location
            {"type": "ip_address", "description": "Replace with fake IP addresses"},
            {"type": "mac_address", "description": "Replace with fake MAC addresses"},
            {"type": "url", "description": "Replace with fake URLs"},
            
            # Vehicle Information
            {"type": "vin", "description": "Replace with fake Vehicle Identification Numbers"},
            {"type": "license_plate", "description": "Replace with fake license plate numbers"},
            
            # Medical Information
            {"type": "medical_record_number", "description": "Replace with fake medical record numbers"},
            {"type": "icd_code", "description": "Replace with fake ICD-9/ICD-10 codes"},
            
            # Generic
            {"type": "text", "description": "Replace with fake text"},
            {"type": "numeric", "description": "Replace with different numeric values"}
        ]

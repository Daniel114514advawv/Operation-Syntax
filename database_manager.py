import sqlite3
import time
import random
from typing import List, Tuple

class DatabaseManager:
    """Handles all database operations for the SQL Hacker Game"""
    
    def loading_animation(self, message: str, duration: float = None):
        """Display loading animation with random duration between 3-10 seconds"""
        if duration is None:
            duration = random.uniform(3.0, 8.0)  # Random between 3-8 seconds
        
        print(f"⚡ {message}", end="")
        
        # Calculate how many dots to show
        dots_count = int(duration * 2)  # 2 dots per second
        dot_delay = duration / dots_count
        
        for i in range(dots_count):
            print(".", end="", flush=True)
            time.sleep(dot_delay)
        
        print(" ✅ COMPLETE")
    def __init__(self, db_path: str = "mission_database.db"):
        self.db_path = db_path
        self.loading_animation("Establishing secure database connection", 4.0)
        self.setup_database()
    
    def setup_database(self):
        """Create the game database with sample data"""
        print("🔧 Debug: Setting up database...")
        self.loading_animation("Initializing secure database tables", 5.0)
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        try:
            # Create tables
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS employees (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    department TEXT,
                    clearance_level INTEGER,
                    shift_start TEXT,
                    shift_end TEXT,
                    weakness TEXT
                )
            ''')
            
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS security_logs (
                    id INTEGER PRIMARY KEY,
                    employee_id INTEGER,
                    location TEXT,
                    access_time TEXT,
                    action TEXT,
                    FOREIGN KEY (employee_id) REFERENCES employees (id)
                )
            ''')
            
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS facilities (
                    id INTEGER PRIMARY KEY,
                    room_name TEXT,
                    floor INTEGER,
                    security_level INTEGER,
                    guard_id INTEGER,
                    FOREIGN KEY (guard_id) REFERENCES employees (id)
                )
            ''')
            
            # Insert sample data
            employees_data = [
                (1, "Marcus Steel", "Security", 3, "22:00", "06:00", "coffee addiction"),
                (2, "Sarah Chen", "IT", 4, "09:00", "17:00", "fear of spiders"),
                (3, "Viktor Petrov", "Executive", 5, "08:00", "18:00", "gambling problem"),
                (4, "Elena Rodriguez", "Security", 2, "06:00", "14:00", "claustrophobia"),
                (5, "David Kim", "Research", 4, "10:00", "22:00", "perfectionist")
            ]
            
            cursor.executemany('''
                INSERT OR REPLACE INTO employees 
                (id, name, department, clearance_level, shift_start, shift_end, weakness)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', employees_data)
            
            security_logs_data = [
                (1, 1, "Main Gate", "23:30", "patrol_start"),
                (2, 1, "Corridor A", "00:15", "patrol_check"),
                (3, 1, "Break Room", "01:00", "break"),
                (4, 4, "Main Gate", "07:00", "patrol_start"),
                (5, 3, "Executive Suite", "09:30", "meeting")
            ]
            
            cursor.executemany('''
                INSERT OR REPLACE INTO security_logs 
                (id, employee_id, location, access_time, action)
                VALUES (?, ?, ?, ?, ?)
            ''', security_logs_data)
            
            facilities_data = [
                (1, "Server Room", 3, 5, 1),
                (2, "Executive Suite", 5, 4, 3),
                (3, "Research Lab", 2, 3, 5),
                (4, "Security Office", 1, 2, 4)
            ]
            
            cursor.executemany('''
                INSERT OR REPLACE INTO facilities 
                (id, room_name, floor, security_level, guard_id)
                VALUES (?, ?, ?, ?, ?)
            ''', facilities_data)
            
            conn.commit()
            self.loading_animation("Encrypting database records", 3.5)
            print("✅ Debug: Database setup completed successfully")
            
        except sqlite3.Error as e:
            print(f"❌ Debug: Database setup error - {e}")
        finally:
            conn.close()
    
    def execute_query(self, query: str) -> List[Tuple]:
        """Execute SQL query and return results"""
        print(f"🔍 Debug: Executing query - {query}")
        
        # Show hacker-style loading
        loading_messages = [
            "Penetrating database firewall",
            "Bypassing security protocols", 
            "Decrypting data streams",
            "Analyzing target database",
            "Extracting classified information"
        ]
        
        self.loading_animation(random.choice(loading_messages))
        
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
            conn.close()
            
            print(f"✅ Debug: Query successful, returned {len(results)} rows")
            return results
            
        except sqlite3.Error as e:
            print(f"❌ Debug: SQL Error - {e}")
            return []
    
    def get_schema(self) -> dict:
        """Get database schema information"""
        print("🔍 Debug: Fetching database schema...")
        self.loading_animation("Scanning database architecture")
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        schema = {}
        
        try:
            # Get all tables
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
            tables = cursor.fetchall()
            
            for table in tables:
                table_name = table[0]
                
                # Get column info for each table
                cursor.execute(f"PRAGMA table_info({table_name})")
                columns = cursor.fetchall()
                schema[table_name] = columns
                
            print(f"✅ Debug: Schema fetched for {len(schema)} tables")
            
        except sqlite3.Error as e:
            print(f"❌ Debug: Schema fetch error - {e}")
        finally:
            conn.close()
            
        return schema
    
    def get_sample_data(self, table_name: str, limit: int = 3) -> List[Tuple]:
        """Get sample data from a specific table"""
        print(f"🔍 Debug: Fetching sample data from {table_name}")
        self.loading_animation(f"Accessing {table_name} records")
        
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {table_name} LIMIT {limit}")
            results = cursor.fetchall()
            conn.close()
            
            print(f"✅ Debug: Sample data fetched - {len(results)} rows")
            return results
            
        except sqlite3.Error as e:
            print(f"❌ Debug: Sample data error - {e}")
            return []
    
    def cleanup(self):
        """Clean up database file"""
        self.loading_animation("Purging mission database", 3.0)
        import os
        if os.path.exists(self.db_path):
            os.remove(self.db_path)
            print("🗑️ Debug: Database file cleaned up")
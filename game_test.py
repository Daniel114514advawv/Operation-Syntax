import os
import time
from typing import List, Tuple
from database_manager import DatabaseManager

class SQLHackerGame:
    """Main game class for SQL Hacker RPG"""
    
    def __init__(self):
        print("🔧 Debug: Initializing game...")
        self.db_manager = DatabaseManager()
        self.current_mission = 1
        self.mission_complete = False
        print("✅ Debug: Game initialization complete")
    
    def print_hacker_header(self):
        """Print the hacker-style interface header"""
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 70)
        print("█▀▀ ▄▀█ █▄█ █▄▄ █▀▀ █▀█   █▀█ █▀█ █▀▀ █▀█ ▄▀█ ▀█▀ █ █▀█ █▄░█ █▀")
        print("█▄▄ █▀█ ░█░ █▄█ █▄▄ █▀▄   █▄█ █▀▀ █▄▄ █▀▄ █▀█ ░█░ █ █▄█ █░▀█ ▄█")
        print("=" * 70)
        print(f"MISSION {self.current_mission} - ACTIVE")
        print("=" * 70)
        
    
    def show_mission_briefing(self):
        """Display the current mission briefing"""
        print("🔍 Debug: Showing mission briefing...")
        
        briefings = {
            1: {
                "title": "OPERATION: NIGHT SHIFT",
                "objective": "Find the security guard who will be on duty at 1 AM",
                "details": [
                    "Agent needs to infiltrate the facility at 1 AM",
                    "Identify which guard will be on patrol during that time",
                    "Find the guard's weakness for potential distraction"
                ],
                "hint": "Check employee shifts and cross-reference with security logs"
            }
        }
        
        mission = briefings[self.current_mission]
        print(f"\n🎯 {mission['title']}")
        print(f"📋 OBJECTIVE: {mission['objective']}")
        print("\n📝 MISSION DETAILS:")
        for detail in mission['details']:
            print(f"   • {detail}")
        print(f"\n💡 INTEL: {mission['hint']}")
        print("\n" + "─" * 50)
    
    def show_database_tools(self):
        """Show available hacker tools"""
        print("\n🔧 HACKER TOOLS AVAILABLE:")
        print("1. [SCHEMA] - View database structure")
        print("2. [QUERY] - Execute SQL command")
        print("3. [SAMPLES] - View sample data from tables")
        print("4. [DEBUG] - Toggle debug mode")
        print("5. [QUIT] - Exit system")
        print("─" * 50)
    
    def show_schema(self):
        """Display database schema"""
        print("🔍 Debug: Displaying schema...")
        schema = self.db_manager.get_schema()
        
        print("\n📊 DATABASE SCHEMA:")
        print("=" * 40)
        
        for table_name, columns in schema.items():
            print(f"\n📋 TABLE: {table_name.upper()}")
            
            for col in columns:
                col_name = col[1]
                col_type = col[2]
                is_pk = " (PRIMARY KEY)" if col[5] else ""
                print(f"   └── {col_name}: {col_type}{is_pk}")
        
        print("=" * 40)
    
    def show_sample_data(self):
        """Show sample data from all tables"""
        print("🔍 Debug: Displaying sample data...")
        
        tables = ["employees", "security_logs", "facilities"]
        
        print("\n📋 SAMPLE DATA:")
        print("=" * 50)
        
        for table in tables:
            print(f"\n🔍 {table.upper()} (showing first 3 rows):")
            rows = self.db_manager.get_sample_data(table, 3)
            
            if rows:
                # Get column names from schema
                schema = self.db_manager.get_schema()
                columns = [col[1] for col in schema[table]]
                
                # Print header
                header = " | ".join(f"{col[:12]:<12}" for col in columns)
                print(f"   {header}")
                print(f"   {'-' * len(header)}")
                
                # Print rows
                for row in rows:
                    row_str = " | ".join(f"{str(val)[:12]:<12}" for val in row)
                    print(f"   {row_str}")
            else:
                print("   No data available")
        
        print("=" * 50)
    
    def check_mission_completion(self, query: str, results: List[Tuple]) -> bool:
        """Check if the query solves the current mission"""
        print(f"🔍 Debug: Checking mission completion for query: {query}")
        print(f"🔍 Debug: Results to check: {results}")
        
        if self.current_mission == 1:
            # Mission 1: Find guard on duty at 1 AM with weakness
            query_lower = query.lower()
            
            # Check if query looks for the right things
            has_time_condition = any(time_indicator in query_lower for time_indicator in 
                                   ["01:00", "1:00", "shift", "time"])
            has_weakness = "weakness" in query_lower
            
            print(f"🔍 Debug: Has time condition: {has_time_condition}")
            print(f"🔍 Debug: Has weakness: {has_weakness}")
            
            if has_time_condition and has_weakness:
                # Check if results contain the correct guard info
                for result in results:
                    result_str = str(result)
                    if "Marcus Steel" in result_str and "coffee addiction" in result_str:
                        print("✅ Debug: Mission completion criteria met!")
                        return True
        
        print("❌ Debug: Mission not yet complete")
        return False
    
    def display_mission_success(self):
        """Display mission completion message"""
        print("\n" + "🎉" * 20)
        print("✅ MISSION ACCOMPLISHED!")
        print("🎉" * 20)
        print("\n📡 TRANSMISSION FROM FIELD AGENT:")
        print("   'Perfect! Marcus Steel is on duty at 1 AM.'")
        print("   'I'll create a coffee emergency to distract him.'")
        print("   'Infiltration window secured. Well done, hacker!'")
        print("\n🏆 MISSION COMPLETE - RETURNING TO BASE...")
        time.sleep(3)
    
    def run_game(self):
        """Main game loop"""
        print("🔍 Debug: Starting main game loop...")
        
        while not self.mission_complete:
            try:
                self.print_hacker_header()
                self.show_mission_briefing()
                self.show_database_tools()
                
                choice = input("\n🔧 Select tool: ").upper().strip()
                print(f"🔍 Debug: User selected: {choice}")
                
                if choice == "SCHEMA" or choice == "1":
                    self.show_schema()
                    input("\nPress Enter to continue...")
                    
                elif choice == "SAMPLES" or choice == "3":
                    self.show_sample_data()
                    input("\nPress Enter to continue...")
                    
                elif choice == "QUERY" or choice == "2":
                    print("\n💻 SQL TERMINAL ACTIVE")
                    print("Enter your SQL query (or 'back' to return):")
                    print(">" * 50)
                    
                    query = input("SQL> ").strip()
                    print(f"🔍 Debug: User entered query: {query}")
                    
                    if query.lower() == 'back':
                        continue
                    
                    if query:
                        print(f"\n⚡ Executing: {query}")
                        results = self.db_manager.execute_query(query)
                        
                        if results:
                            print(f"\n📊 QUERY RESULTS ({len(results)} rows):")
                            print("─" * 50)
                            for i, row in enumerate(results, 1):
                                print(f"{i:2d}. {row}")
                            print("─" * 50)
                            
                            # Check if mission is complete
                            if self.check_mission_completion(query, results):
                                self.mission_complete = True
                                self.display_mission_success()
                            else:
                                print("\n💡 Good data, but keep investigating...")
                        else:
                            print("\n❌ No results found or query error.")
                        
                        if not self.mission_complete:
                            input("\nPress Enter to continue...")
                
                elif choice == "DEBUG" or choice == "4":
                    print("\n🐛 DEBUG INFO:")
                    print(f"   Current Mission: {self.current_mission}")
                    print(f"   Mission Complete: {self.mission_complete}")
                    print(f"   Database Path: {self.db_manager.db_path}")
                    input("\nPress Enter to continue...")
                
                elif choice == "QUIT" or choice == "5":
                    print("\n🔒 Disconnecting from secure database...")
                    print("🚪 Exiting Cyber Operations...")
                    break
                
                else:
                    print(f"\n❌ Invalid command: {choice}. Try again.")
                    time.sleep(1)
                    
            except KeyboardInterrupt:
                print("\n\n🛑 Debug: KeyboardInterrupt caught")
                print("🔒 Emergency shutdown initiated...")
                break
            except Exception as e:
                print(f"\n❌ Debug: Unexpected error - {e}")
                print("🔧 Please report this bug!")
                input("Press Enter to continue...")

def main():
    """Run the SQL Hacker Game"""
    try:
        print("🔐 Initializing Cyber Operations...")
        time.sleep(1)
        print("🔗 Connecting to secure database...")
        time.sleep(1)
        print("✅ Connection established. Welcome, Agent.\n")
        
        game = SQLHackerGame()
        game.run_game()
        
    except Exception as e:
        print(f"❌ Critical Error: {e}")
        print("🚨 System malfunction detected!")
    
    finally:
        # Cleanup
        print("\n🧹 Cleaning up...")
        try:
            if 'game' in locals():
                game.db_manager.cleanup()
        except:
            pass
        print("Mission database purged. Stay safe, Agent.")

if __name__ == "__main__":
    main()
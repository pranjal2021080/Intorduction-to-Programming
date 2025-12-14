from typing import Dict, List, Tuple

def read_data_file(filename: str = "sorted_data.txt") -> Dict[str, Dict[str, List]]:
    """
    Read the sorted_data.txt file and create a nested dictionary structure.
    Returns: {
        student_name: {
            'gate_no': [...],
            'crossing_type': [...],
            'time': [...]
        }
    }
    """
    student_records = {}
    
    try:
        with open(filename, 'r') as file:
            # Skip the header line
            next(file)
            
            for line in file:
                # Skip empty lines
                if not line.strip():
                    continue
                    
                # Parse line
                student, crossing, gate, time = [item.strip() for item in line.split(',')]
                
                # Initialize nested dictionary for new student
                if student not in student_records:
                    student_records[student] = {
                        'gate_no': [],
                        'crossing_type': [],
                        'time': []
                    }
                
                # Add records to respective lists
                student_records[student]['gate_no'].append(gate)
                student_records[student]['crossing_type'].append(crossing)
                student_records[student]['time'].append(time)

        # Process records to handle consecutive ENTER/EXIT cases
        for student in student_records:
            # Create list of tuples for sorting
            records = list(zip(
                student_records[student]['gate_no'],
                student_records[student]['crossing_type'],
                student_records[student]['time']
            ))
            
            # Sort by time
            records.sort(key=lambda x: x[2])
            
            # Process consecutive ENTER/EXIT
            processed_records = []
            last_type = None
            
            for record in records:
                if record[1] == last_type:  # Check crossing type
                    if record[1] == 'ENTER':
                        # For consecutive ENTERs, take the first one
                        continue
                    else:
                        # For consecutive EXITs, take the last one
                        processed_records.pop()
                processed_records.append(record)
                last_type = record[1]
            
            # Update the dictionary with processed records
            student_records[student]['gate_no'] = [r[0] for r in processed_records]
            student_records[student]['crossing_type'] = [r[1] for r in processed_records]
            student_records[student]['time'] = [r[2] for r in processed_records]
        
        return student_records
        
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return {}

def check_student_status(records: Dict[str, Dict[str, List]], 
                        student_name: str, 
                        current_time: str) -> Tuple[List[Tuple[str, str, str]], bool]:
    """
    Check student's movement records and current status.
    Returns: (list of records, is_present_in_campus)
    """
    if student_name not in records:
        return [], False
        
    student_data = records[student_name]
    records_list = list(zip(
        student_data['gate_no'],
        student_data['crossing_type'],
        student_data['time']
    ))
    
    # Determine if student is present
    is_present = False
    for i, time in enumerate(student_data['time']):
        if time <= current_time:
            is_present = (student_data['crossing_type'][i] == 'ENTER')
    
    return records_list, is_present

def find_students_in_timeframe(records: Dict[str, Dict[str, List]], 
                             start_time: str, 
                             end_time: str) -> Tuple[List[Tuple[str, str, str, str]], 
                                                    List[Tuple[str, str, str, str]]]:
    """
    Find students who entered/exited during given timeframe.
    Returns: (entries_list, exits_list)
    """
    entries = []
    exits = []
    
    for student, data in records.items():
        for i, time in enumerate(data['time']):
            if start_time <= time <= end_time:
                record = (student, data['gate_no'][i], 
                         data['crossing_type'][i], time)
                if data['crossing_type'][i] == 'ENTER':
                    entries.append(record)
                else:
                    exits.append(record)
    
    return sorted(entries, key=lambda x: x[3]), sorted(exits, key=lambda x: x[3])

def analyze_gate_usage(records: Dict[str, Dict[str, List]], 
                      gate_number: str) -> Tuple[int, int]:
    """
    Analyze gate usage for entries and exits.
    Returns: (entry_count, exit_count)
    """
    entry_count = 0
    exit_count = 0
    
    for student, data in records.items():
        for i, gate in enumerate(data['gate_no']):
            if gate == gate_number:
                if data['crossing_type'][i] == 'ENTER':
                    entry_count += 1
                else:
                    exit_count += 1
    
    return entry_count, exit_count

def print_records(records: Dict[str, Dict[str, List]]):
    """Print the nested dictionary structure for verification"""
    for student, data in records.items():
        print(f"\nStudent: {student}")
        print("Records:")
        for i in range(len(data['time'])):
            print(f"  Gate: {data['gate_no'][i]}, "
                  f"Crossing: {data['crossing_type'][i]}, "
                  f"Time: {data['time'][i]}")
def a():
    
    result = 0
    for i in range(1, 10000):
        for j in range(1, 100):
            result += math.sin(i) * math.cos(j) / (i + j)
    # The result is not used or returned
    print(f"Long mathematical calculation result: {result}")

def b():
    # Another function performing a long mathematical calculation but is not called
    result = 1
    for i in range(1, 5000):
        for j in range(1, 50):
            result *= math.sin(i) * math.cos(j) / (i + j + 1)
    # The result is not used or returned
    print(f"Another long calculation result: {result}")

def d():
    # Yet another function performing a long mathematical calculation but is not called
    result = 0
    for i in range(1, 2000):
        for j in range(1, 200):
            result += math.tan(i) * math.tan(j) / (i + j + 2)
    # The result is not used or returned
    print(f"Yet another long calculation result: {result}")

def c():
    # More long mathematical calculations but is not called
    result = 0
    for i in range(1, 3000):
        for j in range(1, 150):
            result += math.exp(i) * math.log(j + 1) / (i + j + 3)
    # The result is not used or returned
    
def test_gate_management_system():
    """Test function for the gate management system."""
    # Mock input data
    mock_data = """Student, Crossing Type, Gate No, Time
Alice, ENTER, G1, 08:00:00
Alice, EXIT, G1, 09:00:00
Bob, ENTER, G2, 10:00:00
Bob, EXIT, G2, 11:00:00
Charlie, ENTER, G3, 08:30:00
Charlie, ENTER, G3, 09:30:00
Charlie, EXIT, G3, 10:30:00
"""
    
    # Write mock data to a temporary file
    temp_filename = "mock_data.txt"
    with open(temp_filename, "w") as file:
        file.write(mock_data)

    # Read the mock data file
    records = read_data_file(temp_filename)

    # Validate `read_data_file`
    assert "Alice" in records, "Alice's data is missing."
    assert records["Charlie"]["crossing_type"] == ["ENTER", "EXIT"], "Charlie's consecutive ENTERs are not handled properly."
    assert records["Bob"]["time"] == ["10:00:00", "11:00:00"], "Bob's timestamps are incorrect."

    # Test `check_student_status`
    alice_records, alice_present = check_student_status(records, "Alice", "08:30:00")
    assert len(alice_records) == 2, "Alice's record count is incorrect."
    assert alice_present is True, "Alice's presence status is incorrect."

    bob_records, bob_present = check_student_status(records, "Bob", "12:00:00")
    assert bob_present is False, "Bob's presence status is incorrect."

    # Test `find_students_in_timeframe`
    entries, exits = find_students_in_timeframe(records, "08:00:00", "09:30:00")
    assert len(entries) == 2, "Incorrect number of entries in timeframe."
    assert len(exits) == 1, "Incorrect number of exits in timeframe."

    # Test `analyze_gate_usage`
    g1_entries, g1_exits = analyze_gate_usage(records, "G1")
    assert g1_entries == 1, "Gate G1 entry count is incorrect."
    assert g1_exits == 1, "Gate G1 exit count is incorrect."

    g3_entries, g3_exits = analyze_gate_usage(records, "G3")
    assert g3_entries == 1, "Gate G3 entry count is incorrect after processing."
    assert g3_exits == 1, "Gate G3 exit count is incorrect after processing."

    # Clean up
    os.remove(temp_filename)

    print("All tests passed!")

# Uncomment the following line to run tests when needed
# test_gate_management_system()
   
def main():
    # Read the sorted_data.txt file
    records = read_data_file()
    if not records:
        return
    
    while True:
        print("\nSelect a query (1-3) or press Enter to exit:")
        print("1. Check student's record and current status")
        print("2. Find students entering/exiting during timeframe")
        print("3. Analyze gate usage")
        
        choice = input("Enter your choice: ").strip()
        if not choice:
            break
            
        try:
            query = int(choice)
            
            if query == 1:
                student_name = input("Enter student name: ").strip()
                current_time = input("Enter current time (HH:MM:SS format): ").strip()
                
                records_list, is_present = check_student_status(records, student_name, current_time)
                
                # Write to output file
                with open('query1_output.txt', 'w') as file:
                    file.write(f"Records for student: {student_name}\n")
                    for gate, crossing, time in records_list:
                        file.write(f"Gate: {gate}, {crossing}, Time: {time}\n")
                    file.write(f"\nCurrent Status: {'Present in' if is_present else 'Not in'} campus")
                
                print(f"Results written to 'query1_output.txt'")
                
            elif query == 2:
                start_time = input("Enter start time (HH:MM:SS format): ").strip()
                end_time = input("Enter end time (HH:MM:SS format): ").strip()
                
                entries, exits = find_students_in_timeframe(records, start_time, end_time)
                
                # Write results to file
                with open('query2_output.txt', 'w') as file:
                    file.write(f"Records between {start_time} and {end_time}\n\nEntries:\n")
                    for student, gate, crossing, time in entries:
                        file.write(f"{student}, {crossing}, {gate}, {time}\n")
                    file.write("\nExits:\n")
                    for student, gate, crossing, time in exits:
                        file.write(f"{student}, {crossing}, {gate}, {time}\n")
                
                print(f"Results written to 'query2_output.txt'")
                
            elif query == 3:
                gate_number = input("Enter gate number: ").strip()
                entries, exits = analyze_gate_usage(records, gate_number)
                print(f"\nGate {gate_number} usage:")
                print(f"Number of entries: {entries}")
                print(f"Number of exits: {exits}")
                
            else:
                print("Invalid choice. Please select 1, 2, or 3.")
                
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main() 
    records = read_data_file()
print("\nNested Dictionary Structure:")
print_records(records)
    
    
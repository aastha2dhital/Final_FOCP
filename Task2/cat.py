import sys

def analyze_cat_shelter_log(file_path):
    try:
        # Attempt to open the specified log file
        with open(file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        # If the file is not found, print an error message and return
        print(f'Cannot open "{file_path}"!')
        return

    # Initialize variables to store analysis results
    cat_visits = 0
    intruder_doused = 0
    total_time_in_house = 0
    visit_lengths = []

    # Loop through each line in the log file
    for line in lines:
        # Check if the line contains 'END', indicating the end of the log
        if line.strip() == 'END':
            break

        # Split the line into cat_name, entry_time, and exit_time
        data = line.strip().split(',')
        cat_name, entry_time, exit_time = data[0], int(data[1]), int(data[2])

        # Check if the cat is one of 'OURS' or an intruder
        if cat_name == 'OURS':
            # Update cat visit information
            cat_visits += 1
            total_time_in_house += (exit_time - entry_time)
            visit_lengths.append(exit_time - entry_time)
        else:
            # Update intruder count
            intruder_doused += 1

    # Check if there were no cat visits recorded
    if cat_visits == 0:
        print('No cat visits recorded.')
        return

    # Calculate average, longest, and shortest visit lengths
    average_visit_length = sum(visit_lengths) // cat_visits
    longest_visit = max(visit_lengths)
    shortest_visit = min(visit_lengths)

    # Print the analysis results
    print('\nLog File Analysis\n==================\n')
    print(f'Cat Visits: {cat_visits}')
    print(f'Other Cats: {intruder_doused}\n')
    print(f'Total Time in House: {total_time_in_house // 60} Hours, {total_time_in_house % 60} Minutes\n')
    print(f'Average Visit Length: {average_visit_length} Minutes')
    print(f'Longest Visit: {longest_visit} Minutes')
    print(f'Shortest Visit: {shortest_visit} Minutes\n')

if __name__ == "__main__":
    # Check if the correct number of command line arguments is provided
    if len(sys.argv) != 2:
        print('Missing command line argument!')
    else:
        # Get the log file path from the command line argument and analyze the log
        log_file_path = sys.argv[1]
        analyze_cat_shelter_log(log_file_path)

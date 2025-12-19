# Graph representation of flight routes
flight_graph = {
    "SL": {
        "UK": 11.45,
        "Japan": 8,
        "Singapore": 4,
        "Australia": 9.25
    },
    "UK": {
        "USA": 8
    },
    "Japan": {
        "USA": 16,
        "Australia": 10
    },
    "Singapore": {
        "Japan": 4,
        "Australia": 7.25
    },
    "USA": {},
    "Australia": {}
}

# Country name mappings for user-friendly input
country_names = {
    "SL": "Sri Lanka",
    "Sri Lanka": "SL",
    "UK": "UK",
    "United Kingdom": "UK",
    "USA": "USA",
    "United States": "USA",
    "Japan": "Japan",
    "Singapore": "Singapore",
    "Australia": "Australia"
}


def get_country_code(country_input):
    """Convert user input to country code"""
    if country_input in country_names:
        return country_names[country_input]
    return country_input


def get_country_name(code):
    """Get full country name from code"""
    names = {
        "SL": "Sri Lanka",
        "UK": "UK",
        "USA": "USA",
        "Japan": "Japan",
        "Singapore": "Singapore",
        "Australia": "Australia"
    }
    return names.get(code, code)


def find_all_routes(graph, start, end, path=None, total_duration=0):
    """
    Recursively find all possible routes from start to end country
    Returns list of tuples: (route_list, total_duration)
    """
    if path is None:
        path = []
    
    path = path + [start]
    
    # If we reached the destination, return this route
    if start == end:
        return [(path, total_duration)]
    
    # If start country has no outgoing flights, no route exists
    if start not in graph:
        return []
    
    routes = []
    
    # Explore all neighboring countries
    for neighbor, duration in graph[start].items():
        # Avoid cycles - don't visit same country twice
        if neighbor not in path:
            new_routes = find_all_routes(graph, neighbor, end, path, total_duration + duration)
            routes.extend(new_routes)
    
    return routes


def display_all_routes(graph, start, destination):
    """Display all possible airline routes between two countries"""
    print("\nFlightRoutes Company")
    print("All possible airline routes between two given countries with durations\n")
    
    start_code = get_country_code(start)
    dest_code = get_country_code(destination)
    
    # Validate country codes
    all_countries = set(graph.keys()) | {dest for destinations in graph.values() for dest in destinations.keys()}
    
    if start_code not in all_countries:
        print(f"Error: '{start}' is not a valid country.")
        return
    
    if dest_code not in all_countries:
        print(f"Error: '{destination}' is not a valid country.")
        return
    
    if start_code == dest_code:
        print("Error: Starting country and destination country cannot be the same.")
        return
    
    # Find all routes
    routes = find_all_routes(graph, start_code, dest_code)
    
    if not routes:
        print(f"No routes available from {get_country_name(start_code)} to {get_country_name(dest_code)}.")
        return
    
    print(f"Starting Country: {get_country_name(start_code)}")
    print(f"Destination Country: {get_country_name(dest_code)}\n")
    
    # Display all routes
    for i, (route, duration) in enumerate(routes, 1):
        route_str = " -> ".join([get_country_name(country) for country in route])
        print(f"Route {i}: {route_str}")
        print(f"Expected Duration: {duration} Hours\n")


def display_least_duration_route(graph, start, destination):
    """Display the shortest duration route between two countries"""
    print("\nFlightRoutes Company")
    print("Least duration airline route between two given countries\n")
    
    start_code = get_country_code(start)
    dest_code = get_country_code(destination)
    
    # Validate country codes
    all_countries = set(graph.keys()) | {dest for destinations in graph.values() for dest in destinations.keys()}
    
    if start_code not in all_countries:
        print(f"Error: '{start}' is not a valid country.")
        return
    
    if dest_code not in all_countries:
        print(f"Error: '{destination}' is not a valid country.")
        return
    
    if start_code == dest_code:
        print("Error: Starting country and destination country cannot be the same.")
        return
    
    # Find all routes
    routes = find_all_routes(graph, start_code, dest_code)
    
    if not routes:
        print(f"No routes available from {get_country_name(start_code)} to {get_country_name(dest_code)}.")
        return
    
    # Find minimum duration route
    min_route, min_duration = min(routes, key=lambda x: x[1])
    
    print(f"Starting Country: {get_country_name(start_code)}")
    print(f"Destination Country: {get_country_name(dest_code)}\n")
    
    route_str = " -> ".join([get_country_name(country) for country in min_route])
    print(f"Route: {route_str}")
    print(f"Expected Duration: {min_duration} Hours\n")


def main():
    """Main function to run the flight routes program"""
    print("=" * 60)
    print("Welcome to FlightRoutes Company")
    print("=" * 60)
    
    while True:
        print("\n" + "=" * 60)
        print("FlightRoutes Company")
        print("Main Menu")
        print("=" * 60)
        print("1. Display all possible airline routes between two countries")
        print("2. Display least time airline route between two countries")
        print("3. Exit")
        print("=" * 60)
        
        choice = input("Your Choice: ").strip()
        
        if choice == "1":
            print("\n" + "-" * 60)
            start = input("Starting Country: ").strip()
            destination = input("Destination Country: ").strip()
            display_all_routes(flight_graph, start, destination)
            
            exit_choice = input("\nDo you want to Exit (Yes/No)? ").strip().lower()
            if exit_choice in ['yes', 'y']:
                break
        
        elif choice == "2":
            print("\n" + "-" * 60)
            start = input("Starting Country: ").strip()
            destination = input("Destination Country: ").strip()
            display_least_duration_route(flight_graph, start, destination)
            
            exit_choice = input("\nDo you want to Exit (Yes/No)? ").strip().lower()
            if exit_choice in ['yes', 'y']:
                break
        
        elif choice == "3":
            print("\nThank you for using FlightRoutes Company!")
            break
        
        else:
            print("\nError: Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()

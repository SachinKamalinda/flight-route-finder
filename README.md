# flight-route-finder
A Python program to find flight routes between countries using graph algorithms.
Project Overview
This Python program implements an automated flight route finder that displays all possible airline routes and the shortest duration route between any two countries. The system uses a graph-based data structure to represent flight connections and employs recursive algorithms to find all possible paths.
Supported Countries

SL (Sri Lanka)
UK (United Kingdom)
USA (United States)
Japan
Singapore
Australia


Features
1. Display All Possible Routes

Shows all available flight paths between two countries
Displays each route with step-by-step connections
Shows the total expected duration for each route
Automatically calculates durations by summing individual flight segments

2. Display Least Duration Route

Finds and displays the fastest route between two countries
Compares all possible routes to determine the minimum duration
Shows the complete path and total travel time

3. User-Friendly Interface

Menu-driven system for easy navigation
Accepts both country codes (SL, UK) and full names (Sri Lanka, United Kingdom)
Comprehensive error handling and validation
Option to exit after each query


Data Structure
Graph Representation
The program uses a nested dictionary (adjacency list) to represent the flight network:
pythonflight_graph = {
    "Country1": {
        "Country2": duration,
        "Country3": duration
    },
    ...
}
Advantages of this data structure:

Efficient lookup: O(1) access to check if a direct flight exists
Easy to maintain: Simple to add/remove routes
Natural representation: Mirrors the real-world concept of flight networks
Memory efficient: Only stores existing connections


Algorithm Explanation
Route Finding Algorithm
The program uses a Depth-First Search (DFS) recursive algorithm with backtracking:

Start from the source country
Mark the current country as visited (add to path)
Check if we reached the destination:

If yes: Return the current path and total duration
If no: Continue to step 4


Explore all neighboring countries (direct flights)
Recursively visit each unvisited neighbor
Accumulate all valid routes found
Backtrack to explore other paths

Key Features:

Cycle prevention: Each country is visited only once per path
Complete search: Finds ALL possible routes, not just one
Duration tracking: Accumulates flight times along each path

Complexity Analysis

Time Complexity: O(N!) in worst case where N is number of countries

In practice, much better due to limited connections


Space Complexity: O(N) for recursion depth


How to Run the Program
Prerequisites

Python 3.x installed on your system
Python IDLE or any Python interpreter

Steps to Execute

Save the file as FlightRoute.py
Open Python IDLE:

File → Open → Select the .py file
Press F5 or Run → Run Module


Use the program:

Choose option 1 or 2 from the menu
Enter starting country (e.g., "Sri Lanka" or "SL")
Enter destination country (e.g., "Australia")
View the results
Choose to exit or continue



Example Usage
Starting Country: Sri Lanka
Destination Country: Australia

Route 1: Sri Lanka -> Australia
Expected Duration: 9.25 Hours

Route 2: Sri Lanka -> Singapore -> Australia
Expected Duration: 11.25 Hours

Route 3: Sri Lanka -> Japan -> Australia
Expected Duration: 18.0 Hours

Route 4: Sri Lanka -> Singapore -> Japan -> Australia
Expected Duration: 18.0 Hours

Test Cases
Test Case 1: Direct Flight

Input: Sri Lanka → Australia
Expected: 1 direct route (9.25 hours)
Result: ✓ Pass

Test Case 2: Multiple Routes

Input: Sri Lanka → USA
Expected: 3 possible routes via UK or Japan
Result: ✓ Pass

Test Case 3: No Direct Flight

Input: UK → Australia
Expected: Multiple indirect routes via other countries
Result: ✓ Pass

Test Case 4: Invalid Country

Input: Sri Lanka → France
Expected: Error message "not a valid country"
Result: ✓ Pass

Test Case 5: Same Start and Destination

Input: Japan → Japan
Expected: Error message
Result: ✓ Pass

Test Case 6: Reverse Direction

Input: Australia → Sri Lanka
Expected: No routes available (one-way flights only)
Result: ✓ Pass

Test Case 7: Shortest Route Finding

Input: Sri Lanka → Australia
Expected: Direct route (9.25 hours)
Result: ✓ Pass

Test Case 8: Country Name Variations

Input: "Sri Lanka" vs "SL"
Expected: Both should work identically
Result: ✓ Pass


Error Handling
The program includes comprehensive error handling for:

Invalid country names: Validates against available countries
Same source and destination: Prevents meaningless queries
No route available: Handles cases where no path exists
Invalid menu choices: Validates user input
Case-insensitive input: Accepts various input formats


Assumptions Made

One-way flights
No layover time: Duration only includes flight time, not waiting time
All flights available: No consideration of schedules or availability
Fixed durations: Flight times are constant and don't vary
No cost consideration: Only time is optimized, not price

Future Enhancements
Possible improvements for future versions:

Add round-trip route calculation
Include layover time considerations
Add cost/price optimization
Implement graphical visualization of routes
Add more countries and routes
Include real-time flight data integration

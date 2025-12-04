#!/usr/bin/env python3
import os
import random
from datetime import datetime

def make_contribution():
    """Make a single contribution by updating the data file."""
    timestamp = datetime.now().isoformat()
    
    # Append timestamp to the contributions file
    with open('contributions.txt', 'a') as f:
        f.write(f"{timestamp}\n")
    
    return timestamp

def main():
    # Generate random number of contributions (1-10)
    num_contributions = random.randint(1, 10)
    
    print(f"Making {num_contributions} contributions...")
    
    for i in range(num_contributions):
        timestamp = make_contribution()
        print(f"  {i+1}. Contribution at {timestamp}")
    
    print(f"\nTotal contributions made: {num_contributions}")

if __name__ == "__main__":
    main()

#1. Read startups and alumni csv into lists
#2. Read in README line by line and
#3. Insert formatted tables after reference to csv

import os
import csv
import re
import sys

def main():

    # Read in CSV files
    technologies = list(csv.DictReader(open("technologies.csv", "r"), delimiter=","))
    startups = list(csv.DictReader(open("startups.csv", "r"), delimiter=","))
    alumni = list(csv.DictReader(open("alumni.csv", "r"), delimiter=","))

    # Read in README
    with open('header.md') as f:
        header = f.read().splitlines()

    # Insert csv lists
    with open('README.md', 'w') as f:

        ################################
        # Printing out old README header
        ################################
        for line in header:
            print(line, file=f)

        ################################
        # Printing out technologies
        ################################
        print("\n| Technology| Description                                      |", file=f)
        print(  "|-----------|--------------------------------------------------|", file=f)
        for x in technologies:
            print(f"|{x['Technology']} | {x['Description']}", file=f)

        ################################
        # Printing out all startups
        ################################
        print("\n## Startups", file=f)
        print("\n| Company | Technology | Founded | Country | Description |", file=f)
        print("|---------|------------|---------|---------|-------------|", file=f)
        for x in startups:
            print(f"|[{x['Company']}](https://{x['Website']}) | {x['Technology']} | {x['Founded']} | {x['Country']} |{x['Description']} |", file=f)
            found = False
            for t in technologies:
                if x['Technology'] == t['Technology']:
                    found = True
                    break
            if not found:
               print(f"Warning: {x['Company']} uses undefined technology {x['Technology']}. "
                      "Please spell-check or add to technologies.csv.", file=sys.stderr)

        ################################
        # Printing out exits
        ################################
        print("\n## Alumni", file=f)
        print("\n| Company |  Exit   | Year   | Value($M) | Link |", file=f)
        print("|---------| ------- | ------ | ------|------|", file=f)
        for x in alumni:
            if not re.search(r'http', x['Link']):
                link = "NA"
            else:
                link = f"[Source]({x['Link']})"
            print(f"|{x['Company']} | {x['Exit']} | {x['Year']} | {x['Value($M)']} | {link} |", file=f)

if __name__ == '__main__':
    main()

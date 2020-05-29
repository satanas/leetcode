# Example data:
# ============
# CSSselect|Felix Boehm|me@feedic.com|0.3.11|CSSwhat:domutils|232257|git://github.com/fb55/CSSselect.git
# cookie-jar|Mikeal Rogers|mikeal.rogers@gmail.com|0.3.0||235068|https://github.com/mikeal/cookie-jar
# cookie|Roman Shtylman|shtylman@gmail.com|0.0.4||74127|git://github.com/shtylman/node-cookie.git
# crc|Alex Gorbatchev|alex.gorbatchev@gmail.com|0.2.0||116925|git://github.com/alexgorbatchev/node-crc.git
# crc32|T. Jameson Little|t.jameson.little@gmail.com|0.2.2||49741|http://github.com/beatgammit/crc32.git

# First iteration: Design a program that given the name of a repo as input , print its dependencies.
# For example:
# $ ./program CSSselect
# CSSwhat
# domutils

# Assumptions:
# 1. We assume that the name is a valid id (no spaces, path-like)
# 2. We assume we're using something like OptParser to validate inputs from the command line

import csv

class ProgramV1:
    def __init__(self):
        self.repos = {}

    def dependencies(self, package):
        if package in self.repos:
            for dep in self.repos[package].dependencies:
                print(dep)
        else:
            print("Package not valid")

    def parse_package(self, line):
        return Package(line[0])


    def load_csv(self, filename):
        for line in csv_file:
            package = parse_package(line)
            self.repos[package.name] = package


class Package:
    def __init__(self):
        self.name
        self.author # or maintainer
        self.author_email
        self.version
        self.dependencies = deps.split(':') # list of names
        self.url


# Second iteration: Now, adjust the program to print the transitive dependencies (dependencies of dependencies)

# Assumptions
# 1. Same assumptions from iteration one
# 2. We assume that we can use all the code above unless called out

class ProgramV2:
    filename = "packages.csv"

    def __init__(self):
        self.packages = {}
        self.load_csv()

    def print_dependencies(self, pkg):
        deps = {}
        if pkg in self.packages:
            for d in self.packages[pkg].dependencies:
                self.get_dependencies(deps, d)
            for k in deps.keys():
                print(k)
        else:
            print("Package not valid")

    def get_dependencies(self, curr_deps, pkg):
        if pkg != '':
            curr_deps[pkg] = True
        if pkg in self.packages:
            for p in self.packages[pkg].dependencies:
                self.get_dependencies(curr_deps, p)
        return


    def load_csv(self):
        with open(self.filename, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter='|')
            for row in reader:
                package = Package(row)
                self.packages[package.name] = package


class Package:
    def __init__(self, row):
        self.name = row[0]
        self.author = row[1]
        self.email = row[2]
        self.version = row[3]
        self.dependencies = row[4].split(':') # list of names
        self.url = row[6]

if __name__ == "__main__":
    p = ProgramV2()
    p.print_dependencies("grunt")
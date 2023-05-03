#!/usr/bin/env ruby

# Get the first command line argument
argument = ARGV[0]

# Define a regular expression to match "School"
regex = /School/

# Use the regular expression to match the argument
if regex.match(argument)
  puts argument + "$"
else
  puts ""
end
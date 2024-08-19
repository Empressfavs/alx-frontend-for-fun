#!/usr/bin/python3.8
"""
markdown2html.py

This script converts a Markdown file to an HTML file.
"""

import sys
import os
import markdown

def markdown_to_html(input_file, output_file):
    """
    Convert Markdown file to HTML file.

    Args:
        input_file (str): Path to the input Markdown file.
        output_file (str): Path to the output HTML file.
    """
    # Read the Markdown content and convert it to HTML
    with open(input_file, 'r') as markdown_file:
        markdown_text = markdown_file.read()
        html_text = markdown.markdown(markdown_text)

    # Write the HTML content to the output file
    with open(output_file, 'w') as html_file:
        html_file.write(html_text)

if __name__ == "__main__":
    # Check if the correct number of arguments are provided
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    # Get input file and output file from arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check if the input Markdown file exists
    if not os.path.exists(input_file):
        sys.stderr.write(f"Missing {input_file}\n")
        sys.exit(1)

    # Convert the Markdown file to HTML
    markdown_to_html(input_file, output_file)

    # Exit without printing anything
    sys.exit(0)

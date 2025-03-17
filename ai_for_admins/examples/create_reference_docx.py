#!/usr/bin/env python3
"""
Create a reference.docx file for pandoc to use for styling the converted documents.
This creates a DOCX file with the PSU colors and styles that pandoc will use as a reference.
"""

import os
from docx import Document
from docx.shared import RGBColor
from docx.enum.style import WD_STYLE_TYPE

# PSU Colors
PSU_BLUE = RGBColor(0, 61, 112)  # #003d70
PSU_LIGHT_BLUE = RGBColor(0, 156, 222)  # #009cde

def create_reference_docx(output_path):
    """Create a reference DOCX with PSU styles."""
    document = Document()
    
    # Modify styles for the document
    styles = document.styles
    
    # Update Heading 1 style
    h1_style = styles['Heading 1']
    h1_style.font.color.rgb = PSU_BLUE
    h1_style.font.bold = True
    h1_style.font.size = 18  # 18pt
    
    # Update Heading 2 style
    h2_style = styles['Heading 2']
    h2_style.font.color.rgb = PSU_LIGHT_BLUE
    h2_style.font.bold = True
    h2_style.font.size = 16  # 16pt
    
    # Update Heading 3 style
    h3_style = styles['Heading 3']
    h3_style.font.bold = True
    h3_style.font.size = 14  # 14pt
    
    # Make a code style
    if 'Code' not in styles:
        code_style = styles.add_style('Code', WD_STYLE_TYPE.CHARACTER)
        code_style.font.name = 'Consolas'
        code_style.font.size = 10  # 10pt
    
    # Save the document
    document.save(output_path)
    print(f"Created reference DOCX at {output_path}")

if __name__ == "__main__":
    # Save reference file to examples directory
    output_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'reference.docx'
    )
    create_reference_docx(output_path)
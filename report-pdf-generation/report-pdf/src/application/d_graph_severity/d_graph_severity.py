import os

import reportlab
from reportlab.pdfgen import canvas

from src.utils.draw_bar_chart import draw_bar_chart


def d_graph_severity(c: reportlab.pdfgen.canvas.Canvas, assets_list: list):
    """
    Creates a graph in the PDF showing the severity of vulnerabilities for each asset.

    Arguments:
    c -- Canvas object to render the PDF
    assets_list -- List of assets with vulnerabilities.
    """
    # Initialize counters for severity levels
    severity_counts = {"critical": 0, "high": 0, "medium": 0, "low": 0}

    # Iterate through each asset and count the severities
    for asset in assets_list:
        for vuln in asset.get('vulnerability_list', []):
            severity = vuln['severity'].lower()
            if severity in severity_counts:
                severity_counts[severity] += 1
    print(f"{severity_counts}")

    # Extract data for the bar chart
    severities = list(severity_counts.keys())
    counts = list(severity_counts.values())

    # Create and save the bar chart as an image
    output_path = os.path.join("_tmp", "severity_chart.png")
    draw_bar_chart(severities, counts, output_path)

    # Embed the image into the PDF canvas
    c.drawImage(output_path, 100, 400, width=400, height=300)

    # Save the PDF
    c.showPage()

    return c

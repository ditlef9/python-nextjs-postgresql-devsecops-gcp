import reportlab
from reportlab.lib import colors
from reportlab.pdfgen import canvas


def e_assets(c: reportlab.pdfgen.canvas.Canvas,
             datetime_ym: str,
             assets_list: list):
    """
    Loads asset data from Google Cloud Storage and writes it to a PDF.

    :param c: ReportLab canvas object to write PDF content.
    :param datetime_ym: Year and month string (YYYY-MM).
    :param storage_client: Google Cloud Storage client instance.
    :param bucket: Google Cloud Storage Bucket object.
    :return: Updated ReportLab canvas.
    """
    print("e_assets() · Init")


    # Initial PDF text positioning
    y_position = 800  # Start near the top
    line_height = 20  # Space between each line

    if not assets_list:
        c.setFont("Helvetica-Bold", 14)  # Set a larger font for the message
        c.drawString(100, y_position, f"No asset data found for {datetime_ym}")
        return c

    for asset in assets_list:
        if y_position < 100:  # Create a new page if space runs out
            c.showPage()
            y_position = 800

        # Extract asset details
        asset_name = asset.get("asset_name", "Unknown")
        asset_external_ip = asset.get("asset_external_ip", "N/A")
        asset_internal_ip = asset.get("asset_internal_ip", "N/A")
        asset_type = asset.get("asset_type", "N/A")
        asset_risk_score = asset.get("asset_risk_score", "N/A")
        vulnerabilities = asset.get("vulnerability_list", [])

        # Draw an "H2"-style heading for the asset
        c.setFont("Helvetica-Bold", 16)  # Bold and large font
        c.setFillColor(colors.darkblue)  # Blue color for emphasis
        c.drawString(50, y_position, f"{asset_name} ({asset_type}) · Risk Score: {asset_risk_score}")
        y_position -= line_height  # Move down

        # Reset font for normal text
        c.setFont("Helvetica", 12)
        c.setFillColor(colors.black)
        c.drawString(50, y_position, f"External IP: {asset_external_ip} | Internal IP: {asset_internal_ip}")
        y_position -= line_height

        # Draw vulnerability details with color coding based on severity
        for vuln in vulnerabilities:
            if y_position < 100:  # Prevent text overflow
                c.showPage()
                y_position = 800

            severity = vuln.get('severity', 'low')
            # Color code based on severity
            if severity == 'critical':
                severity_color = colors.red
            elif severity == 'high':
                severity_color = colors.orange
            elif severity == 'medium':
                severity_color = colors.purple
            else:  # low severity
                severity_color = colors.grey

            # Bold font for vulnerability title (acts like an <h3>)
            c.setFont("Helvetica-Bold", 12)
            c.setFillColor(severity_color)  # Apply severity color
            c.drawString(50, y_position, f"{vuln.get('title', 'N/A')} · {severity.title()}")
            y_position -= line_height

            # Normal font for description
            c.setFont("Helvetica", 10)
            c.setFillColor(colors.black)
            c.drawString(50, y_position, f"  {vuln.get('description', 'N/A')}")
            y_position -= line_height

            # Normal font for how to fix
            c.setFont("Helvetica", 10)
            c.drawString(50, y_position, f"  How to Fix: {vuln.get('how_to_fix', 'N/A')}")
            y_position -= line_height

            # Normal font for the link
            c.setFont("Helvetica", 10)
            c.drawString(50, y_position, f"  Link: {vuln.get('link', 'N/A')}")
            y_position -= line_height

        y_position -= line_height  # Extra space between assets

    return c

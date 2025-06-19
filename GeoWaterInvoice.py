from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import folium
import geopandas as gpd
import cairosvg

# Invoice Data
invoice_data = {
    "company": "XYZ Water Distribution Co.",
    "billing_address": "123 Farm Road, CA",
    "invoice_date": "June 15, 2025",
    "due_date": "June 30, 2025",
    "invoice_number": "INV-2025-00123",
    "items": [
        {"description": "Water Supply - 100 Acres", "quantity": 100, "unit_price": 25, "total": 2500},
        {"description": "Maintenance Fee", "quantity": 1, "unit_price": 150, "total": 150},
    ],
}

# Create Invoice PDF
def generate_invoice(pdf_filename):
    c = canvas.Canvas(pdf_filename, pagesize=letter)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(200, 750, "Professional Invoice")

    c.setFont("Helvetica", 12)
    c.drawString(50, 720, f"Company: {invoice_data['company']}")
    c.drawString(50, 705, f"Billing Address: {invoice_data['billing_address']}")
    c.drawString(50, 690, f"Invoice Date: {invoice_data['invoice_date']}")
    c.drawString(50, 675, f"Due Date: {invoice_data['due_date']}")
    c.drawString(50, 660, f"Invoice Number: {invoice_data['invoice_number']}")

    # Draw Items Table
    y = 630
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Description")
    c.drawString(300, y, "Quantity")
    c.drawString(400, y, "Unit Price")
    c.drawString(500, y, "Total")

    c.setFont("Helvetica", 12)
    y -= 20
    for item in invoice_data["items"]:
        c.drawString(50, y, item["description"])
        c.drawString(310, y, str(item["quantity"]))
        c.drawString(410, y, f"${item['unit_price']}")
        c.drawString(510, y, f"${item['total']}")
        y -= 20

    # Total
    c.setFont("Helvetica-Bold", 14)
    c.drawString(400, y - 30, f"Total Due: ${sum(item['total'] for item in invoice_data['items'])}")

    c.save()

    # Generate Map
    def generate_map():
        map = folium.Map(location=[37.7749, -122.4194], zoom_start=10)

    # Load parcel GeoJSON
    parcels = gpd.read_file("parcels.geojson")
    folium.GeoJson(parcels, name="Parcels", style_function=lambda x: {"color": "blue", "weight": 2}).add_to(map)

    # Load pipelines GeoJSON
    pipelines = gpd.read_file("pipelines.geojson")
    folium.GeoJson(pipelines, name="Pipelines", style_function=lambda x: {"color": "green", "weight": 3, "dashArray": "5,5"}).add_to(map)

    map.save("map.html")

    # Convert Map to PDF with Explicit Dimensions
    cairosvg.svg2pdf(url="map.html", write_to="map.pdf", output_width=800, output_height=600)

# Execute Invoice & Map Generation
generate_invoice("invoice.pdf")
generate_map()

# GeoWaterInvoice

I developed a streamlined solution that automates the creation and delivery of client proposal PDFs, accelerating the sales process and enhancing operational efficiency. The automated system uses Google Cloud for generating client proposals, integrating water mapping and invoicing into a seamless workflow. The Python script, `GeoWaterInvoice.py`, outputs `invoice.pdf`, `map.html`, and `map.pdf` all generated in sequence from a single file.

# Automated Client Proposal PDF Generation System


### 📄 `GeoWaterInvoice.py`  
Generates a professional invoice (`invoice.pdf`) and visual map (`map.pdf`) for agricultural water distribution. It integrates invoice data, parcel and pipeline overlays, and automates PDF creation.

---

### 🗺️ `map.html`  
An interactive Leaflet.js map that visualizes parcel boundaries and pipeline routes using GeoJSON. Used as the visual reference for the map PDF and displayed in the browser.

---

### 🌐 `parcels.geojson`  
Contains geographic data for agricultural parcels including ownership and water usage. Displayed in blue on the map.

---

### 🚰 `pipelines.geojson`  
Contains pipeline route data with capacity and identifiers. Displayed as green dashed lines on the map.

Perfect. Here’s a polished section you can drop directly into your `README.md`:

---

## 📁 Project File Overview

| File Name            | Description |
|---------------------|-------------|
| `GeoWaterInvoice.py` | Automates generation of a professional invoice and accompanying map PDF. Combines GIS overlays and invoice data into client-ready deliverables. |
| `map.html`           | An interactive Leaflet.js map displaying parcel boundaries and pipeline routes. Supports browser rendering and static image conversion. |
| `parcels.geojson`    | GeoJSON file with parcel outlines and property data such as ownership and water usage. Rendered in blue on the map. |
| `pipelines.geojson`  | GeoJSON file containing pipeline paths, capacities, and IDs. Rendered as green dashed lines on the map. |


---

# 🚰 GeoWaterInvoice  
**Streamlining agricultural billing and infrastructure with Python-powered precision.**  

A lightweight tool for generating polished invoices and geospatial maps in PDF format. Ideal for water distribution companies and agricultural consultants looking to improve transparency, automate deliverables, and visually communicate infrastructure.

---

## 🚀 Features
- ✅ Professional invoice generation (PDF)
- 🗺️ Visual mapping of parcel and pipeline data (GeoJSON-based)
- 💼 Clear breakdown of water usage and revenue per project
- 📬 Option to auto-email invoices to clients

---

## 🧱 Files & Components

| File                | Description |
|---------------------|-------------|
| `GeoWaterInvoice.py` | Main script that generates invoices and maps using ReportLab, Folium, GeoPandas, and CairoSVG. |
| `map.html`           | Interactive Leaflet.js map of parcels and pipelines. Also supports headless rendering for PDF export. |
| `parcels.geojson`    | Geographic data showing parcels, owners, and water usage (rendered in blue). |
| `pipelines.geojson`  | Line data for irrigation pipelines with ID and flow capacity (rendered in green dashed lines). |

---

## 📦 Installation

Make sure you have Python 3 installed, then:

```bash
git clone https://github.com/your-username/GeoWaterInvoice.git
cd GeoWaterInvoice
pip install -r requirements.txt
```

> **Tip:** If you’re using macOS, run inside a virtual environment to avoid PEP 668 errors.

---

## ✅ Usage

```bash
python3 GeoWaterInvoice.py
```

This will:
1. Generate `invoice.pdf` with billing information
2. Render `map.html` as an interactive map
3. Convert map to `map.pdf` for printable inclusion

Optional: You can extend the script to auto-email invoices to clients once generated.

---

## 🛠 Requirements

- Python 3.8+
- `folium`, `geopandas`, `reportlab`, `cairosvg`
- Optional: `selenium`, `Pillow` for image-to-PDF conversion
- GeoJSON inputs: `parcels.geojson` and `pipelines.geojson`

---

## 📬 Email Integration (Optional)

To email the invoice automatically, configure SMTP settings in the script and call:

```python
send_invoice("invoice.pdf", "client@example.com")
```

---

## 🌱 License

MIT — use it, build on it, make it your own.

---

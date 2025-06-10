class ReportService:
    """Simple report service stub."""

    def generate(self, records: list[dict]):
        """Placeholder for report generation."""
        # For now, just return the records
        return records

    def export(self, kind: str, rows: list[dict], path: str) -> None:
        """Export rows to CSV or PDF (text-based placeholder)."""
        if kind == "csv":
            self._export_csv(rows, path)
        elif kind == "pdf":
            self._export_pdf(rows, path)
        else:
            raise ValueError(f"Unsupported format: {kind}")

    def _export_csv(self, rows: list[dict], path: str) -> None:
        import csv

        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if rows:
                writer.writerow(rows[0].keys())
            for row in rows:
                writer.writerow([row.get(k, "") for k in rows[0].keys()])

    def _export_pdf(self, rows: list[dict], path: str) -> None:
        """Very basic PDF export using plain text when FPDF is unavailable."""
        try:
            from fpdf import FPDF
        except Exception:
            # Fallback: write plain text with .pdf extension
            with open(path, "w", encoding="utf-8") as f:
                for row in rows:
                    line = ", ".join(str(v) for v in row.values())
                    f.write(line + "\n")
            return

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        if rows:
            pdf.cell(200, 10, txt=", ".join(rows[0].keys()), ln=1)
        for row in rows:
            pdf.cell(200, 10, txt=", ".join(str(v) for v in row.values()), ln=1)
        pdf.output(path)

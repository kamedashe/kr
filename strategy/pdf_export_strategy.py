import os
from fpdf import FPDF
from strategy.export_strategy import ExportStrategy

class PDFExportStrategy(ExportStrategy):
    def export(self, rows, out_path):
        pdf = FPDF(orientation='L', unit='mm', format='A4')
        pdf.add_page()

        # Отримуємо абсолютний шлях до TTF
        font_path = os.path.join(os.path.dirname(__file__), 'DejaVuSans.ttf')
        pdf.add_font('DejaVu', '', font_path, uni=True)

        pdf.set_font('DejaVu', '', 10)
        col_width = pdf.w / len(rows[0].keys())

        for h in rows[0].keys():
            pdf.cell(col_width, 10, h, border=1)
        pdf.ln()

        for row in rows:
            for val in row.values():
                pdf.cell(col_width, 10, str(val), border=1)
            pdf.ln()

        pdf.output(out_path)
        return out_path

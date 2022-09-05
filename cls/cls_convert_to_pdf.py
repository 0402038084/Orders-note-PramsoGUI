from fpdf import FPDF



'''
P : portrait (vertical)
L : landscape (horizontal)


A4 : 210x297
'''

class pdfclass(FPDF):
    def _init_(self):
        super(pdfclass, self).__init__()
        self.pdf = FPDF(orientation = 'P', unit = 'mm', format='A4')

    def control_entrega_tractor(self, data, directory):
        self.pdf = FPDF(orientation = 'P', unit = 'mm', format='A4')
        TABLE_DATA = data
        self.pdf.add_page()

        self.pdf.set_font("helvetica", size=16, style="B")
        line_height = self.pdf.font_size * 3
        self.pdf.cell(180, txt="CONTROL DE ENTREGA", align="C")
        self.pdf.ln(line_height)
        #--------------------------------------------------------

        self.pdf.set_font("helvetica", size=11, style="B")
        line_height = self.pdf.font_size * 1.2

        self.pdf.cell(txt="Cliente: {}".format(TABLE_DATA[0].title()))
        self.pdf.cell(120, txt="Fecha: {}".format(TABLE_DATA[1]), align="C")
        self.pdf.ln(10)
        self.pdf.set_font("helvetica", size=11)
        line_height = self.pdf.font_size * 1.2

        self.pdf.set_font(style="B")  # enabling bold text
        self.pdf.cell(38, line_height, "Pieza", border=1, align="C")
        self.pdf.set_font(style="B")  # enabling bold text
        self.pdf.cell(24, line_height, "Cantidad", border=1, align="C")
        self.pdf.set_font(style="B")  # enabling bold text
        self.pdf.cell(18, line_height, "Estado", border=1, align="C")
        self.pdf.set_font(style="B")  # enabling bold text
        self.pdf.cell(80, line_height, "Modelo", border=1, align="C")
        self.pdf.ln(line_height)

        self.pdf.set_font(style="")  # enabling bold text
        self.pdf.set_font("helvetica", size=10)

        self.pdf.cell(38, line_height, "Bases", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[4].title()), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "Tractor {}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Adaptadores", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[5]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "Tractor {}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Cogote", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[6]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "Tractor {}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Frente", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[7]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "Tractor {}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Brazos", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[8]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "Tractor {}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Placa Porta Brazos", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[9]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "Tractor {}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Porta Rolo", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[10]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "Tractor {}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Rolo", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[11]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "Tractor {}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Cilindros", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[12]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "Tractor {}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Topes", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[13]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "Tractor {}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Mangueras", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[14]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "Tractor {}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Banderas", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[15]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "Tractor {}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Riendas", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[16]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "Tractor {}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Bulones 5/8", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[17]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "Tractor {}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Bulones 7/8", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[18]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "Tractor {}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Bulones 20mm", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[19]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "Tractor {}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Bulones 9/16", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[20]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "Tractor {}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Grampas", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[21]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "Tractor {}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Resortes", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[22]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "Tractor {}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Calcos", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[23]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "Tractor {}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Kit de resortes", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[24]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "Tractor {}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Kit Hidraúlico", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[25]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "Tractor {}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Kit transferencia", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[26]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "Tractor {}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Teflon", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[27]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "Tractor {}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Precintos", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[28]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "Tractor {}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(160, line_height, "Observaciones: ", border="L, R, T")
        self.pdf.ln(line_height)
        line_height = self.pdf.font_size * 6
        self.pdf.cell(160, line_height, "", border="L, R, B")

        line_height = self.pdf.font_size * 1.2
        self.pdf.ln(line_height)

        self.pdf.output("{}".format(directory[0]))








    def control_entrega_cosechadora(self, data, directory):
        self.pdf = FPDF(orientation = 'P', unit = 'mm', format='A4')
        TABLE_DATA = data
        self.pdf.add_page()

        self.pdf.set_font("helvetica", size=16, style="B")
        line_height = self.pdf.font_size * 3
        self.pdf.cell(180, txt="CONTROL DE ENTREGA", align="C")
        self.pdf.ln(line_height)
        #--------------------------------------------------------

        self.pdf.set_font("helvetica", size=11, style="B")
        line_height = self.pdf.font_size * 1.2

        self.pdf.cell(txt="Cliente: {}".format(TABLE_DATA[0].title()))
        self.pdf.cell(120, txt="Fecha: {}".format(TABLE_DATA[1]), align="C")
        self.pdf.ln(10)
        self.pdf.set_font("helvetica", size=11)
        line_height = self.pdf.font_size * 1.2

        self.pdf.set_font(style="B")  # enabling bold text
        self.pdf.cell(38, line_height, "Pieza", border=1, align="C")
        self.pdf.set_font(style="B")  # enabling bold text
        self.pdf.cell(24, line_height, "Cantidad", border=1, align="C")
        self.pdf.set_font(style="B")  # enabling bold text
        self.pdf.cell(18, line_height, "Estado", border=1, align="C")
        self.pdf.set_font(style="B")  # enabling bold text
        self.pdf.cell(80, line_height, "Modelo", border=1, align="C")
        self.pdf.ln(line_height)

        self.pdf.set_font(style="")  # enabling bold text
        self.pdf.set_font("helvetica", size=10)

        self.pdf.cell(38, line_height, "Bases", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[4].title()), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "Cosechadora {}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Placa Porta Cadenas", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[5]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "Cosechadora {}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Grampas Cadena", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[6]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "Cosechadora {}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Frente", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[7]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "Cosechadora {}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Brazos", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[8]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "Cosechadora {}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Placa Porta Brazos", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[9]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "Cosechadora {}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Porta Rolo", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[10]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "Cosechadora {}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Rolo", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[11]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "Cosechadora {}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Bulones 5/8", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[12]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "Cosechadora {}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Bulones 7/8", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[13]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "Cosechadora {}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Bulones 20mm", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[14]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "Cosechadora {}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Bulones 9/16", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[15]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "Cosechadora {}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Bulones 1/2", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[16]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "Cosechadora {}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Grampas", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[17]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "Cosechadora {}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Resortes", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[18]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "Cosechadora {}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Calcos", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[19]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "Cosechadora {}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(160, line_height, "Observaciones: ", border="L, R, T")
        self.pdf.ln(line_height)
        line_height = self.pdf.font_size * 6
        self.pdf.cell(160, line_height, "", border="L, R, B")

        line_height = self.pdf.font_size * 1.2
        self.pdf.ln(line_height)

        self.pdf.output("{}".format(directory[0]))





    def control_entrega_plataformas(self, data, datatwo, directory):
        self.pdf = FPDF(orientation = 'P', unit = 'mm', format='A4')
        TABLE_DATA = data
        TABLE_DATO = datatwo
        self.pdf.add_page()

        self.pdf.set_font("helvetica", size=16, style="B")
        line_height = self.pdf.font_size * 3
        self.pdf.cell(180, txt="CONTROL DE ENTREGA", align="C")
        self.pdf.ln(line_height)
        #--------------------------------------------------------

        self.pdf.set_font("helvetica", size=11, style="B")
        line_height = self.pdf.font_size * 1.2

        self.pdf.cell(txt="Cliente: {}".format(TABLE_DATA[0].title()))
        self.pdf.cell(120, txt="Fecha: {}".format(TABLE_DATA[1]), align="C")
        self.pdf.ln(10)
        self.pdf.set_font("helvetica", size=11)
        line_height = self.pdf.font_size * 1.2

        self.pdf.set_font(style="B")  # enabling bold text
        self.pdf.cell(38, line_height, "Pieza", border=1, align="C")
        self.pdf.set_font(style="B")  # enabling bold text
        self.pdf.cell(24, line_height, "Cantidad", border=1, align="C")
        self.pdf.set_font(style="B")  # enabling bold text
        self.pdf.cell(18, line_height, "Estado", border=1, align="C")
        self.pdf.set_font(style="B")  # enabling bold text
        self.pdf.cell(80, line_height, "Modelo", border=1, align="C")
        self.pdf.ln(line_height)

        self.pdf.set_font(style="")  # enabling bold text
        self.pdf.set_font("helvetica", size=10)

        self.pdf.cell(38, line_height, "Bases", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[4].title()), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "{}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Brazos", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[5]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "{}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Porta Rolo", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[6]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "{}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Rolo", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[7]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "{}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Bulones 5/8", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[8]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "{}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Bulones 1/2", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[9]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "{}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Bulones 20mm", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[10]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "{}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Bulones 9/16", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[11]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "{}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Grampas", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[12]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "{}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Resortes", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[13]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "{}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Calcos", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[14]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "{}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Adaptadores", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[15]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "{}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(160, line_height, "Observaciones: ", border="L, R, T")
        self.pdf.ln(line_height)
        line_height = self.pdf.font_size * 6
        self.pdf.cell(160, line_height, "", border="L, R, B")


        line_height = self.pdf.font_size * 13
        self.pdf.ln(line_height)
        line_height = self.pdf.font_size * 1.2

        self.pdf.set_font(style="B")  # enabling bold text
        self.pdf.cell(38, line_height, "Pieza", border=1, align="C")
        self.pdf.set_font(style="B")  # enabling bold text
        self.pdf.cell(24, line_height, "Cantidad", border=1, align="C")
        self.pdf.set_font(style="B")  # enabling bold text
        self.pdf.cell(18, line_height, "Estado", border=1, align="C")
        self.pdf.set_font(style="B")  # enabling bold text
        self.pdf.cell(80, line_height, "Modelo", border=1, align="C")
        self.pdf.ln(line_height)
        self.pdf.set_font(style="")

        self.pdf.cell(38, line_height, "Bases", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATO[4].title()), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "{}".format(TABLE_DATO[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Brazos", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATO[5]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "{}".format(TABLE_DATO[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Porta Rolo", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATO[6]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "{}".format(TABLE_DATO[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Rolo", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATO[7]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "{}".format(TABLE_DATO[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Bulones 5/8", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATO[8]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "{}".format(TABLE_DATO[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Bulones 1/2", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATO[9]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "{}".format(TABLE_DATO[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Bulones 20mm", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATO[10]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "{}".format(TABLE_DATO[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Bulones 9/16", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATO[11]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "{}".format(TABLE_DATO[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Grampas", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATO[12]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "{}".format(TABLE_DATO[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Resortes", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATO[13]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "{}".format(TABLE_DATO[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Calcos", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATO[14]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "{}".format(TABLE_DATO[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Adaptadores", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATO[15]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "{}".format(TABLE_DATO[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(160, line_height, "Observaciones: ", border="L, R, T")
        self.pdf.ln(line_height)
        line_height = self.pdf.font_size * 6
        self.pdf.cell(160, line_height, "", border="L, R, B")

        ##########################################################################
        line_height = self.pdf.font_size * 1.2
        self.pdf.ln(line_height)

        self.pdf.output("{}".format(directory[0]))




    def control_entrega_plataforma(self, data, directory):
        self.pdf = FPDF(orientation = 'P', unit = 'mm', format='A4')
        TABLE_DATA = data
        self.pdf.add_page()

        self.pdf.set_font("helvetica", size=16, style="B")
        line_height = self.pdf.font_size * 3
        self.pdf.cell(180, txt="CONTROL DE ENTREGA", align="C")
        self.pdf.ln(line_height)
        #--------------------------------------------------------

        self.pdf.set_font("helvetica", size=11, style="B")
        line_height = self.pdf.font_size * 1.2

        self.pdf.cell(txt="Cliente: {}".format(TABLE_DATA[0].title()))
        self.pdf.cell(120, txt="Fecha: {}".format(TABLE_DATA[1]), align="C")
        self.pdf.ln(10)
        self.pdf.set_font("helvetica", size=11)
        line_height = self.pdf.font_size * 1.2

        self.pdf.set_font(style="B")  # enabling bold text
        self.pdf.cell(38, line_height, "Pieza", border=1, align="C")
        self.pdf.set_font(style="B")  # enabling bold text
        self.pdf.cell(24, line_height, "Cantidad", border=1, align="C")
        self.pdf.set_font(style="B")  # enabling bold text
        self.pdf.cell(18, line_height, "Estado", border=1, align="C")
        self.pdf.set_font(style="B")  # enabling bold text
        self.pdf.cell(80, line_height, "Modelo", border=1, align="C")
        self.pdf.ln(line_height)

        self.pdf.set_font(style="")  # enabling bold text
        self.pdf.set_font("helvetica", size=10)

        self.pdf.cell(38, line_height, "Bases", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[4].title()), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "{}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Brazos", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[5]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "{}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Porta Rolo", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[6]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "{}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Rolo", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[7]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "{}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Bulones 5/8", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[8]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "{}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Bulones 1/2", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[9]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "{}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Bulones 20mm", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[10]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "{}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Bulones 9/16", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[11]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "{}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Grampas", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[12]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "{}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Resortes", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[13]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "{}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Calcos", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[14]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "{}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(38, line_height, "Adaptadores", border=1)
        self.pdf.cell(24, line_height, "{}".format(TABLE_DATA[15]), border=1)
        self.pdf.cell(18, line_height, "", border=1)
        self.pdf.cell(80, line_height, "{}".format(TABLE_DATA[2].title()), border=1)
        self.pdf.ln(line_height)
        self.pdf.cell(160, line_height, "Observaciones: ", border="L, R, T")
        self.pdf.ln(line_height)
        line_height = self.pdf.font_size * 6
        self.pdf.cell(160, line_height, "", border="L, R, B")
        
        ##########################################################################
        line_height = self.pdf.font_size * 1.2
        self.pdf.ln(line_height)

        self.pdf.output("{}".format(directory[0]))

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4, landscape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser
import os
class Relatorios:

    def pegarLinhas(self):
        lista = []
        x = 15
        y = 500
        sala = ''
        cor = ''
        ncor = 0
        y2 = 500
        cotador = 1
        for i in self.tabelacao.get_children():
            lista.append(self.tabelacao.item(i)['values'])

        for linhas in lista:
                self.canvas.setFont("Times-Bold", 10)
                self.canvas.line(x1=15, y1=y2 + 15, x2=15, y2=y2 - 10)
                self.canvas.line(x1=825, y1=y2 + 15, x2=825, y2=y2 - 10)

                if cotador == 1:
                    cor = 'gray'
                    sala = linhas[0]

                if linhas[0] != sala and ncor == 0:
                    cor = 'black'
                    sala = linhas[0]
                    ncor = 1

                else:
                    if linhas[0] != sala and ncor == 1:
                        cor = 'gray'
                        sala = linhas[0]
                        ncor = 0


                self.canvas.setFillColor(cor)
                self.canvas.drawString(x=20, y=y, text=str(linhas[0]))
                self.canvas.drawString(x=63, y=y, text=str(linhas[2]))
                self.canvas.drawString(x=125, y=y, text=str(linhas[3]))
                self.canvas.drawString(x=420, y=y, text=str(linhas[5]))
                self.canvas.drawString(x=765, y=y, text=str(linhas[6]))
                self.canvas.line(x1=15,y1=y-10, x2=825,y2=y-10)
                y = y - 25
                y2 = y2 - 25
                cotador = cotador + 1
                if cotador%20 == 0:
                    self.canvas.showPage()
                    self.cabecalho()
                    x = 15
                    y = 500
                    y2 = 500


    def gerarRelatorios(self):
        self.canvas.showPage()
        self.canvas.save()



    def cabecalho(self):
        self.canvas.setFont("Times-Bold", 16)
        self.canvas.drawString(330, 560, 'Lista De Não Devolvidos')
        self.canvas.setFont("Times-Bold", 12)
        self.canvas.drawString(x=20, y=520, text='Sala')
        self.canvas.line(59, 530, 59, 520)#
        self.canvas.drawString(x=63, y=520, text='Turno')
        self.canvas.line(120, 530, 120, 520)#
        self.canvas.drawString(x=125, y=520, text='Nome')
        self.canvas.line(415, 530, 415, 520)#
        self.canvas.drawString(x=420, y=520, text='Livro')
        self.canvas.line(760, 530, 760, 520)#
        self.canvas.drawString(x=765, y=520, text='Data-Início')
        self.canvas.line(15, 515, 825, 515)#


    def chamar(self):
        self.canvas = canvas.Canvas('<CAMINHO>', pagesize=(landscape(A4)))
        self.cabecalho()
        self.pegarLinhas()
        self.gerarRelatorios()
        webbrowser.open(f'file://<CAMINHO>')






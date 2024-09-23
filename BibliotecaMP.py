"""Produção do Projeto de Extensão,
Ano: 2024
Autor: Alessandro Rodrigues de Oliveira
Direitos Autorais: Autor e E.E.M.T.I. Menezes Pimentel"""
import time
import tkinter as tk
import tkinter.ttk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import importar.conexaobd
from importar.conexaobd import *
from datetime import datetime
# 'conexaobd.py' estão funções para fazer inserção banco de dados ou pegar dados do banco
from importar.validacoes import *
# validações são funções para validar as entrys se são apenas letras ou números
from importar.gerarpdf import *
from tkinter import messagebox
import os

#para funcionar substitua '<CAMINHO> nas seguintes linhas pelo diretorio da sua maquina onde estão as imagens
#linhas: 27, 79, 80, 81, 83, 84, 117, 1057, 1389, 1430, 1620

#EDITE TAMBEM O ARQUIVO 'conexaobd.py' no diretório: importar, pelos dados do seu banco de dados

class BibliotecaMP(Validacoes, Relatorios):
    # def principal, contém as iniciações de todas as funcões
    def __init__(self):
        self.root = ttk.Window(themename='cosmo')
        image = ttk.PhotoImage(file='<CAMINHO>/logo.png')
        self.root.iconphoto(True, image)
        self.tela_root()
        self.frames_da_tela_pesquisas()
        self.frames_da_tela_cadastros()
        self.botoes_pesquisas()
        self.labels_pesquisa()
        self.labels_cadastro()
        self.entrys_pesquisas()
        self.lista_pesquisas()
        self.botoes_cadastro()
        self.frames_queima_arquivos()
        self.labels_queima()
        self.entrys_queima()
        self.botoes_queima()
        self.entrys_cadastros()
        Validacoes.__init__(self)
        self.creditos()
        self.frame_aluno_atualizacao()
        self.frame_atualizacoes()
        self.root.mainloop()



# ********************************************************************************************** Pesquisas
# conficurações da tela root e das abas do notebook
    def tela_root(self):
        # root
        self.root.title("Biblioteca E.E.M.T.I. Menezes Pimentel")
        self.root.configure(background='white')

        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        self.root.geometry("%dx%d" % (width, height))
        self.root.resizable(True, True)
        self.root.minsize(width=1800, height=900)

        style = ttk.style.Style()

        style.configure('custom.TNotebook', tabposition='n')

        # notebook com as abas que serão o menu
        self.notebook = ttk.Notebook(self.root, style='custom.TNotebook')
        self.abas_pesquisas = ttk.Frame(self.notebook)
        self.abas_cadastro = ttk.Frame(self.notebook)
        self.aba_queima_de_arquivos = ttk.Frame(self.notebook)
        self.aba_creditos = ttk.Frame(self.notebook)
        self.aba_atualizao = ttk.Frame(self.notebook)



        # instanciando os icones para as abas
        self.icon_lupa = ttk.PhotoImage(file='<CAMINHO>lupa.png')
        self.icon_cadastros = ttk.PhotoImage(file='<CAMINHO>/cadastros.png')
        self.icon_queima = ttk.PhotoImage(file='<CAMINHO>/queima.png')
        self.icon_atualizacao = ttk.PhotoImage(
            file='<CAMINHO>/atualizacao.png')
        self.icon_sobre = ttk.PhotoImage(file='<CAMINHO>/sobre.png')

        # adicionando título, imagem e lado do texto
        self.notebook.add(self.abas_pesquisas, text='  Pesquisas', compound='left', image=self.icon_lupa)
        self.notebook.add(self.abas_cadastro, text='  Cadastros',  compound='left', image=self.icon_cadastros)
        self.notebook.add(self.aba_queima_de_arquivos, text='  Queima de Arquivos',
                          compound='left', image=self.icon_queima)

        self.notebook.add(self.aba_atualizao, text='  Atualizações', compound='left', image=self.icon_atualizacao)
        self.notebook.add(self.aba_creditos, text='  Créditos',
                          compound='left', image=self.icon_sobre)

        self.notebook.place(relx=0, rely=0, relwidth=1, relheight=0.95)







# configurações dos frames da primeira aba(aba de pesquisa)
    def frames_da_tela_pesquisas(self):

        # frame da parte superior(colocar as informações) e parte inferior(aparecer resultados) da aba pesquisas
        self.frame_pesquisa = ttk.Frame(self.abas_pesquisas)
        self.frame_pesquisa.place(relx=0, rely=0, relwidth=1, relheight=0.5)
        # parte inferior
        self.frame_resultado = ttk.Frame(self.abas_pesquisas)
        self.frame_resultado.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)
        # quando clicar no frame superior todas as listbox(treeview) dos campos entry serão fechados(destruídos)
        self.frame_pesquisa.bind('<1>', self.destroy_all)

        self.logo = ttk.PhotoImage(file=os.path.abspath(
          '<CAMINHO>/logo.png'))
        self.labe_logo = ttk.Label(self.frame_pesquisa, image=self.logo)
        self.labe_logo.place(relx=0.03, rely=0.15)


    def frame_feito(self):
        messagebox.showinfo("", "Ação realizada com sucesso!")

# botões da aba cadastro


# labels da aba pesquisas
    def labels_pesquisa(self):
        # label da entry do id do aluno
        self.label_id_nome = ttk.Label(self.frame_pesquisa, text='ID do Aluno', font=30)
        self.label_id_nome.place(relx=0.2, rely=0.2)

        # label da  entry do id do livro
        self.label_id_livro = ttk.Label(self.frame_pesquisa, text='ID do Livro', font=30)
        self.label_id_livro.place(relx=0.2, rely=0.38)

        # label da entry do nome do aluno
        self.label_nome = ttk.Label(self.frame_pesquisa, text='Nome do Aluno', font=30)
        self.label_nome.place(relx=0.3, rely=0.2)

        # label da entry do nome do livro
        self.label_livro = ttk.Label(self.frame_pesquisa, text='Nome do Livro', font=30)
        self.label_livro.place(relx=0.3, rely=0.38)

        # label da entry da sala
        self.label_sala = ttk.Label(self.frame_pesquisa, text='Sala', font=30)
        self.label_sala.place(relx=0.7, rely=0.2)


# entrys da aba pesquisa
    def entrys_pesquisas(self):

        # entry do id do aluno  ------------------------------------------
        self.id_nome_entry = ttk.Entry(self.frame_pesquisa, bootstyle="success", font=30)
        self.id_nome_entry.place(relx=0.2, rely=0.27, relwidth=0.05)
        # enquando digita o id do aluno é validado o dígito. Será aceito apenas números
        self.id_nome_entry.bind('<KeyRelease>', self.id_nome_keyrelease)
        # quando apertar no botão enter na entry do id do aluno, será preenchido automáticamento o nome do aluno correspodente
        # ao id sem precisar digitar o nome na entry nome(aluno)
        self.id_nome_entry.bind('<Return>', self.buscar_por_idnome)
        self.id_nome_entry.bind('<1>', self.destroy_all)

        # entry do id do livro --------------------------------------------
        self.id_livro_entry = ttk.Entry(self.frame_pesquisa, bootstyle="success", font=30)
        self.id_livro_entry.place(relx=0.2, rely=0.45, relwidth=0.05)
        # enquando digita o id do aluno é validado o dígito. Será aceito apenas números
        self.id_livro_entry.bind('<KeyRelease>', self.id_livro_keyrelease)
        # quando apertar no botão enter na entry do id do livro, será preenchido automáticamento o nome do livro correspodente
        #  ao id sem precisar digitar o nome na entry livro(nome)
        self.id_livro_entry.bind('<Return>', self.buscar_por_idlivro)
        self.id_livro_entry.bind('<1>', self.destroy_all)

        # entry do nome do aluno ------------------------------------------
        self.nome_entry = ttk.Entry(self.frame_pesquisa, bootstyle="success", font=30)
        self.nome_entry.place(relx=0.3, rely=0.27, relwidth=0.35)

        # enquando digita o nome do aluno, é validado o dígito. Será aceito apenas letras. E também será feito uma busca no
        # banco de dados pelo nome do aluno correspondente as letras e apareceram na treeview abaixo
        self.nome_entry.bind('<KeyRelease>', self.cliclar_nome)
        # quando clicar na entry do nome do aluno será aberto a listbox(treeview) do nome do aluno

        self.nome_entry.bind('<1>', self.listboxs_nome)

        # entry do nome do livro ----------------------------------------
        self.livro_entry = ttk.Entry(self.frame_pesquisa, font=30, bootstyle="success")
        self.livro_entry.place(relx=0.3, rely=0.45, relwidth=0.35)

        # será feito uma busca no banco de dados pelo nome do livro correspondente as letras e apareceram na treeview abaixo
        # que será acionado quando clicar na entry livro
        self.livro_entry.bind('<KeyRelease>', self.cliclar_livro)
        self.livro_entry.bind('<1>', self.listboxs_livro)

        # entry da sala -------------------------------------
        self.sala_entry = ttk.Entry(self.frame_pesquisa, bootstyle="success", font=30, )
        self.sala_entry.place(relx=0.7, rely=0.27, relwidth=0.08)
        # será feito uma busca no banco de dados pelo id da sala correspondente as letras e/ou números e apareceram na treeview
        # abaixo que será acionado quando clicar na entry sala
        self.sala_entry.bind('<KeyRelease>', self.cliclar_sala)
        self.sala_entry.bind('<1>', self.listboxs_sala)

        self.notebook.bind('<1>', self.destroy_por_notebook)


    def destroy_por_notebook(self, event):
        self.destroy_all()
        self.destroy_queima_all()
        self.destroy_atualizacoes_all()




# treeview da aba pesquisas(parte inferior da aba pesquisas)
    def lista_pesquisas(self):
        # colunas da treeview que receberá os resultados
        self.columns = ("sala", "id do aluno", "turno", "nome", "id do livro", 'livro', 'data-pegou', "data-devolucao",
                        "status", "telefone")
        self.tabelacao = ttk.Treeview(self.frame_resultado, columns=self.columns, show='headings',
                                      selectmode="browse", bootstyle=SUCCESS)
        self.tabelacao.heading("sala", text='Sala', anchor='w') #1
        self.tabelacao.heading('id do aluno', text='ID.A', anchor='w') #2
        self.tabelacao.heading('turno', text="Turno", anchor='w') #3
        self.tabelacao.heading("nome", text='Nome', anchor='w') #4
        self.tabelacao.heading("id do livro", text='ID.L', anchor='w') #5
        self.tabelacao.heading("livro", text='Livro', anchor='w') #6
        self.tabelacao.heading("data-pegou", text='Data quando pegou', anchor='w') #7
        self.tabelacao.heading("data-devolucao", text='Data de devolução', anchor='w') #8
        self.tabelacao.heading('status', text="Status", anchor='w') #9
        self.tabelacao.heading('telefone', text='Telefone', anchor='w') #10

        self.tabelacao.place(relx=0, rely=0, relwidth=0.99, relheight=0.9)

        self.tabelacao.column('#0', width=0, stretch='no')
        self.tabelacao.column('#1', width=80, stretch='no')
        self.tabelacao.column('#2', width=70, stretch='no')
        self.tabelacao.column('#3', width=120, stretch='no')
        self.tabelacao.column('#4', width=495, stretch='no')
        self.tabelacao.column('#5', width=72, stretch='no')
        self.tabelacao.column('#6', width=495, stretch='no')
        self.tabelacao.column('#7', width=160, stretch='no')
        self.tabelacao.column('#8', width=160, stretch='no')
        self.tabelacao.column('#9', width=120, stretch='no')
        self.tabelacao.column('#10', width=120, stretch='no')

        # duplo clique vai acionar a função para devolver o livro emprestado e atualizar o seu status
        self.tabelacao.bind('<Double-1>', self.baixar)
        # quando clicar também fecha todas as listbox abertas
        self.tabelacao.bind('<1>', self.destroy_all)

        # scrollbar da treeview
        self.scrolllist = ttk.Scrollbar(self.frame_resultado, orient='vertical')
        self.tabelacao.configure(yscroll=self.scrolllist.set)
        self.scrolllist.place(relx=0.99, rely=0, relheight=0.9, relwidth=0.01)



# botoôes da aba pesquisas
    def botoes_pesquisas(self):
        # botão para pesquisar e inserir na treeview da parte inferior
        self.bt_pesquisar = ttk.Button(self.frame_pesquisa, text='Pesquisar', bootstyle='success-outline',
                                       command=self.pesquisar)
        self.bt_pesquisar.place(relx=0.665, rely=0.9, relwidth=0.06)

        # botã para fazer a ficha de empréstimo dos livros
        self.bt_cadastrar = ttk.Button(self.frame_pesquisa, text='Fazer a ficha', bootstyle="success-outline",
                                       command=self.fazer_a_ficha)
        self.bt_cadastrar.place(relx=0.73, rely=0.9, relwidth=0.06)

        # botão para limpar todos os campos
        self.bt_limpar = ttk.Button(self.frame_pesquisa, text='Limpar', bootstyle="success-outline",
                                    command=self.limpar)
        self.bt_limpar.place(relx=0.796, rely=0.9, relwidth=0.06)

        # botão para buscar não devolvidos
        self.bt_ndevolvido = ttk.Button(self.frame_pesquisa, text='Não devolvidos', bootstyle='danger-outline',
                                        command=self.pesquisar_nao_devolvidos)
        self.bt_ndevolvido.place(relx=0.863, rely=0.9)


        self.bt_imprimir = ttk.Button(self.frame_resultado, text='Imprimir', bootstyle='info',
                                      command=self.chamar)
        self.bt_imprimir.place(relx=0.94, rely=0.91)


# listbox da entry nome
    def listboxs_nome(self, event):
        # listbox nome
        self.destroy_all()
        self.scrollbar_nome = ttk.Scrollbar(self.frame_pesquisa, orient='vertical')
        self.scrollbar_nome.place(relx=0.65, rely=0.34, relheight=0.5, relwidth=0.01)
        self.listbox_nome = ttk.Treeview(self.frame_pesquisa, columns=('nomes'), show='tree', bootstyle='success',
                                         selectmode="browse")
        self.listbox_nome.column('#0', width=0, stretch='no')
        self.listbox_nome.column('#1', width=400, )
        self.listbox_nome.place(relx=0.3, rely=0.34, relwidth=0.35, relheight=0.5)
        # double clique coloca a seleção da treeview na entry
        self.listbox_nome.bind('<Double-Button>', self.selecionar_na_entry_nome)


# listbox da enrty sala
    def listboxs_sala(self, event):
        self.destroy_all()
        # listbox sala
        self.scrollbar_sala = ttk.Scrollbar(self.frame_pesquisa, orient='vertical')
        self.scrollbar_sala.place(relx=0.78, rely=0.34, relheight=0.3, relwidth=0.01)
        self.listbox_sala = ttk.Treeview(self.frame_pesquisa, column=('salas'), show='tree', bootstyle='success')
        self.listbox_sala.column('#0', width=0, stretch='no')
        self.listbox_sala.column('#1', width=150, anchor=CENTER, stretch='no')
        self.listbox_sala.place(relx=0.7, rely=0.34, relwidth=0.08, relheight=0.3)
        # double clique coloca a seleção da treeview na entry
        self.listbox_sala.bind('<Double-Button>', self.selecionar_na_entry_sala)


# listbox da entry livro
    def listboxs_livro(self, event):
        # listbox sala
        self.destroy_all()
        self.scrollbar_livro = ttk.Scrollbar(self.frame_pesquisa, orient='vertical')
        self.scrollbar_livro.place(relx=0.65, rely=0.52, relheight=0.3, relwidth=0.01)
        self.listbox_livro = ttk.Treeview(self.frame_pesquisa, columns=('codigo, livros'), show='tree',
                                          bootstyle='success')
        self.listbox_livro.column('#0', width=0, stretch='no')
        self.listbox_livro.column('#1', width=60, stretch='no')
        self.listbox_livro.column('#2', width=605, stretch='no')
        self.listbox_livro.place(relx=0.3, rely=0.52, relwidth=0.35, relheight=0.3)
        # double clique coloca a seleção da treeview na entry
        self.listbox_livro.bind('<Double-Button>', self.selecionar_na_entry_livro)


# comando para aparecer resultados na listbox nome
    def cliclar_nome(self, event):
        # transformar letras maiúsculas na entry
        self.letras_maiusculas(self.nome_entry)
        # validar apenas letras
        Validacoes.validar_letras(self, self.nome_entry)
        # coneção com o banco e inserção do nome dos alunos na treeview(listbox), se o campo não estiver vazio
        conexao = bd()
        if not self.nome_entry.get():
            self.listbox_nome.delete(*self.listbox_nome.get_children())
        else:
            rows = conexao.get_rows(f"SELECT nome FROM alunos WHERE nome like '%{self.nome_entry.get()}%'")
            self.listbox_nome.delete(*self.listbox_nome.get_children())
            for i in rows:
                self.listbox_nome.insert('', END, values=i)


# comando para aparecer resultados na listbox sala
    def cliclar_sala(self, event):
        # transformar letras maiúsculas na entry
        self.letras_maiusculas(self.sala_entry)
        # coneção com o banco e inserção do id das salas na treeview(listbox), se o campo não estiver vazio
        conexao = bd()
        if not self.sala_entry.get():
            self.listbox_sala.delete(*self.listbox_sala.get_children())
        else:
            rows = conexao.get_rows(f"SELECT id FROM salas WHERE id like '%{self.sala_entry.get()}%'")
            self.listbox_sala.delete(*self.listbox_sala.get_children())
            for i in rows:
                self.listbox_sala.insert('', END, values=i)


# comando para aparecer resultados na listbox livro
    def cliclar_livro(self, event):
        # transformar letras maiúsculas na entry
        self.letras_maiusculas(self.livro_entry)
        # coneção com o banco e inserção dos nomes dos livros na treeview(listbox), se o campo não estiver vazio
        conexao = bd()
        if not self.livro_entry.get():
            self.listbox_livro.delete(*self.listbox_livro.get_children())
        else:
            rows = conexao.get_rows(f"SELECT codigo, nome FROM livros WHERE nome like '%{self.livro_entry.get()}%'")
            self.listbox_livro.delete(*self.listbox_livro.get_children())
            for i in rows:
                self.listbox_livro.insert('', END, values=i)


# destruir todas as listbox de uma vez só
    def destroy_all(self, event=""):
        try:
            if self.listbox_nome:
                self.scrollbar_nome.destroy()
                self.listbox_nome.destroy()
        except AttributeError:
            pass

        try:
            if self.listbox_sala:
                self.listbox_sala.destroy()
                self.scrollbar_sala.destroy()
        except AttributeError:
            pass

        try:
            if self.listbox_livro:
                self.listbox_livro.destroy()
                self.scrollbar_livro.destroy()
        except AttributeError:
            pass


# função para pegar o valor da listbox e colocar dentro nas entrys
    def selecionar_na_entry_sala(self, event):
        try:
            select = self.listbox_sala.focus()
            pegar = self.listbox_sala.item(select)
            pegar2 = pegar.get("values")[0]
            self.sala_entry.delete(0, END)
            self.sala_entry.insert(0, pegar2)
            self.destroy_all()

        except (IndexError, UnboundLocalError, _tkinter.TclError):
            pass


    def selecionar_na_entry_nome(self, event):
        try:
            select = self.listbox_nome.focus()
            pegar = self.listbox_nome.item(select)
            pegar2 = pegar.get("values")[0]
            self.nome_entry.delete(0, END)
            self.nome_entry.insert(0, pegar2)
            self.destroy_all()

        except (IndexError, UnboundLocalError ,_tkinter.TclError):
            pass

        bbanco = bd()
        rows = bbanco.get_rows(f"SELECT idsala FROM alunos WHERE nome = '{self.nome_entry.get()}'")
        self.sala_entry.delete(0, END)
        for i in rows:
            self.sala_entry.insert(0, i[0])

        # função para buscar ids do livro ou do aluno no banco de dados e inserir os dados nas entrys (todas)
        self.selecionar_ids(self.nome_entry, self.id_nome_entry, 'id', 'alunos')


    def selecionar_na_entry_livro(self, event):
        try:
            select = self.listbox_livro.focus()
            pegar = self.listbox_livro.item(select)
            pegar2 = pegar.get("values")[1]
            self.livro_entry.delete(0, END)
            self.livro_entry.insert(0, pegar2)
            self.destroy_all()
        except (IndexError, UnboundLocalError, _tkinter.TclError):
            pass

        # função para buscar ids do livro ou do aluno no banco de dados e inserir os dados nas entrys (todas)
        self.selecionar_ids(self.livro_entry, self.id_livro_entry, 'codigo', 'livros')


# função para devolver o livro e mudar o statu da ficha
    def baixar(self, event):
            # condição para só ativar caso na seção de status conter o status 'NÃO DEVOLVIDO'
            select = self.tabelacao.focus()
            pegar = self.tabelacao.item(select)
            try:
                if pegar.get('values')[8] and pegar.get('values')[8].find('NÃO DEVOLVIDO') == 0:
                    # chama função para aparecer um toplevel(aba) de confimação
                    top = Top(self.devolvido_livro, self.frame_feito)
                    top.chamar(self.abas_pesquisas, self.root)

            except IndexError:
                pass


# função para fazer uma ficha de empréstimo
    def fazer_a_ficha(self):
            # caso esse campos não estejão vazios, inserir dados na tabela ficha
            if self.nome_entry.get() and self.livro_entry.get() and self.sala_entry.get():
                # pegar a data da criação da ficha
                pegar_data = datetime.now()
                data = pegar_data.strftime('%d/%m/%Y')

                banco = bd()
                banco.inserir(f"INSERT INTO fichas(inicio, status, codigolivro, idaluno) values('{data}',"
                              f" 'NÃO DEVOLVIDO', {int(self.id_livro_entry.get())}, {int(self.id_nome_entry.get())})")
                # limpar entrys
                self.livro_entry_cadastros.delete(0, END)

                self.id_livro_cadastros.delete(0, END)
                # sinalizar sucesso
                self.frame_feito()




# função ṕara buscar as ids e inserir na listbox(treeview)
    def selecionar_ids(self, entry, id_entry, id, table):
            try:
                select = entry.get()
                banco = bd()
                rows = banco.get_rows(f"SELECT {id} FROM {table} WHERE nome = '{select}'")
                id_entry.delete(0, END)
                id_entry.insert(0, str(rows[0][0]))

            except (IndexError, UnboundLocalError, _tkinter.TclError):
                pass


# função para pesquisar dados e inserir na listbox(treeview) da parte superior da aba pesquisas
    def pesquisar(self):
            # caso não pegue as informações necessárias para buscar algo, retorna a função e não faz nada
            if not self.id_nome_entry.get() and not self.id_livro_entry.get() and not self.sala_entry.get():
                return
            # limpar
            if self.tabelacao.get_children():
                for row in self.tabelacao.get_children():
                    self.tabelacao.delete(row)
            # buscar todas as fichas de um aluno
            if self.nome_entry.get() and not self.livro_entry.get():
                banco = bd()
                rows = banco.get_rows(f"SELECT salas.nome, alunos.id, salas.turno, alunos.nome, fichas.codigolivro, "
                                      f"livros.nome, "
                                      f" TO_CHAR(fichas.inicio, 'dd/mm/yyyy'),"
                                      f" TO_CHAR(fichas.fim, 'dd/mm/yyyy'), fichas.status, alunos.telefone FROM fichas"
                                      f" INNER JOIN alunos ON alunos.id = fichas.idaluno"
                                      f" INNER JOIN salas ON salas.id = alunos.idsala "
                                      f" INNER JOIN livros ON livros.codigo = fichas.codigolivro"
                                      f" WHERE fichas.idaluno = {self.id_nome_entry.get()}")

                for i in rows:
                    self.tabelacao.insert('', END, values=i)
            else:
                # buscar todas as fichas que contenham um certo livro
                if self.livro_entry.get() and not self.nome_entry.get():
                    banco = bd()
                    rows = banco.get_rows(
                        f"SELECT salas.nome, alunos.id, salas.turno, alunos.nome, fichas.codigolivro, livros.nome,  "
                        f"TO_CHAR(fichas.inicio, 'dd/mm/yyyy'), TO_CHAR(fichas.fim, 'dd/mm/yyyy'), fichas.status, alunos.telefone FROM fichas "
                        f" INNER JOIN alunos ON aluno.id = fichas.idaluno "
                        f" INNER JOIN salas on sala.id = alunos.idsala "
                        f"INNER JOIN livros ON livros.codigo = fichas.codigolivro"
                        f" WHERE fichas.codigolivro = {self.id_livro_entry.get()}")
                    for i in rows:
                        self.tabelacao.insert('', END, values=i)
                else:
                    # buscar todas as fichas de uma certa sala
                    if self.sala_entry.get() and not self.nome_entry.get() and not self.livro_entry.get():
                        banco = bd()
                        rows = banco.get_rows(
                            f"SELECT salas.nome, alunos.id,salas.turno, alunos.nome, fichas.codigolivro, livros.nome,"
                            f" TO_CHAR(fichas.inicio, 'dd/mm/yyyy'),  TO_CHAR(fichas.fim, 'dd/mm/yyyy'), "
                            f"fichas.status, alunos.telefone FROM fichas "
                            f" INNER JOIN alunos ON alunos.id = fichas.idaluno "
                            f" INNER JOIN salas on salas.id = alunos.idsala "
                            f" INNER JOIN livros ON livros.codigo = fichas.codigolivro"
                            f" WHERE salas.id = '{self.sala_entry.get()}'"
                            f" ORDER BY salas.id")
                        for i in rows:
                            self.tabelacao.insert('', END, values=i)
                    else:
                        # buscar quando todos os campo estão preenchidos, uma ficha específica
                        banco = bd()
                        rows = banco.get_rows(
                            f"SELECT salas.nome, alunos.id,salas.turno, fichas.codigolivro, livros.nome, alunos.nome, "
                            f" TO_CHAR(fichas.inicio, 'dd/mm/yyyy'),"
                            f"  TO_CHAR(fichas.fim, 'dd/mm/yyyy'),fichas.status,alunos.telefone FROM fichas "
                            f" INNER JOIN alunos ON alunos.id = fichas.idaluno INNER JOIN salas on salas.id = "
                            f"alunos.idsala "
                            f" INNER JOIN livros ON livros.codigo = fichas.codigolivro"
                            f" WHERE fichas.idaluno = {self.id_nome_entry.get()} and fichas.codigolivro = "
                            f" {self.id_livro_entry.get()} AND salas.id = '{self.sala_entry.get()}'")
                        for i in rows:
                            self.tabelacao.insert('', END, values=i)



# pesquisar 'NÃO DEVOLVIDOS'
    def pesquisar_nao_devolvidos(self):

            # limpar
            if self.tabelacao.get_children():
                for row in self.tabelacao.get_children():
                    self.tabelacao.delete(row)
            # filtrar por sala
            if self.sala_entry.get() and not self.nome_entry.get() and not self.livro_entry.get():
                banco = bd()
                rows = banco.get_rows(f"SELECT salas.nome, alunos.id,salas.turno, alunos.nome, fichas.codigolivro, "
                                      f"livros.nome,"
                                      f" TO_CHAR(fichas.inicio, 'dd/mm/yyyy'),  TO_CHAR(fichas.fim, 'dd/mm/yyyy'), fichas.status, "
                                      f"alunos.telefone FROM fichas "
                                      f" INNER JOIN alunos ON alunos.id = fichas.idaluno "
                                      f" INNER JOIN salas on salas.id = alunos.idsala "
                                      f" INNER JOIN livros ON livros.codigo = fichas.codigolivro"
                                      f" WHERE salas.id = '{self.sala_entry.get()}'"
                                      f" AND fichas.status = 'NÃO DEVOLVIDO' ORDER BY salas.id")
                for i in rows:
                    self.tabelacao.insert('', END, values=i)
            else:
                # todos em geral
                if not self.sala_entry.get() and not self.nome_entry.get() and not self.livro_entry.get():
                    banco = bd()
                    rows = banco.get_rows(f"SELECT salas.nome, alunos.id,salas.turno, alunos.nome, fichas.codigolivro, "
                                          f"livros.nome,"
                                          f" TO_CHAR(fichas.inicio, 'dd/mm/yyyy'),  TO_CHAR(fichas.fim, 'dd/mm/yyyy'), fichas.status, "
                                          f"alunos.telefone FROM fichas "
                                          f" INNER JOIN alunos ON alunos.id = fichas.idaluno "
                                          f" INNER JOIN salas on salas.id = alunos.idsala "
                                          f" INNER JOIN livros ON livros.codigo = fichas.codigolivro"
                                          f" WHERE fichas.status = 'NÃO DEVOLVIDO' ORDER BY salas.id")
                    for  i in rows:
                        self.tabelacao.insert('', END, values=i, )



# função para limpar todas as entrys
    def limpar(self):
            self.id_nome_entry.delete(0, END)
            self.nome_entry.delete(0, END)
            self.sala_entry.delete(0, END)
            self.id_livro_entry.delete(0, END)
            self.livro_entry.delete(0, END)
            self.tabelacao.delete(*self.tabelacao.get_children())


# função de buscar o nome do livro pelo id quando apertar enter
    def buscar_por_idlivro(self, event):
            self.livro_entry.delete(0, END)
            bbanco = bd()
            rows = bbanco.get_rows(f"SELECT nome FROM livros WHERE codigo = '{int(self.id_livro_entry.get())}'")
            for i in rows:
                self.livro_entry.insert(0, i[0])


# função de buscar o nome do aluno e/ou da sala pelo id quando apertar enter
    def buscar_por_idnome(self, event):
            self.nome_entry.delete(0, END)
            self.sala_entry.delete(0, END)
            bbanco = bd()
            rows = bbanco.get_rows(f"SELECT nome FROM alunos WHERE id = {int(self.id_nome_entry.get())}")

            for i in rows:
                self.nome_entry.insert(0, i[0])

            rows = bbanco.get_rows(f"SELECT idsala FROM alunos WHERE nome = '{self.nome_entry.get()}'")

            for i in rows:
                self.sala_entry.insert(0, i[0])



# função para mudar status no banco de dados para 'DEVOLVIDO'
    def devolvido_livro(self):
            select = self.tabelacao.focus()
            pegar = self.tabelacao.item(select)

            banco = bd()
            banco.inserir(f" UPDATE fichas SET status = 'DEVOLVIDO' "
                          f" WHERE idaluno = {int(pegar.get('values')[1])}"
                          f" AND inicio = '{pegar.get('values')[6]}'"
                          f" AND codigolivro = {int(pegar.get('values')[4])}")
            # adicionar data da entregua na ficha
            pegar_data = datetime.now()
            data = pegar_data.strftime('%d/%m/%Y')
            banco.inserir(f" UPDATE fichas SET fim = '{data}' "
                          f" WHERE idaluno = {int(pegar.get('values')[1])}"
                          f" AND inicio = '{pegar.get('values')[6]}'"
                          f" AND codigolivro = {int(pegar.get('values')[4])}")


#****************************************************************************************************** Cadastros
# entrys da aba cadastro
    def entrys_cadastros(self):
# entry nome do aluno -----------------------------------------------------------------------------------
        self.nome_entry_cadastros = ttk.Entry(self.frame_cadastro_nome, bootstyle="success", font=15)
        self.nome_entry_cadastros.place(relx=0.04, rely=0.12, relwidth=0.9)

        self.matricula_entry_cadastros = ttk.Entry(self.frame_cadastro_nome, bootstyle="success", font=15)
        self.matricula_entry_cadastros.place(relx=0.7, rely=0.4, relwidth=0.2)

# enquando digita, o nome do aluno será convertido para letras maiúsculas automáticamente
        self.nome_entry_cadastros.bind('<KeyRelease>', self.nome_cadastro_maiuscula)

# entry telefone do aluno
        self.telefone_entry_cadastros = ttk.Entry(self.frame_cadastro_nome, bootstyle="success", font=15)
        self.telefone_entry_cadastros.place(relx=0.3, rely=0.4)

# combobox para escolher uma sala já cadastrada
        self.sala_escolha = ttk.Combobox(self.frame_cadastro_nome, bootstyle="success", font=15)
        self.sala_escolha.place(relx=0.04, rely=0.4, relwidth=0.1)

# quando clicar será feito a busca no banco de dados pelas salas existentes e inserção no combobox
        self.sala_escolha.bind('<1>', self.sala_list)

# entry do nome do livro ------------------------------------------------------------------------------------
        self.livro_entry_cadastros = ttk.Entry(self.frame_cadastro_livros, font=15, bootstyle="success")
        self.livro_entry_cadastros.place(relx=0.04, rely=0.12, relwidth=0.9)
        # enquanto digita o nome do livro, as letras serão convertidas em maiúsculas
        self.livro_entry_cadastros.bind('<KeyRelease>', self.livro_cadastro_maiuscula)

# entry id do livro ---------------------------------------------------------------------------------------
        self.id_livro_cadastros = ttk.Entry(self.frame_cadastro_livros, bootstyle='success', font=15)
        self.id_livro_cadastros.place(relx=0.04, rely=0.4, relwidth=0.18)

# entry nome da sala ------------------------------------------------------------------------------------
        self.sala_entry_cadastros = ttk.Entry(self.frame_cadastro_sala, bootstyle="success", font=15)
        self.sala_entry_cadastros.place(relx=0.04, rely=0.1, relwidth=0.5)

        self.sala_escolha_turno = ttk.Combobox(self.frame_cadastro_sala, bootstyle="success", font=15)
        self.sala_escolha_turno.place(relx=0.04, rely=0.37)

        self.sala_escolha_turno.bind('<1>', self.turnos_list)

# entry do id da sala (sendo obrigado o seu não preenchimento) ----------------------
        self.sala_entry_cadastros_id = ttk.Entry(self.frame_cadastro_sala, bootstyle='success', font=15)
        self.sala_entry_cadastros_id.place(relx=0.04, rely=0.57, relwidth=0.2)
        # enquanto digita, automáticamente, vai formando o id da sala na entry do id da sala
        self.sala_entry_cadastros.bind('<KeyRelease>', self.id_sala)

# entry turnos -----------------------------------------------------------------------------------------
        self.turnos_entry = ttk.Entry(self.frame_cadastro_turno, bootstyle="success", font=15)
        self.turnos_entry.place(relx=0.04, rely=0.2, relwidth=0.5)
# converte letras maiúsculas no campo do turnos
        self.turnos_entry.bind('<KeyRelease>', self.turno_cadastro_maiuscula)


    def botoes_cadastro(self):
# botão para cadastrar sala
        self.bt_cadastrar_sala = ttk.Button(self.frame_cadastro_sala, text='Cadastrar', bootstyle="success-outline",
                                            command=self.cadastrar_sala)
        self.bt_cadastrar_sala.place(relx=0.75, rely=0.85, relwidth=0.2)

# botão para cadastrar alunos
        self.bt_cadastrar_nome = ttk.Button(self.frame_cadastro_nome, text='Cadastrar', bootstyle="success-outline",
                                            command=self.cadastrar_nome)
        self.bt_cadastrar_nome.place(relx=0.85, rely=0.8, relwidth=0.13)

# botão para cadastrar livros
        self.bt_cadastrar_livro = ttk.Button(self.frame_cadastro_livros, text='Cadastrar',
                                             bootstyle="success-outline",
                                             command=self.cadastrar_livros)
        self.bt_cadastrar_livro.place(relx=0.85, rely=0.8, relwidth=0.13)

# botão para cadastrar turnos
        self.bt_cadastrar_turno = ttk.Button(self.frame_cadastro_turno, text='Cadastrar',
                                             bootstyle="success-outline",
                                             command=self.cadastro_turnos)
        self.bt_cadastrar_turno.place(relx=0.75, rely=0.6, relwidth=0.2)


# labels da aba cadastro
    def labels_cadastro(self):
# labels do campo aluno
        self.label_nome_cadastro = ttk.Label(self.frame_cadastro_nome, text='Nome do Aluno', font=30)
        self.label_nome_cadastro.place(relx=0.04, rely=0.03)

        self.label_escolha_sala = ttk.Label(self.frame_cadastro_nome, text='Sala', font=30)
        self.label_escolha_sala.place(relx=0.04, rely=0.3)

        self.label_obrigratorio = ttk.Label(self.frame_cadastro_nome, text='Obrigatório')
        self.label_obrigratorio.place(relx=0.7, rely=0.52)

        self.label_escolha_telefone = ttk.Label(self.frame_cadastro_nome, text='Telefone', font=30)
        self.label_escolha_telefone.place(relx=0.3, rely=0.3)

        self.label_matricula = ttk.Label(self.frame_cadastro_nome, text='N° da Matrícula', font=30)
        self.label_matricula.place(relx=0.7, rely=0.3)

        # labels do campo livro
        self.label_livro_cadastro = ttk.Label(self.frame_cadastro_livros, text='Nome do Livro', font=30)
        self.label_livro_cadastro.place(relx=0.04, rely=0.03)

        self.label_id_livro_cadastro = ttk.Label(self.frame_cadastro_livros, text='Código do Livro', font=30)
        self.label_id_livro_cadastro.place(relx=0.04, rely=0.3)

        self.label_id_livro_cadastro_ex = ttk.Label(self.frame_cadastro_livros, text='Obrigatório')
        self.label_id_livro_cadastro_ex.place(relx=0.04, rely=0.52)

        # labels do campo sala
        self.label_sala_cadastro = ttk.Label(self.frame_cadastro_sala, text='Nome da Sala', font=30)
        self.label_sala_cadastro.place(relx=0.04, rely=0.03)

        self.label_sala_cadastro_ex = ttk.Label(self.frame_cadastro_sala, text='Exemplo: 1 ANO A')
        self.label_sala_cadastro_ex.place(relx=0.04, rely=0.18)

        self.label_sala_cadastro_id_ex = ttk.Label(self.frame_cadastro_sala, text='Automático')
        self.label_sala_cadastro_id_ex.place(relx=0.04, rely=0.65)

        self.label_sala_cadastro_id = ttk.Label(self.frame_cadastro_sala, text='ID da sala', font=30)
        self.label_sala_cadastro_id.place(relx=0.04, rely=0.5)

        self.label_sala_turnos = ttk.Label(self.frame_cadastro_sala, text='Turno', font=30)
        self.label_sala_turnos.place(relx=0.04, rely=0.3)

        # labels do campo gênero
        self.label_turnos_cadastro = ttk.Label(self.frame_cadastro_turno, text='Turno', font=30)
        self.label_turnos_cadastro.place(relx=0.04, rely=0.03)


# confugurações dos frames da aba cadastros
    def frames_da_tela_cadastros(self):

        # frame para cadastrar alunos
        self.frame_cadastro_nome = tk.Frame(self.abas_cadastro, bg='#bac8ba', bd=4, highlightbackground='green',
                                            highlightthickness=3)
        self.frame_cadastro_nome.place(relx=0.15, rely=0.02, relwidth=0.4, relheight=0.45)

        # frame para cadastrar livros
        self.frame_cadastro_livros = tk.Frame(self.abas_cadastro, bg='#bac8ba', bd=4, highlightbackground='green',
                                              highlightthickness=3)
        self.frame_cadastro_livros.place(relx=0.15, rely=0.5, relwidth=0.4, relheight=0.45)

        # frame para cadastrar salas
        self.frame_cadastro_sala = tk.Frame(self.abas_cadastro, bg='#bac8ba', bd=4, highlightbackground='green',
                                            highlightthickness=3)
        self.frame_cadastro_sala.place(relx=0.57, rely=0.02, relwidth=0.25, relheight=0.65)

        # frame para cadastrar gêneros dos livros
        self.frame_cadastro_turno = tk.Frame(self.abas_cadastro, bg='#bac8ba', bd=4, highlightbackground='green',
                                              highlightthickness=3)
        self.frame_cadastro_turno.place(relx=0.57, rely=0.7, relwidth=0.25, relheight=0.25)


    # função para cadastrar sala
    def cadastrar_sala(self):
        # se o campo não estiver vazio, inserir dados na tabela salas
        try:
            if self.sala_entry_cadastros.get():
                banco = bd()
                banco.inserir(f"INSERT INTO salas(id, nome, turno) VALUES('{self.sala_entry_cadastros_id.get().strip()}',"
                              f"'{self.sala_entry_cadastros.get().title()}', '{self.sala_escolha_turno.get().strip()}')")
                # limpa as entrys
                self.sala_entry_cadastros.delete(0, END)
                self.sala_entry_cadastros_id.delete(0, END)
                self.sala_escolha_turno.delete(0, END)
                # aparece uma mensagem para saber que foi realizado com sucesso
                self.frame_feito()


        except (psycopg2.errors.UniqueViolation):
            pass


    # função para cadstrar alunos
    def cadastrar_nome(self):
        # caso o campo do nome do aluno e da sala não estiverem vazios, inserir os dados na tabela alunos

            if self.nome_entry_cadastros.get() and self.sala_escolha.get() or self.telefone_entry_cadastros.get():
                banco = bd()
                banco.inserir(f"INSERT INTO alunos(id, telefone, idsala, nome) VALUES("
                              F"{self.matricula_entry_cadastros.get().strip()},"
                              f"'{self.telefone_entry_cadastros.get().strip()}', "
                              f"'{self.sala_escolha.get().strip()}','{self.nome_entry_cadastros.get().strip()}')")
                # limpar entrys
                self.nome_entry_cadastros.delete(0, END)
                self.sala_escolha.delete(0, END)
                self.telefone_entry_cadastros.delete(0, END)
                self.matricula_entry_cadastros.delete(0, END)

                # sinalizar sucesso
                self.frame_feito()


    # função para cadastrar livros
    def cadastrar_livros(self):
        # caso os campos do nome do livros, id do livro e gênero não estiverem vazios, inserir dados na tabela livros
        try:
            if self.livro_entry_cadastros.get() and self.id_livro_cadastros.get():
                banco = bd()
                banco.inserir(
                    f"INSERT INTO livros(nome, codigo) VALUES('{self.livro_entry_cadastros.get().strip()}', "
                    f"{int(self.id_livro_cadastros.get())})")
                # limpar entrys
                self.livro_entry_cadastros.delete(0, END)
                self.id_livro_cadastros.delete(0, END)
                # sinalizar sucesso
                self.frame_feito()

        except (psycopg2.errors.UniqueViolation):
            pass


    # função para cadastrar turnos
    def cadastro_turnos(self):
        # caso a entry turno não estiver vazia, inserir dados na tabela turnos
        try:
            if self.turnos_entry.get():
                banco = bd()
                banco.inserir(f"INSERT INTO turnos(turno) VALUES('"
                              f"{"".join(self.turnos_entry.get().strip())}')")
                # limpar entrys
                self.turnos_entry.delete(0, END)

                # sinalizar sucesso
                self.frame_feito()

        except psycopg2.errors.UniqueViolation:
            pass


    # função para gerar o id da sala automático
    def id_sala(self, event):
        try:
            # transformar letras da entry sala em maiúsculas
            self.letras_maiusculas(self.sala_entry_cadastros)
            # vai deletando as letras que serão colocadas sem necessidade na entry da id sala
            self.sala_entry_cadastros_id.delete(0, END)
            # por segurança pegar o noome e levar pra maiúscula com o upper
            self.salanome = self.sala_entry_cadastros.get().upper().strip()
            # split a frase em letras separadas
            self.salanome.split()
            # insere o primeiro dígito no começo
            self.sala_entry_cadastros_id.insert(0, self.salanome[0])
            # insere o último dígito no final
            self.sala_entry_cadastros_id.insert(1, self.salanome[-1])
        except IndexError:
            pass


# função para transformar automaticamente as letras das entrys em maiúsculas
    def letras_maiusculas(self, entry):
        upper = entry.get().upper()
        entry.delete(0, END)
        entry.insert(0, upper)


# função para chamar a função de letras maiúsculas para a entry nome(aluno)
    def nome_cadastro_maiuscula(self, event):
        self.letras_maiusculas(self.nome_entry_cadastros)


# função para chamar a função de letras maiúsculas para a entry livro(nome)
    def livro_cadastro_maiuscula(self, event):
        self.letras_maiusculas(self.livro_entry_cadastros)


# função para chamar a função de letras maiúsculas para a entry turnos na aba cadastros
    def turno_cadastro_maiuscula(self, event):
        self.letras_maiusculas(self.turnos_entry)


# busca no banco de dados os turnos na aba cadastros
    def  turnos_list(self, event):
        banco = bd()
        rows_turnos = banco.get_rows('SELECT turno FROM turnos ')

        lista_turnos = []
        for i in rows_turnos:
            lista_turnos.append(i[0])

        self.sala_escolha_turno['values'] = lista_turnos


# busca no banco de dados os ids das salas e colocar na aba cadastros
    def sala_list(self, event):

        banco = bd()
        rows_ids = banco.get_rows('select id from salas')

        lista_ids_salas = []
        for i in rows_ids:
            lista_ids_salas.append(i[0])

        self.sala_escolha['values'] = lista_ids_salas


# função para validar id do aluno
    def id_nome_keyrelease(self, event):
        Validacoes.validar_numeros(self, self.id_nome_entry)


# função para validar id do livro
    def id_livro_keyrelease(self, event):
        Validacoes.validar_numeros(self, self.id_livro_entry)


# ******************************************************************************************************* Queima
    def frames_queima_arquivos(self):
        self.frame_queima = tk.Frame(self.aba_queima_de_arquivos)
        self.frame_queima.place(relx=0, rely=0, relwidth=1, relheight=1)

        # frame para apagar fichas por ano
        self.frame_queimar_ano = tk.Frame(self.frame_queima, bg='#bac8ba', bd=4,
                                          highlightbackground='green',
                                          highlightthickness=3)
        self.frame_queimar_ano.place(relx=0.3, rely=0.1, relwidth=0.19, relheight=0.2)


        # frame para apagar uma certa sala e suas fichas
        self.frame_queimar_sala = tk.Frame(self.frame_queima, bg='#bac8ba', bd=4,
                                           highlightbackground='green',
                                           highlightthickness=3)
        self.frame_queimar_sala.place(relx=0.51, rely=0.1, relwidth=0.19, relheight=0.2)

        # frame para apagar um certo aluno e suas fichas
        self.frame_queimar_aluno = tk.Frame(self.frame_queima, bg='#bac8ba', bd=4,
                                            highlightbackground='green',
                                            highlightthickness=3)
        self.frame_queimar_aluno.place(relx=0.3, rely=0.34, relwidth=0.4, relheight=0.2)

        self.frame_queimar_livro = tk.Frame(self.frame_queima, bg='#bac8ba', bd=4,
                                            highlightbackground='green',
                                            highlightthickness=3)
        self.frame_queimar_livro.place(relx=0.3, rely=0.58, relwidth=0.4, relheight=0.22)

        self.frame_queima.bind('<1>', self.destroy_queima_all)


# entrys da aba queima de arquivos
    def entrys_queima(self):
        self.entry_ano_queima = ttk.Combobox(self.frame_queimar_ano, bootstyle="success")
        self.entry_ano_queima.place(relx=0.1, rely=0.3, relwidth=0.2)


        self.entry_ano_queima.bind('<1>', self.ano_list)


        self.entry_aluno_queima = ttk.Entry(self.frame_queimar_aluno, bootstyle="success", font=15)
        self.entry_aluno_queima.place(relx=0.1, rely=0.3, relwidth=0.7)

        self.entry_aluno_queima.bind('<KeyRelease>', self.cliclar_nome_queima)
        self.entry_aluno_queima.bind('<1>', self.listboxs_aluno_queima)

        self.entry_sala_queima = ttk.Entry(self.frame_queimar_sala, bootstyle="success", font=15)
        self.entry_sala_queima.place(relx=0.1, rely=0.3, relwidth=0.2)

        self.entry_sala_queima.bind('<KeyRelease>', self.cliclar_sala_queima)
        self.entry_sala_queima.bind('<1>', self.listboxs_sala_queima)

        self.entry_livro_queima = ttk.Entry(self.frame_queimar_livro, bootstyle='success', font=15)
        self.entry_livro_queima.place(relx=0.1, rely=0.25, relwidth=0.7)

        self.entry_livro_queima.bind('<1>', self.listboxs_livro_queima)
        self.entry_livro_queima.bind('<KeyRelease>', self.cliclar_livro_queima)

        self.codigolivro = ttk.Entry(self.frame_queimar_livro, bootstyle='success', font=15)
        self.codigolivro.place(relx=0.1, rely=0.65, relwidth=0.15)

        self.codigolivro.bind('<Return>', self.buscar_por_idlivro_queima)





# labels da aba queima de arquivos
    def labels_queima(self):
        self.label_ano_queima = ttk.Label(self.frame_queimar_ano, font=30, text='Ano')
        self.label_ano_queima.place(relx=0.1, rely=0.1)

        self.label_aluno_queima = ttk.Label(self.frame_queimar_aluno, font=30, text='Nome do Aluno')
        self.label_aluno_queima.place(relx=0.1, rely=0.1)

        self.label_sala_queima = ttk.Label(self.frame_queimar_sala, text='Sala', font=30)
        self.label_sala_queima.place(relx=0.1, rely=0.1)

        self.label_livro_queima = ttk.Label(self.frame_queimar_livro, text='Nome do Livro', font=30)
        self.label_livro_queima.place(relx=0.1, rely=0.05)

        self.label_cod_queima = ttk.Label(self.frame_queimar_livro, text='Cod. Livro', font=30)
        self.label_cod_queima.place(relx=0.1, rely=0.5)

        self.label_automatico_queima = ttk.Label(self.frame_queimar_livro, text='Automático')
        self.label_automatico_queima.place(relx=0.1, rely=0.85)

        self.cuidado= ttk.PhotoImage(file=os.path.abspath(
           '<CAMINHO>/cuidado.png'))
        self.cuidado_label = ttk.Label(self.frame_queimar_sala, image=self.cuidado)
        self.cuidado_label.place(relx=0.89, rely=0.018)



# botões da aba queima de arquivos
    def botoes_queima(self):
        self.btn_ano_queima = ttk.Button(self.frame_queimar_ano, text='Apagar', bootstyle='success-outline',
                                         command=self.apagar_ano)
        self.btn_ano_queima.place(relx=0.7, rely=0.6)

        self.btn_aluno_queima = ttk.Button(self.frame_queimar_aluno, text='Apagar', bootstyle='success-outline',
                                           command=self.apagar_por_aluno)
        self.btn_aluno_queima.place(relx=0.85, rely=0.6)

        self.btn_sala_queima = ttk.Button(self.frame_queimar_sala, text='Apagar', bootstyle='success-outline',
                                          command=self.apagar_por_sala)
        self.btn_sala_queima.place(relx=0.7, rely=0.6)

        self.btn_livro_queima = ttk.Button(self.frame_queimar_livro, text='Apagar', bootstyle='success-outline',
                                          command=self.apagar_livro)
        self.btn_livro_queima.place(relx=0.85, rely=0.6)



# treeview da entry aluno queima de arquivos
    def listboxs_aluno_queima(self, event):
        self.destroy_queima_all()
        # listbox nome
        self.scrollbar_nome_queima = ttk.Scrollbar(self.frame_queimar_aluno, orient='vertical')
        self.scrollbar_nome_queima.place(relx=0.8, rely=0.51, relheight=0.5, relwidth=0.02)
        self.listbox_nome_queima = ttk.Treeview(self.frame_queimar_aluno, columns=('nomes'), show='tree',
                                           bootstyle='success',
                                         selectmode="browse")
        (self.listbox_nome_queima.column('#0', width=0, stretch='no'))
        self.listbox_nome_queima.column('#1', width=150, )
        self.listbox_nome_queima.place(relx=0.1, rely=0.51, relwidth=0.7, relheight=0.5)
        # double clique coloca a seleção da treeview na entry
        self.listbox_nome_queima.bind('<Double-Button>', self.double_queima_aluno)




    def listboxs_livro_queima(self, event):
        self.destroy_queima_all()
        # listbox livro
        self.scrollbar_livro_queima = ttk.Scrollbar(self.frame_queimar_livro, orient='vertical')
        self.scrollbar_livro_queima.place(relx=0.8, rely=0.44, relheight=0.5, relwidth=0.02)
        self.listbox_livro_queima = ttk.Treeview(self.frame_queimar_livro, columns=('codigo, nomes'), show='tree',
                                                bootstyle='success',
                                                selectmode="browse")
        (self.listbox_livro_queima.column('#0', width=0, stretch='no'))
        self.listbox_livro_queima.column('#1', width=60, stretch='no')
        self.listbox_livro_queima.column('#2', width=90, )
        self.listbox_livro_queima.place(relx=0.1, rely=0.44, relwidth=0.7, relheight=0.5)
        # double clique coloca a seleção da treeview na entry
        self.listbox_livro_queima.bind('<Double-Button>', self.double_queima_livro)





#  treeview da entry sala queima de arquivos
    def listboxs_sala_queima(self, event):
        self.destroy_queima_all()
        # listbox nome
        self.scrollbar_sala_queima = ttk.Scrollbar(self.frame_queimar_sala, orient='vertical')
        self.scrollbar_sala_queima.place(relx=0.3, rely=0.5, relheight=0.3, relwidth=0.02)
        self.listbox_sala_queima = ttk.Treeview(self.frame_queimar_sala, columns=('nomes'), show='tree',
                                                bootstyle='success',
                                                selectmode="browse")
        (self.listbox_sala_queima.column('#0', width=0, stretch='no'))
        self.listbox_sala_queima.column('#1', width=30, )
        self.listbox_sala_queima.place(relx=0.1, rely=0.5, relwidth=0.2, relheight=0.3)
        # double clique coloca a seleção da treeview na entry
        self.listbox_sala_queima.bind('<Double-Button>', self.double_queima_sala)



# função de buscar o nome do livro pelo id quando apertar enter
    def buscar_por_idlivro_queima(self, event):
        self.entry_livro_queima.delete(0, END)
        banco = bd()
        rows = banco.get_rows(f"SELECT nome FROM livros WHERE codigo = {self.codigolivro.get()}")
        for i in rows:
            self.entry_livro_queima.insert(0, i[0])




# fazer busca no banco de dados e inserir no combobox dos anos
    def ano_list(self, event):
        self.destroy_queima_all()
        banco = bd()
        rows_ids = banco.get_rows('SELECT DISTINCT EXTRACT(year from inicio) FROM fichas')

        lista_anos = []
        for i in rows_ids:
            lista_anos.append(i[0])

        self.entry_ano_queima['values'] = lista_anos


# função para colocar na entry da treewvie aluno
    def double_queima_aluno(self, event):

        try:
            select = self.listbox_nome_queima.focus()
            pegar = self.listbox_nome_queima.item(select)
            pegar2 = pegar.get("values")[0]
            self.entry_aluno_queima.delete(0, END)
            self.entry_aluno_queima.insert(0, pegar2)
            self.listbox_nome_queima.destroy()
            self.scrollbar_nome_queima.destroy()

        except (IndexError, UnboundLocalError, _tkinter.TclError):
            pass




# função para colocar na entry sala
    def double_queima_sala(self, event):

        try:
            select = self.listbox_sala_queima.focus()
            pegar = self.listbox_sala_queima.item(select)
            pegar2 = pegar.get("values")[0]
            self.entry_sala_queima.delete(0, END)
            self.entry_sala_queima.insert(0, pegar2)
            self.listbox_sala_queima.destroy()
            self.scrollbar_sala_queima.destroy()

        except (IndexError, UnboundLocalError, _tkinter.TclError):
            pass




# função para colocar na entry aluno
        # comando para aparecer resultados na listbox nome
    def cliclar_nome_queima(self, event):
# transformar letras maiúsculas na entry
        self.letras_maiusculas(self.entry_aluno_queima)
# validar apenas letras
        Validacoes.validar_letras(self, self.entry_aluno_queima)
# coneção com o banco e inserção do nome dos alunos na treeview(listbox), se o campo não estiver vazio

        if not self.entry_aluno_queima.get():
                self.listbox_nome_queima.delete(*self.listbox_nome_queima.get_children())
        else:
            conexao = bd()
            rows = conexao.get_rows(f"SELECT nome FROM alunos WHERE nome like '%{self.entry_aluno_queima.get()}%'")
            self.listbox_nome_queima.delete(*self.listbox_nome_queima.get_children())
            for i in rows:
                self.listbox_nome_queima.insert('', END, values=i)






# função para colocar na entry ano
    def double_queima_livro(self, event):

        try:
            select = self.listbox_livro_queima.focus()
            pegar = self.listbox_livro_queima.item(select)
            pegar2 = pegar.get("values")[1]
            self.entry_livro_queima.delete(0, END)
            self.entry_livro_queima.insert(0, pegar2)
            self.listbox_livro_queima.destroy()
            self.scrollbar_livro_queima.destroy()
            self.selecionar_ids(self.entry_livro_queima, self.codigolivro, 'codigo', 'livros')

        except (IndexError, UnboundLocalError, _tkinter.TclError):
            pass


    def cliclar_sala_queima(self, event):
        # transformar letras maiúsculas na entry
        self.letras_maiusculas(self.entry_sala_queima)
        # coneção com o banco e inserção do nome dos alunos na treeview(listbox), se o campo não estiver vazio

        if not self.entry_sala_queima.get():
            self.listbox_sala_queima.delete(*self.listbox_sala_queima.get_children())
        else:
            conexao = bd()
            rows = conexao.get_rows(f"SELECT id FROM salas WHERE nome like '%{self.entry_sala_queima.get()}%'")
            self.listbox_sala_queima.delete(*self.listbox_sala_queima.get_children())
            for i in rows:
                self.listbox_sala_queima.insert('', END, values=i)




    def cliclar_livro_queima(self, event):
        # transformar letras maiúsculas na entry
        self.letras_maiusculas(self.entry_livro_queima)
        # coneção com o banco e inserção do nome dos alunos na treeview(listbox), se o campo não estiver vazio

        if not self.entry_livro_queima.get():
            self.listbox_livro_queima.delete(*self.listbox_livro_queima.get_children())
        else:
            conexao = bd()
            rows = conexao.get_rows(f"SELECT codigo, nome FROM livros WHERE nome like '"
                                    f"%{self.entry_livro_queima.get().strip()}%'")
            self.listbox_livro_queima.delete(*self.listbox_livro_queima.get_children())
            for i in rows:
                self.listbox_livro_queima.insert('', END, values=i)



    def destroy_queima_all(self, event=''):
        try:
            if self.listbox_nome_queima:
                self.scrollbar_nome_queima.destroy()
                self.listbox_nome_queima.destroy()
        except AttributeError:
            pass

        try:
            if self.listbox_sala_queima:
                self.scrollbar_sala_queima.destroy()
                self.listbox_sala_queima.destroy()
        except AttributeError:
            pass

        try:
            if self.listbox_livro_queima:
                self.scrollbar_livro_queima.destroy()
                self.listbox_livro_queima.destroy()
        except AttributeError:
            pass



# função para apagar de um certo ano as fichas
    def apagar_ano(self):
        if self.entry_ano_queima.get():
            banco = bd()
            banco.inserir(f"Delete FROM fichas WHERE EXTRACT(YEAR FROM inicio) IN ({int(self.entry_ano_queima.get())})")
            self.entry_ano_queima.delete(0, END)
            self.frame_feito()


# funcção para apagar sala, aluno e fichas de uma sala
    def apagar_por_sala(self):
        if self.entry_sala_queima.get():
            banco = bd()
            banco.inserir(f"delete from fichas where fichas.idaluno in (select alunos.id from alunos where "
                          f"alunos.idsala = '{self.entry_sala_queima.get()}')")
            banco.inserir(f"DELETE FROM alunos WHERE alunos.idsala = '{self.entry_sala_queima.get()}'")
            banco.inserir(f"Delete FROM salas WHERE id = '{self.entry_sala_queima.get()}'")
            self.entry_sala_queima.delete(0, END)
            self.frame_feito()


#função para apagar o aluno
    def apagar_por_aluno(self):
        if self.entry_aluno_queima.get():
            banco = bd()
            banco.inserir(f"DELETE FROM fichas WHERE fichas.idaluno IN (SELECT alunos.id FROM alunos WHERE "
                          f"alunos.nome = "
                          f"'{self.entry_aluno_queima.get()}')")
            banco.inserir(f"DELETE FROM alunos WHERE nome = '{self.entry_aluno_queima.get()}'")
            self.entry_aluno_queima.delete(0, END)
            self.frame_feito()



    def apagar_livro(self):
        if self.entry_livro_queima.get():
            banco = bd()
            banco.inserir(f"DELETE FROM fichas WHERE codigolivro = {self.codigolivro.get().strip()}")
            banco.inserir(f"DELETE FROM livros WHERE nome = '{self.entry_livro_queima.get().strip()}' AND "
                          f"codigo = "
                          f"{self.codigolivro.get().strip()}")
            self.entry_livro_queima.delete(0, END)
            self.codigolivro.delete(0, END)
            self.frame_feito()



#***********************************************************************************************Atualizacoes

# frame aluno atualizacoes
    def frame_aluno_atualizacao(self):
        self.frame_aluno_atualizacoes = tk.Frame(self.aba_atualizao, bg='#bac8ba', bd=4, highlightbackground='green',
                                            highlightthickness=3)
        self.frame_aluno_atualizacoes.place(relx=0.3, rely=0.15, relwidth=0.4, relheight=0.25)

    #****************************************************************************************************Entrys
        self.entry_aluno_atualizacoes = ttk.Entry(self.frame_aluno_atualizacoes, bootstyle='success')
        self.entry_aluno_atualizacoes.place(relx=0.05, rely=0.2, relwidth=0.6)

        self.antes = ttk.Entry(self.frame_aluno_atualizacoes, bootstyle='success')
        self.antes.place(relx=0.05, rely=0.65, relwidth=0.1)

        self.depois = ttk.Combobox(self.frame_aluno_atualizacoes, bootstyle='success')
        self.depois.place(relx=0.3, rely=0.65, relwidth=0.1)

        self.label_aluno_atualizacoes = ttk.Label(self.frame_aluno_atualizacoes, text='Nome do Aluno', font=30)
        self.label_aluno_atualizacoes.place(relx=0.05, rely=0.02)

        self.mudar_telefone = ttk.Entry(self.frame_aluno_atualizacoes, bootstyle='success')
        self.mudar_telefone.place(relx=0.7, rely=0.2)

    #********************************************************************************************************Labels

        self.label_antes = ttk.Label(self.frame_aluno_atualizacoes, text='Antes')
        self.label_antes.place(relx=0.075, rely=0.55)

        self.label_antes = ttk.Label(self.frame_aluno_atualizacoes, text='Depois')
        self.label_antes.place(relx=0.32, rely=0.55)

        self.label_automatico = ttk.Label(self.frame_aluno_atualizacoes, text='Automático')
        self.label_automatico.place(relx=0.05, rely=0.85)

        self.label_fone = ttk.Label(self.frame_aluno_atualizacoes, text='Telefone', font=30)
        self.label_fone.place(relx=0.7, rely=0.02)


        self.label_fone = ttk.Label(self.frame_aluno_atualizacoes, text='Telefone', font=30)
        self.label_fone.place(relx=0.7, rely=0.02)

        self.label_opcional = ttk.Label(self.frame_aluno_atualizacoes, text='Opcional')
        self.label_opcional.place(relx=0.7, rely=0.4)

    #**********************************************************************************Outros
        self.seta_load = ttk.PhotoImage(file=os.path.abspath(
         '<CAMINHO>/seta.png'))
        self.seta = ttk.Label(self.frame_aluno_atualizacoes, image=self.seta_load)
        self.seta.place(relx=0.185, rely=0.69)

        self.btn_mudar_aluno = ttk.Button(self.frame_aluno_atualizacoes, text='Alterar', bootstyle='outline-success',
                                          command=self.mudar_aluno)
        self.btn_mudar_aluno.place(relx=0.85, rely=0.7)


        self.entry_aluno_atualizacoes.bind('<1>', self.listboxs_aluno_atualizacoes)
        self.entry_aluno_atualizacoes.bind('<KeyRelease>', self.inserir_aluno_atualizacoes)
        self.depois.bind('<1>', self.inserir_depois_atualizacoes)
        self.aba_atualizao.bind('<1>', self.destroy_atualizacoes_all)
        self.mudar_telefone.bind('<1>', self.destroy_atualizacoes_all)








# frame atualizacoes sala
    def frame_atualizacoes(self):
    #************************************************************************************************Sala
        self.frame_sala_atualizacoes = tk.Frame(self.aba_atualizao, bg='#bac8ba', bd=4, highlightbackground='green',
                                                 highlightthickness=3)
        self.frame_sala_atualizacoes.place(relx=0.35, rely=0.45, relwidth=0.3, relheight=0.23)
        self.entry_sala_atualizacoes = ttk.Combobox(self.frame_sala_atualizacoes, bootstyle='success')
        self.entry_sala_atualizacoes.place(relx=0.05, rely=0.2, relwidth=0.12)
        self.entry_sala_atualizacoes.bind('<1>', self.inserir_sala_atualizacoes)

        self.turno_antes = ttk.Entry(self.frame_sala_atualizacoes, bootstyle='success')
        self.turno_antes.place(relx=0.05, rely=0.6, relwidth=0.18)
        self.entry_sala_atualizacoes.bind('<<ComboboxSelected>>', self.inserir_turno_arualizacoes)

        self.turno_depois = ttk.Combobox(self.frame_sala_atualizacoes, bootstyle='success')
        self.turno_depois.place(relx=0.41, rely=0.6, relwidth=0.18)

        self.turno_depois.bind('<1>', self.turnos_list_atualizacoes)

        self.seta_load2 = ttk.PhotoImage(file=os.path.abspath('<CAMINHO>/seta.png'))
        self.seta2 = ttk.Label(self.frame_sala_atualizacoes, image=self.seta_load2)
        self.seta2.place(relx=0.26, rely=0.65)

        self.btn_mudar_sala = ttk.Button(self.frame_sala_atualizacoes, text='Alterar', bootstyle='outline-success',
                                         command=self.mudar_turno)
        self.btn_mudar_sala.place(relx=0.8, rely=0.65)


        self.label_sala_atualizacoes = ttk.Label(self.frame_sala_atualizacoes, text='Sala', font=30)
        self.label_sala_atualizacoes.place(relx=0.05, rely=0.02)

        self.label_sala_antes = ttk.Label(self.frame_sala_atualizacoes, text='Antes')
        self.label_sala_antes.place(relx=0.1, rely=0.49)

        self.label_sala_depois = ttk.Label(self.frame_sala_atualizacoes, text='Depois')
        self.label_sala_depois.place(relx=0.46, rely=0.49)

        self.label_automa = ttk.Label(self.frame_sala_atualizacoes, text='Automático')
        self.label_automa.place(relx=0.05, rely=0.82)



# funções para fazer a alteração(troca) no banco de uma sala no turno ou aluno mudar de sala
    def mudar_turno(self):
        banco = bd()
        banco.inserir(f"UPDATE salas SET turno = '{self.turno_depois.get().strip()}' WHERE id = '"
                      f"{self.entry_sala_atualizacoes.get()}'")
        self.entry_sala_atualizacoes.delete(0, END)
        self.turno_antes.delete(0, END)
        self.turno_depois.delete(0, END)
        self.frame_feito()




    def mudar_aluno(self):
        if self.antes.get() and self.depois.get():
            banco = bd()
            banco.inserir(f"UPDATE alunos SET idsala = '{self.depois.get().strip()}' WHERE nome = '"
                          f"{self.entry_aluno_atualizacoes.get().strip()}'")
            self.entry_aluno_atualizacoes.delete(0, END)
            self.antes.delete(0, END)
            self.depois.delete(0, END)
        if self.mudar_telefone.get():
            banco = bd()
            banco.inserir(F"UPDATE alunos SET telefone = '{self.mudar_telefone.get().strip()}' WHERE nome = '"
                          F"{self.entry_aluno_atualizacoes.get().strip()}'")
            self.entry_aluno_atualizacoes.delete(0, END)
            self.antes.delete(0, END)
            self.depois.delete(0, END)
            self.mudar_telefone.delete(0, END)

        self.frame_feito()



    def listboxs_aluno_atualizacoes(self, event):
        # listbox nome
        self.scrollbar_nome_atualizacoes = ttk.Scrollbar(self.frame_aluno_atualizacoes, orient='vertical')
        self.scrollbar_nome_atualizacoes.place(relx=0.65, rely=0.33, relheight=0.5, relwidth=0.02)
        self.listbox_nome_atualizacoes = ttk.Treeview(self.frame_aluno_atualizacoes, columns=('nomes'), show='tree',
                                           bootstyle='success',
                                         selectmode="browse")
        (self.listbox_nome_atualizacoes.column('#0', width=0, stretch='no'))
        self.listbox_nome_atualizacoes.column('#1', width=150, )
        self.listbox_nome_atualizacoes.place(relx=0.05, rely=0.33, relwidth=0.6, relheight=0.5)
        # double clique coloca a seleção da treeview na entry
        self.listbox_nome_atualizacoes.bind('<Double-Button>', self.double_aluno_atualizacoes)



# funções para pegar do banco e colocarnas comboboxs ou treeviews
    def double_aluno_atualizacoes(self, event):


        try:
            select = self.listbox_nome_atualizacoes.focus()
            pegar = self.listbox_nome_atualizacoes.item(select)
            pegar2 = pegar.get("values")[0]
            self.entry_aluno_atualizacoes.delete(0, END)
            self.entry_aluno_atualizacoes.insert(0, pegar2)
            self.listbox_nome_atualizacoes.destroy()
            self.scrollbar_nome_atualizacoes.destroy()
            self.antes.delete(0, END)

            banco = bd()
            rows = banco.get_rows(f"SELECT idsala FROM alunos WHERE nome = '{self.entry_aluno_atualizacoes.get()}'")

            for i in rows:
                self.antes.insert(0,i)

        except (IndexError, UnboundLocalError, _tkinter.TclError):
            pass

        # comando para aparecer resultados na listbox nome



    def inserir_aluno_atualizacoes(self, event):

            # transformar letras maiúsculas na entry
            self.letras_maiusculas(self.entry_aluno_atualizacoes)
            # validar apenas letras
            Validacoes.validar_letras(self, self.entry_aluno_atualizacoes)
            # coneção com o banco e inserção do nome dos alunos na treeview(listbox), se o campo não estiver vazio

            if not self.entry_aluno_atualizacoes.get():
                self.listbox_nome_atualizacoes.delete(*self.listbox_nome_atualizacoes.get_children())
            else:
                conexao = bd()
                rows = conexao.get_rows(f"SELECT nome FROM alunos WHERE nome like '"
                                        f"%{self.entry_aluno_atualizacoes.get()}%'")
                self.listbox_nome_atualizacoes.delete(*self.listbox_nome_atualizacoes.get_children())
                for i in rows:
                    self.listbox_nome_atualizacoes.insert('', END, values=i)




    def inserir_depois_atualizacoes(self, event):
        self.destroy_atualizacoes_all()
        banco = bd()
        rows_ids = banco.get_rows('SELECT id FROM salas')
        lista_ids_salas = []
        for i in rows_ids:
            lista_ids_salas.append(i[0])
        self.depois['values'] = lista_ids_salas



    def inserir_sala_atualizacoes(self, event):
        self.destroy_atualizacoes_all()
        banco = bd()
        rows_ids = banco.get_rows('SELECT id FROM salas')
        lista_ids_salas = []
        for i in rows_ids:
            lista_ids_salas.append(i[0])
        self.entry_sala_atualizacoes['values'] = lista_ids_salas



    def destroy_atualizacoes_all(self, event=''):
        try:
            if self.listbox_nome_atualizacoes:
                self.scrollbar_nome_atualizacoes.destroy()
                self.listbox_nome_atualizacoes.destroy()
        except AttributeError:
            pass

        try:
            if self.listbox_sala_atualizacoes:
                self.scrollbar_sala_atualizacoes.destroy()
                self.listbox_sala_atualizacoes.destroy()
        except AttributeError:
            pass



    def inserir_turno_arualizacoes(self, event):

        # transformar letras maiúsculas na entry
        self.letras_maiusculas(self.entry_sala_atualizacoes)

        conexao = bd()
        rows = conexao.get_rows(f"SELECT turno FROM salas WHERE id = '"
                                    f"{self.entry_sala_atualizacoes.get()}'")
        self.turno_antes.delete(0, END)
        for i in rows:
            self.turno_antes.insert(0, i)




    # busca no banco de dados os turnos na aba cadastros
    def turnos_list_atualizacoes(self, event):
        banco = bd()
        rows_turnos = banco.get_rows('SELECT turno FROM turnos ')

        lista_turnos = []
        for i in rows_turnos:
            lista_turnos.append(i[0])

        self.turno_depois['values'] = lista_turnos



#*********************************************************************************************Creditos
# aba creditos
    def creditos(self):
        self.logo_creditos = ttk.PhotoImage(file='<CAMINHO>/logo.png')
        self.label_logo = ttk.Label(self.aba_creditos, image=self.logo_creditos)
        self.label_logo.place(relx=0.445, rely=0.15)
        self.label_menezes1 = ttk.Label(self.aba_creditos, text='\u00A9'+' Menezes Pimentel')
        self.label_menezes1.place(relx=0.47, rely=0.46)
        self.label_menezes = ttk.Label(self.aba_creditos, text='\u00A9' + ' Alessandro Rodrigues de Oliveira (A.R.O)')
        self.label_menezes.place(relx=0.44, rely=0.48)


class Top:
    def __init__(self,funcao, feito):
        self.funcao = funcao
        self.feito = feito


    def chamar(self, aba, root):
        self.top = ttk.Toplevel(master=aba, title='')
        self.top.geometry("250x100")
        self.top.wait_visibility()
        x = root.winfo_x() + root.winfo_width() // 2 - self.top.winfo_width() // 2
        y = root.winfo_y() + root.winfo_height() // 2 - self.top.winfo_height() // 2
        self.top.geometry(f"+{x}+{y}")
        self.top.focus()
        self.top.transient(root)
        message = ttk.Label(self.top, text='Devolver o livro')
        message.place(relx=0.1, rely=0.2)
        buttonsim = ttk.Button(self.top, text='Sim', bootstyle='success', command=self.fazer)
        buttonsim.place(relx=0.5, rely=0.6)
        buttonnao = ttk.Button(self.top, text='Não', bootstyle='danger', command=self.top.destroy)
        buttonnao.place(relx=0.7, rely=0.6)

    def fazer(self):
        funcao = self.funcao()
        self.top.destroy()
        self.feito()


BibliotecaMP()



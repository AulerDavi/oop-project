# gui.py
from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLabel, QLineEdit, QPushButton, QComboBox, 
                             QTextEdit, QGroupBox, QFormLayout, QMessageBox)
from PySide6.QtCore import Qt
import models

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Análise de Solos")
        self.resize(750, 720)

        self.setStyleSheet("""
            QMainWindow { 
                background-color: #121212; 
            }
            QLabel {
                color: #e2e8f0;
                font-size: 12px;
            }
            QGroupBox { 
                font-weight: bold; 
                border: 1px solid #2d2d2d; 
                border-radius: 6px; 
                margin-top: 10px;
                padding: 15px 10px 10px 10px; 
                background-color: #1e1e1e; 
                color: #f1f5f9;
            }
            QGroupBox::title { 
                subcontrol-origin: padding; 
                subcontrol-position: top left;
                top: 2px;
                left: 10px;
                color: #60a5fa;
                font-size: 13px;
            }
            QLineEdit, QComboBox { 
                border: 1px solid #475569; 
                border-radius: 4px; 
                padding: 6px; 
                background-color: #1e293b; 
                color: #f8fafc; 
            }
            QLineEdit:focus, QComboBox:focus { 
                border: 1px solid #3b82f6; 
                background-color: #0f172a; 
            }
            QComboBox::drop-down {
                border: none;
            }
            QComboBox QAbstractItemView {
                background-color: #1e293b;
                color: #f8fafc;
                selection-background-color: #2563eb;
                selection-color: #ffffff;
            }
            QPushButton { 
                background-color: #2563eb; 
                color: white; 
                font-weight: bold; 
                border-radius: 4px; 
                padding: 10px; 
                border: none; 
                margin-top: 10px;
            }
            QPushButton:hover { 
                background-color: #1d4ed8; 
            }
            QPushButton:pressed {
                background-color: #1e40af;
            }
            QTextEdit { 
                background-color: #09090b; 
                color: #34d399;  
                font-family: 'Consolas', monospace; 
                border: 1px solid #27272a;
                border-radius: 4px; 
                padding: 8px; 
                margin-top: 10px;
            }
            QMessageBox {
                background-color: #1e1e1e;
            }
            QMessageBox QLabel {
                color: #ffffff;
            }
        """)

        # Widget Central e Layout Principal
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # ---- Bloco do Técnico ----
        tec_group = QGroupBox("Dados do Técnico")
        tec_layout = QFormLayout(tec_group)
        self.input_txt_nome = QLineEdit()
        
        # CPF configurado com resposta dinâmica ao digitar
        self.input_txt_cpf = QLineEdit()
        self.input_txt_cpf.setPlaceholderText("000.000.000-00")
        self.input_txt_cpf.textEdited.connect(self.formatar_cpf)
        
        self.input_txt_registro = QLineEdit()
        self.input_txt_empresa = QLineEdit()
        self.input_txt_email = QLineEdit()
        
        # Telefone configurado com resposta dinâmica ao digitar
        self.input_txt_telefone = QLineEdit()
        self.input_txt_telefone.setPlaceholderText("(00) 00000-0000")
        self.input_txt_telefone.textEdited.connect(self.formatar_telefone)
        
        tec_layout.addRow("Nome:", self.input_txt_nome)
        tec_layout.addRow("CPF:", self.input_txt_cpf)
        tec_layout.addRow("Registro:", self.input_txt_registro)
        tec_layout.addRow("Empresa:", self.input_txt_empresa)
        tec_layout.addRow("Email:", self.input_txt_email)
        tec_layout.addRow("Telefone:", self.input_txt_telefone)

        # ---- Bloco do Solo ----
        solo_group = QGroupBox("Dados do Solo")
        solo_layout = QFormLayout(solo_group)
        
        self.input_solo_tipo = QComboBox()
        self.input_solo_tipo.addItems(["Arenoso", "Argiloso", "Humoso", "Calcário"])
        
        self.input_solo_lat = QLineEdit()
        self.input_solo_lat.setPlaceholderText("Ex: -23.5505")
        self.input_solo_lon = QLineEdit()
        self.input_solo_lon.setPlaceholderText("Ex: -46.6333")
        
        solo_layout.addRow("Tipo de Solo:", self.input_solo_tipo)
        solo_layout.addRow("Latitude:", self.input_solo_lat)
        solo_layout.addRow("Longitude:", self.input_solo_lon)

        # Colocar Técnico e Solo lado a lado
        top_layout = QHBoxLayout()
        top_layout.addWidget(tec_group)
        top_layout.addWidget(solo_group)
        main_layout.addLayout(top_layout)

        # ---- Bloco da Análise ----
        analise_group = QGroupBox("Configuração da Análise")
        analise_layout = QFormLayout(analise_group)
        
        self.input_ana_codigo = QLineEdit()
        
        self.combo_tipo_analise = QComboBox()
        self.combo_tipo_analise.addItems(["pH", "Umidade", "Análise de Nutrientes", "Temperatura"])
        self.combo_tipo_analise.currentIndexChanged.connect(self.atualizar_label_medida)
        
        self.label_sub_metrica = QLabel("Nutriente específico:")
        self.combo_sub_metrica = QComboBox()
        self.combo_sub_metrica.addItems(["Nitrogênio", "Fósforo", "Potássio"])
        self.combo_sub_metrica.currentIndexChanged.connect(self.atualizar_label_medida)
        
        self.label_valor_medida = QLabel("Valor do pH:")
        self.input_ana_valor = QLineEdit()

        analise_layout.addRow("Código da Análise:", self.input_ana_codigo)
        analise_layout.addRow("Tipo de Análise:", self.combo_tipo_analise)
        analise_layout.addRow(self.label_sub_metrica, self.combo_sub_metrica)
        analise_layout.addRow(self.label_valor_medida, self.input_ana_valor)
        main_layout.addWidget(analise_group)

        # ---- Botão de Ação ----
        self.btn_calcular = QPushButton("Gerar Relatório de Análise")
        self.btn_calcular.clicked.connect(self.processar_analise)
        main_layout.addWidget(self.btn_calcular)

        # ---- Output do Resultado ----
        self.txt_resultado = QTextEdit()
        self.txt_resultado.setReadOnly(True)
        self.txt_resultado.setPlaceholderText("O relatório detalhado aparecerá aqui...")
        main_layout.addWidget(self.txt_resultado)
        
        self.atualizar_label_medida()

    def formatar_cpf(self, text):
        pos = self.input_txt_cpf.cursorPosition()
        old_len = len(text)

        digitos = "".join(filter(str.isdigit, text))[:11]
        if not digitos:
            self.input_txt_cpf.setText("")
            return
            
        if len(digitos) <= 3:
            formatado = digitos
        elif len(digitos) <= 6:
            formatado = f"{digitos[:3]}.{digitos[3:]}"
        elif len(digitos) <= 9:
            formatado = f"{digitos[:3]}.{digitos[3:6]}.{digitos[6:]}"
        else:
            formatado = f"{digitos[:3]}.{digitos[3:6]}.{digitos[6:9]}-{digitos[9:]}"
            
        self.input_txt_cpf.setText(formatado)
        
        # Reposiciona o cursor de forma inteligente baseado no fluxo da digitação
        if pos == old_len:
            self.input_txt_cpf.setCursorPosition(len(formatado))
        else:
            self.input_txt_cpf.setCursorPosition(min(pos, len(formatado)))

    def formatar_telefone(self, text):
        pos = self.input_txt_telefone.cursorPosition()
        old_len = len(text)

        # Filtra mantendo apenas números e limitando a 11 dígitos (DDD + 9 dígitos)
        digitos = "".join(filter(str.isdigit, text))[:11]
        if not digitos:
            self.input_txt_telefone.setText("")
            return
            
        if len(digitos) <= 2:
            formatado = f"({digitos}"
        elif len(digitos) <= 6:
            formatado = f"({digitos[:2]}) {digitos[2:]}"
        elif len(digitos) <= 10:
            formatado = f"({digitos[:2]}) {digitos[2:6]}-{digitos[6:]}"
        else:
            formatado = f"({digitos[:2]}) {digitos[2:7]}-{digitos[7:]}"
            
        self.input_txt_telefone.setText(formatado)
        
        # Reposiciona o cursor de forma inteligente baseado no fluxo da digitação
        if pos == old_len:
            self.input_txt_telefone.setCursorPosition(len(formatado))
        else:
            self.input_txt_telefone.setCursorPosition(min(pos, len(formatado)))

    def atualizar_label_medida(self):
        opcao = self.combo_tipo_analise.currentText()

        if opcao == "Análise de Nutrientes":
            self.label_sub_metrica.show()
            self.combo_sub_metrica.show()
            
            sub_opcao = self.combo_sub_metrica.currentText()
            unidades = {
                "Nitrogênio": "Teor de Nitrogênio (g/dm³):",
                "Fósforo": "Teor de Fósforo (mg/dm³):",
                "Potássio": "Teor de Potássio (mg/dm³):"
            }
            self.label_valor_medida.setText(unidades.get(sub_opcao, "Valor:"))
        else:
            self.label_sub_metrica.hide()
            self.combo_sub_metrica.hide()
            
            unidades = {
                "pH": "Valor do pH:",
                "Umidade": "Porcentagem de Umidade (%):",
                "Temperatura": "Temperatura do Solo (°C):"
            }
            self.label_valor_medida.setText(unidades.get(opcao, "Valor:"))

    def processar_analise(self):
        try:
            cpf_limpo = "".join(filter(str.isdigit, self.input_txt_cpf.text()))
            telefone_limpo = "".join(filter(str.isdigit, self.input_txt_telefone.text()))

            if len(cpf_limpo) != 11:
                raise ValueError("O CPF deve conter exatamente 11 dígitos numéricos.")
            if len(telefone_limpo) < 10:
                raise ValueError("O Telefone deve conter o DDD e o número completo.")

            # Instanciar Técnico
            tecnico = models.Tecnico(
                nome=self.input_txt_nome.text(),
                cpf=cpf_limpo,
                registro=int(self.input_txt_registro.text()),
                empresa=self.input_txt_empresa.text(),
                email=self.input_txt_email.text(),
                telefone=int(telefone_limpo)
            )
            
            # Instanciar Solo
            solo = models.Solo(
                tipo=self.input_solo_tipo.currentText(),
                latitude=float(self.input_solo_lat.text()),
                longitude=float(self.input_solo_lon.text())
            )
            
            codigo_analise = int(self.input_ana_codigo.text())
            valor_medido = float(self.input_ana_valor.text())
            tipo_analise = self.combo_tipo_analise.currentText()

            if tipo_analise == "Análise de Nutrientes":
                tipo_analise = self.combo_sub_metrica.currentText()

            if tipo_analise == "pH":
                analise = models.AnalisePH(codigo_analise, tecnico, solo, valor_medido)
            elif tipo_analise == "Umidade":
                analise = models.AnaliseUmidade(codigo_analise, tecnico, solo, valor_medido)
            elif tipo_analise == "Nitrogênio":
                analise = models.AnaliseNitrogenio(codigo_analise, tecnico, solo, valor_medido)
            elif tipo_analise == "Fósforo":
                analise = models.AnaliseFosforo(codigo_analise, tecnico, solo, valor_medido)
            elif tipo_analise == "Potássio":
                analise = models.AnalisePotassio(codigo_analise, tecnico, solo, valor_medido)
            elif tipo_analise == "Temperatura":
                analise = models.AnaliseTemperatura(codigo_analise, tecnico, solo, valor_medido)
            
            self.txt_resultado.setText(analise.exibir_informacoes())

        except ValueError as err:
            QMessageBox.critical(self, "Erro de Validação", f"Verifique os dados inseridos.\nErro: {err}")
        except Exception as err:
            QMessageBox.critical(self, "Erro Inesperado", f"Preencha todos os campos corretamente.\nErro: {err}")

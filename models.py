class Tecnico:
    def __init__(self, nome: str, cpf: str, registro: int, empresa: str, email: 
                 str, telefone: int):
        self.nome = nome
        self.cpf = cpf
        self.registro = registro
        self.empresa = empresa
        self.email = email
        self.telefone = telefone

    def validar_cpf(self, cpf: str):
        if len(cpf) != 11:
            return False
        return True

    def validar_email(self, email: str):
        if '@' not in email:
            return False
        return True

    def exibir_dados(self):
        if self.validar_cpf(self.cpf) and self.validar_email(self.email):
            return (f'Nome -> {self.nome}\n'
                    f'CPF -> {self.cpf}\n'
                    f'Registro -> {self.registro}\n'
                    f'Empresa -> {self.empresa}\n'
                    f'Email -> {self.email}\n'
                    f'Telefone -> {self.telefone}\n')
        else:
            raise ValueError('Dados inválidos')

class Solo:
    def __init__(self, tipo: str, latitude: float, longitude: float):
        self.tipo = tipo
        self.latitude = latitude
        self.longitude = longitude

    def validar_coordenadas(self, latitude, longitude):
        if not -90 <= latitude <= 90 or not -180 <= longitude <= 180:
            return False
        return True

    def exibir_dados(self):
        if self.validar_coordenadas(self.latitude, self.longitude):
            return (f'Tipo -> {self.tipo}\n'
                    f'Localização -> {self.latitude}, {self.longitude}\n')
        else:
            raise ValueError('Coordenada inválida')

class Analise:
    def __init__(self, codigo: int, responsavel: Tecnico, solo: Solo):
        self.codigo = codigo
        self.responsavel = responsavel
        self.solo = solo
    def gerar_resultado(self):
        return
    def exibir_informacoes(self):
        return (f'Responsável: \n{self.responsavel.exibir_dados()}\n'
                f'Solo: \n{self.solo.exibir_dados()}\n')

class AnalisePH(Analise):
    def __init__(self, codigo: int, responsavel: Tecnico, solo: Solo, ph: float):
        super().__init__(codigo, responsavel, solo)
        self.ph = ph
    def gerar_resultado(self):
        if self.ph < 6:
            return 'Solo ácido'
        elif 6 <= self.ph <= 7:
            return 'Solo neutro'
        else:
            return 'Solo alcalino'
    def exibir_informacoes(self):
        return (f'{super().exibir_informacoes()}'
                f'pH -> {self.ph}\n'
                f'Resultado -> {self.gerar_resultado()}\n')

class AnaliseUmidade(Analise):
    def __init__(self, codigo: int, responsavel: Tecnico, solo: Solo, umidade: float):
        super().__init__(codigo, responsavel, solo)
        self.umidade = umidade
    def gerar_resultado(self):
        if self.umidade < 30:
            return 'Umidade baixa'
        elif 30 <= self.umidade <= 70:
            return 'Umidade ideal'
        else:
            return 'Solo muito úmido'
    def exibir_informacoes(self):
        return (f'{super().exibir_informacoes()}'
                f'Umidade -> {self.umidade}%\n'
                f'Resultado -> {self.gerar_resultado()}\n')

class AnaliseNitrogenio(Analise):
    def __init__(self, codigo: int, responsavel: Tecnico, solo: Solo, nitrogenio: float):
        super().__init__(codigo, responsavel, solo)
        self.nitrogenio = nitrogenio
    def gerar_resultado(self):
        if self.nitrogenio < 40:
            return 'Baixo nitrogênio'
        else:
            return 'Nitrogênio adequado'
    def exibir_informacoes(self):
        return (f'{super().exibir_informacoes()}'
                f'Nitrogênio -> {self.nitrogenio}g/dm³\n'
                f'Resultado -> {self.gerar_resultado()}\n')

class AnaliseFosforo(Analise):
    def __init__(self, codigo: int, responsavel: Tecnico, solo: Solo, fosforo: float):
        super().__init__(codigo, responsavel, solo)
        self.fosforo = fosforo
    def gerar_resultado(self):
        if self.fosforo < 15:
            return 'Fósforo baixo'
        else:
            return 'Fósforo adequado'
    def exibir_informacoes(self):
        return (f'{super().exibir_informacoes()}'
                f'Fósforo -> {self.fosforo}mg/dm³\n'
                f'Resultado -> {self.gerar_resultado()}\n')

class AnalisePotassio(Analise):
    def __init__(self, codigo: int, responsavel: Tecnico, solo: Solo, potassio: float):
        super().__init__(codigo, responsavel, solo)
        self.potassio = potassio
    def gerar_resultado(self):
        if self.potassio < 20:
            return 'Potássio insuficiente'
        else:
            return 'Potássio adequado'
    def exibir_informacoes(self):
        return (f'{super().exibir_informacoes()}'
                f'Potássio -> {self.potassio}mg/dm³\n'
                f'Resultado -> {self.gerar_resultado()}\n')

class AnaliseTemperatura(Analise):
    def __init__(self, codigo: int, responsavel: Tecnico, solo: Solo, temperatura: float):
        super().__init__(codigo, responsavel, solo)
        self.temperatura = temperatura
    def gerar_resultado(self):
        if self.temperatura < 10:
            return 'Solo frio'
        elif self.temperatura <= 30:
            return 'Temperatura ideal'
        else:
            return 'Solo muito quente'
    def exibir_informacoes(self):
        return (f'{super().exibir_informacoes()}'
                f'Temperatura -> {self.temperatura}°C\n'
                f'Resultado -> {self.gerar_resultado()}\n')

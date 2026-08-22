import csv

# Molde do Aluno: dados estruturados para salvar e metodo para retornar
class Discente:
    def __init__(self, dados):
        self.matricula = dados['matricula']
        self.nome_discente = dados['nome_discente']
        self.ano_ingresso = dados['ano_ingresso']
        self.periodo_ingresso = dados['periodo_ingresso']
        self.tipo_discente = dados['tipo_discente']
        self.status_discente = dados['status_discente']
        self.nivel_ensino = dados['nivel_ensino']
        self.nome_curso = dados['nome_curso']
        self.modalidade_educacao = dados['modalidade_educacao']
        self.nome_unidade = dados['nome_unidade']
        self.nome_unidade_gestora = dados['nome_unidade_gestora']

    def get_dados(self):
        return {
            'matricula': self.matricula,
            'nome_discente': self.nome_discente,
            'ano_ingresso': self.ano_ingresso,
            'periodo_ingresso': self.periodo_ingresso,
            'tipo_discente': self.tipo_discente,
            'status_discente': self.status_discente,
            'nivel_ensino': self.nivel_ensino,
            'nome_curso': self.nome_curso,
            'modalidade_educacao': self.modalidade_educacao,
            'nome_unidade': self.nome_unidade,
            'nome_unidade_gestora': self.nome_unidade_gestora
        }

# Função para Ler o CSV e criar a Lista de Objetos
def ler_csv(arquivo):
   #TODO 
    return

# Função para Imprimir um Aluno
def imprimir_aluno(aluno):
    #TODO 
    return

# Função para Salvar TODA a lista em Arquivo TXT
def salvar_txt(lista_de_alunos, arquivo_saida):
    #TODO 
    return

def main():
    #TODO 


# Start do arquivo
if __name__ == "__main__":
    main()   
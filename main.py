

class AFN():
    def __init__(self):
        self.numero_de_estados = 4
        self.numero_de_alfabetos = 2
        self.numero_de_estados_finais = 1
        self.estado_inicial = 0
        self.estado_final = 1
        self.alfabetos = ['0', '1']
        self.afn = [[0 for x in range(int(self.numero_de_alfabetos))] for y in range(int(self.numero_de_estados))]
        self.afn = [['1', '0'], ['1', '2'], ['2', '2']]

    def setAfn(self):
        self.numero_de_estados = 4
        self.numero_de_alfabetos = 2
        self.numero_de_estados_finais = 1
        self.estado_inicial = 'q1'
        self.estado_final = '4'

        arquivo_entrada_automato = open('AFN/arquivos/arquivo_entrada_automato.txt', 'r')
        for automato in arquivo_entrada_automato:
            self.alfabetos = [0 for x in range(int(self.numero_de_alfabetos))]
            for i in range(0, int(self.numero_de_alfabetos)):
                self.alfabetos[i]= automato
    
        self.afn = [[0 for x in range(int(self.numero_de_alfabetos))] for y in range(int(self.numero_de_estados))]

        print("Presione Enter para as transições:")
        for i in range(0,int(self.numero_de_estados)):
            for j in range(0, int(self.numero_de_alfabetos)):
                self.afn[i][j] = input("(q"+str(i)+","+str(j)+")--> q" + str(i))

    def setarParametros(self, ns, na, nf, fs, ff, a, d):
        self.numero_de_estados = ns
        self.numero_de_alfabetos = na
        self.numero_de_estados_finais = nf
        self.estado_inicial = fs
        self.estado_final = ff
        self.alfabetos = a
        self.afn = d

    def mostrarSet(self):
        arquivo_saida_resultado = open('AFN/arquivos/arquivo_saida_resultado.txt','w')
        arquivo_saida_resultado.write("\n")
        arquivo_saida_resultado.write("===========================================\n")
        arquivo_saida_resultado.write("               AFN - INICIO                \n")
        arquivo_saida_resultado.write("===========================================\n")
        
        arquivo_saida_resultado.write("\n")
        
        arquivo_saida_resultado.write("Alfabetos:\n")
        for i in range(0, int(self.numero_de_alfabetos)):
            arquivo_saida_resultado.write(self.alfabetos[i]),
        arquivo_saida_resultado.write("\n")
        arquivo_saida_resultado.write("\n")

        arquivo_saida_resultado.write("Estados:\n")
        for i in range(0, int(self.numero_de_estados)):
            arquivo_saida_resultado.write("q"+str(i)+" "),
        arquivo_saida_resultado.write("\n")
        arquivo_saida_resultado.write("\n")
        
        arquivo_saida_resultado.write("Transicoes:\n")
        for i in range(0,int(self.numero_de_estados)):
            for j in range(0, int(self.numero_de_alfabetos)):
                arquivo_saida_resultado.write("(q"+str(i)+","+str(j)+")--> q" + str(i) + "\n")
        arquivo_saida_resultado.write("\n")

        arquivo_saida_resultado.write("\nEstado inicial: q0")
        arquivo_saida_resultado.write("\nEstado final: q"+str(self.estado_final))
        arquivo_saida_resultado.write("\nQxE->Q\n\n")

        arquivo_saida_resultado.write("\n")
        arquivo_saida_resultado.write("===========================================\n")
        arquivo_saida_resultado.write("               AFN - FIM!                  \n")
        arquivo_saida_resultado.write("===========================================\n")
        

if __name__ == "__main__":
    afnObj=AFN()
    i = True
    while (i):
        print("############  AFN - INÍCIO!  ############")
        afnObj.setAfn()
        afnObj.mostrarSet()
        i = False
    print("############  AFN - FIM!  ############")
       


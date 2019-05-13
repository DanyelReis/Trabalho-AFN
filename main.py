

class AFN():
    def __init__(self):
        self.estados = ''
        self.numero_de_estados = 0
        self.numero_de_alfabetos = 0
        self.numero_de_estados_finais = 0
        self.estado_inicial = 0
        self.estado_final = 0
        self.alfabetos = ['0', '1']
        self.afn = [[0 for x in range(int(self.numero_de_alfabetos))] for y in range(int(self.numero_de_estados))]
        self.afn = [['1', '0'], ['1', '2'], ['2', '2']]
        self.transition = ''
        self.entrada = ''

    def setAfn(self):
        
        input = open('AFN/arquivos/input.txt', 'r')
        self.estados = (input.readline().split('#')[0]).split()
        self.numero_de_estados = len(self.estados)
        self.alfabetos = (input.readline().split('#')[0]).split()
        self.numero_de_alfabetos = len(self.alfabetos)
        self.estado_inicial = (input.readline().split('#')[0]).split()
        self.estados_finais = (input.readline().split('#')[0]).split()
        self.numero_de_estados_finais = len(self.estados_finais)
        self.afn = [[0 for x in range(int(self.numero_de_alfabetos))] for y in range(int(self.numero_de_estados))]

        

        for i in range(0,int(self.numero_de_estados)):
            for j in range(0, int(self.numero_de_alfabetos)):
                self.transition = (input.readline().split('#')[0]).split()
                if self.transition == '*' : self.transition = ''             
                self.afn[i][j] = self.transition       

    def setarParametros(self, ns, na, nf, fs, ff, a, d):
        self.numero_de_estados = ns
        self.numero_de_alfabetos = na
        self.numero_de_estados_finais = nf
        self.estado_inicial = fs
        self.estado_final = ff
        self.alfabetos = a
        self.afn = d

    def mostrarSet(self):
        output = open('AFN/arquivos/output.txt','w')
        output.write("\n")
        output.write("===========================================\n")
        output.write("               AFN - INICIO                \n")
        output.write("===========================================\n")
        
        output.write("\n")
        
        output.write("Alfabetos:\n")
        for i in range(0, int(self.numero_de_alfabetos)):
            output.write(self.alfabetos[i]),
        output.write("\n")
        output.write("\n")

        output.write("Estados:\n")
        for i in range(0, int(self.numero_de_estados)):
            output.write("q"+str(i)+" "),
        output.write("\n")
        output.write("\n")
        
        output.write("Transicoes:\n")
        for i in range(0,int(self.numero_de_estados)):
            for j in range(0, int(self.numero_de_alfabetos)):
                output.write("(q"+str(i)+","+str(j)+")--> q" + str(i) + "\n")
        output.write("\n")

        output.write("\nEstado inicial: " + str(self.estado_inicial))
        output.write("\nEstado final: q"+str(self.estado_final))
        output.write("\nQxE->Q\n\n")

        output.write("\n")
        output.write("===========================================\n")
        output.write("               AFN - FIM!                  \n")
        output.write("===========================================\n")
        

if __name__ == "__main__":
    afnObj=AFN()
    i = True
    while (i):
        print("############  AFN - INÍCIO!  ############")
        afnObj.setAfn()
        afnObj.mostrarSet()
        i = False
    print("############  AFN - FIM!  ############")
       


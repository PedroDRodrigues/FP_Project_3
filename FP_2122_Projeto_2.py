#Pedro Dias Rodrigues 99300

"""
TAD Posicao

Representacao: R[x,y] = {'x': x, 'y': y}
cria_posicao: int X int -> posicao
Recebe os valores correspondentes as coordenadas e devolve a posicao
num dicionario.
"""

def cria_posicao(x, y):
    if type(x) != int or type(y) != int or x < 0 or y < 0:
        raise ValueError('cria_posicao: argumentos invalidos')
    return {'x': x, 'y' : y}

"""
cria_copia_posicao: posicao -> posicao
Recebe uma posicao e devolve uma copia nova da posicao.
"""

def cria_copia_posicao(p):
    return {'x': p['x'], 'y': p['y']}

"""
obter_pos_x: posicao -> int
Devolve a componente x da posicao p.
"""

def obter_pos_x(p):
    return p['x']

"""
obter_pos_y: posicao -> int
Devolve a componente y da posicao p.
"""

def obter_pos_y(p):
    return p['y']  

"""
eh_posicao: universal -> booleano
Devolve True caso o seu argumento seja um TAD posicao e False caso contrario.
"""

def eh_posicao(p):
    if type(p) == dict and len(p) == 2:
        if 'x' in p and 'y' in p:
            if type(p['x']) == int and type(p['y']) == int:
                if p['x'] >= 0 and p['y'] >= 0:
                    return True              
    return False

"""
posicoes_iguais: posicao X posicao -> booleano
Devolve True apenas se p1 e p2 sao posicoes e sao iguais.
"""

def posicoes_iguais(p1, p2):
    if eh_posicao(p1) and eh_posicao(p2):
        if obter_pos_x(p1) == obter_pos_x(p2):
            if obter_pos_y(p1) == obter_pos_y(p2):
                return True
    return False

"""
posicao_para_str: posicao -> str
Devolve a cadeia de caracteres '(x, y)' que representa as coordenadas da
posicao dada.
"""

def posicao_para_str(p):
    return str((obter_pos_x(p), obter_pos_y(p)))

"""
obter_posicoes_adjacentes: posicao -> tuplo
Devolve um tuplo com as posicoes adjacentes a posicao p comecando com a posicao
acima de p e seguindo no sentido harario.
"""

def obter_posicoes_adjacentes(p):
    adjacentes = []
    x = obter_pos_x(p)
    y = obter_pos_y(p)

    if x == 0:
        if y == 0: #direita e abaixo
            adjacentes += [(cria_posicao(x + 1, y))]
            adjacentes += [(cria_posicao(x, y + 1))]
        if y == int (p['y']) - 1: #acima e direita
            adjacentes += [(cria_posicao(x, y - 1))]
            adjacentes += [(cria_posicao(x + 1, y))]            
        if y != 0 and y != int (p['y']) - 1: #acima, direita e abaixo
            adjacentes += [(cria_posicao(x, y - 1))]
            adjacentes += [(cria_posicao(x + 1, y))]
            adjacentes += [(cria_posicao(x, y + 1))]            
    if x == int (p['x']) - 1:
        if y == 0: #abaixo e esquerda
            adjacentes += [(cria_posicao(x, y + 1))]
            adjacentes += [(cria_posicao(x - 1, y))]
        if y == int (p['y']) - 1: #acima e esquerda
            adjacentes += [(cria_posicao(x, y - 1))]
            adjacentes += [(cria_posicao(x - 1, y))]
        if y != 0 and y != int (p['y']) - 1: #acima, abaixo e esquerda
            adjacentes += [(cria_posicao(x, y - 1))]
            adjacentes += [(cria_posicao(x, y + 1))]
            adjacentes += [(cria_posicao(x - 1, y))]
    if y == 0:
        if x!= 0 and x != int (p['x']) - 1: #direita, baixo e esquerda
            adjacentes += [(cria_posicao(x + 1, y))]
            adjacentes += [(cria_posicao(x, y + 1))]
            adjacentes += [(cria_posicao(x - 1, y))]
    if y == int (p['y']) - 1:
        if x!= 0 and x != int (p['x']) - 1: #acima, direita e esquerda
            adjacentes += [(cria_posicao(x, y - 1))]
            adjacentes += [(cria_posicao(x + 1, y))]
            adjacentes += [(cria_posicao(x - 1, y))]
    if x != 0 and y != 0 and x != int (p['x']) -1 and y != int (p['y']) - 1: 
        #acima, direita, baixo e esquerda
        adjacentes += [(cria_posicao(x, y - 1))]
        adjacentes += [(cria_posicao(x + 1, y))]
        adjacentes += [(cria_posicao(x, y + 1))]
        adjacentes += [(cria_posicao(x - 1, y))]  
    return tuple(adjacentes)

"""
ordenar_posicoes: tuplo -> tuplo
Recebe um tuplo e devolve um tuplo ordenado de acordo com a ordem de leitura
do prado
"""

def ordenar_posicoes(t):
    listT = list(t)
    aux = {}
    for i in range(len(listT) - 1):
        for i in range(len(listT) - 1): #para y com valores diferentes
            if listT[i]['y'] > listT[i+1]['y']:
                aux = listT[i] 
                listT[i] = listT[i+1]
                listT[i+1] = aux
            if listT[i]['y'] == listT[i+1]['y']: #para y iguais mas x diferentes
                if listT[i]['x'] > listT[i+1]['x']:
                    aux = listT[i] 
                    listT[i] = listT[i+1]
                    listT[i+1] = aux    
    
    return tuple(listT)

"""
TAD Animal

Representacao: R[s, r, a] = {'s': s, 'r': r, 'a': a}
cria_animal: str X int X int -> animal
Recebe uma cadeia de caracteres s nao vazia com a especie do animal 
e dois valores inteiros correspondentes a frequencia de reproducao r > 0
e a frequencia de alimentacao a > o e devolve o animal.
"""

def cria_animal(s, r, a):
    if type(s) != str or len(s) < 1 or type(r) != int or type(a) != int or \
       r <= 0 or a < 0:
        raise ValueError('cria_animal: argumentos invalidos')
    return {'s': s, 'r': r, 'a': a, 'i': 0, 'f': 0}

"""
cria_copia_animal: animal -> animal
Recebe um animal a e devolve a copia do animal.
"""

def cria_copia_animal(a):
    return {'s': a['s'], 'r': a['r'], 'a': a['a'], 'i': a['i'], 'f': a['f']}

"""
obter_especie: animal -> str
Devolve a cadeia de caracteres correspondentes a especie do animal
"""

def obter_especie(a):
    return a['s']


"""
obter_freq_reproducao: animal -> int
Devolve a frequencia de reproducao do animal a.
"""

def obter_freq_reproducao(a):
    return a['r']


"""
obter_freq_alimentacao: animal -> int
Devolve a frequencia de alimentacao do animal a.
"""

def obter_freq_alimentacao(a):
    return a['a']

"""
obter_freq_reproducao: animal -> int
Devolve a idade do animal a.
"""

def obter_idade(a):
    return a['i']

"""
obter_fome: animal -> int
Devolve a fome do animal a.
"""

def obter_fome(a):
    return a['f']

"""
aumenta_idade: animal -> animal
Modifica destrutivamente o animal a incrementando o valor
da sua idade em uma unidade e devolve o proprio animal.
"""

def aumenta_idade(a):
    a['i'] += 1
    return a

"""
reset_idade: animal -> animal
Modifica destrutivamente o animal a definindo o valor da sua
idade igual a 0 e devolve o proprio animal.
"""

def reset_idade(a):
    a['i'] = 0
    return a
    
"""
aumenta_fome: animal -> animal
Modifica destrutivamente o animal predador a incrementando
o valor da sua fome em uma unidade, e devolve o proprio animal. Esta
operacao nao modifica os animais presa.
"""

def aumenta_fome(a):
    if not eh_presa(a):
        a['f'] += 1
    return a
            
"""
reset_fome: animal -> animal
Modifica destrutivamente o animal a definindo o valor da sua
fome igual a 0 e devolve o proprio animal.
"""

def reset_fome(a):
    if not eh_presa(a):
        a['f'] = 0
    return a

"""
eh_animal: universal -> booleano
Devolve True caso o seu argumento seja um TAD animal ou False no caso contrario.
"""

def eh_animal(arg):
    if type(arg) == dict and len(arg) == 5:
        if 's' in arg and type(arg['s']) == str and len(arg['s']) > 0:
            if 'r' in arg and type(arg['r']) == int and arg['r'] > 0:
                if 'a' in arg and type(arg['a']) == int and arg['a'] >= 0:
                    if 'i' in arg and type(arg['i']) == int and arg['i'] >= 0:
                        if 'f' in arg and type(arg['f']) == int and arg['f'] >= 0:
                            return True
    return False

"""
eh_predador: universal -> booleano
Devolve True caso o seu argumento seja um TAD animal do tipo predador
ou False no caso contrario.
"""

def eh_predador(arg):
    if eh_animal(arg) and arg['a'] > 0:
        return True
    return False

"""
eh_presa: universal -> booleano
Devolve True caso o seu argumento seja um TAD animal do tipo presa
ou False no caso contrario.
"""

def eh_presa(arg):
    if eh_animal(arg) and arg['a'] == 0:
        return True
    return False

"""
animais_iguais: animal X animal -> booleano
Devolve True apenas se a1 e a2 sao animais e sao iguais.
"""

def animais_iguais(a1, a2):
    if eh_animal(a1) == eh_animal(a2):
        if eh_presa(a1) == eh_presa(a2):
            if eh_predador(a1) == eh_predador(a2):
                if obter_especie(a1) == obter_especie(a2):
                    if obter_freq_reproducao(a1) == obter_freq_reproducao(a2):
                        if obter_freq_alimentacao(a1) == obter_freq_alimentacao(a2):
                            if obter_idade(a1) == obter_idade(a2):
                                if obter_fome(a1) == obter_fome(a2):
                                    return True
    return False

"""
animal_para_char: animal -> str
Devolve a cadeia de caracteres dum unico elemento correspondente
ao primeiro caracter da especie do animal passada por argumento,
em maiuscula para animais predadores e em minuscula para animais presa.
"""

def animal_para_char(a):
    if eh_presa(a): #se for presa eh minuscula
        char = a['s'][0]
        char = char.lower()
        return char
    if eh_predador(a): #se for predador eh maiuscula
        char = a['s'][0]
        char = char.upper()        
        return char

"""
animal_para_str : animal -> str
Devolve a cadeia de caracteres que representa o animal.
"""

def animal_para_str(a):
    if eh_predador(a):
        return (a['s'] + ' [' + str(a['i']) + '/' + str(a['r']) + ';' \
                + str(a['f']) + '/' + str(a['a']) + ']')
    if eh_presa(a):
        return (a['s'] + ' [' + str(a['i']) + '/' + str(a['r']) + ']')

"""
eh_animal_fertil : animal -> booleano
Devolve True caso o animal a tenha atingido a idade de reproducao 
e False caso contrario.
"""

def eh_animal_fertil(a):
    if a['i'] >= a['r']:
        return True
    return False

"""
eh_animal_faminto : animal -> booleano
Devolve True caso o animal a tenha atingido um valor de fome igual ou superior 
a sua frequencia de alimentacao e False caso contrario.
As presas devolvem sempre False.
"""

def eh_animal_faminto(a):
    if a['f'] >= a['a'] and not eh_presa(a):
        return True
    return False

"""
reproduz_animal: animal -> animal
Recebe um animal a devolvendo um novo animal da mesma especie com idade 
e fome igual a 0, e modificando destrutivamente o animal passado
como argumento a alterando a sua idade para 0.
"""

def reproduz_animal(a):
    a['i'] = 0
    return cria_animal(a['s'], a['r'], a['a'])

"""
TAD Prado

Representacao: R[d, r, a, p] = {'d': d, 'r': r, 'a': a, 'p': p}
cria_prado: posicao X tuplo X tuplo X tuplo -> prado
Recebe uma posicao d correspondente a posicao que ocupa a montanha 
do canto inferior direito do prado, um tuplo r de 0 ou mais posicoes 
correspondentes aos rochedos que nao sao as montanhas dos limites exteriores 
do prado, um tuplo a de 1 ou mais animais, e um tuplo p da mesma dimensao 
do tuplo a com as posicoes correspondentes ocupadas pelos animais.
Devolve o prado que representa internamente o mapa e os animais presentes.
"""

def cria_prado(d, r, a, p):
    if type(d) != dict or not eh_posicao(d):
        raise ValueError('cria_prado: argumentos invalidos')
    if type(r) != tuple or len(r) < 0: 
        raise ValueError('cria_prado: argumentos invalidos')
    for i in range(len(r)):
        if not eh_posicao(r[i]):
            raise ValueError('cria_prado: argumentos invalidos')
        if r[i]['x'] >= d['x'] or r[i]['y'] >= d['y']:
            raise ValueError('cria_prado: argumentos invalidos')
        if r[i]['x'] == 0 or r[i]['y'] == 0:
            raise ValueError('cria_prado: argumentos invalidos')    
    if type(a) != tuple or len(a) < 1:
        raise ValueError('cria_prado: argumentos invalidos')
    if type(p) != tuple or len(p) != len(a):
        raise ValueError('cria_prado: argumentos invalidos')
    for i in range(len(p)):
        if not eh_posicao(p[i]):
            raise ValueError('cria_prado: argumentos invalidos')
        if p[i]['x'] >= d['x'] or p[i]['y'] >= d['y']:
            raise ValueError('cria_prado: argumentos invalidos')
        if p[i]['x'] == 0 or p[i]['y'] == 0:
            raise ValueError('cria_prado: argumentos invalidos')
    return {'d': d, 'r': r, 'a': a, 'p': p}

"""
cria_copia_prado: prado -> prado
Recebe um prado e devolve uma nova copia do prado.
"""

def cria_copia_prado(m):
    return {'d': m['d'], 'r': m['r'], 'a': m['a'], 'p': m['p']}

"""
obter_tamanho_x: prado -> int
Devolve o valor inteiro que corresponde a dimensao Nx do prado.
"""

def obter_tamanho_x(m):
    return (m['d']['x'] + 1)

"""
obter_tamanho_y: prado -> int
Devolve o valor inteiro que corresponde a dimensao Ny do prado.
"""

def obter_tamanho_y(m):
    return (m['d']['y'] + 1)
    
"""
obter_numero_predadores: prado -> int
Devolve o numero de animais predadores no prado.
"""

def obter_numero_predadores(m):
    resultado = 0
    for i in range(len(m['a'])):
        if eh_predador(m['a'][i]):
            resultado += 1
    return resultado

"""
obter_numero_presas: prado -> int
Devolve o numero de animais presa no prado.
"""

def obter_numero_presas(m):
    resultado = 0
    for i in range(len(m['a'])):
        if eh_presa(m['a'][i]):
            resultado += 1
    return resultado    

"""
obter_posicao_animais: prado -> tuplo posicoes
Devolve um tuplo contendo as posicoes do prado ocupadas por animais, ordenadas 
em ordem de leitura do prado.
"""

def obter_posicao_animais(m):
    return ordenar_posicoes(m['p'])

"""
obter_animal: prado X posicao -> animal
Devolve o animal do prado que se encontra na posicao p.
"""

def obter_animal(m, p):
    for i in range(len(m['p'])):
        if p == m['p'][i]:
            return m['a'][i]  

"""
eliminar_animal: prado X posicao -> prado
Modifica destrutivamente o prado m eliminando o animal da posicao p 
deixando-a livre. Devolve o proprio prado.
"""

def eliminar_animal(m, p):
    modificarP = list(m['p'])
    modificarA = list(m['a'])
    for i in range(len(modificarP)):
        if p == modificarP[i]:
            del(modificarP[i])
            del(modificarA[i])
            break
    m['p'] = tuple(modificarP)
    m['a'] = tuple(modificarA)
    return m


"""
mover_animal: prado X posicao X posicao -> prado
Modifica destrutivamente o prado m movimentando o animal da posicao p1 
para a nova posicao p2, deixando livre a posicao onde se encontrava. 
Devolve o proprio prado.
"""

def mover_animal(m, p1, p2):
    animal = obter_animal(m, p1)
    inserir_animal(m, animal, p2)
    eliminar_animal(m, p1)
    return m

"""
inserir_animal: prado X animal X posicao -> prado
Modifica destrutivamente o prado m acrescentando na posicao p do prado o 
animal a passado como argumento. Devolve o proprio prado.
"""

def inserir_animal(m, a, p):
    comprimento = len(m['a'])
    modificarA = list(m['a']) 
    modificarP = list(m['p'])
    modificarA += [a]
    modificarP += [p]
    m['p'] = tuple(modificarP)
    m['a'] = tuple(modificarA)    
    return m

"""
eh_prado: universal -> booleano
Devolve True caso o seu argumento seja um TAD prado e False caso contrario.
"""

def eh_prado(arg):
    if type(arg) == dict and len(arg) == 4:
        if 'd' in arg and type(arg['d']) == dict and len(arg['d']) == 2 and eh_posicao(arg['d']):
            if 'r' in arg and type(arg['r']) == tuple and len(arg['r']) >= 0:             
                if 'a' in arg and type(arg['a']) == tuple and len(arg['a']) >= 1:
                    if 'p' in arg and type(arg['p']) == tuple and len(arg['p']) == len(arg['a']):
                            return True
                        
    return False

"""
eh_posicao_animal: prado X posicao -> booleano
Devolve True apenas no caso da posicao p do prado estar ocupada por um animal.
"""

def eh_posicao_animal(m, p):
    if p in m['p']: #percorrer posicoes dos animais
        return True
    return False

"""
eh_posicao_obstaculo: prado X posicao -> booleano
Devolve True apenas no caso da posicao p do prado correspoder a uma 
montanha ou rochedo.
"""

def eh_posicao_obstaculo(m, p):
    if p in m['r']: #percorrer os rochedos
        return True
    if p['x'] == 0:
        return True
    if p['y'] == 0:
        return True
    if p['x'] == obter_tamanho_x(m) - 1:
        return True
    if p['y'] == obter_tamanho_y(m) - 1:
        return True    
    return False        

"""
eh_posicao_livre: prado X posicao -> booleano
Devolve True apenas no caso da posicao p do prado corresponder a um 
espaco livre.
"""

def eh_posicao_livre(m, p):
    if eh_posicao_animal(m, p) or eh_posicao_obstaculo(m, p):
        return False
    return True

"""
prados_iguais: prado X prado -> booleano
Devolve True apenas se p1 e p2 forem prados e forem iguais.
"""

def prados_iguais(p1, p2):
    if eh_prado(p1) and eh_prado(p2):
        if p1['d'] == p2['d']:
            if p1['r'] == p2['r']:
                if p1['a'] == p2['a']:
                    if p1['p'] == p2['p']:
                        return True
    return False

"""
prado_para_str : prado -> str
Devolve uma cadeia de caracteres que representa o prado.
"""

def prado_para_str(m):
    resultado = []
    fim = ''
    for y in range(obter_tamanho_y(m)):
        for x in range(obter_tamanho_x(m)):
            resultado += [(cria_posicao(x, y))]
    
    for pos in range(len(resultado)):
        if resultado[pos]['x'] == 0 and resultado[pos]['y'] == 0:
            fim += ('+')
        elif resultado[pos]['x'] == 0 and resultado[pos]['y'] == obter_tamanho_y(m) - 1:
            fim += ('+')
        elif resultado[pos]['x'] == obter_tamanho_x(m) - 1 and resultado[pos]['y'] == 0:
            fim += ('+\n')
        elif resultado[pos]['x'] == obter_tamanho_x(m) - 1 and resultado[pos]['y'] == obter_tamanho_y(m) - 1:
            fim += ('+')
        elif resultado[pos]['x'] == 0:
            fim += ('|')
        elif resultado[pos]['x'] == obter_tamanho_x(m) - 1:
            fim += ('|\n')
        elif resultado[pos]['y'] == 0:
            fim += ('-')
        elif resultado[pos]['y'] == obter_tamanho_y(m) - 1:
            fim += ('-')          
        elif eh_posicao_animal(m, resultado[pos]):
            fim += str(animal_para_char(obter_animal(m, resultado[pos])))
        elif eh_posicao_obstaculo(m, resultado[pos]):
            fim += ('@')
        elif eh_posicao_livre(m, resultado[pos]):
            fim += ('.')        
    
    return fim

"""
obter_valor_numerico: prado X posicao -> int
Devolve o valor numerico da posicao p correspondente a ordem de 
leitura no prado m.
"""

def obter_valor_numerico(m, p):
    return obter_tamanho_x(m) * obter_pos_y(p) + obter_pos_x(p)

"""
obter_movimento: prado X posicao -> posicao
Devolve a posicao seguinte do animal na posicao p dentro do prado m de 
acordo com as regras de movimentos dos animais no prado.
"""

def obter_movimento(m, p):
    valor = obter_valor_numerico(m, p)
    opcoes = obter_posicoes_adjacentes(p)
    aux = []
    animal = obter_animal(m, p)
    if eh_predador(animal):
        for i in range(len(opcoes)): #percorrer opcoes todas das adjacentes
            if eh_presa(obter_animal(m, opcoes[i])): #se for presa adicionar
                aux += [opcoes[i]]
        
        if len(aux) > 0: #se houverem presas na lista devolve essa pos
            return aux[valor % len(aux)] 
        
        for i in range(len(opcoes)): #percorrer todas as ocpoes das adjacentes de novo
            if eh_posicao_livre(m, opcoes[i]):
                aux += [opcoes[i]]
        
        if len(aux) > 0: #se houverem opcoes devolver uma dessas
            return aux[valor % len(aux)]        
           
    if eh_presa(animal):
        i = 0
        while i <= len(opcoes) - 1: #percorrer todas as ocpoes das adjacentes
            if eh_posicao_livre(m, opcoes[i]):
                aux += [opcoes[i]]
            i += 1
            
        if len(aux) > 0: #se houverem opcoes devolver uma dessas
            return aux[valor % len(aux)]  
          
    return p

"""
geracao: prado -> prado
Funcao auxiliar que modifica o prado m fornecido como argumento de acordo com a 
evolucao correspondente a uma geracao completa, e devolve o proprio prado.
Isto é seguindo a ordem de leitura do prado cada animal (vivo) realiza o seu 
turno de acao de acordo com as regras descritas.
"""

def geracao(m):
    t = ordenar_posicoes(m['p'])
    aux = {}
    ignorar = ()
    
    for i in range(len(t)):
        if eh_posicao_animal(m, t[i]) and t[i] not in ignorar:
            animal = obter_animal(m, t[i])
            aux = obter_movimento(m, t[i])
            if eh_predador(animal):
                aumenta_idade(animal)
                aumenta_fome(animal)
            if eh_presa(animal):
                aumenta_idade(animal)  
                
            #caso a posicao para onde vai mover tenha uma presa naquela posicao
            if eh_predador(animal) and eh_presa(obter_animal(m, aux)):
                eliminar_animal(m, aux)
                reset_fome(animal)
                
            #verificar se existe alguma posicao para onde mover o animal
            if aux != t[i] : #adicionar a ignorar caso mova
                mover_animal(m, t[i], aux)
                ignorar += (aux,)
                if eh_animal_fertil(animal):
                    inserir_animal(m, reproduz_animal(animal), t[i])
                    reset_idade(animal)
                if eh_animal_faminto(animal):
                    eliminar_animal(m, aux)
    return m

"""
simula_ecossistema: str X int X booleano -> tuplo
Funcao principal que permite simular o ecossistema de um prado.
Recebe uma cadeia de caracteres f correspondente ao nome do ficheiro de 
configuracao de simulacao.
Recebe  um valor inteiro g correspondente ao numero de geracoes a simular.
Recebe um valor booleano v que ativa um dos dois modos disponiveis:
Modo verboso (True) - mostra-se pela saida standard o prado, o numero de animais
e o numero de geracao, apenas se o numero de animais predadores ou presas se
tiver alterado.
Modo quiet (False) - mostra-se pela saida standard o prado, o numero de animais
e o numero de geracao do inicio da simulacao e apos a ultima geracao.
"""   

def simula_ecossistema(f, g, v):
    contador = g
    geracaoN = 0
    
    predadoresN = 0
    presasN = 0
    predadoresNComparador = 1
    presasNComparador = 1  
    
    with open(f, 'r') as f:
        lines = f.readlines()     
        for i in range(len(lines)):
            lines[i] = lines[i].replace("’", "'")
        
        d = eval("cria_posicao" + str(eval(lines[0])))
        
        r = ()
        rochas = eval(lines[1])
        for rocha in rochas:
            r += (eval("cria_posicao" + str(rocha)),)
        
        a = ()
        p = ()
        animalPosition = ()
        for i in range(2, len(lines)):
            animalPosition += (eval(lines[i]),)
        
        for i in range(len(animalPosition)):
            a += (eval("cria_animal" + str(animalPosition[i][:-1])),)
            p += (eval("cria_posicao" + str(animalPosition[i][3])),)
    prado = cria_prado(d, r, a, p)

    f.close()      
    
    if v == True:
        while contador > 0:
            if predadoresN != predadoresNComparador or presasN != presasNComparador:
                print('Predadores: ' + str(obter_numero_predadores(prado)) + ' vs Presas: ' + str(obter_numero_presas(prado)) + ' (Gen. {})'.format(str(geracaoN)))
                print(prado_para_str(prado))
            geracaoN += 1
            contador -= 1            
            predadoresN = obter_numero_predadores(prado)
            presasN = obter_numero_presas(prado)
            geracao(prado)
            predadoresNComparador = obter_numero_predadores(prado)
            presasNComparador = obter_numero_presas(prado)
        
    if v == False:
        print('Predadores: ' + str(obter_numero_predadores(prado)) + ' vs Presas: ' + str(obter_numero_presas(prado)) + ' (Gen. {})'.format(geracaoN))
        print(prado_para_str(prado))
            
        while contador > 0:
            geracao(prado)
            geracaoN += 1
            contador -= 1
                
        print('Predadores: ' + str(obter_numero_predadores(prado)) + ' vs Presas: ' + str(obter_numero_presas(prado)) + ' (Gen. {})'.format(str(geracaoN)))
        print(prado_para_str(prado))
        
    return (obter_numero_predadores(prado), obter_numero_presas(prado))
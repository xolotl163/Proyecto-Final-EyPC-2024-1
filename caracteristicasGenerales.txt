
Proyecto EyPC, 2024-1

Prof. Alberto Navarrete Hernández

Alumnos:
    
    -> Chavez Madrid Ismael Angel
    -> Hernández Jiménez Efrén Antonio
    -> Padilla Cazares Jesus Alejandro 

Descripción general:

    -> Se requiere crear un programa en python 3.10 capaz de leer e interpretar una pseudo
       estrutura o arquitectura de ya sea 20, 22 o 24 bits. Esto implica crear un programa
       capaz de tomar la estructura asignada para el pesudolenguaje de programación creado,
       parecido a NASM x86, y convertir las instrucciones o directivas dadas a sus equivalentes
       binarios, o mejor dicho, al codigo binario equivalente. 


Instrucciones:

    ~ Mas comunes o generales
        
        mov: [holder1/destino], [holder2] -> mueve holder 2 a holder 1
        cmp: [holder1/destino], [holder2] -> comparacion directa entre los operandos
        equ: [holder1/destino], [holder2] -> asignacion entre los operandos
        shw: [holder1/destino], [holder2] -> muestra mensaje en pantalla
        inc: [holder1/destino], [holder2] -> incrementa el operando en una unidad  
        dec: [holder1/destino], [holder2] -> decrementa el operando en una unidad
    
    ~ Aritmeticas o matematicas

        add: [holder1/destino], [holder2] -> suma los operandos
        sub: [holder1/destino], [holder2] -> resta los operandos
        mul: [holder1/destino], [holder2] -> multiplica los operandos
        sqr: [holder1/destino], [holder2] -> raiz enesima de los operandos
        pwr: [holder1/destino], [holder2] -> potencia enesima de los operandos
        divC: [holder1/destino], [holder2] -> divide los operandos y devuelve el cociente
        divR: [holder1/destino], [holder2] -> divide los operandos y devuelve el residuo
    

    ~ logicas o a nivel de bit:
    
        and: [holder1/destino], [holder2]
        not: [holder1/destino], [holder2] 
        mbl: [holder1/destino], [holder2] -> se mueve una cantidad n de bits al operando 1 a la izquierda
        mbr: [holder1/destino], [holder2] -> se mueve una cantidad n de bits al operando 1 a la derecha
        cpl: [holder1/destino]            -> complemento a bits del operando

Registros: 

    -> Todavia sin especificar 

Estructuras de datos requeridas para el backend:

    -> Stack
    -> diccionario
    -> lista doblemente ligada (tentativo pero no indispensable)
    -> arbol binario    (tentativo pero no indispensable)
     
    -> función para convertir numeros decimales, hexadecimales, octales y caracteres a binarios
    -> función para convertir binario a datos de tipo caracter, octal, hexadecimal y decimal 

Requerimientos del Front End:

    -> Minimamente se van a requerir [numero todavia no especificado] ventanas con los siguientes propositos:

        Mostrar el pseudocodigo nasm
        Mostrar el equivalente binario del pseudocodigo nasm
        







 
        

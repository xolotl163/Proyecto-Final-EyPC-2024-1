
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
        
        1.- mov [holder1/destino], [holder2] -> mueve holder 2 a holder 1
        2.- cmp [holder1/destino], [holder2] -> comparacion directa entre los operandos
        3.- equ [holder1/destino], [holder2] -> asignacion entre los operandos
        4.- shw [holder1/destino], [holder2] -> muestra mensaje en pantalla
        5.- inc [holder1/destino], [holder2] -> incrementa el operando en una unidad  
        6.- dec [holder1/destino], [holder2] -> decrementa el operando en una unidad
    
    ~ Aritmeticas o matematicas

        7.-  add [holder1/destino], [holder2] -> suma los operandos
        8.-  sub [holder1/destino], [holder2] -> resta los operandos
        9.-  mul [holder1/destino], [holder2] -> multiplica los operandos
        10.- sqr [holder1/destino], [holder2] -> raiz enesima de los operandos
        11.- pwr [holder1/destino], [holder2] -> potencia enesima de los operandos
        12.- divC [holder1/destino], [holder2] -> divide los operandos y devuelve el cociente
        13.- divR [holder1/destino], [holder2] -> divide los operandos y devuelve el residuo
    

    ~ logicas o a nivel de bit:
    
        14.- and [holder1/destino], [holder2]
        15.- not [holder1/destino], [holder2] 
        16.- mbl [holder1/destino], [holder2] -> se mueve una cantidad n de bits al operando 1 a la izquierda
        17.- mbr [holder1/destino], [holder2] -> se mueve una cantidad n de bits al operando 1 a la derecha
        18.- cpl [holder1/destino]            -> complemento a bits del operando

    ~ Uso de Stacks:

        19.- call [function] -> se llama a la función indicada y se hace push al stack de funciones
        20.- puAS [holder]   -> se hace push al stack de argumentos
        21.- popSF           -> se hace pop al stack de funciones
        22.- popAs           -> se hace pop al stack de argumentos


Registros: 

    ~ Proposito general:

        Pueden Alamacenar hasta un maximo de 16 bits:

            Ah -> Se divide en Al y Ah
            Bh -> Se divide en Bl y Bh
            Ch -> Se divide en Cl y Ch
            Eh -> Se divide en El y Eh

    ~ Uso de Stacks:

        Pueden almacenar hasta un maximo de 20 bits, no tiene secciones:

            stAR -> stack Argument Register
            stFR -> sstack Function Register

    ~ Banderas (flags): 

        CF -> Carry Flag , bandera de acarreo
        OF -> Overflow Flag, bandera de desborde
        ZF -> Zero Flag , bandera de cero
        EF -> Equal Flag, bandera de igualdad
        GF -> Greater Flag, bandera "mayor que"
        SMF -> Smaller Flag, bandera "menor que"

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
        

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

    ~ Arimeticas
        
        01.- add [], []  -> suma operandos
        02.- sub [], []  -> resta operandos
        03.- mul [], []  -> producto operandos
        04.- cmp [], []  -> compara operandos
        05.- divC [], [] -> divide operandos, retorna cociente
        06.- divR [], [] -> divide operandos, retorna residuo
    
    ~ logicas
    
        07.- and [], [] 
        08.- or  [], []
        09.- not []
        10.- xor [], []
        11.- shl [a], [b] -> mueve b cantidad de bits a la izquierda de a 
        12.- shr [a], [b] -> mueve b cantidad de bits a la derecha de a
        13.- rol [], []   -> rotación cantidad b de bits a la izquierda de a
        14.- ror [], []   -> rotación cantidad b de bits a la derecha de a
        15.- test [], []  -> se hace un and entre los operandos, pero solo afecta las banderas, no se almacena resultado

    ~ administración de memoria:
    
        16.- mov [a], [b] -> mueve los datos de 'b' a 'a', 'a' es un registro de proposito general
        17.- wrt []       -> se muestran datos en pantalla o en consola (bash/shell)
        18.- read []      -> se leen datos del teclado y se almacenan en el operando
        
    ~ Uso de Stacks y funciones:

        19.- call [function] -> se llama a la función indicada y se hace push al stack de funciones
        20.- puAS [holder]   -> se hace push al stack de argumentos
        21.- popSF           -> se hace pop al stack de funciones
        22.- popAS           -> se hace pop al stack de argumentos
        23.- jmp []          -> se salta el programa a la dirección operando
        24.- je  []          -> se salta el programa a la dirección operando si bandera equal es 1
        25.- jne []          -> se salta el programa a la dirección operando si bendera equal es 0
        26.- ja  []          -> se salta el programa a la dirección operando si "está por arriba"
        27.- jae []          -> se salta el programa a la dirección operando si "esta por arriba o es igual"
        28.- jb  []          -> se salta el programa a la dirección operando si "esta por abajo"
        29.- jbe []          -> se salta el programa a la dirección operando si "esta por abajo o es igual"

Registros: 

    ~ Proposito general:

        r1      r4
        r2      r5
        r3      r6

    ~ Uso de Stacks:

        rSF -> registro stack de funciones
        rSA -> registro stack de argumentos

    ~ Lectura Escritura:

        rR -> registro de lectura
        rW -> regsitro de escritura

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
        
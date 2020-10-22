valor = 2       #(DEFINCIÓN VARIABLE PARA EJEMPLO)

#LAS SUBRUTINAS NOS PERMITEN AGRUPAR PARTES DE CÓDIGO. BIEN PORQUE SE UTILICE VARIAS VECES EN DIFERENTES PARTES
#O PORQUE NOS INTERESE TENER EL CÓDIGO SEPARADO PARA FACILITAR LA REVISIÓN.

#LAS VARIABLES DE LAS SUBRUTINAS SON PRIVADAS DE CADA SUBRUTINA. ESTO ES, NO PUEDEN UTILIZARSE FUERA DE LA MISMA
#SI QUEREMOS UTILIZAR UNA VARIABLE DE UNA SUBRUTINA FUERA, DEBEREMOS DEVOLVERLA CON LA PALABRA 'RETURN (VALOR)'
#MISMO SISTEMA SI QUEREMOS UTILIZAR UNA VARIABLE DE FUERA DE LA SUBRUTINA DENTRO DE ELLA.
#PARA HACERLO, PASAREMOS EL VALOR COMO PARÁMETRO.

#PARA CREAR UNA SUBRUTINA, UTILIZAMOS LA PALABRA 'DEF' SEGUIDA POR EL NOMBRE DE LA SUBRUTINA
#Y POR LOS PARÁMETROS (SI LOS HAY) ENTRE PARÉNTESIS. FINALIZAMOS CON :
#ASÍ PUES, QUEDARÍA ALGO ASÍ:

def Subrutina (valor):      #PASAMOS EL VALOR DE LA VARIABLE VALOR COMO PARÁMETRO
    #INDENTADO, ESCRIBIREMOS EL CÓDIGO QUE QUEREMOS EJECUTAR.
    print ("El doble del valor es =",valor*2)
    boolean = (valor*2>5)
    #AL IGUAL QUE EN JAVA, PODEMOS HACER QUE DEVUELVA UN VALOR.
    return boolean   #DEVOLVEMOS BOOLEAN

print (Subrutina(valor))        #PARA LLAMAR A LA SUBRUTINA, ESCRIBIMOS SU NOMBRE
            #ENTRE PARÉNTESIS INTRODUCIMOS EL PARÁMETRO
            #EL NOMBRE DEL PARÁMETRO NO TIENE POR QUÉ COINCIDIR DENTRO Y FUERA DE LA SUBRUTINA

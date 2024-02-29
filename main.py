# Parcial l
from list import List

a = List()
b = List()

a.insert_at_start(-10)
a.insert_at_start(18)
a.insert_at_start(3)

b.insert_at_start(-25)
b.insert_at_start(0)
b.insert_at_start(4)
b.insert_at_start(-17)

while True:
    print('POLINOMIOS')
    print('Polinomio A:')
    a.print_list()
    print('Polinomio B:')
    b.print_list()
    print('\nMenu')
    print('1. Ingresar componentes a un polinomio\n2. Adicion y Sustraccion\n3. Evaluar Polinomios')
    opcion = int(input('Elija una opcion: '))
    if opcion == 1:
        print('Ingresar componentes')
        print('1. a\n2. b')
        polinomio = int(input('Ingrese numero de opcion segun el polinomio que desea: '))
        if polinomio == 1:
            pos = int(input('Ingrese el exponente: '))
            num = int(input('Ingrese la base: '))
            if pos > a.pos_g():
                a.insert_at_start(num)
            elif pos < 0:
                print('No es posible ingresar el exponente')
            else:
                a.insert_at_index(pos - 1, num)

        elif polinomio == 2:
            pos = int(input('Ingrese el exponente: '))
            num = int(input('Ingrese la base: '))
            if pos > b.size():
                b.insert_at_start(num)
            elif pos < 0:
                print('No es posible ingresar el exponente')
            else:
                b.insert_at_index(pos - 1, num)

        else:
            print('Ingrese una opcion valida')

    elif opcion == 2:
        c = List()
        print('Adicion y Sustraccion')
        current_a = a.tail
        current_b = b.tail
        cont = 0
        if a.pos_g() > b.pos_g():
            cont += a.pos_g()
        elif a.pos_g() < b.pos_g():
            cont += b.pos_g()
        else:
            cont += a.pos_g()

        while cont >= 0:
            if current_a.prev != a.tail:
                if current_b.prev != b.tail:
                    new = current_a.data + current_b.data
                    cont -= 1
                    current_a = current_a.prev
                    current_b = current_b.prev
                    c.insert_at_start(new)
                if current_b.prev == b.tail:
                    new = current_a
                    cont -= 1
                    current_a = current_a.prev
                    c.insert_at_start(new)
            if current_b is not None:
                new = current_b
                cont -= 1
                current_b = current_b.prev
                c.insert_at_start(new)
        c.print_list()

    elif opcion == 3:
        print('Ingresar componentes')
        print('1. a\n2. b')
        polinomio = int(input('Ingrese numero de opcion segun el polinomio que desea evaluar: '))
        if polinomio == 1:
            resultado = 0
            variable = int(input('Ingrese variable x: '))
            current_a = a.head
            cont = a.pos_g()
            while cont >= 0:
                mult = current_a.data * pow(variable, cont)
                resultado += mult
                cont -= 1
            print(f'El valor del polinomio es: ', resultado)

        elif polinomio == 2:
            resultado = 0
            variable = int(input('Ingrese variable x: '))
            current_b = b.head
            cont = b.pos_g()
            while cont >= 0:
                mult = current_b.data * pow(variable, cont)
                resultado += mult
                cont -= 1
            print(f'El valor del polinomio es: ', resultado)
        else:
            print('Ingrese opcion valida')

    else:
        print('Salida')
        break

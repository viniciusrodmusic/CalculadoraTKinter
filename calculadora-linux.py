from tkinter import *


"""
DOC STRING

    A Janela Principal tem:
     - 4 colunas
     - 6 linhas
    (Row 0 --> Linha 1  //  Column 0 --> Coluna 1)

    Muitas informações estão escritas em inglês porque simplesmente quis praticar o idioma

    A maior parte dos posicionamentos com TKinter foram feitas com o recurso Grid, 
    dividindo a interface em uma espécie de tabela de linhas e colunas

    Após calcular, por exemplo "1 + 1", aparecerá o resultado (2) e 
    logo após isso não será possível adicionar um ponto ".", 
    pois a continuação dos cálculos após o botão "=" ser pressionado será interpretado como uma expressão entre parênteses ()
    ou seja, se você calculou 1+1 e o resultado saiu "2" na parte inferior do display, após apertar um ponto "." ele tentará 
    calcular algo como "(1+1)." [...]

     Sobre as variáveis:
        "accumulating" armazena o resultado acumulado
        "expressions" armazena o resultado para mostrar na parte superior da calculadora
        "results" armazena o resultado e mostra abaixo da "expressions"


    O botão C de fundo vermelho (Clear) reseta a calculadora.

        Os cálculos são executados de acordo com a sintaxe do Python, ou seja, se pode fazer:
        - Divisão inteira com "//"
        - Exponenciação com "**"

        Etc.

    ----------------------------------------------------------

    Na seção '# Main Window' foram feitos alguns cálculos para centralizar a calculadora na tela ao ser inicializada

        root.geometry("%dx%d+%d+%d" % (300, 400, root_position_x, root_position_y))

    ----------------------------------------------------------

    No final do arquivo py há a antiga maneira usada para capturar os valores dos botões a serem calculados.
    Ao decorrer do projeto fui aprendendo muitas coisas e consegui fazer o mesmo de maneira mais enxuta.

    ----------------------------------------------------------

    Percebi que, ao executar no Windows 11, a aplicação ficou um pouco problemática, principalmente no layout e não entendi
    o porquê. Então esse arquivo em específico está feito para sistemas Linux. Provavelmente tentarei criar outro arquivo
    adaptado para Windows.

    Se você encontrar mais algum problema sério na calculadora peço que entre em contato comigo pelo LinkedIn, gratidão.

    Autor: Vinícius Rodrigues.

"""




    # Functions, variables, etc...

minus = plus = equals = divide = times = accumulating = ""


    # Values of Buttons
    # Get a value of the pressed button and put into the variable: accumulating

def char_collect(num):
    global accumulating, expressions, results

    accumulating += num

    if expressions.cget('text') != "":
        expressions.configure(text=f"{accumulating}")
    else:
        results.configure(text=f"{accumulating}")



    # Clear button function
def clear_function():
    global results, expressions, accumulating
    accumulating = ""
    print(accumulating)
    results.configure(text="")
    expressions.configure(text="")






# = 
def equals_value():
    global accumulating, results, expressions
    accumulating = f"({accumulating})"
    print(accumulating)
    try:
        print(eval(accumulating))
        results.configure(text=f"{eval(accumulating)}")
        expressions.configure(text=f"{accumulating}")
    except:
        print("Houve um erro")
        accumulating = ""
        results.configure(text="Houve um erro.")
        expressions.configure(text=f"{accumulating}")
  








    # Main Window

root = Tk()

screen_width = root.winfo_screenwidth() # Get the screen width
screen_height = root.winfo_screenheight() # Get the screen height

root_position_x = (screen_width / 2) - (300 / 2)
root_position_y = (screen_height / 2) -  (400 / 2)
root.geometry("%dx%d+%d+%d" % (300, 400, root_position_x, root_position_y)) # Defines the 'root' size and initial position

root.configure(bg="#101010")
root.resizable(False, False) # Isn't resizable (X and Y)
root.title("Calculadora do Vinícius Rod")








    # Grid Initial Configurations

root.columnconfigure((0, 1, 2, 3), weight=1) # 4 Columns
root.rowconfigure((0, 1, 2, 3, 4, 5), weight=1) # 6 Rows
root.columnconfigure((0, 1, 2), uniform="a") # Uniform makes them proportional cells
root.rowconfigure((2, 3, 4, 5), uniform="a")





    # Result Text

results = Label(root, text="", bg="#101010", fg="lightblue", font=("Arial", 20), justify=RIGHT)
results.grid(row=1, column=0, columnspan=4, sticky="nsew", pady=(0, 25))
results.grid_propagate(False)

    # Expressions Text (First Row) // Where numbers will be placed when equals button is clicked

expressions = Label(root, text="", bg="#101010", fg="#465358", font=("Arial", 15), justify=RIGHT)
expressions.grid(row=0, column=0, columnspan=4, sticky="ewsn", pady=(50, 10))
expressions.grid_propagate(False)




    # Extra Buttons

botao_limpar = Button(root, text="C", bg="#901F1F",command=clear_function, font=("Arial",10), fg="white", height=1, activebackground="pink", relief="flat", highlightthickness=0)
botao_limpar.grid(row=1, column=0, sticky="ws")

botao_point = Button(root, text=".", command=lambda: char_collect(botao_point.cget('text')), bg="white", fg="black", activebackground="lightblue", relief="flat", highlightthickness=0, font=("Arial", 10), height=1, width=2)
botao_point.grid(row=1, column=0, sticky="es")




    # Buttons (Numbers)

botao1 = Button(root, text="1", command=lambda: char_collect(botao1.cget('text')), bg="#091218", fg="lightblue", activebackground="lightblue", relief="flat", highlightthickness=0, font=("Arial", 20))
botao1.grid(row=2, column=0, sticky="nsew")

botao2 = Button(root, text="2", command=lambda: char_collect(botao2.cget('text')), bg="#091218", fg="lightblue", activebackground="lightblue", relief="flat", highlightthickness=0, font=("Arial", 20))
botao2.grid(row=2, column=1, sticky="nsew")

botao3 = Button(root, text="3", command=lambda: char_collect(botao3.cget('text')), bg="#091218", fg="lightblue", activebackground="lightblue", relief="flat", highlightthickness=0, font=("Arial", 20))
botao3.grid(row=2, column=2, sticky="nsew")

botao4 = Button(root, text="4", command=lambda: char_collect(botao4.cget('text')), bg="#091218", fg="lightblue", activebackground="lightblue", relief="flat", highlightthickness=0, font=("Arial", 20))
botao4.grid(row=3, column=0, sticky="nsew")

botao5 = Button(root, text="5", command=lambda: char_collect(botao5.cget('text')), bg="#091218", fg="lightblue", activebackground="lightblue", relief="flat", highlightthickness=0, font=("Arial", 20))
botao5.grid(row=3, column=1, sticky="nsew")

botao6 = Button(root, text="6", command=lambda: char_collect(botao6.cget('text')), bg="#091218", fg="lightblue", activebackground="lightblue", relief="flat", highlightthickness=0, font=("Arial", 20))
botao6.grid(row=3, column=2, sticky="nsew")

botao7 = Button(root, text="7", command=lambda: char_collect(botao7.cget('text')), bg="#091218", fg="lightblue", activebackground="lightblue", relief="flat", highlightthickness=0, font=("Arial", 20))
botao7.grid(row=4, column=0, sticky="nsew")

botao8 = Button(root, text="8", command=lambda: char_collect(botao8.cget('text')), bg="#091218", fg="lightblue", activebackground="lightblue", relief="flat", highlightthickness=0, font=("Arial", 20))
botao8.grid(row=4, column=1, sticky="nsew")

botao9 = Button(root, text="9", command=lambda: char_collect(botao9.cget('text')), bg="#091218", fg="lightblue", activebackground="lightblue", relief="flat", highlightthickness=0, font=("Arial", 20))
botao9.grid(row=4, column=2, sticky="nsew")

botao0 = Button(root, text="0", command=lambda: char_collect(botao0.cget('text')), bg="#091218", fg="lightblue", activebackground="lightblue", relief="flat", highlightthickness=0, font=("Arial", 20))
botao0.grid(row=5, column=1, sticky="nsew")






    # Buttons (Operators)

plus_button = Button(root, text="+", command=lambda: char_collect(plus_button.cget('text')), bg="#284152", fg="lightblue", activebackground="lightblue", relief="flat", borderwidth=0, highlightthickness=0, font=("Arial", 20))
plus_button.grid(row=2, column=3, sticky="nsew")

minus_button = Button(root, text="-", command=lambda: char_collect(minus_button.cget('text')), bg="#284152", fg="lightblue", activebackground="lightblue", relief="flat", borderwidth=0, highlightthickness=0, font=("Arial", 35))
minus_button.grid(row=3, column=3, sticky="nsew")

times_button = Button(root, text="*", command=lambda: char_collect(times_button.cget('text')), bg="#284152", fg="lightblue", activebackground="lightblue", relief="flat", borderwidth=0, highlightthickness=0, font=("Arial", 20))
times_button.grid(row=5, column=0, sticky="nsew")

divide_button = Button(root, text="/", command=lambda: char_collect(divide_button.cget('text')), bg="#284152", fg="lightblue", activebackground="lightblue", relief="flat", borderwidth=0, highlightthickness=0, font=("Arial", 20))
divide_button.grid(row=5, column=2, sticky="nsew")

equals_button = Button(root, text="=", command=equals_value, bg="#5FCCBD", fg="#000000", activebackground="lightblue", relief="flat", borderwidth=0, highlightthickness=0, font=("Arial", 20))
equals_button.grid(row=4, column=3, sticky="nsew", rowspan=5)












root.mainloop()












'''

    Abordagem usada, a princípio, para capturar o valor dos botões, porém deixava o código muito largo




def number0():
    global n0, accumulating, expressions, results
    n0 = "0"
    accumulating += n0

    if expressions.cget('text') != "":
        expressions.configure(text=f"{accumulating}")
    else:
        results.configure(text=f"{accumulating}")

def number1():
    global n1, accumulating, expressions, results
    n1 = "1"
    accumulating += n1
  
    if expressions.cget('text') != "":
        expressions.configure(text=f"{accumulating}")
    else:
        results.configure(text=f"{accumulating}")

    

def number2():
    global n2, accumulating, expressions, results
    n2 = "2"
    accumulating += n2

    if expressions.cget('text') != "":
        expressions.configure(text=f"{accumulating}")
    else:
        results.configure(text=f"{accumulating}")

def number3():
    global n3, accumulating, expressions, results
    n3 = "3"
    accumulating += n3

    if expressions.cget('text') != "":
        expressions.configure(text=f"{accumulating}")
    else:
        results.configure(text=f"{accumulating}")

def number4():
    global n4, accumulating, expressions, results
    n4 = "4"
    accumulating += n4

    if expressions.cget('text') != "":
        expressions.configure(text=f"{accumulating}")
    else:
        results.configure(text=f"{accumulating}")

def number5():
    global n5, accumulating, expressions, results
    n5 = "5"
    accumulating += n5

    if expressions.cget('text') != "":
        expressions.configure(text=f"{accumulating}")
    else:
        results.configure(text=f"{accumulating}")

def number6():
    global n6, accumulating, expressions, results
    n6 = "6"
    accumulating += n6

    if expressions.cget('text') != "":
        expressions.configure(text=f"{accumulating}")
    else:
        results.configure(text=f"{accumulating}")

def number7():
    global n7, accumulating, expressions, results
    n7 = "7"
    accumulating += n7

    if expressions.cget('text') != "":
        expressions.configure(text=f"{accumulating}")
    else:
        results.configure(text=f"{accumulating}")

def number8():
    global n8, accumulating, expressions, results
    n8 = "8"
    accumulating += n8

    if expressions.cget('text') != "":
        expressions.configure(text=f"{accumulating}")
    else:
        results.configure(text=f"{accumulating}")

def number9():
    global n9, accumulating, expressions, results
    n9 = "9"
    accumulating += n9

    if expressions.cget('text') != "":
        expressions.configure(text=f"{accumulating}")
    else:
        results.configure(text=f"{accumulating}")




    
# +
def plus_value():
    global plus, accumulating
    plus = "+"
    accumulating += plus

    if expressions.cget('text') != "":
        expressions.configure(text=f"{accumulating}")
    else:
        results.configure(text=f"{accumulating}")
# -
def minus_value():
    global minus, accumulating
    minus = "-"
    accumulating += minus

    if expressions.cget('text') != "":
        expressions.configure(text=f"{accumulating}")
    else:
        results.configure(text=f"{accumulating}")
# *
def times_value():
    global times, accumulating, expressions, results
    times = "*"
    accumulating = accumulating + times
    if expressions.cget('text') != "":
        expressions.configure(text=f"{accumulating}")
    else:
        results.configure(text=f"{accumulating}")
        
    print(accumulating)

    # if expressions.cget('text') != "":
    #     print("Oi")

        
# /
def divide_value():
    global divide, accumulating
    divide = "/"
    accumulating = accumulating + divide

    if expressions.cget('text') != "":
        expressions.configure(text=f"{accumulating}")
    else:
        results.configure(text=f"{accumulating}")



'''

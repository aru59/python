'''
W internecie działają color pickery, które dla wybranego koloru poza wartościami RGB czy hex podają też ich nazwę.
Potrzebują one odwzorowania RGB -> nazwa koloru.

Ściągnij plik colors.txt: https://www.dropbox.com/s/pjojinz35fg3d7s/colors.txt?dl=0.
Zawiera on listę nazw kolorów wraz z ich kodami RGB, przykładowo:
Ecru:240 234 218
Snow White:255 255 255
White:252 251 248
Dusty Rose Ult Vy Dk:171 2 73

Napisz program, który na podstawie takiego pliku stworzy strukturę danych do sprawdzania nazwy koloru na podstawie
podanych wartości RGB. Dla celów testowych użytkownik podaje w jednej linii 3 wartości RGB, a nazwa koloru jest
wypisywana na konsolę, np.:
> 240 234 218
Color name: Ecru

Jeżeli kolor z danym kodem RGB nie istnieje, to powinien zamiast tego zostać wyświetlony napis "Color not found".

'''

def rgb_from_str_to_int(rgb_string):
    r, g, b = rgb_string.split()
    r = int(r)
    g = int(g)
    b = int(b)
    return r, g, b

def load_colors_file():
    colors_dictionary = {}
    file_path = 'colors.txt'
    with open(file_path) as file:
        for line in file:
            color_name, rgb_string = line.split(":")
            r,  g , b = rgb_from_str_to_int(rgb_string)
            colors_dictionary[(r,g,b)] = color_name
    return colors_dictionary

if __name__ == "__main__":
    colors_dictionary = load_colors_file()
    rgb_string = input("> ")
    r, g, b = rgb_from_str_to_int(rgb_string)
    if(r,g,b) in colors_dictionary:
        print("Color name:",colors_dictionary[(r,g,b)])
    else:
        print("Color not found")

from pyscript import display, document

non_metals = {
"H" :("Hydrogen", 1, 1.008),
"He" : ("Helium", 2, 4.0026),
"N" : ("Nitrogen", 7, 14.007),
"O" : ("Oxygen", 8, 15.999),
"F" : ("Fluorine", 9, 18.998),
"N" : ("Neon", 10, 20.180),
"Cl" : ("Chlorine", 17, 35.45),
"Ar" : ( "Argon", 18, 39.95),
"Kr" : ("Krypton", 36, 83.798),
"Xe" : ("Xenon", 54, 131.29),
"Rn" : ("Radon", 86, 222),
"Br" : ("Bromine", 35, 79.904),
"C" : ("Carbon", 6, 12.011),
"p" : ("Phosphorus", 15, 30.974),
"S" : ["Sulfur", 16, 32.06],
"Se" : ["Selenium", 34, 78.97],
"I" : ["Iodine", 53, 126.90]


}

def element_checker(e):
document.getElementById.innerHTML=""

element1=
document.getElementById('element').value.strip().title()

#Using ..get()- no if statement
result = non_metals.get(
    element1,
    ("Element not found", "-", "-")
)

document.getElementById('result').innerHTML=f""""

<b>Symbol:</b>{element 1}<br>
<b>Element:</b>{result[0]}<br>
<b>Atomic Number:</b{result[1]}<br>
<b>Atomic Mass:</b>{result[2]}
""""

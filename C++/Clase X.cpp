/*
	CLASE X BLOQUE II, OPERADORES Y EXPESIONES
		Realice un programa que calcule el valor que toma la siguiente funcion para unos valores dados de x
		e y

		Ejercicio f(x,y) = raiz cuadrada de x / y potencia a la 2 - 1
		
		<math.h> es la libreria matematica y trigonometria
		sqrt() es una funcion para sacar la raiz de una variable
		pow() es una funcion para exponenciar una variable
*/

#include<iostream>
#include<math.h>

using namespace std;

int main() {
	float x,y;
	
	cout<<"Ingrese un valor para x"<<endl;
	cin>>x;
	cout<<"Ingrese un valor para y"<<endl;
	cin>>y;
	
	float calculo1 = (sqrt(x))/(pow(y,2)-1);
	
	
	cout<<"\nEl valor de f(x,y) es: "<<calculo1;
	
	return 0;
}

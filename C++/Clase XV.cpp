/*
	CLASE XV BLOQUE III, ESTRUCTURAS CONDICIONALES

Ejercicio 5: Escriba un programa que lea de la entrada estándar un carácter e indique en 
la salida estándar si el carácter es una vocal minúscula o no.

Ejercicio 6: Escriba un programa que lea de la entrada estándar un carácter e indique en
la salida estándar si el carácter es una vocal minúscula, es una vocal mayúscula o no es una vocal.

*/

#include<iostream>

using namespace std;
//Ejercicio 5 y 6
int main(){
	
	char letra;
	cout<<"dar un valor a letra"<<endl;
	cin>>letra;
	
	switch(letra){
		case 'a':

		case 'e':

		case 'i':

		case 'o':

		case 'u':
			cout<<"vocal minuscula"<<endl;
			break;
			
		case 'A':
			
		case 'E':

		case 'I':

		case 'O':

		case 'U':
			cout<<" es vocal Mayuscula"<<endl;
			break;
		default:
			cout<<"no es una vocal";
	}
	
	return 0;
}

/*
	CLASE XV BLOQUE III, ESTRUCTURAS CONDICIONALES

Ejercicio 5: Escriba un programa que lea de la entrada est�ndar un car�cter e indique en 
la salida est�ndar si el car�cter es una vocal min�scula o no.

Ejercicio 6: Escriba un programa que lea de la entrada est�ndar un car�cter e indique en
la salida est�ndar si el car�cter es una vocal min�scula, es una vocal may�scula o no es una vocal.

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

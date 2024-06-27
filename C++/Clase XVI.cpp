/*
	CLASE XVI BLOQUE III, ESTRUCTURAS CONDICIONALES

Ejercicio 7:	Escriba un progrma que solicite una edad e indique si la edad introducida esta en el rango [18-25]

*/

#include <iostream>

using namespace std;

int main(){
	int edad;
	cout<<"Ingrese una edad"<<endl;
	cin>>edad;
	
	if (edad > 17 && edad < 26){
		cout<<"Su edad esta entre 18 y 25"<<endl;
	}
	else{
		cout<<"Su edad no esta entre el rango de 18 y 25"<<endl;
	}
	return 0;
}

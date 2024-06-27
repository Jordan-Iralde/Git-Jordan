/*
	Clase VIII Bloque II, Operadores y Expresiones
		Escriba un fragmento de programa que intercambie los valores de dos variables
		Ejemplo x = 5, y = 10 >>>>> x = 10, y = 5
*/

#include<iostream>

using namespace std;
	//Programa principal
	/*
int main() {
	int x, y, auxiliar;
	//valor de x
	cout<<"ingrese valor de x:"<<endl;
	cin>>x;
	//valor de y
	cout<<"ingrese valor de y:"<<endl;
	cin>>y;
	
	auxiliar = x;
	x = y;
	y = auxiliar;
	
	cout<<"se intercambio el valor de x, y. El ultimo valor de x es "<<x;
	cout<<", y el ultimo valor de y es "<<y;
	
	return 0;
}
	*/
//Tarea: Escriba un programa que lea la nota final de cuatro estudiantes y calcule la nota final media de los cuatro
int main() {
	int est1, est2, est3, est4;
	
	//nota final
	cout<<"la nota final de pepe fue: "<<endl;
	cin>>est1;
	cout<<"la nota final de juan fue: "<<endl;
	cin>>est2;
	cout<<"la nota final de lucas fue: "<<endl;
	cin>>est3;
	cout<<"la nota final de santi fue: "<<endl;
	cin>>est4;
	int nfinal = est1 + est2 + est3 + est4;
	float promedio = nfinal / 4;
	//nota final
	cout.precision(2),
	cout<<"la nota final de todos (suma) fue:"<<nfinal<<endl;
	//promedio
	cout.precision(2),
	cout<<"la nota final promedio de los cuatro fue:"<<promedio;
	
	return 0;
}

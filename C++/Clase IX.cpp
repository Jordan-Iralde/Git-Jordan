/*
	CLASE IX BLOQUE II, OPERADORES Y EXPRESIONES
		La calificacion final de un estudiante es la media ponderada de tres notas: la nota de practicas 
		que cuenta con un 30% del total, la nota teorica que cuenta un 60% y la nota de participacion
		que cuenta el 10% restante. Escriba un programa que lea de la entrada estandar las tres notas y escriba
		la nota final (100%)
		Para sacar el % se hace a menos de 1
		60% = 0.60
		30% = 0.30
		10% = 0.10
*/

#include<iostream>

using namespace std;

int main() {
	float nota1,nota2,nota3, resultado;
	cout<<"la nota 1 del practico fue: "<<endl;
	cin>>nota1;
	cout<<"la nota 2 del teorico fue: "<<endl;
	cin>>nota2;
	cout<<"la nota 3 de la participacion fue: "<<endl;
	cin>>nota3;
	
	nota1 = nota1 * 0.30;
	nota2 = nota2 * 0.60;
	nota3 = nota3 * 0.10;
	resultado = nota1 + nota2 + nota3;
	
	cout<<"\n de las notas es: "<<resultado;
	
	return 0;
}

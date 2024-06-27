/* 
Ultima clase de introducion - Entrada y Salida
Realice un programa que lea de la entrada estandar los siguientes datos de una persona:
	edad: Int
	sexo: char
	altura: Float	
Tras leer los datos, el programa debe mostrarlos en la salida estandar
*/

#include<iostream>

using namespace std;

int main()
{
	//datos
	int edad;
	char sexo[3];
	float altura;
	
	cout<<"Ingrese su edad: "<<endl;
	cin>>edad;
	cout<<"Ingrese su sexo: "<<endl;
	cin>>sexo;
	cout<<"Ingrese su altura: "<<endl;
	cin>>altura;
	
	cout<<"\nedad: "<<edad;
	cout<<"\nsexo: "<<sexo;
	cout<<"\naltura: "<<altura;
	
	return 0;
}

/*
Clase VI BLOQUE II, Operadores y Expresiones

Escribir la expresion [a/b + 1] en C++

el limite de caracteres de float y double es 6, por ejemplo 3.141592, la diferencia es casi nada
hasta ahora
Tarea: Escribir la expresion (a+b)/(c+d)
*/

#include<iostream>

using namespace std;

int main() 
{
	double a, b, c, d;
	int expresion = 1;
	//a & b
	cout<<"ingrese un valor para la variable a: "<<endl;
	cin>>a;
	cout<<"ingrese un valor para la variable b: "<<endl;
	cin>>b;
	int ab = (a+b);
	cout<<"\nEl valor de a+b= "<<ab<<endl;
	// c & d
	cout<<"\ningrese un valor para la variable c: "<<endl;
	cin>>c;
	cout<<"ingrese un valor para la variable d: "<<endl;
	cin>>d;
	int cd = (c+d);
	cout<<"\nEl valor de c+d= "<<cd<<endl;
	//division
	double division = (ab / cd);
	cout.precision(4);
	cout<<"\nEl resultado de la division de "<<ab;
	cout<<" dividido "<<cd;
	cout<<"\nEs: "<<division;
	
	double resultado = division + expresion;
	//ejercicio 1 cout<<precision(9)<<"\nel resultado de la divition anterior + 1 es= "<<resultado;
	
	return 0;
}

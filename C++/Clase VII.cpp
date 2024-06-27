/* 
	Clase VII BLOQUE II, Operadores y Expresiones
		Escribir la siguiente expresion a+(b/c) / d+(e/f)
		Tarea: Escribir la siguiente expresion a + [b/(c-d)]
*/

#include<iostream>

using namespace std;
// Actividad Principal
int main() {
	float a, b, c, d, e, f;
	//valores que se van a sumar a la division bc y ef
	cout<<"Estos valores se van a sumar, a + (b/c) y d + (e/f)"<<endl;
	cout<<"ingrese el valor para a: "<<endl;
	cin>>a;
	cout<<"ingrese el valor para d: "<<endl;
	cin>>d;
	//valores que se van a dividir en la primera parte (b/c)
	cout<<"\nEstos valores se van a dividir (b/c)"<<endl;
	cout<<"ingrese el valor para b: "<<endl;
	cin>>b;
	cout<<"ingrese el valor para c: "<<endl;
	cin>>c;
	//valores que se van a dividir en la segunda parte (e/f)
	cout<<"\nEstos valores se van a dividir (e/f)"<<endl;
	cout<<"ingrese el valor para e: "<<endl;
	cin>>e;
	cout<<"ingrese el valor para f: "<<endl;
	cin>>f;
	//valores que se van a dividir
	float division1 = (b/c);
	cout<<"\nla division de b/c es: "<<division1<<endl;
	float division2 = (e/f);
	cout<<"la division de e/f es: "<<division2<<endl;
	//Expresion1
	float expresion1 = a + division1;
	cout<<"la suma de "<<a<<" + "<<division1<<" es "<<expresion1<<endl;
	//Expresion2
	float expresion2 = d + division2;
	cout<<"la suma de "<<d<<" + "<<division2<<" es "<<expresion2<<endl;
	//Division Final
	float division3 = expresion1 / expresion2;
	cout<<"\nLa division de "<<expresion1<<" dividido "<<expresion2<<" es igual a "<<division3;
	
	return 0;
}
//		Tarea a + [b/(c-d)]
/*
int main() {
	float a,b,c,d;
	cout<<"se va a realizar la expresion a + [b/(c-d)]"<<endl;
	cout<<"Valor para a"<<endl;
	cin>>a;
	cout<<"Valor para b"<<endl;
	cin>>b;
	cout<<"Valor para c"<<endl;
	cin>>c;
	cout<<"Valor para d"<<endl;
	cin>>d;
	
	float resta = c - d;
	cout<<c<<" - "<<d<<" es igual a "<<resta<<endl;
	float division = b / resta;
	cout<<b<<" / "<<resta<<" es igual a "<<division<<endl;
	float resultado = a + division;
	
	cout<<"el resultado de "<<a<<" + "<<division<<" es= "<<resultado;
	
	return 0;
}
*/

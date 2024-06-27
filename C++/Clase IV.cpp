//Clase IV
#include<iostream>
using namespace std;

//para que se usa main= para tener ordenado por secciones
int main() {
	//variables
	int n1,n2; 
	int suma = 0;
	int resta = 0;
	int multiplicacion = 0;
	int division = 0;
	//input
	cout<<"ingrese primer numero: ";
	cin>>n1;
	
	cout<<"ingrese segundo numero: ";
	cin >>n2;
	//resultados
	suma = n1 + n2;
	resta = n1 - n2;
	multiplicacion = n1 * n2;
	division = n1 / n2;
	
	cout<<"\nel resultado de la suma es: ";
	cout<<suma;
	cout<<"\nel resultado de la resta es: ";
	cout<<resta;
	cout<<"\nel resultado de la multiplicacion es: ";
	cout<<multiplicacion;
	cout<<"\nel resultado de la division es : ";
	cout<<division;
	
	return 0;
	
}






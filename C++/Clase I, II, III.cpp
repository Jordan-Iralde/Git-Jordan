//Comentarios
//#include      Es para poner una libreria, iostream significa Input Output Stream
//con namespace, se usa para declarar un ambito de un conjunto de objetos relacionados
//con std, se puede habilitar todas las funcionalidades del compilador y biblioteca estandar (iostream)

// con // se pueden hacer comentarios de una sola linea
/*
Estos son comentarios multilinea
*/

//#<<endl es para un salto de linea, es lo mismo que \n, pero \n tiene que estar dentro de las ""

//cout Sirve para imprimir algo en pantalla
//cin para ingresar un dato en la pantalla

//double es un tipo de dato mas preciso que el float, se guardan más numeros
//Con char se imprime cualquier caracter que este dentro del ''

#include<iostream>

using namespace std;

int main()
{	//calculadora 1
    cout<<"Hola Mundos \n";
		
	int numero1;
	int numero2;
	float flotante = 15.14;
	double mayor = 16.425555;
	char caracteres = 'a';
	
	cout<<"ingrese un numero sin decimales: ";
	cin>>numero1;
	
	cout<<"\ningrese otro numero sin decimales (2): ";
	cin>>numero2;
	
	cout<<"los numeros digitados son: \n";
	cout<<numero1;
	cout<<"\n";
	cout<<numero2;
	
	return 0;
}

/*
	CLASE XII BLOQUE III, SENTENCIA SWITCH

sentencia if, else

	switch (expresion){			la expreseion es un valor que si se cumple ocurren case
		case literal1:
			acciones1;
			break;
			 
		case literal2:
			acciones2;
			break;
			 
		case literaln:
			accionesn;
			break;
			 
		default:
			acciones por defecto;
			break;
	}
*/

#include<iostream>

using namespace std;
//	std::cout

int main(){
	int numero;
	
	cout<<"valor de numero de 1 a 5"<<endl;
	cin>>numero;
	
	switch(numero){
		case 1: 	//(numero === 1)
			cout<<"numero 1";
			break;
		case 2: 	//(numero === 2)
			cout<<"numero 2";
			break;
		case 3: 	//(numero === 3)
			cout<<"numero 3";
			break;
		case 4: 	//(numero === 4)
			cout<<"numero 4";
			break;
		case 5: 	//(numero === 5)
			cout<<"numero 5";
			break;
		default:	//(numero != 1,2,3,4,5)
			cout<<"no esta dentro de 1-5";
			break;
	}
	
	return 0;
}

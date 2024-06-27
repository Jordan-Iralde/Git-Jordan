/*
	CLASE XI BLOQUE III, ESTRUCTURAS CONDICIONALES

sentencia if, else

	if (condicion){
		acciones;
	}
	else if (condicion){
		acciones;
	}
	else{
		acciones;
	}
*/

#include<iostream>;

using namespace std;

int main(){
	int numero = 0;
	cout<<"ingrese un numero"<<endl;
	cin>>numero;
	
	if (numero == 1) {
		cout<<"ingreso 1!!!";
	}
	else if (numero == 2){
		cout<<"ingreso 2???";
	}
	else{
		cout<<"no ingreso 1 :(";
	}
	return 0;
}

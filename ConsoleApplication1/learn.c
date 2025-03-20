#include <stdio.h>
#include <stdbool.h>

void someFunction(int arg)
{
	printf("This is someFunction being called and arg is: %d\n", arg);
	printf("Whoops leaving the function now!\n");
}

int main(void) {
	printf("Hello World! 你好 世界\n");

	int myAge = 43; // variable declaration
	int* ptr = &myAge; // pointer declaration

	// Reference: output myAge with a pointer
	// memory address (0x7ffe5367e044)
	printf("%p\n", ptr);
	// dereference: output the value of myAge with a pointer (43)
	printf("%d\n", *ptr);


	//// Constant pointer and pointer to constant in C
	int num1=1, num2=2;
	int* const p = &num2;
	// p = &num1; //错误,指针本身是常量，不可修改地址
	*p = 45;
	printf("num=%-9d%-9d\n",num1, num2);

	int const* p2c = &num1;
	// *p2c = 100;//错误 指针指向的常量不可更改


	//unsigned short char int long  long long
	bool b = true;
	if (b) puts("yes!");

	void (*pf)(int) = someFunction;
	pf(24);

	return 0;
}
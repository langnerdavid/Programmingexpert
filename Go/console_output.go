package main

import "fmt"

func main(){
	x := 5
	fmt.Printf("%T %v %b", x, x, x)
	// %T Type 
	// %v value
	// %b binary
	// %e scientific notation
	// %f decimal
	// %s string
	// %.2f round to the nearest decimal (2) 
	// %d digit 

	fmt.Println("hello\n", 2.45)
	str := fmt.Sprintf("%T", 1)
	fmt.Println(str)
}


func returnValues(x string) (string, int) {
	return x, 1
}
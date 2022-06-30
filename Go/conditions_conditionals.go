package main

import "fmt"

func main() {
	a := 1
	//b := 1
	//c := a < b cannot compare different types	-> c := a < float64(b)
	//c := a < float64(b) && b < 1.*0
	if a < 2 {
		fmt.Println("a is less than 2")
	} else if a == 3 {
		fmt.Println("a is equal to 3")
	} else {
		fmt.Println("a is greater than 3")
	}

	fmt.Println(a) 
}
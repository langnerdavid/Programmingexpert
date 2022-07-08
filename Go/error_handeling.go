package main

import ("fmt"
		"errors")

func doPanic() {
	panic("fail")
}

func handlePanic() {
	r := recover() //recover only from deferred func
	fmt.Println(r)
}

func divide (a int, b int) (int, error) {
	if b == 0 {
		return 0, errors.New("division by zero")
	}

	return a / b, nil
}

func main() {
	defer fmt.Println("defer")
	defer handlePanic() 
	fmt.Println("hello")

	result, err := divide(1, 0)
	if err != nil {
		fmt.Println("Error", err)
	}else {
		fmt.Println(result)
	}
	//panic("I failed") like excpetion in python


}
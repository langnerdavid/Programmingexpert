package main

import "fmt"

func main() {
	for i := 0; i < 10; i++ {
		fmt.Println(i)
	}

	//while is not available instead:
	x := 0
	for x < 10 {
		x ++
		fmt.Println(x)
	}

	str := "hello"
	fmt.Println(string(str[0])) //type uint8

	/*
	ASCII uint8 byte
	UTF8 4 bytes 32 bits (emojis etc)
	*/

	for i := 0; i < len(str); i++ {
		fmt.Println(str[i])
		fmt.Printf("%c\n", str[i])
	}

	for i, char := range str {
		fmt.Println(i, char)
		fmt.Printf("%T", char)
	}
}
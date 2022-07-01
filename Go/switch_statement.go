package main

import "fmt"

func main() {
    a := 3
	switch a {
	case 1: 
		fmt.Println("one")
	case 2: 
		fmt.Println("two")
	default: 
		fmt.Println("default")
	}


	switch a := -1; {
	case a < -1: 
		fmt.Println("a less than -1")
		fallthrough // if case 1 is true then case2 will automatically be executed
	case a < 0: 
		fmt.Println("a less than 0")
		fallthrough
	case a < 1: 
		fmt.Println("a less than 1")
	}


	switch {
	case 1 < 2: 
		fmt.Println("one")
	case 2 < 3: 
		fmt.Println("two")
	default: 
		fmt.Println("default")
	}

	b := "h"
	switch b {
	case "h", "a", "j":
		fmt.Println("worked")
	}

}


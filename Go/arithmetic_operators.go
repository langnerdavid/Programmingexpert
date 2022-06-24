package main

import (
	"fmt"
	"math"
	"strconv"
)

//import "fmt"
//import "math"

func main() {
	a := 1
	a++ //+1
	b := math.Max(5,10)
	c := math.Sqrt(21) //square root
	d := math.Pow(10, 2) //10 to the power of 2
	//c := a + b //has to be same exact type to add together int8!=int16
	fmt.Println(a, b, c, d)

	str := "1234"
	z, err := strconv.Atoi(str)
	fmt.Println(z, err) //1234 <nil>
	//strconv.ParseInt ParseFloat ParseBool .......

}
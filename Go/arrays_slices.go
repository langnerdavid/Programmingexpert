package main

import "fmt"

func main() {
	var arr [2]int
	arr2 := [...]int{4,2,4,2,4,2,4,2,4,2} //... counts how many elements in the array
	arr3 := [2][2]string{{"hello", "world"}, {"code", "go"}}
	fmt.Println(arr, arr2)

	for _, nestedArr := range arr3 {	
		for j, str := range nestedArr {
			fmt.Println(j, str)
		}
	}

	test(arr3)

	arr4 := [5]int{1, 2, 3, 4, 5}
	//sliceArr := arr4[:]
	sliceArr := arr4[1:4]
	sliceArr[0] = 100
	fmt.Println(sliceArr, len(sliceArr), cap(sliceArr))


	arr5 := []string{}
	for i := 0; i < 10; i++ {
		arr5 = append(arr5, "hello")
		fmt.Println(arr)
	}
	

	arr6 := make([][]int, 5, 10)
	fmt.Println(arr6, len(arr6), cap(arr6))

	
}

func test(x [2][2] string) {
	x [0][0] = "new string"
}
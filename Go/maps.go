package main

import "fmt"

func main() {
	mp := map[string]int{}
	mp2 := map[string][]int{"r": {4}, "h": {0}}
	mp3 := make(map[int]rune)
	fmt.Println(mp, mp2, mp3)

	mp3[9] = 1
	delete(mp3, 9)	
	value, ok := mp[9]
	fmt.Println((value, ok))

	mp4 := map[string]int{"z": 3, "k": 0, "v": 7, "r": 2}

	for key, value := range mp4 {
		fmt.Println(key, value)
	}


	n := 100
	div_map := make(map[int]uint)	//map[int]int{3: 0, 5:0}
	for num := 1; num <= n; num++ {
		for d := 1; d <= 5; d++ {
			if num % d == 0 {
				div_map[d]++
			}
		}
	}

	fmt.Println(div_map)
}
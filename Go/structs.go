package main

import "fmt"

type Clothing struct {
	shoeSize uint
	shirtColor string
}

type Person struct {
	name string
	age uint
	clothing Clothing  //embedded struc (kind of like inheritance)
}


func (c Clothing) GetShoeSize() uint {
	return c.shoeSize
}

func (p Person) GetShoeSize() uint {
	return p.clothing.GetShoeSize()
}
/*
func (p Person) GetName() string {
	return p.name
}

func (p Person) SetName(newName string) {
	p.name = newName
	fmt.Println(p)
}

//p1.SetName("Joey")
*/


func (p Person) Equal(p2 Person) bool {
	return p.age == p2.age && p.name == p2.name
}

func main() {
	p1 := Person{"Tim", 21, Clothing{12, "Blue"}} // Person{age:21, name:"Tim"}
	shoeSize := p1.clothing.GetShoeSize()
	fmt.Println(p1.clothing.shirtColor, shoeSize)
	
	mp := map[int]Person{}
	slice := []Person{{"Joe", 10, Clothing{10, "Red"}}, {"Joe", 10,Clothing{10, "Red"}}}
	fmt.Println(slice[0].Equal(slice[1]))
}
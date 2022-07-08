package main 

import "fmt"

type Name interface {
	GetName() string
}

type Person struct {
	firstName string
	lastName string
}

func (p Person) GetName() string {
	return p.firstName + " " + p.lastName
}

func (p Person) SayHi() {
	fmt.Println("Hi")
}

type Employee struct {
	name string
}

func (e Employee) GetName() string {
	return e.name
}

func PrintName(s Name) {
	fmt.Println(s.GetName())
}

func main() {
	var name Name = Person{"Tim", "Ruscica"}
	names := []Name{Employee{"Tim"}, Person{"Joe", "Bob"}}

	for _, name := range names {
		fmt.Println(name.GetName())
	}

	fmt.Println(name, names)
}
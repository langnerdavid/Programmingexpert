package main

import "fmt"

func change_to_40(x *int){
	*x = 40
}

type Book struct {
	title string
	id int
}

func (b *Book) changeTitle2(title string) {
	b.title = title
}

func changeTitle(book *Book, title string) {
	book.title = title
}

func main() {
	x1 := 0
	change_to_40(&x1)
	//*y = 2
	fmt.Println(x1)


	x := []string{"Hello", "world"}
	y := &x
	z := &y
	fmt.Println(x, *y, **z)


	book := Book{"Tim is great", 1}
	changeTitle(&book, "new title")
	fmt.Println(book)

	books := []*Book{{"a", 1}}

}
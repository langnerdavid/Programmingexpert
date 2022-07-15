package main

import ("fmt" 
		"time"
		"sync")

func run1() {
	time.Sleep(1 * time.Second)
	fmt.Println("run1")
}

func run2() {
	time.Sleep(2 * time.Second)
	fmt.Println("run2")
}

func run3() {
	time.Sleep(3 * time.Second)
	fmt.Println("run3")
}



func add(a int, b int, delay int, rv chan int) {
	time.Sleep(time.Duration(delay) * time.Second)
	rv <- a + b
}


type Counter struct {
	value int
	mutex sync.Mutex
}

func increment(counter *Counter, wg *sync.WaitGroup) {
	counter.mutex.Lock()
	defer counter.mutex.Unlock()
	counter.value = counter.value + 1
	fmt.Println(counter.value)
	wg.Done()
}

func main() {
	go run1()
	go run2()
	go run3()
	time.Sleep(4 * time.Second)
	fmt.Println("done running")

	

	returnChan := make(chan int)
	go add(1, 2, 2, returnChan)
	<-returnChan
	go add(1, 3, 5, returnChan)
	<-returnChan
	

	chan1 := make(chan int)
	chan2 := make(chan int)

	go add(5,5, chan1)
	go add(10,10, chan2)

	select {
	case rv1 := <-chan1:
		fmt.Println(rv1)
	case rv2 := <-chan2:
		fmt.Println(rv2)	
	}



	ch := make(chan int, 2)
	ch <- 1
	ch <- 2 //send
	fmt.Println(<-ch)
	<- ch //receive



	wg := sync.WaitGroup{}
	counter := Counter{value: 0}
	
	wg.Add(100)

	for i := 0; i < 100; i++ { 
		go increment(&counter, &wg)
	}
	
	wg.Wait()
}
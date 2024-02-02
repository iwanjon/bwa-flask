// package main
// import "fmt"

// func uniqueNames(a, b []string) []string {
//     var result []string
//     return result
// }
    
// func main() {
//     // should print Ava, Emma, Olivia, Sophia
//     fmt.Println(uniqueNames(
//         []string{"Ava", "Emma", "Olivia"}, 
//         []string{"Olivia", "Sophia", "Emma"}))  
// }

// should retun slice of ava emma olivia and shopia
// please complete that code



package main

import "fmt"

func uniqueNames(a, b []string) []string {
	uniqueMap := make(map[string]bool) // Map to store unique names
	var result []string

	// Iterate over the first slice and add names to the map
	for _, name := range a {
		uniqueMap[name] = true
	}

	// Iterate over the second slice and add names to the map
	for _, name := range b {
		uniqueMap[name] = true
	}

	// Append the unique names from the map to the result slice
	for name := range uniqueMap {
		result = append(result, name)
	}

	return result
}

func main() {
	// should print Ava, Emma, Olivia, Sophia
	fmt.Println(uniqueNames(
		[]string{"Ava", "Emma", "Olivia"},
		[]string{"Olivia", "Sophia", "Emma"}))
}

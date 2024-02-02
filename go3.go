// The quadratic equation is a second-degree polynomial equation of the form:

// ax^2 + bx + c = 0

// In this equation, "a", "b", and "c" are coefficients, and "x" is the variable.

// The quadratic equation can be used to solve various problems that involve finding unknown values or analyzing the behavior of quadratic functions.

// To find the solutions or roots of the quadratic equation, you can use the quadratic formula:

// x = (-b ± √(b^2 - 4ac)) / (2a)

// The quadratic formula provides the values of "x" that satisfy the equation.

// The discriminant, represented as "Δ" (delta), is part of the quadratic formula and is calculated as:

// Δ = b^2 - 4ac

// The value of the discriminant determines the nature of the roots:

// 1. If Δ > 0, the quadratic equation has two distinct real roots. The square root term in the quadratic formula yields two different values of "x".

// 2. If Δ = 0, the quadratic equation has one real root, which is a repeated root. The square root term in the quadratic formula becomes zero, resulting in a single value of "x".

// 3. If Δ < 0, the quadratic equation has no real roots. The square root term in the quadratic formula involves an imaginary number, indicating that the roots are complex conjugates. The equation cannot be solved using real numbers.

// By substituting the values of "a", "b", and "c" into the quadratic formula and evaluating the expressions, you can determine the solutions or roots of the quadratic equation.

// package main
// import "fmt"

// func findRoots(a, b, c float64) (float64, float64) {
//     return 0, 0
// }

// func main() {
//     x1, x2 := findRoots(2, 10, 8)
//     fmt.Printf("Roots: %f, %f", x1, x2)
// }

// based on the answer above please complete thecode

package main

import (
	"fmt"
	"math"
)

func findRoots(a, b, c float64) (float64, float64) {
	discriminant := b*b - 4*a*c

	// Check the value of the discriminant
	if discriminant > 0 {
		root1 := (-b + math.Sqrt(discriminant)) / (2 * a)
		root2 := (-b - math.Sqrt(discriminant)) / (2 * a)
		return root1, root2
	} else if discriminant == 0 {
		root := -b / (2 * a)
		return root, root
	} else {
		// No real roots
		return math.NaN(), math.NaN()
	}
}

func main() {
	x1, x2 := findRoots(2, 10, 8)
	fmt.Printf("Roots: %f, %f\n", x1, x2)
}

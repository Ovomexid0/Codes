package main

import (
	"fmt"
	"math/rand"
)

func main() {
	var a int
	var b string
	var c string
	var tentativas []int
	var tentativas2 [][]int

	for b != "n" {
		P := rand.Intn(101)
		count := 0
		for a != P {
			fmt.Println("Chute um numero entre 0 e 100!")
			fmt.Scan(&a)

			if a < P {
				fmt.Println("O numero é maior que a resposta escrita ")
				count++
			} else if a > P {
				fmt.Println("O número é menor que a resposta escrita")
				count++
			}
			if a == P {
				count++
			}

		}
		tentativas = append(tentativas, count)
		tentativas2 = append(tentativas2, tentativas)
		fmt.Println("Parabéns você acertou!")
		fmt.Printf("Você levou %d tentativas para acertar o número!\n", tentativas)
		fmt.Println("Deseja ver o número de tentativas utilizadas em cada rodada?(s/n)")
		fmt.Scan(&c)
		if c == "s" {
			for _, S := range tentativas2 {
				fmt.Println("tentativas", S)
			}
			fmt.Println("Deseja jogar novamente?(s/n)")
			fmt.Scan(&b)
			if b == "s" {
				tentativas = nil
				a = -1
			}
		}
	}

}

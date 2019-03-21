# FizzBuzz

- Reference link: http://codingdojo.org/kata/FizzBuzz/

- Requirements: 
   + Write a program that prints the numbers from 1 to 100. 
   + For multiples of three print “Fizz” instead of the number and 
   + For the multiples of five print “Buzz”. 
   + For numbers which are multiples of both three and five print “FizzBuzz “.
   
- New requirements:
   + A number is fizz if it is divisible by 3 or if it has a 3 in it.
   + A number is buzz if it is divisible by 5 or if it has a 5 in it.
   
- Steps to do TDD:
   + Check if can call get_fizz_buzz
   + Check if get_fizz_buzz(1) return '1'
   + Check if get_fizz_buzz(2) return '2'
   + Check if get_fizz_buzz(3) return 'Fizz'
   + Check if get_fizz_buzz(5) return 'Buzz'
   + Check if get_fizz_buzz(6) return 'Fizz'
   + Check if get_fizz_buzz(10) return 'Buzz'
   + Check if get_fizz_buzz(15) return 'FizzBuzz'
   + Check if get_fizz_buzz(23) return 'Fizz'
   + Check if get_fizz_buzz(51) return 'Buzz'

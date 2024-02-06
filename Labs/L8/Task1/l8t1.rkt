#lang racket

(define (palindrome word)
  (define (iter word i)
    (cond
      [(= (string-length word) 0) true]
      [(char=? (string-ref word i) (string-ref word (- (- (string-length word) i) 1)))
       (cond
         [(<= (- (- (string-length word) i) 1) 1) true]
         [else (iter word (+ i 1))])]
      [else false]))
  (iter word 0))
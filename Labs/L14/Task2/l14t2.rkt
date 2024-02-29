#lang racket

(define matching 
    (lambda (l1 l2 i)
        (cond
            [(<= (abs (- (list-ref l1 i) (list-ref l2 i))) 1) i]
            [(or (= (length l1) (+ i 1)) (= (length l2) (+ i 1))) -1]
            [else (matching l1 l2 (+ i 1))])))

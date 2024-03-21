#lang racket
(require racket/class)

(define point% (class object%
                   (super-new)
                  ;other.x doesn't work in Racket. There should be an accessor method and from there, you can do (send other get-x) to get the value of x
                 (define/public (distance other) (+ (expt (- x (other.x)) 2) (expt (- y (other.y)) 2))) ;To get the distance, the square root must be taken of this value
                 ;The accessors for both x and y are missing
                 (define/public (set-x nx) (= x nx)) ;The equals function doesn't work as it is for comparasion. (set!) should be used to set a value in a field
                 (define/public (set-y ny) (= y ny)) ;Same feedback as set-x
                   (init-field x y)))

(define p1 (make-object point% 9 3))
(define p2 (make-object point% -1 2))
(send p1 distance p2) 

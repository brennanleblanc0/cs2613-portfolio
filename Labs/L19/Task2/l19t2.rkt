#lang racket

(define point% (class object%
                (super-new)
                (define/public (distance other) (sqrt (+ (expt (- x (send other get-x)) 2) (+ (expt (- y (send other get-y)) 2) (expt (- z (send other get-z)) 2)))))
                (define/public (get-x) x)
                (define/public (get-y) y)
                (define/public (get-z) z)
                (define/public (set-x nx) (set! x nx))
                (define/public (set-y ny) (set! y ny))
                (define/public (set-z nz) (set! z nz))
                (define/public (distance-range other range) (>= range (distance other)))
                (define/public (triangle-perimeter other1 other2) (+ (distance other1) (+ (distance other2) (send other1 distance other2))))
                (init-field x y z)))

(define p1 (make-object point% 9 3 6))
(define p2 (make-object point% -1 2 8))

(send p1 distance-range p2 11)
(send p1 distance-range p2 10)

(define p3 (make-object point% 2 -4 3))

(send p1 triangle-perimeter p2 p3)
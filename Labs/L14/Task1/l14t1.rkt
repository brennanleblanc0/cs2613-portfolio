#lang racket

(define Vf
    (lambda (t)
        (+ 32 (* -0.35 t))))

(displayln (Vf 5))

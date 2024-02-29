#lang racket

(define accel
  (lambda (time)
  (+ 5 (* 0.5 time))))

(accel 5)

(define list-60
  (lambda (num)
    (cond
    [(= num 61) '()]
    [else (cons num (list-60 (+ num 1)))])))

(list-60 0)

(define decel
   (lambda (t)
       (+ 32 (* -0.35 t))))

(define matching
   (lambda (l1 l2 i)
       (cond
           [(<= (abs (- (list-ref l1 i) (list-ref l2 i))) 1) i]
           [(or (= (length l1) (+ i 1)) (= (length l2) (+ i 1))) -1]
           [else (matching l1 l2 (+ i 1))])))


(define same-speed
  (lambda (func1 func2 lst)
    (matching (map func1 lst) (map func2 lst) 0)))

(same-speed accel decel (list-60 0))

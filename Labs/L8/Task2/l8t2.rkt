#lang racket

(define (cipher word key start)
  (cond
    [(<= start (- (string-length word) 1))
     (define running (append (list (integer->char (+ (char->integer (string-ref word start)) key))) (cipher word key (+ start 1))))
     (cond
       [(= start 0) (remove (list-ref running (string-length word)) running)]
       [else running])]
    [else (list void)]))
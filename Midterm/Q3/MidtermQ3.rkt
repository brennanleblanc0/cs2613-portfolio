;Add comments to the code to identify errors.
;There are 6 errors in total for full points, clearly identify all of them.
;You are not required to correct the code, but you may find that correcting it will help you find errors.

;Should be racket
#lang racket


(define (decipher word key pos)
  ;Should be (>= (- (string-length word) 1) pos) --- no not and subtract from length, not pos
  (cond [(>= (- (string-length word) 1) pos)
         ;should be (- (char->integer (string-ref word pos)) key)
         (cons (integer->char (- (char->integer (string-ref word pos)) key))
               ;should add1 to pos, not key
               (decipher word key (add1 pos)))
         ]
        ;The space character should be in a list
        [else (list #\ )]
  )
)

;Should be (list->string (decipher "Phvvdjh" 3 0))
(list->string (decipher "Phvvdjh" 3 0))
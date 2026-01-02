;;; Return whether there are n perfect squares with no repeats that sum to total
;;;
;;; scm> (fit 10 2)
;;; #t
;;; scm> (fit 9 2)
;;; #f
(define (fit total n)
    (define (f total n k)
        (if (and (= n 0) (= total 0))
            #t
        (if (< total (* k k))
            #f
            (or (f total n (+ k 1)) (f (- total (* k k)) (- n 1) (+ k 1)))
        )))
    (f total n 1))

(define with-list
        (list
            (list 'a 'b) 'c 'd (list 'e)
        )
    )
    ; (draw with-list)  ; Uncomment this line to draw with-list

(define with-quote'((a b) c d (e)))
    ; (draw with-quote)  ; Uncomment this line to draw with-quote

(define with-cons
        (cons
             (cons 'a (cons 'b nil)) (cons 'c (cons 'd (cons (cons 'e nil) nil)))
        )
    )
    ; (draw with-cons)  ; Uncomment this line to draw with-cons

;;; Return a list with all numbers equal to x removed
;;;
;;; scm> (remove '(3 4 3 4 4 3) 3)
;;; (4 4 4)
;;; scm> (remove '(3 4 3 4 4 3) 4)
;;; (3 3 3)
(define (remove s x)
  (if (null? s) nil
    (if (equal? x (car s)) (remove (cdr s) x) (cons (car s) (remove (cdr s) x)))
))

(define (pair-up s)
    (if (<= (length s) 3)
        (list s)
        (append (list (list (car s) (car (cdr s)))) (pair-up (cdr (cdr s))))
    ))

(define (up n)
    (define (helper n result)
        (define first (remainder n 10))  ; Using first will shorten your code
        (if (zero? n) result
            (helper
                (quotient n 10)
                (if (< first (car result))
                    (cons first result)
                    (list first result))
                )))
    (helper
      (quotient n 10)
      (cons (remainder n 10) nil)
    ))
(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cadar x) (car (cdr (car x))))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

;; Problem 13
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 13
  (define (recur li num)
    (if (null? li)
        nil
        (cons (cons num (cons (car li) nil)) (recur (cdr li) (+ num 1)))))
  (recur s 0)
  ; END PROBLEM 13
  )

;; Return the value for a key in a dictionary list
(define (get dict key)
  ; BEGIN PROBLEM 14
  (if (null? dict)
      #f
      (if (equal? key (caar dict))
          (cadar dict)
          (get (cdr dict) key)))
  ; END PROBLEM 14
  )

;; Return a dictionary list with a (key value) pair
(define (set dict key val)
  ; BEGIN PROBLEM 14
  (if (null? dict)
      (cons(cons key (cons val nil)) nil)
      (if (equal? key (caar dict))
          (cons (cons key (cons val nil)) (cdr dict))
          (cons (car dict) (set (cdr dict) key val))))
  ; END PROBLEM 14
  )

;; Problem 15`

;; implement solution-code
(define (solution-code problem solution)
  ; BEGIN PROBLEM 15
  (if (null? problem)
      nil
      (if (equal? (car problem) '_____)
          (cons solution (solution-code (cdr problem) solution))
          (if (list? (car problem))
              (cons (solution-code (car problem) solution) (solution-code (cdr problem) solution))
              (cons (car problem) (solution-code (cdr problem) solution))
      )
  ))
  ; END PROBLEM 15
)

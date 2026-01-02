(define (over-or-under num1 num2) 
  (if (> num1 num2) 
    1
    (if (< num1 num2)
      -1
      0)))

(define (over-or-under1 num1 num2) 
  (cond ((> num1 num2) 1)
        ((< num1 num2) -1)
        (else 0)))

(define (make-adder num) 
        (lambda (x1) (+ x1 num)))

(define (composed f g) 
  (lambda 
    (x1) 
    (f (g x1))
  )
)

(define 
  (repeat f n) 
  (
    cond
    ((= n 1) f)
    ((> n 1) (composed (repeat f (- n 1)) f))
  )
)

(define (max a b)
  (if (> a b)
      a
      b))

(define (min a b)
  (if (> a b)
      b
      a))

(define (gcd a b)
  (cond ((zero? (modulo a b)) b)
        (else (gcd b (modulo a b)))))

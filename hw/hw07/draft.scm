(define (even-sub a)
    (if (null? a)
        nil
        (append (even-sub (cdr a))
                (map (lambda (x) (cons (car a) x)) (if (even? (car a)) (even-sub (cdr a))(odd-sub (cdr a))))
                (if (even? (car a))
                    (list (list (car a)))
                    nil)
                    )))

(define (odd-sub a)
    (if (null? a)
        nil
        (append (odd-sub (cdr a))
                (some-sub a odd?)
                    )))

(define (even-sub a)
    (if (null? a)
        nil
        (append (even-sub (cdr a))
                (some-sub a even?)
                    )))

(define (some-sub a f)
    (append   
        (map (lambda (x) (cons (car a) x)) (if (f (car a)) (even-sub (cdr a))(odd-sub (cdr a))))
        (if (f (car a))
            (list (list (car a)))
            nil)))
(defrule bentuksegitiga
    (jumlahsudut 3)
    =>
    (assert (bentuk segitiga))
)

(defrule bentuksegiempat
    (jumlahsudut 4)
    =>
    (assert (bentuk segiempat))
)

(defrule bentuklima
    (jumlahsudut 5)
    =>
    (assert (bentuk segilima))
)

(defrule bentuksegienam
    (jumlahsudut 6)
    =>
    (assert (bentuk segienam))
)

;;****************
;;* segitiga     *
;;****************

(defrule samakaki
    (bentuk segitiga)
    (jumlahsudutsama 2)
    =>
    (assert (samakaki))
)

(defrule samasisi
    (bentuk segitiga)
    (jumlahsudutsama 3)
    =>
    (assert (samasisi))
)

(defrule segitigatumpulsamakaki
    (bentuk segitiga)
    (samakaki)
    (jumlahsuduttumpul 1)
    =>
    (printout t "segitigatumpulsamakaki" crlf) 
    (halt) 
)

(defrule segitigasikusamakaki
    (bentuk segitiga)
    (samakaki)
    (jumlahsudutsiku 1)
    =>
    (printout t "segitigasikusamakaki" crlf)
    (halt)
)

(defrule segitigalancipsamakaki
    (bentuk segitiga)
    (samakaki)
    =>
    (printout t "segitigalancipsamakaki" crlf)
    (halt)
)
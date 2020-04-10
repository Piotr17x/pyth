miesiace=["styczen","luty","marzec","kwiecien",
"maj","czerwiec","lipiec","sierpien",
"wrzesien","pazdziernik","listopad","grudzien"]

miesiac=(n for n in miesiace)
for n in range(len(miesiace)):
    print(next(miesiac))

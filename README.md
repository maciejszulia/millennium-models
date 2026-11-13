# Minimalne modele 7 problemów milenijnych

**OSTRZEŻENIE:** Nie cytuj żadnej propozycji z repozytorium `millennium-models` jako dowodu. Każda propozycja dla problemu otwartego ma brakujący krok, którego dowodu autor nie zna.

## Streszczenie

Repozytorium sprowadza 7 problemów milenijnych do 3 modeli. W modelu teza ma dowód z co najwyżej 4 wierszy albo sprawdzian liczbowy. Wyjątek: wzór modelu dla równań Naviera–Stokesa jest rachunkiem bez dowodu. Repozytorium nie zawiera dowodu żadnego problemu otwartego: każda propozycja kończy się nazwanym brakującym krokiem. Algorytm 2 wątków szuka na przemian dowodu i kontrprzykładu. Wątek kontrprzykładów istnieje dla hipotezy Riemanna i nie znalazł naruszenia dla n od 2 do 1 000 000.

10 dowodów zawiera sekcja „Najkrótsze dowody” w pliku [REPORT.md](REPORT.md). Każdy dowód ma co najwyżej 4 wiersze.

Autor: Maciej Szulia, maciej.szulia@gmail.com

## Pliki

| Plik | Zawartość |
|---|---|
| [REPORT.md](REPORT.md) | Raport: streszczenie, 10 dowodów, 3 modele, 7 propozycji, algorytm, 8 sprawdzianów, uproszczenia, zastosowania, problematyka, dyskusja, bibliografia. |
| [models_check.py](models_check.py) | 8 sprawdzianów. Jeżeli co najmniej 1 sprawdzian daje liczby niezgodne z twierdzeniem, to skrypt kończy pracę błędem. |
| [figures.py](figures.py) | Skrypt, który rysuje 9 rysunków. |
| [figures](figures) | 9 rysunków: po 1 rysunku na problem oraz 2 rysunki algorytmu. |
| [LICENSE](LICENSE) | Licencja MIT. |

## 3 modele i 1 algorytm

| Element | Opis | Problemy |
|---|---|---|
| Model 1 | Powierzchnia E × E z 4 krzywymi i z liczbą przecięć krzywych. | Riemann, Birch i Swinnerton-Dyer (BSD), Hodge |
| Model 2 | 1 liczba na każdą skalę długości. Model pyta, w którą stronę liczba zmienia się, gdy skala maleje. | Poincaré, Yang–Mills, Navier–Stokes |
| Model 3 | Liczba zapytań algorytmu i liczba bramek obwodu. | P a NP |
| Algorytm 2 wątków | Pętla, która na przemian sprawdza teksty jako dowody i kandydatów na kontrprzykład. | każdy z 7 problemów |

## Rysunki

Tytuł każdego rysunku podaje wniosek. Podtytuł podaje, co rysunek przedstawia. Stopka podaje źródło liczb.

### 1. Hipoteza Riemanna

Brakujący krok: odpowiednik powierzchni E × E z formą przecięcia dla pierścienia liczb całkowitych.

![Lewy panel: punkty krzywej y² + y = x³ − x nad ciałem o 97 elementach. Prawy panel: pary (p, a) dla krzywych eliptycznych leżą wewnątrz paraboli a² = 4p.](figures/riemann-hasse-bound.png)

### 2. Hipoteza Bircha i Swinnertona-Dyera

Brakujący krok: skończoność grupy Tate'a–Szafarewicza dla krzywych o randze co najmniej 2.

![Suma ln(N_p/p) dla 4 krzywych o rangach 0, 1, 2, 3 na skali ln ln X. Nachylenie linii rośnie z rangą.](figures/bsd-product-slopes.png)

### 3. Hipoteza Hodge'a

Brakujący krok: konstrukcja podrozmaitości dla klasy typu (k,k) przy k ≥ 2.

![Lewy panel: krata kwadratowa pokrywa się z obrazem kraty po obrocie o 90°. Prawy panel: krata prostokątna i obraz kraty po obrocie mają wspólny tylko punkt 0.](figures/hodge-lattice-rotation.png)

### 4. Teoria Yanga–Millsa i luka masowa

Brakujący krok: dolne ograniczenie odstępu E₁ − E₀, które pozostaje dodatnie w nieskończonej objętości.

![Lewy panel: 1/g² maleje liniowo do 0 na długości ℓ*. Środkowy panel: gęstość stanu podstawowego skupiona w środku i kontur potencjału z 4 otwartymi dolinami. Prawy panel: 3 poziomy energii, granica dolna i odstęp E₁ − E₀.](figures/yang-mills-coupling-and-gap.png)

### 5. Równania Naviera–Stokesa

Brakujący krok dla ruchu bez siły zewnętrznej: kres górny ułamka θ dla prawdziwego równania.

![Lewy panel, 3 wymiary: liczba Reynoldsa rośnie dla θ = 0,70, jest stała dla θ = 0,50 i maleje dla θ = 0,35. Prawy panel, 2 wymiary: liczba Reynoldsa maleje dla każdej z 3 wartości θ.](figures/navier-stokes-reynolds-cascade.png)

### 6. Problem P a NP

Brakujący krok: dolne ograniczenie liczby bramek dla funkcji z klasy NP, które przewyższa każdy wielomian zmiennej n.

![Lewy panel: funkcja OR wymaga n zapytań, a certyfikat odpowiedzi 1 ma 1 bit. Prawy panel: ograniczenie ze zliczania rośnie wykładniczo, a ograniczenie dla funkcji podanej wzorem rośnie liniowo.](figures/p-vs-np-queries-and-gates.png)

### 7. Hipoteza Poincarégo

Dowód istnieje (Perelman 2002, 2003). Model 2 odtwarza szkielet dowodu na okrągłej sferze.

![Lewy panel: przekrój sfery w 4 chwilach, coraz mniejsze okręgi. Prawy panel: r² maleje liniowo do 0 w chwili T.](figures/poincare-sphere-shrinks.png)

### 8. Algorytm 2 wątków

Algorytm kończy pracę, gdy istnieje dowód, obalenie albo kontrprzykład. Żaden algorytm nie rozpoznaje przypadku, w którym teoria nie rozstrzyga tezy.

![Schemat blokowy algorytmu 2 wątków: start, wątek dowodów, 2 pytania o dowód, wątek kontrprzykładów, pytanie o kandydata, 2 wyniki i pętla ze zwiększeniem k o 1.](figures/algorithm-two-threads.png)

### 9. Wątek kontrprzykładów dla hipotezy Riemanna

Hipoteza Riemanna jest równoważna 1 nierówności dla liczb naturalnych (Lagarias 2002). Sprawdzian 8 nie znalazł naruszenia nierówności.

![Największy iloraz w 59 przedziałach liczby n zostaje pod granicą 1. Mediana ilorazu maleje od 0,9 do 0,3. Największy iloraz 0,9886 daje liczba n = 12.](figures/riemann-counterexample-thread.png)

## Jak powtórzyć obliczenia

Wykonaj każdy krok w tej kolejności:

1. Utwórz środowisko: `python3 -m venv .venv`.
2. Zainstaluj biblioteki: `.venv/bin/pip install -r requirements.txt`.
3. Uruchom sprawdziany: `.venv/bin/python models_check.py`. Wynik: skrypt wypisuje wiersz `all checks passed`.
4. Narysuj rysunki: `.venv/bin/python figures.py`. Wynik: katalog `figures` zawiera 9 plików PNG.

Skrypt `models_check.py` pracuje 16 s ± 4 s. Skrypt `figures.py` pracuje 18 s ± 4 s. Pomiar: laptop autora z 8 wątkami procesora.

## Problematyka

- Sprawdzian obejmuje skończoną liczbę przypadków. Sprawdzian nie jest dowodem.
- Autor nie sprawdził żadnego odsyłacza do literatury w pracy źródłowej.
- Stan problemów z 2026 r. pochodzi ze streszczeń wyników wyszukiwania z dnia 2026-11-13.
- Pełną listę zawiera sekcja „Problematyka” w pliku [REPORT.md](REPORT.md).

# Minimalne modele 7 problemów milenijnych

**OSTRZEŻENIE:** Nie cytuj żadnej propozycji z tego repozytorium jako dowodu. Każda propozycja dla problemu otwartego ma brakujący krok, którego dowodu autor nie zna.

Repozytorium zawiera 3 modele, 7 sprawdzianów liczbowych i 7 rysunków dla 7 problemów milenijnych. Repozytorium nie zawiera dowodu żadnego problemu otwartego. Pełny tekst zawiera plik [REPORT.md](REPORT.md).

Autor: Maciej Szulia, maciej.szulia@gmail.com

## Pliki

| Plik | Zawartość |
|---|---|
| [REPORT.md](REPORT.md) | Raport: 3 modele, 7 propozycji, 7 sprawdzianów, ograniczenia, bibliografia. |
| [models_check.py](models_check.py) | 7 sprawdzianów. Jeżeli co najmniej 1 sprawdzian daje liczby niezgodne z twierdzeniem, to skrypt kończy pracę błędem. |
| [figures.py](figures.py) | Skrypt, który rysuje 7 rysunków. |
| [figures](figures) | 7 rysunków, po 1 rysunku na problem. |
| [LICENSE](LICENSE) | Licencja MIT. |

## 3 modele

| Model | Opis | Problemy |
|---|---|---|
| Model 1 | Powierzchnia E × E z 4 krzywymi i z liczbą przecięć krzywych. | Riemann, Birch i Swinnerton-Dyer (BSD), Hodge |
| Model 2 | 1 liczba na każdą skalę długości. Model pyta, w którą stronę liczba zmienia się, gdy skala maleje. | Poincaré, Yang–Mills, Navier–Stokes |
| Model 3 | Liczba zapytań algorytmu i liczba bramek obwodu. | P a NP |

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

![Lewy panel: 1/g² maleje liniowo do 0 na długości ℓ*. Środkowy panel: gęstość stanu podstawowego skupiona w środku i kontur potencjału z 4 otwartymi dolinami. Prawy panel: 3 poziomy energii i odstęp E₁ − E₀.](figures/yang-mills-coupling-and-gap.png)

### 5. Równania Naviera–Stokesa

Brakujący krok dla ruchu bez siły zewnętrznej: kres górny ułamka θ dla prawdziwego równania.

![Lewy panel, 3 wymiary: liczba Reynoldsa rośnie dla θ = 0,70, jest stała dla θ = 0,50 i maleje dla θ = 0,35. Prawy panel, 2 wymiary: liczba Reynoldsa maleje dla każdej z 3 wartości θ.](figures/navier-stokes-reynolds-cascade.png)

### 6. Problem P a NP

Brakujący krok: dolne ograniczenie liczby bramek dla funkcji z klasy NP, które przewyższa każdy wielomian zmiennej n.

![Lewy panel: funkcja OR wymaga n zapytań, a certyfikat odpowiedzi 1 ma 1 bit. Prawy panel: ograniczenie ze zliczania rośnie wykładniczo, a ograniczenie dla funkcji podanej wzorem rośnie liniowo.](figures/p-vs-np-queries-and-gates.png)

### 7. Hipoteza Poincarégo

Dowód istnieje (Perelman 2002, 2003). Model 2 odtwarza szkielet dowodu na okrągłej sferze.

![Lewy panel: przekrój sfery w 4 chwilach, coraz mniejsze okręgi. Prawy panel: r² maleje liniowo do 0 w chwili T.](figures/poincare-sphere-shrinks.png)

## Jak powtórzyć obliczenia

Wykonaj każdy krok w tej kolejności:

1. Utwórz środowisko: `python3 -m venv .venv`.
2. Zainstaluj biblioteki: `.venv/bin/pip install -r requirements.txt`.
3. Uruchom sprawdziany: `.venv/bin/python models_check.py`. Wynik: skrypt wypisuje wiersz `all checks passed`.
4. Narysuj rysunki: `.venv/bin/python figures.py`. Wynik: katalog `figures` zawiera 7 plików PNG.

Każdy z 2 skryptów pracuje od 60 s do 120 s włącznie na laptopie autora.

## Ograniczenia

- Sprawdzian obejmuje skończoną liczbę przypadków. Sprawdzian nie jest dowodem.
- Autor nie sprawdził żadnego odsyłacza do literatury w pracy źródłowej.
- Stan problemów z 2026 r. pochodzi ze streszczeń wyników wyszukiwania z dnia 2026-11-13.
- Pełną listę ograniczeń zawiera sekcja „Ograniczenia” w pliku [REPORT.md](REPORT.md).

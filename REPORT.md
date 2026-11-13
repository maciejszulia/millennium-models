# Minimalne modele 7 problemów milenijnych: 3 modele, 7 propozycji, 14 sprawdzianów, 1 algorytm

Maciej Szulia, maciej.szulia@gmail.com

Raport opisuje stan z dnia 2026-11-13.

**OSTRZEŻENIE:** Nie cytuj żadnej propozycji z raportu jako dowodu. Każda propozycja dla problemu otwartego ma brakujący krok, którego dowodu autor nie zna.

## Streszczenie

Raport sprowadza 7 problemów milenijnych do 3 modeli. W modelu teza ma dowód z co najwyżej 4 wierszy albo sprawdzian liczbowy. Raport nie zawiera dowodu żadnego problemu otwartego: każda propozycja kończy się nazwanym brakującym krokiem. Algorytm 2 wątków szuka na przemian dowodu i kontrprzykładu. Wątek kontrprzykładów istnieje dla hipotezy Riemanna i nie znalazł naruszenia dla $n$ od 2 do 1 000 000 `[obliczenie: skrypt]`. 4 symulacje i 18 rysunków pokazują modele w 2 wymiarach i w 3 wymiarach.

## Najkrótsze dowody

Każdy dowód dotyczy twierdzenia w modelu albo własności algorytmu. Żaden dowód nie dotyczy problemu otwartego. Oznaczenia definiują sekcje „Model 1”, „Model 2”, „Model 3” i „Algorytm”.

1. **Riemann w modelu 1: $a^2 \le 4p$** `[źródło: Grothendieck 1958; Mattuck, Tate 1958]`.
   - Klasy $D' = D - H - V$ oraz $G' = G - H - pV$ są prostopadłe do $H$ i do $V$.
   - $(D', D') = -2$; $(G', G') = -2p$; $(D', G') = -a$.
   - Forma przecięcia jest ujemnie określona na klasach prostopadłych do $H$ i do $V$, więc $(D', G')^2 \le (D', D')(G', G')$.
2. **Hodge dla klas typu $(1,1)$** `[źródło: Lefschetz 1924 dla twierdzenia; Griffiths, Harris 1994 dla dowodu]`.
   - Ciąg wykładniczy snopów $0 \to \mathbb{Z} \to \mathcal{O} \to \mathcal{O}^{\ast} \to 0$ daje ciąg dokładny $\mathrm{Pic}(X) \to H^2(X, \mathbb{Z}) \to H^2(X, \mathcal{O})$.
   - Klasa całkowita typu $(1,1)$ przechodzi na 0 w $H^2(X, \mathcal{O})$, więc klasa pochodzi z grupy $\mathrm{Pic}(X)$.
   - Klasa z grupy $\mathrm{Pic}(X)$ jest klasą dywizora.
3. **Poincaré dla okrągłej sfery.**
   - Okrągła sfera $S^3$ o promieniu $r$ ma tensor Ricciego $\mathrm{Ric} = (2/r^2) g$.
   - Równanie $\partial g/\partial t = -2 \mathrm{Ric}$ daje $d(r^2)/dt = -4$, więc $r^2(t) = r_0^2 - 4t$.
4. **Yang–Mills, hamiltonian $H = -\Delta + x^2y^2$: widmo dyskretne** `[źródło: Simon 1983]` **oraz $E_0 \ge 1{,}0188$.**
   - Oscylator $-\partial^2/\partial y^2 + x^2y^2$ ma poziom podstawowy $\lvert x\rvert$, więc $-\partial^2/\partial y^2 + x^2y^2 \ge \lvert x\rvert$. Zamiana zmiennych daje $-\partial^2/\partial x^2 + x^2y^2 \ge \lvert y\rvert$.
   - Suma 2 nierówności daje $-\Delta + 2x^2y^2 \ge \lvert x\rvert + \lvert y\rvert$.
   - Dodanie operatora $-\Delta$ do obu stron daje $2H \ge -\Delta + \lvert x\rvert + \lvert y\rvert$.
   - Operator $-\Delta + \lvert x\rvert + \lvert y\rvert$ ma widmo dyskretne i poziom podstawowy $2 \times 1{,}0188$ `[obliczenie: skrypt; źródło: DLMF §9.9]`. Zatem $H$ ma widmo dyskretne oraz $E_0 \ge 1{,}0188$.
5. **P a NP w modelu zapytań** `[źródło: Buhrman, de Wolf 2002]`.
   - Przeciwnik odpowiada „0” na każde pytanie o bit.
   - Po mniej niż $n$ pytaniach 2 wejścia zgodne z odpowiedziami dają różne wartości funkcji $\mathrm{OR}_n$.
   - Zatem deterministyczne drzewo decyzyjne zadaje $n$ pytań, a certyfikat odpowiedzi „1” ma 1 bit.
6. **Zliczanie obwodów** `[źródło: Shannon 1949, argument dla sieci przekaźnikowych]`.
   - Obwodów o $s$ bramkach jest co najwyżej $(16(n+s)^2)^s$, a funkcji $n$ zmiennych jest $2^{2^n}$.
   - Jeżeli pierwsza liczba jest mniejsza niż druga liczba, to co najmniej 1 funkcja nie ma obwodu o $s$ bramkach.
7. **Algorytm: dowód albo obalenie kończy pracę.**
   - Dowód jest tekstem o skończonej długości $k_0$.
   - Pętla sprawdza każdy tekst o długości $k_0$ w kroku $k = k_0$.
8. **Algorytm: fałszywe zdanie klasy $\Pi_1$ kończy pracę.**
   - Fałszywe zdanie klasy $\Pi_1$ ma kontrprzykład o numerze $k_0$.
   - Wątek kontrprzykładów sprawdza kandydata numer $k_0$ w kroku $k = k_0$.
9. **Algorytm: zdanie klasy $\Pi_1$, którego teoria nie rozstrzyga, jest prawdziwe** `[źródło: Aaronson, „P =? NP”]`. Warunek: teoria dowodzi wyniku każdego skończonego obliczenia.
   - Fałszywe zdanie klasy $\Pi_1$ ma kontrprzykład.
   - Obliczenie na kontrprzykładzie jest dowodem zaprzeczenia zdania, więc teoria rozstrzyga zdanie fałszywe.
10. **Algorytm nie rozpoznaje braku rozstrzygnięcia** `[źródło: Turing 1936]`.
    - Niech algorytm $A$ kończy pracę dla każdego zdania z 1 z 3 wyników: dowód, obalenie, brak rozstrzygnięcia.
    - Algorytm $A$ rozstrzyga wtedy, które zdania mają dowód.
    - Rozstrzyganie, które zdania mają dowód, rozwiązuje problem stopu. Problem stopu nie ma algorytmu.
11. **Navier–Stokes w modelu 2: $\mathrm{Re}_{n+1} = \mathrm{Re}_n \sqrt{\theta \lambda^{d-2}}$.**
    - Wir $n$ ma rozmiar $\ell_n = \lambda^{-n}$, prędkość $U_n$, energię $E_n = U_n^2 \ell_n^d$ i liczbę $\mathrm{Re}_n = U_n \ell_n / \nu$.
    - Model zakłada $E_{n+1} = \theta E_n$, więc $U_{n+1}^2 = \theta \lambda^d U_n^2$.
    - Zatem $\mathrm{Re}_{n+1} = U _{n+1} \ell _{n+1} / \nu = \mathrm{Re}_n \sqrt{\theta \lambda^{d-2}}$.
12. **P a NP: brakujący krok daje tezę.**
    - Algorytm o wielomianowym czasie pracy daje obwody o wielomianowej liczbie bramek `[założenie]`.
    - Jeżeli zadanie spełnialności nie ma takich obwodów, to zadanie nie ma takiego algorytmu, czyli $P \ne NP$.

1 teza nie ma dowodu w modelu: hipoteza BSD. Model 1 daje dla BSD liczby i nierówność nad ciałem funkcyjnym. Dowód 11 dotyczy modelu, a związek modelu 2 z prawdziwym równaniem Naviera–Stokesa jest założeniem.

Legenda: znacznik `[obliczenie: skrypt]` oznacza liczbę, którą obliczył plik `models_check.py`. Znacznik `[źródło: autor rok]` wskazuje pracę z sekcji „Bibliografia”. Plik [references-check.md](references-check.md) podaje stan sprawdzenia każdego odsyłacza. Znacznik `[źródło: sieć]` wskazuje sekcję „Źródła z sieci”. Znacznik `[założenie]` oznacza zdanie bez dowodu i bez sprawdzenia.

## Słownik

| Termin | Definicja | Słowa zakazane dla tego pojęcia |
|---|---|---|
| model | Obiekt matematyczny, w którym odpowiednik tezy problemu ma opublikowany dowód. | uproszczenie, przybliżenie |
| twierdzenie w modelu | Zdanie o modelu, które ma opublikowany dowód. | fakt |
| brakujący krok | Zdanie bez opublikowanego dowodu, które przenosi twierdzenie w modelu na pełny problem. | dziura |
| propozycja | Plan dowodu, który nazywa model, twierdzenie w modelu i brakujący krok. | rozwiązanie, dowód |
| sprawdzian | Obliczenie skryptu, które porównuje liczby z twierdzeniem w modelu albo z hipotezą. | test, dowód |
| symulacja | Obliczenie, które przybliża ruch układu w czasie. | eksperyment |
| algorytm 2 wątków | Pętla z sekcji „Algorytm”, która na przemian szuka dowodu i kontrprzykładu. | metoda, procedura |
| wątek dowodów | Część algorytmu 2 wątków, która sprawdza teksty jako dowody. | szukanie dowodu |
| wątek kontrprzykładów | Część algorytmu 2 wątków, która sprawdza kandydatów. | szukanie błędu |
| kandydat | Obiekt o numerze $k$, który wątek kontrprzykładów sprawdza w kroku $k$. | przypadek |
| zdanie klasy $\Pi_1$ | Zdanie „każda liczba naturalna $n$ spełnia warunek $W(n)$”, w którym skończone obliczenie sprawdza warunek $W(n)$. | zdanie sprawdzalne |

## Stan problemów w dniu 2026-11-13

| Problem | Stan | Znacznik |
|---|---|---|
| Poincaré | Dowód istnieje. Clay Mathematics Institute (CMI) przyznał nagrodę G. Perelmanowi 2010-03-18. Perelman odrzucił nagrodę. | `[źródło: Perelman 2002, 2003a, 2003b; sieć]` |
| Navier–Stokes | OpenAI ogłosił 2026-09-08 dowód wariantów (C) i (D): osobliwość przy gładkiej sile zewnętrznej. W październiku 2026 r. dowód czekał na niezależną weryfikację. Praca z 2026-10-06 podważa zgodność formalizacji w Lean z dowodem słownym. Pytanie o ruch bez siły nie ma dowodu. | `[źródło: sieć]` |
| Yang–Mills | OpenAI ogłosił 2026-10-26 dowód istnienia teorii. Firma OpenAI powołała komitet 5 osób pod kierunkiem D. Grossa. Komitet opublikował 2026-11-10 objaśnienie dowodu i kod Lean firmy OpenAI. Komitet pisze, że nie rozumie jeszcze dowodu w pełni. Luka masowa nie ma dowodu. | `[źródło: sieć]` |
| Riemann, Birch i Swinnerton-Dyer (BSD), Hodge, P a NP | Żaden z 4 problemów nie ma dowodu. | `[źródło: sieć]` |

Strona CMI oznacza 5 problemów statusem „Unsolved”, problem Naviera–Stokesa statusem „Active” i hipotezę Poincarégo statusem „Solved” `[źródło: sieć]`. Opis problemu Naviera–Stokesa uznaje za rozwiązanie dowód co najmniej 1 z 4 wariantów: (A), (B), (C), (D) `[źródło: Fefferman, opis problemu]`. Jeżeli dowód wariantu (C) przejdzie weryfikację, to opis problemu Naviera–Stokesa jest spełniony `[założenie]`.

## Model 1: powierzchnia $E \times E$ z 4 krzywymi (Riemann, BSD, Hodge)

$E$ oznacza krzywą eliptyczną. $f$ oznacza odwzorowanie $E \to E$. Model 1 zawiera 4 krzywe na powierzchni $E \times E$:

- $H = E \times \lbrace\text{punkt}\rbrace$,
- $V = \lbrace\text{punkt}\rbrace \times E$,
- $D$ = przekątna,
- $G$ = wykres odwzorowania $f$.

Zapis $(A, B)$ oznacza liczbę przecięć krzywej $A$ z krzywą $B$. Model 1 ma 1 rachunek:

$$a^2 \le 4 \deg f, \qquad a = \deg f + 1 - (D, G)$$

- $\deg f$: stopień odwzorowania $f$,
- $(D, G)$: liczba punktów stałych odwzorowania $f$, liczona z krotnościami.

Dowód rachunku: dowód 1 w sekcji „Najkrótsze dowody”, z liczbą $\deg f$ w miejscu liczby $p$.

![Torus z 4 krzywymi: H, V, przekątna D i wykres G odwzorowania x → 3x. Krzywe D i G przecinają się w 2 punktach.](figures/model-1-torus-curves.png)

Rysunek pokazuje model 1 w przekroju rzeczywistym: krzywa $E$ jest okręgiem, a powierzchnia $E \times E$ torusem. Model 1 obsługuje 3 problemy.

**Riemann.** $f$ oznacza odwzorowanie Frobeniusa nad ciałem $F_p$. Wtedy $\deg f = p$, a $(D, G)$ równa się liczbie punktów krzywej $E$ nad $F_p$. Nierówność $a^2 \le 4p$ jest hipotezą Riemanna dla funkcji dzeta krzywej $E$ `[źródło: Hasse 1933, zapowiedź; Hasse 1936, dowód]`.

![Lewy panel: punkty krzywej y² + y = x³ − x nad ciałem o 97 elementach. Prawy panel: pary (p, a) dla krzywych eliptycznych leżą wewnątrz paraboli a² = 4p.](figures/riemann-hasse-bound.png)

Pełna hipoteza Riemanna dotyczy funkcji $\zeta$. Rysunek pokazuje powierzchnię $\lvert\zeta(\sigma + it)\rvert$ w 3 wymiarach. Sprawdzian 13 znajduje 6 zer dla $t \lt 40$, każde na prostej $\sigma = 1/2$. Pierwsze zero ma $t = 14{,}135$ `[obliczenie: skrypt]`.

![Powierzchnia modułu funkcji dzeta nad pasem krytycznym: 6 zer leży na prostej σ = 1/2.](figures/riemann-zeta-surface.png)

**BSD.** Liczby $N_p = (D, G)$ dla każdej liczby pierwszej $p$ budują funkcję $L$ krzywej $E$. Postać pierwotna hipotezy: iloczyn liczb $N_p/p$ dla $p \le X$ rośnie jak $(\ln X)^r$ `[źródło: Birch, Swinnerton-Dyer 1965]`. Symbol $r$ oznacza rangę krzywej $E$. Nad ciałem funkcyjnym rachunek przecięć na powierzchni eliptycznej dowodzi nierówności: ranga $\le$ krotność zera funkcji $L$ `[źródło: Tate 1966]`.

![Suma ln(N_p/p) dla 4 krzywych o rangach 0, 1, 2, 3 na skali ln ln X. Nachylenie linii rośnie z rangą.](figures/bsd-product-slopes.png)

Liczby $a = p + 1 - N_p$ tej samej krzywej spełniają nierówność Hassego. Sprawdzian 14 porównuje 9 590 wartości $a/(2\sqrt{p})$ krzywej 37a1 z rozkładem półokręgu. Największa różnica dystrybuant wynosi 0,0066 `[obliczenie: skrypt]`.

![Histogram wartości a/(2√p) krzywej 37a1 i gęstość rozkładu półokręgu.](figures/bsd-sato-tate.png)

**Hodge.** Nad ciałem liczb zespolonych każda wymierna klasa typu $(1,1)$ na $E \times E$ jest kombinacją klas krzywych (dowód 2). Rysunek pokazuje kratę torusa $E = \mathbb{C}/(\mathbb{Z} + \tau\mathbb{Z})$. Mnożenie przez $i$ obraca kratę o 90°. Tylko jeżeli obrót zachowuje kratę, mnożenie przez $i$ jest odwzorowaniem $f$ i torus ma krzywą $G$.

![Lewy panel: krata kwadratowa pokrywa się z obrazem kraty po obrocie o 90°. Prawy panel: krata prostokątna i obraz kraty po obrocie mają wspólny tylko punkt 0.](figures/hodge-lattice-rotation.png)

W modelu 1 hipoteza Riemanna mówi o znaku formy przecięcia. Hipoteza Hodge'a mówi, że lista krzywych jest pełna. Hipoteza BSD mówi o liczbach $(D, G)$ dla każdej liczby pierwszej $p$ razem.

## Model 2: 1 liczba na skalę (Poincaré, Yang–Mills, Navier–Stokes)

Model 2 przypisuje każdej skali długości $\ell$ dokładnie 1 liczbę $g(\ell)$. Model 2 pyta o 1 rzecz: w którą stronę liczba $g$ zmienia się, gdy $\ell$ maleje.

**Poincaré.** $g = 1/r^2$, gdzie $r$ oznacza promień okrągłej sfery $S^3$ pod przepływem Ricciego. Wzór (dowód 3):

$$r^2(t) = r_0^2 - 4t$$

Symbol $t$ oznacza czas przepływu, a $r_0$ oznacza promień w chwili $t = 0$. Sfera znika w chwili $T = r_0^2/4$.

![Lewy panel: przekrój sfery w 4 chwilach, coraz mniejsze okręgi. Prawy panel: r² maleje liniowo do 0 w chwili T.](figures/poincare-sphere-shrinks.png)

Symulacja 9 pokazuje ten sam mechanizm o 1 wymiar niżej. Krzywa zamknięta pod przepływem skracającym krzywą staje się okręgiem, a pole maleje w tempie $2\pi$ `[źródło: Gage, Hamilton 1986; Grayson 1987]`. Odchylenie symulacji od prostej $A_0 - 2\pi t$ wynosi 0,83 % pola początkowego. Iloraz izoperymetryczny spada z 1,732 do 1,0008 `[obliczenie: skrypt]`.

![Animacja: krzywa o 3 płatach kurczy się do okręgu, a pole z symulacji leży na prostej teoretycznej.](figures/poincare-curve-shortening.gif)

**Yang–Mills.** $g$ oznacza sprzężenie teorii z grupą $SU(N)$ bez fermionów. Wzór w rachunku 1 pętli `[źródło: Gross, Wilczek 1973; Politzer 1973]`:

$$\frac{1}{g^2(\ell)} = \frac{1}{g^2(\ell_0)} - 2 b_0 \ln\frac{\ell}{\ell_0}, \qquad b_0 = \frac{11N}{48\pi^2}$$

Wielkość $1/g^2$ spada do 0 na długości $\ell^{\ast} = \ell_0 \exp\left(1/(2 b_0 g^2(\ell_0))\right)$. Masa cząstki jest proporcjonalna do $1/\ell^{\ast}$ `[założenie]`.

Rachunek pomocniczy: pola jednorodne w pudle o boku $L \lt \ell^{\ast}$ mają hamiltonian z potencjałem o płaskich dolinach `[źródło: Lüscher 1983]`. Hamiltonian $-\Delta + x^2y^2$ jest przekrojem hamiltonianu pól jednorodnych z 2 zmiennymi `[założenie]`. Potencjał $x^2y^2$ ma doliny o energii 0. Widmo hamiltonianu $-\Delta + x^2y^2$ jest jednak dyskretne (dowód 4). Odstęp $E_1 - E_0$ jest proporcjonalny do $\hbar^{4/3}$, więc odstęp znika w teorii klasycznej `[obliczenie: przeskalowanie zmiennych]`. Przeskalowanie mnoży każdą zmienną przez $\hbar^{1/3}$.

![Lewy panel: 1/g² maleje liniowo do 0 na długości ℓ*. Środkowy panel: gęstość stanu podstawowego skupiona w środku i kontur potencjału z 4 otwartymi dolinami. Prawy panel: 3 poziomy energii, granica dolna i odstęp E₁ − E₀.](figures/yang-mills-coupling-and-gap.png)

![Powierzchnia potencjału x²y² w 3 wymiarach: 4 ramiona dolin i kontur poziomu podstawowego. Dno dolin ma wartość potencjału 0.](figures/yang-mills-potential-3d.png)

Symulacja 11 pokazuje różnicę ruchu klasycznego i stanu kwantowego. Każda z 32 orbit klasycznych o energii $E_0$ wychodzi poza kwadrat o boku 6, a 12 orbit dochodzi do odległości 30. Stan kwantowy ma poza kwadratem 0,28 % masy `[obliczenie: skrypt]`.

![Animacja: orbita klasyczna wchodzi w doliny potencjału, a gęstość kwantowa zostaje w środku.](figures/yang-mills-classical-orbit.gif)

**Navier–Stokes.** $g = \mathrm{Re}_n$, czyli liczba Reynoldsa wiru o rozmiarze $\lambda^{-n}$. Wzór modelu (dowód 11):

$$\mathrm{Re}_{n+1} = \mathrm{Re}_n \sqrt{\theta \lambda^{d-2}}$$

- $\theta$: ułamek energii wiru $n$, który przechodzi do wiru $n + 1$ ($0 \lt \theta \le 1$),
- $\lambda$: iloraz rozmiarów wiru $n$ i wiru $n + 1$ ($\lambda \gt 1$),
- $d$: wymiar przestrzeni.

Dla $d = 2$ liczba $\mathrm{Re}_n$ nie rośnie przy żadnym $\theta$. Wniosek dla $d = 2$ zgadza się z twierdzeniem o gładkości w 2 wymiarach `[źródło: Ładyżenska 1959; Fefferman, opis problemu]`. Tylko jeżeli $\theta \gt 1/\lambda$, liczba $\mathrm{Re}_n$ rośnie dla $d = 3$. Zdanie „model 2 opisuje prawdziwe równanie” jest założeniem `[założenie]`.

![Lewy panel, 3 wymiary: liczba Reynoldsa rośnie dla θ = 0,70, jest stała dla θ = 0,50 i maleje dla θ = 0,35. Prawy panel, 2 wymiary: liczba Reynoldsa maleje dla każdej z 3 wartości θ.](figures/navier-stokes-reynolds-cascade.png)

Symulacja 10 rozwiązuje prawdziwe równania w 2 wymiarach, czyli w wymiarze, w którym gładkość ma dowód. Enstrofia spada z 2,206 do 1,147, a największa wirowość spada z 6,00 do 4,51. Żadna z 2 wielkości nie rośnie w żadnym kroku `[obliczenie: skrypt]`.

![Animacja: pole wirowości w 2 wymiarach wygładza się, a enstrofia i największa wirowość maleją.](figures/navier-stokes-vorticity-2d.gif)

Przepływ Ricciego jest przepływem grupy renormalizacji modelu sigma w rachunku 1 pętli `[źródło: Friedan 1980]`. Dlatego sfera z problemu Poincarégo i sprzężenie z problemu Yanga–Millsa spełniają równania o jednej postaci.

## Model 3: licz zapytania i bramki (P a NP)

- **Zapytania.** Algorytm poznaje wejście tylko przez pytania o pojedyncze bity. Dla funkcji $\mathrm{OR}_n$ certyfikat odpowiedzi „1” ma 1 bit, a drzewo decyzyjne potrzebuje $n$ zapytań (dowód 5). Istnieje wyrocznia $A$, dla której $P^A = NP^A$, oraz wyrocznia $B$, dla której $P^B \ne NP^B$ `[źródło: Baker, Gill, Solovay 1975]`.
- **Bramki.** Zliczanie obwodów daje dolne ograniczenie liczby bramek (dowód 6). Dla $n = 20$ co najmniej 1 funkcja wymaga co najmniej 30 986 bramek `[obliczenie: skrypt]`. Dla funkcji podanej wzorem dolne ograniczenie wynosi $3{,}1n - o(n)$ bramek `[źródło: Li, Yang 2022]`. Dla $n = 20$ człon $3{,}1n$ wynosi 62 bramki.

![Sześcian 8 wejść o 3 bitach: 1 bit równy 1 ustala wartość OR na całej ścianie, a wartość 0 wymaga 3 zapytań.](figures/p-vs-np-cube.png)

![Lewy panel: funkcja OR wymaga n zapytań, a certyfikat odpowiedzi 1 ma 1 bit. Prawy panel: ograniczenie ze zliczania rośnie wykładniczo, a ograniczenie dla funkcji podanej wzorem rośnie liniowo.](figures/p-vs-np-queries-and-gates.png)

Symulacja 12 przeszukuje losowe formuły 3-SAT metodą nawrotów. Mediana liczby węzłów rośnie od 6 dla $n = 10$ do 87 dla $n = 40$. Nachylenie wynosi 0,118 bitu na zmienną, czyli liczba węzłów podwaja się co 8,4 zmiennej `[obliczenie: skrypt]`.

![Mediana liczby węzłów przeszukiwania dla losowych formuł 3-SAT leży na prostej w skali logarytmicznej.](figures/p-vs-np-sat-search.png)

## 7 propozycji

1. **Riemann (model 1).** Propozycja zakłada, że hipoteza jest prawdziwa `[założenie]`. Brakujący krok: zbuduj dla pierścienia liczb całkowitych odpowiednik powierzchni $E \times E$ z formą przecięcia i z odpowiednikiem krzywej $G$. Zdanie równoważne: forma Weila jest nieujemna `[źródło: Weil 1952]`. Pierwszy krok roboczy: udowodnij nieujemność formy Weila dla funkcji próbnych, których nośnik dopuszcza wkład dokładnie 1 liczby pierwszej `[założenie]`. Connes i Consani badają przypadek samego miejsca archimedesowego i podają konceptualne źródło dodatniości `[źródło: Connes, Consani 2021]`.
2. **BSD (model 1).** Propozycja zakłada, że hipoteza jest prawdziwa `[założenie]`. Nad ciałem funkcyjnym hipoteza BSD jest równoważna skończoności grupy Tate'a–Szafarewicza `[źródło: Tate 1966; Kato, Trihan 2003]`. Nad ciałem $\mathbb{Q}$ równość rangi i krotności zera ma dowód dla krzywych z zerem o krotności co najwyżej 1 `[źródło: Gross, Zagier 1986; Koływagin 1990; Wiles, opis problemu]`. Dowód używa też twierdzenia o modularności. Wzór na współczynnik wiodący nie ma pełnego dowodu. Brakujący krok: skończoność grupy Tate'a–Szafarewicza dla krzywych o randze co najmniej 2. Pierwszy krok roboczy: udowodnij skończoność całej grupy dla krzywej 389a1.
3. **Hodge (model 1).** Propozycja zakłada, że hipoteza jest prawdziwa `[założenie]`. Dowód dla klas typu $(1,1)$ używa ciągu wykładniczego snopów (dowód 2). Brakujący krok: konstrukcja podrozmaitości dla klasy typu $(k,k)$ przy $k \ge 2$, bo ciąg wykładniczy nie ma odpowiednika dla $k \ge 2$. Dowód MUSI używać współczynników wymiernych, bo wersja całkowita jest fałszywa `[źródło: Atiyah, Hirzebruch 1962]`. Dowód MUSI używać rzutowości: na rozmaitości Kählera klasy Cherna snopów koherentnych nie dają każdej klasy Hodge'a `[źródło: Voisin 2002]`. Pierwszy krok roboczy: rozmaitości abelowe wymiaru 6 `[założenie]`. Dla wymiaru co najwyżej 5 hipoteza wynika z preprintów bez potwierdzonej recenzji `[źródło: Markman 2025a, 2025b]`.
4. **Yang–Mills (model 2).** Istnienie teorii ma ogłoszony dowód z 2026-10-26, więc raport nie dodaje propozycji dla istnienia. Na kracie przy silnym sprzężeniu luka masowa ma dowód `[założenie: Osterwalder, Seiler 1978, twierdzenie niesprawdzone w pracy]`. Brakujący krok: dolne ograniczenie odstępu $E_1 - E_0$, które pozostaje dodatnie, gdy bok pudła $L$ rośnie do nieskończoności. Metoda dowodu MUSI odróżniać grupę $SU(2)$ od grupy $U(1)$. Teoria $U(1)$ na kracie w 4 wymiarach ma fazę bez uwięzienia `[źródło: Guth 1980]`. Abelowe teorie z cechowaniem mają fazy bezmasowe `[źródło: Fröhlich, Spencer 1982]`. Pierwszy krok roboczy: luka masowa w modelu $O(3)$ w 2 wymiarach przy każdej wartości sprzężenia `[założenie]`.
5. **Navier–Stokes (model 2).** Warianty (C) i (D) mają ogłoszony dowód z 2026-09-08, więc raport nie dodaje propozycji dla wariantów z siłą. W modelu 2 siła zewnętrzna dostarcza energię wirowi $n + 1$, więc ograniczenie $\theta \le 1$ przestaje obowiązywać `[założenie]`. Brakujący krok dla ruchu bez siły: wyznacz kres górny ułamka $\theta$ dla prawdziwego równania. Jeżeli kres górny $\theta$ jest większy niż $1/\lambda$ na każdej skali, to model 2 daje osobliwość `[założenie]`. Jeżeli kres górny $\theta$ wynosi co najwyżej $1/\lambda$, to model 2 daje gładkość `[założenie]`. Równanie uśrednione ma tę samą tożsamość energii i ma osobliwość `[źródło: Tao 2016]`. Dowód gładkości MUSI więc użyć własności, której równanie uśrednione nie ma. Jeżeli rozwiązanie ma osobliwość w chwili $T^{\ast}$, to $\limsup_{t \to T^{\ast}} \lVert u(t)\rVert_{L^3} = \infty$ `[źródło: Escauriaza, Seregin, Šverák 2003]`. W modelu 2 norma $L^3$ jest proporcjonalna do $\mathrm{Re}_n$ `[założenie]`.
6. **P a NP (model 3).** Propozycja zakłada odpowiedź $P \ne NP$ `[założenie]`. Brakujący krok: dolne ograniczenie liczby bramek dla funkcji z klasy NP, które przewyższa każdy wielomian zmiennej $n$. Dowód MUSI ominąć 3 bariery: relatywizację, dowody naturalne i algebraizację `[źródło: Baker, Gill, Solovay 1975; Razborow, Rudich 1997; Aaronson, Wigderson 2009]`. Model zapytań pokazuje barierę relatywizacji: dowód, który działa w modelu zapytań, zostawia problem otwarty. Algorytm sprawdzania spełnialności, który wykonuje mniej kroków niż przegląd zupełny, daje dolne ograniczenie `[źródło: Williams 2011]`. Droga Williamsa omija relatywizację i algebraizację. Według Williamsa droga omija barierę dowodów naturalnych tylko intuicyjnie. Pierwszy krok roboczy: taki algorytm dla obwodów progowych o głębokości 3 `[założenie]`.
7. **Poincaré (model 2).** Dowód istnieje. Każda zamknięta jednospójna rozmaitość wymiaru 3 kończy przepływ Ricciego z chirurgią w skończonym czasie, tak jak okrągła sfera z modelu 2 `[źródło: Perelman 2003b]`. Narzędzie dowodu: entropia $\mathcal{W}$, która nie maleje wzdłuż przepływu ze sprzężonym równaniem ciepła `[źródło: Perelman 2002]`. Entropia $\mathcal{W}$ zachowuje wartość przy jednoczesnym skalowaniu metryki i parametru $\tau$. Propozycjom 4 i 5 brakuje wielkości o tych 2 własnościach `[założenie]`.

## Propozycje uzupełnienia brakujących kroków

Autor nie udowodnił żadnego brakującego kroku. Każdy wiersz podaje krok w postaci z 1 wzorem, twierdzenie warunkowe i przypadek, od którego autor proponuje zacząć.

| Problem | Brakujący krok w postaci z 1 wzorem | Twierdzenie warunkowe | Przypadek na początek |
|---|---|---|---|
| Riemann | $\sigma(n) \le H_n + e^{H_n} \ln H_n$ dla każdego $n \ge 1$. | Krok jest równoważny hipotezie `[źródło: Lagarias 2002]`. | Nieujemność formy Weila dla nośnika z wkładem dokładnie 1 liczby pierwszej `[założenie]`. |
| BSD | Grupa Tate'a–Szafarewicza krzywej o randze co najmniej 2 jest skończona. | Nad ciałem funkcyjnym krok jest równoważny hipotezie `[źródło: Kato, Trihan 2003]`. Autor nie zna takiego twierdzenia nad ciałem $\mathbb{Q}$. | Krzywa 389a1: równość rangi i krotności zera ma dowód, a skończoność całej grupy nie ma dowodu `[źródło: LMFDB]`. |
| Hodge | Każda wymierna klasa typu $(2,2)$ na rozmaitości rzutowej wymiaru 4 jest klasą cyklu. | Dla wymiaru co najwyżej 3 hipoteza wynika z dowodu 2 `[źródło: sieć]`. | Rozmaitości abelowe wymiaru 6 `[założenie]`. |
| Yang–Mills | $\inf_L \left(E_1(L) - E_0(L)\right) \gt 0$. | Dla przekroju z 2 zmiennymi dowód 4 daje widmo dyskretne i $E_0 \ge 1{,}0188$. | Model $O(3)$ w 2 wymiarach. Preprint z 2026 r. bez recenzji sprawdza lukę komputerowo w 8 punktach sprzężenia `[źródło: Research Square]`. |
| Navier–Stokes | $\sup_{t \lt T} \lVert u(t)\rVert_{L^3} \lt \infty$ dla każdego gładkiego rozwiązania bez siły. | Krok daje gładkość `[źródło: Escauriaza, Seregin, Šverák 2003]`. | Model diadyczny: rozwiązania dodatnie są gładkie dla $\beta \in (2, 5/2]$ `[źródło: Barbato, Morandin, Romito 2011]`. |
| P a NP | Zadanie spełnialności nie ma obwodów o wielomianowej liczbie bramek. | Krok daje $P \ne NP$ (dowód 12). | Dolne ograniczenie większe niż $3{,}1n - o(n)$ dla funkcji podanej wzorem `[założenie]`. |
| Poincaré | Brak. Dowód istnieje. | Nie dotyczy. | Nie dotyczy. |

Każda propozycja uzupełnienia ma 3 kroki w tej kolejności:

1. Udowodnij krok w przypadku z kolumny „Przypadek na początek”.
2. Zapisz dowód w systemie, który sprawdza dowody, i porównaj tezę formalną z tezą słowną.
3. Uogólnij dowód na pełny brakujący krok albo wskaż własność, która blokuje uogólnienie.

## Algorytm

Algorytm 2 wątków przyjmuje tezę $T$ oraz teorię z programem, który sprawdza dowody. Zacznij od $k = 1$. Wykonaj każdy krok w tej kolejności:

1. Wątek dowodów: sprawdź każdy tekst o długości $k$ znaków.
2. Jeżeli tekst jest dowodem tezy $T$, to zakończ pracę z wynikiem „teza $T$ ma dowód”.
3. Jeżeli tekst jest dowodem zaprzeczenia tezy $T$, to zakończ pracę z wynikiem „teza $T$ jest fałszywa”.
4. Wątek kontrprzykładów: sprawdź kandydata numer $k$.
5. Jeżeli kandydat narusza tezę $T$, to zakończ pracę z wynikiem „teza $T$ jest fałszywa”.
6. Zwiększ $k$ o 1 i wróć do kroku 1.

![Schemat algorytmu 2 wątków: start, wątek dowodów, 2 pytania o dowód, wątek kontrprzykładów, pytanie o kandydata, 2 wyniki i pętla ze zwiększeniem k o 1.](figures/algorithm-two-threads.png)

Algorytm ma 4 własności:

- Jeżeli teoria rozstrzyga tezę $T$, to algorytm kończy pracę (dowód 7).
- Jeżeli teza $T$ jest fałszywym zdaniem klasy $\Pi_1$, to wątek kontrprzykładów kończy pracę (dowód 8).
- Jeżeli teoria nie rozstrzyga zdania klasy $\Pi_1$, to zdanie jest prawdziwe (dowód 9).
- Jeżeli teoria nie rozstrzyga tezy $T$ i teza $T$ nie ma kontrprzykładu, to algorytm pracuje bez końca. Żaden algorytm nie rozpoznaje takiego przypadku w skończonym czasie (dowód 10).

Wniosek: algorytm stwierdza brak rozwiązania tylko przez obalenie tezy. Brak rozstrzygnięcia w teorii zostaje poza zasięgiem każdego algorytmu. Wątek dowodów ma koszt wykładniczy: liczba tekstów o długości $k$ wynosi $c^k$, gdzie $c$ oznacza liczbę znaków alfabetu.

| Problem | Postać tezy | Wątek kontrprzykładów |
|---|---|---|
| Riemann | Zdanie klasy $\Pi_1$: $\sigma(n) \le H_n + e^{H_n} \ln H_n$ dla każdego $n \ge 1$ `[źródło: Lagarias 2002]`. | Kandydat numer $k$ jest liczbą $n = k$. Sprawdzian 8: 0 naruszeń dla $n$ od 2 do 1 000 000. |
| BSD | Dla 1 krzywej zdanie „ranga $\ge r$” ma świadectwo skończone: $r$ punktów niezależnych `[założenie]`. | Wątek punktów ogranicza rangę od dołu. Autor nie zna listy kandydatów dla pełnej hipotezy. |
| Hodge | Autor nie zna postaci klasy $\Pi_1$ `[założenie]`. | Brak. Wyliczanie podrozmaitości potwierdza algebraiczność klasy i nie obala hipotezy. |
| Yang–Mills | Autor nie zna postaci klasy $\Pi_1$ `[założenie]`. | Brak. Obliczenia na kracie dają oszacowanie luki masowej bez dowodu `[założenie]`. |
| Navier–Stokes | Wariant (A) ma kontrprzykład: dane początkowe z osobliwością. | Kandydat jest parą: dane początkowe oraz dowód osobliwości sprawdzony komputerowo `[założenie]`. |
| P a NP | Zdanie $P = NP$ jest zdaniem klasy $\Sigma_2$, a zdanie $P \ne NP$ jest zdaniem klasy $\Pi_2$ `[źródło: Aaronson, „P =? NP”]`. | Brak listy kandydatów. Algorytm przeszukiwania uniwersalnego rozwiązuje w czasie wielomianowym każdą formułę spełnialną wtedy i tylko wtedy, gdy $P = NP$ `[źródło: Levin 1973]`. |
| Poincaré | Twierdzenie. | Rozpoznawanie sfery $S^3$ jest rozstrzygalne `[źródło: Rubinstein 1995]`. |

$\sigma(n)$ oznacza sumę dzielników liczby $n$. $H_n$ oznacza sumę $1 + 1/2 + \dots + 1/n$. Sprawdzian 8 wykonuje wątek kontrprzykładów dla hipotezy Riemanna. Największy iloraz lewej strony do prawej strony wynosi 0,9886 dla $n = 12$ `[obliczenie: skrypt]`. Obliczenia zer funkcji dzeta obejmują część urojoną od 0 do $3 \times 10^{12}$ i nie dały kontrprzykładu `[źródło: Platt, Trudgian 2021]`.

![Największy iloraz w 59 przedziałach liczby n zostaje pod granicą 1. Mediana ilorazu maleje od 0,9 do 0,3. Największy iloraz 0,9886 daje liczba n = 12.](figures/riemann-counterexample-thread.png)

## Sprawdziany

Każdy wiersz tabeli ma znacznik `[obliczenie: skrypt]`. Sprawdziany od 9 do 12 są symulacjami z pliku `simulations.py`.

| Nr | Model | Sprawdzian | Liczby |
|---|---|---|---|
| 1 | 1 | Nierówność $a^2 \lt 4p$ dla 64 728 krzywych nad $F_p$, $p$ od 5 do 97 włącznie | 0 naruszeń; największy iloraz $a^2/(4p)$ = 0,9897 |
| 2 | 1 | Sygnatura formy przecięcia na klasach $H$, $V$, $D$, $G$ dla 589 par $(p, N_p)$ | $(1, 3)$ dla każdej pary |
| 3 | 1 | Liczba wymiernych klas typu $(1,1)$ na $E \times E$ oraz liczba niezależnych klas krzywych | $\tau = i$: 4 oraz 4; $\tau = i \sqrt[3]{2}$: 3 oraz 3 |
| 4 | 1 | Nachylenie $\ln \prod (N_p/p)$ względem $\ln \ln X$, $X$ od 100 do 100 000 włącznie | ranga 0: 0,00; ranga 1: 1,07; ranga 2: 2,05; ranga 3: 2,77 |
| 5 | 2 | Poziomy hamiltonianu $-\Delta + x^2y^2$ w 3 bazach: 12 × 12, 16 × 16, 20 × 20 | $E_0$ = 1,10822 w każdej bazie; $E_1$ = 2,37864; $E_1 - E_0$ = 1,27041; granica dolna dla $E_0$: 1,0188 |
| 6 | 3 | Funkcja $\mathrm{OR}_n$, $n$ od 1 do 8 włącznie | $n$ zapytań; certyfikat odpowiedzi „1” ma 1 bit |
| 7 | 3 | Zliczanie obwodów dla $n = 20$ | 30 986 bramek; człon $3{,}1n$: 62 bramki |
| 8 | algorytm | Nierówność Lagariasa dla $n$ od 2 do 1 000 000 włącznie | 0 naruszeń; największy iloraz 0,9886 dla $n = 12$ |
| 9 | 2 | Przepływ skracający krzywą: pole względem prostej $A_0 - 2\pi t$ | odchylenie 0,83 % pola początkowego; iloraz izoperymetryczny z 1,732 do 1,0008 |
| 10 | 2 | Równania Naviera–Stokesa w 2 wymiarach, siatka 64 × 64 | enstrofia z 2,206 do 1,147; największa wirowość z 6,00 do 4,51; 0 kroków ze wzrostem |
| 11 | 2 | 32 orbity klasyczne w potencjale $x^2y^2$ o energii $E_0$ | 32 orbity poza kwadratem o boku 6; masa kwantowa poza kwadratem: 0,28 % |
| 12 | 3 | Przeszukiwanie z nawrotami, 25 losowych formuł 3-SAT na rozmiar | mediana węzłów od 6 do 87; nachylenie 0,118 bitu na zmienną |
| 13 | 1 | Zera funkcji $\zeta$ na prostej $\sigma = 1/2$ dla $t \lt 40$ | 6 zer; pierwsze zero $t$ = 14,135; najmniejsza wartość $\lvert\zeta\rvert$ na prostych $\sigma = 0{,}25$ i $\sigma = 0{,}75$: 0,179 |
| 14 | 1 | Rozkład 9 590 wartości $a/(2\sqrt{p})$ krzywej 37a1 | różnica dystrybuant względem rozkładu półokręgu: 0,0066 |

Sprawdzian 4 używa 4 krzywych: 11a3, 37a1, 389a1, 5077a1. Hipoteza BSD przewiduje nachylenie równe randze. Wzrost iloczynu jak $(\ln X)^r$ jest hipotezą, która implikuje hipotezę Riemanna dla funkcji $L(E, s)$ `[źródło: Goldfeld 1982; Kuo, Murty 2005]`. Sprawdziany 1 i 2 są równoważne: sygnatura $(1, 3)$ zachodzi wtedy i tylko wtedy, gdy $a^2 \lt 4p$. Wartość $E_0$ = 1,10822 zgadza się z wartością $1{,}10822315759$ z literatury `[źródło: Fernández, García 2014]`.

## Rysunki interaktywne

Plik [docs/index.html](docs/index.html) zawiera 14 rysunków interaktywnych z biblioteki plotly. Wskazanie znaku na rysunku pokazuje liczby. 5 rysunków w 3 wymiarach obraca się myszą, a 2 rysunki mają suwak czasu. Strona pobiera biblioteki plotly.js i MathJax z sieci. Rysunki z katalogu `figures` powstają w bibliotekach matplotlib i seaborn.

## Uproszczenia

Każdy czas w tabeli ma znacznik `[pomiar: time.perf_counter, 2026-11-13, laptop autora z 8 wątkami procesora]`.

| Nr | Element | Przed | Po | Skutek dla liczb |
|---|---|---|---|---|
| 1 | Sprawdzian 5: rozmiar baz | bazy 20, 35, 50; 15,2 s | bazy 12, 16, 20; 0,3 s | $E_0$ i $E_1$ bez zmian w 5 cyfrach |
| 2 | Sprawdzian 4: pętla po liczbach pierwszych | 1 proces; 54 s | 8 procesów; 11 s | każda suma bez zmian |
| 3 | Sprawdziany od 1 do 8 | 68 s | 16 s | 3 nowe liczby |
| 4 | Dowód widma dyskretnego hamiltonianu $-\Delta + x^2y^2$ | odsyłacz do pracy | 4 wiersze (dowód 4) i asercja $E_0 \ge 1{,}0188$ | nowa liczba 1,0188 |
| 5 | Postać hipotezy Riemanna | zdanie o zerach funkcji dzeta | 1 nierówność dla liczb naturalnych (sprawdzian 8) | nowa liczba 0,9886 |
| 6 | Dowody w raporcie | 1 dowód w tekście | 12 dowodów na początku, każdy ma co najwyżej 4 wiersze | brak |
| 7 | Wzór dla $\mathrm{Re}_n$ | rachunek bez dowodu | dowód 11 w modelu; założeniem zostaje związek modelu z równaniem | brak |

3 elementy zostają bez uproszczenia:

- Liczba modeli wynosi 3. Autor nie znalazł układu z 2 modelami, który zachowuje twierdzenie w modelu dla każdego problemu.
- Sprawdzian 4 zachowuje zakres $X$ = 100 000. Zakres $X$ mniejszy niż 100 000 zmienia nachylenia.
- Wątek dowodów zachowuje koszt wykładniczy. Autor nie zna algorytmu ogólnego o koszcie wielomianowym `[założenie]`.

## Zastosowania

Każdy punkt jest propozycją zastosowania, bez wdrożenia.

1. Kryptografia krzywych eliptycznych: dobór krzywej wymaga liczby punktów $N$ i granicy $a^2 \le 4p$. Sprawdzian 1 liczy obie wielkości `[założenie]`.
2. Kryptografia z kluczem publicznym zakłada zdanie $P \ne NP$ `[założenie]`. Model zapytań pokazuje metody dowodu, które nie rozstrzygają zdania $P \ne NP$.
3. Nauczanie: 1 problem dostaje co najmniej 2 rysunki i 1 dowód z co najwyżej 4 wierszy.
4. Test regresji bibliotek liczbowych: skrypt `models_check.py` porównuje 23 liczby z raportem i kończy pracę błędem przy różnicy.
5. Symulacje przepływów: liczba $\mathrm{Re}_n$ wskazuje skalę, na której siatka obliczeniowa wymaga zagęszczenia `[założenie]`.
6. Metody wariacyjne w fizyce: hamiltonian $-\Delta + x^2y^2$ daje poziom $E_0$ z 5 cyframi oraz granicę dolną do porównań `[obliczenie: skrypt]`.
7. Sprawdzanie dowodów: wątek dowodów jest programem, który sprawdza dowody. Formalizacje z 2026 r. używają systemu Lean `[źródło: sieć]`.

## Problematyka

1. Sprawdzian obejmuje skończoną liczbę przypadków. Sprawdzian nie jest dowodem. Symulacja przybliża ruch z błędem kroku czasu.
2. Autor nie udowodnił żadnego brakującego kroku. Sekcja „Propozycje uzupełnienia brakujących kroków” podaje plany.
3. Algorytm 2 wątków nie rozpoznaje braku rozstrzygnięcia w teorii (dowód 10).
4. Wątek dowodów ma koszt wykładniczy, więc algorytm 2 wątków nie nadaje się do praktycznego szukania dowodów.
5. 5 z 7 problemów nie ma listy kandydatów: BSD, Hodge, Yang–Mills, P a NP, Poincaré. Hipoteza Poincarégo ma dowód, więc lista jest zbędna.
6. Sprawdzian 8 jest słabym sprawdzianem. Obliczenia zer funkcji dzeta wykluczają kontrprzykład w zakresie, którego sprawdzian 8 nie osiąga `[źródło: Platt, Trudgian 2021]`.
7. Sprawdzian 4 nie potwierdza rangi 3 z dokładnością lepszą niż 0,23. Iloczyn zbiega logarytmicznie.
8. Dla hipotezy BSD model 1 dowodzi tylko nierówności nad ciałem funkcyjnym. Model 1 spełnia definicję modelu ze słownika dla BSD częściowo.
9. Związek modelu 2 z prawdziwym równaniem Naviera–Stokesa jest założeniem. Symulacja 10 dotyczy 2 wymiarów, a problem milenijny dotyczy 3 wymiarów.
10. Hamiltonian $-\Delta + x^2y^2$ jest przekrojem z 2 zmiennymi. Przeniesienie odstępu $E_1 - E_0$ na teorię pola nie ma dowodu.
11. Sprawdzenie odsyłaczy z 2026-11-13 objęło tekst 4 prac i abstrakty 5 prac. 26 twierdzeń ma potwierdzenie tylko w źródle wtórnym, a 4 twierdzenia nie mają potwierdzenia.
12. Sprawdzenie wykazało 1 błędne przypisanie: dowód przez ciąg wykładniczy nie pochodzi z pracy Lefschetza. Raport ma poprawkę w dowodzie 2.
13. Sprawdzenie otworzyło 8 z 10 stron z sekcji „Źródła z sieci”. Raport zna stronę OpenAI i pracę arXiv:2610.08144 tylko ze źródeł wtórnych.
14. Formalizacja dowodu w systemie Lean nie gwarantuje zgodności z tezą słowną. Praca z 2026-10-06 zarzuca taką niezgodność 1 formalizacji `[źródło: sieć]`.
15. Rysunek torusa pokazuje przekrój rzeczywisty modelu 1. Powierzchnia $E \times E$ ma 4 wymiary rzeczywiste i nie ma rysunku.
16. Rysunki 3 wymiarów na stronie interaktywnej wymagają przeglądarki z WebGL.

## Dyskusja

Autor proponuje 6 pytań do dyskusji:

1. Czy liczba 3 jest najmniejszą liczbą modeli? Kontrpropozycja: 2 modele, jeżeli problem P a NP dostanie model w geometrii algebraicznej, np. permanent a wyznacznik `[założenie]`.
2. Czy dowód wariantu (C) z siłą zewnętrzną zamyka problem Naviera–Stokesa, skoro pytanie o ruch bez siły zostaje otwarte?
3. Czy dowód, który znalazł program i który sprawdził system Lean, rozwiązuje problem bez zrozumienia dowodu przez człowieka?
4. Czy ułamek $\theta$ ma definicję dla prawdziwego równania, przy której model 2 opisuje równanie?
5. Czy hipoteza Hodge'a albo luka masowa ma postać równoważną klasy $\Pi_1$, czyli postać z listą kandydatów?
6. Która wielkość pełni dla Yanga–Millsa i dla Naviera–Stokesa rolę entropii $\mathcal{W}$ z dowodu hipotezy Poincarégo?

## Jak powtórzyć obliczenia

Wykonaj każdy krok w tej kolejności:

1. Utwórz środowisko: `python3 -m venv .venv`.
2. Zainstaluj biblioteki: `.venv/bin/pip install -r requirements.txt`.
3. Uruchom sprawdziany: `.venv/bin/python models_check.py`. Wynik: skrypt wypisuje wiersz `all checks passed`.
4. Narysuj rysunki: `.venv/bin/python figures.py`. Wynik: katalog `figures` zawiera 14 plików PNG z tego skryptu.
5. Narysuj animacje: `.venv/bin/python animations.py`. Wynik: katalog `figures` zawiera 3 pliki GIF i 1 plik PNG z tego skryptu.
6. Zbuduj stronę interaktywną: `.venv/bin/python interactive.py`. Wynik: plik `docs/index.html`.

Skrypt `models_check.py` porównuje 23 liczby z raportu z obliczeniem. Jeżeli raport podaje inną liczbę niż obliczenie, to skrypt kończy pracę błędem.

Czasy pracy 4 skryptów: `models_check.py` 23 s, `figures.py` 27 s, `animations.py` 66 s, `interactive.py` 24 s `[pomiar: 1 przebieg, 2026-11-13, laptop autora z 8 wątkami procesora]`.

## Decyzje i braki

| Nr | Fragment | Reguła | Znaczenia lub brak | Wybór |
|---|---|---|---|---|
| 1 | „propozycja” | A4 | 2 znaczenia: dowód; plan dowodu. | Plan dowodu. Autor nie zna dowodu żadnego problemu otwartego. |
| 2 | liczba modeli | A5 | Brak kryterium dla najmniejszej liczby modeli. | 3 modele. Autor nie znalazł układu z 2 modelami, który zachowuje twierdzenie w modelu dla każdego problemu. |
| 3 | „problemy milenijne” | A2 | 2 znaczenia: 6 problemów otwartych; 7 problemów z listy CMI. | 7 problemów. Dowód hipotezy Poincarégo służy za wzorzec. |
| 4 | pochodzenie modeli | A4 | 2 znaczenia: modele nowe; modele dobrane z literatury. | Modele dobrane z literatury i złożone w 1 układ. |
| 5 | terminy matematyczne | A4 | Raport nie definiuje terminów matematycznych. | Odstępstwo od reguły A4. Każdy termin ma znaczenie z pracy wskazanej znacznikiem. |
| 6 | znaczniki źródła i wzory | B8, E5 | Licznik słów pomija znaczniki i wzory. Wzór stoi w zdaniu albo w osobnym wierszu. | Limit 25 słów dotyczy zdania bez znacznika i bez wzoru. Wzory mają zapis LaTeX. Tekst zastępczy rysunku nie wyświetla zapisu LaTeX, więc tekst zastępczy używa znaków Unicode. |
| 7 | kolejność sekcji | A4 | Sekcja „Najkrótsze dowody” stoi przed definicjami oznaczeń. | Odstępstwo od reguły A4. Streszczenie i dowody stoją na początku, a dowody odsyłają do sekcji z definicjami. |
| 8 | „brak rozwiązania” | A4 | 2 znaczenia: teza jest fałszywa; teoria nie rozstrzyga tezy. | Algorytm stwierdza tylko fałszywość tezy. Dowód 10 wyklucza algorytm dla drugiego znaczenia. |
| 9 | „uzupełnienie brakującego kroku” | A4 | 2 znaczenia: dowód kroku; plan dowodu kroku. | Plan dowodu kroku. Autor nie zna dowodu żadnego brakującego kroku. |

Raport stosuje reguły standardu Polszczyzna Kontrolowana (PK) 0.1. Kolumna „Reguła” podaje numer reguły PK.

## Bibliografia

Plik [references-check.md](references-check.md) podaje dla pozycji z 2026-11-13 strony, DOI i stan sprawdzenia. Sprawdzenie nie objęło pozycji oznaczonych słowem „nowa”.

- Aaronson, S. P =? NP. Przegląd, plik PDF na stronie autora (nowa).
- Aaronson, S., Wigderson, A. (2009). Algebrization: a new barrier in complexity theory. ACM Transactions on Computation Theory 1.
- Atiyah, M., Hirzebruch, F. (1962). Analytic cycles on complex manifolds. Topology 1.
- Baker, T., Gill, J., Solovay, R. (1975). Relativizations of the P =? NP question. SIAM Journal on Computing 4.
- Barbato, D., Morandin, F., Romito, M. (2011). Smooth solutions for the dyadic model. Nonlinearity 24 (nowa).
- Birch, B., Swinnerton-Dyer, H. P. F. (1965). Notes on elliptic curves. II. Journal für die reine und angewandte Mathematik 218.
- Buhrman, H., de Wolf, R. (2002). Complexity measures and decision tree complexity: a survey. Theoretical Computer Science 288 (nowa).
- Connes, A., Consani, C. (2021). Weil positivity and trace formula, the archimedean place. Selecta Mathematica 27.
- Escauriaza, L., Seregin, G., Šverák, V. (2003). $L_{3,\infty}$-solutions of the Navier–Stokes equations and backward uniqueness. Russian Mathematical Surveys 58.
- Fefferman, C. Existence and smoothness of the Navier–Stokes equation. Opis problemu, Clay Mathematics Institute.
- Fernández, F., García, J. (2014). Eigenvalues and eigenfunctions of the anharmonic oscillator $V(x,y) = x^2y^2$. Open Physics 12 (nowa).
- Friedan, D. (1980). Nonlinear models in 2 + ε dimensions. Physical Review Letters 45.
- Fröhlich, J., Spencer, T. (1982). Massless phases and symmetry restoration in abelian gauge theories and spin systems. Communications in Mathematical Physics 83.
- Gage, M., Hamilton, R. (1986). The heat equation shrinking convex plane curves. Journal of Differential Geometry 23 (nowa).
- Goldfeld, D. (1982). Sur les produits partiels eulériens attachés aux courbes elliptiques. Comptes Rendus de l'Académie des Sciences 294 (nowa).
- Grayson, M. (1987). The heat equation shrinks embedded plane curves to round points. Journal of Differential Geometry 26 (nowa).
- Griffiths, P., Harris, J. (1994). Principles of algebraic geometry. Wiley (nowa).
- Gross, B., Zagier, D. (1986). Heegner points and derivatives of L-series. Inventiones Mathematicae 84.
- Gross, D., Wilczek, F. (1973). Ultraviolet behavior of non-abelian gauge theories. Physical Review Letters 30.
- Grothendieck, A. (1958). Sur une note de Mattuck–Tate. Journal für die reine und angewandte Mathematik 200.
- Guth, A. (1980). Existence proof of a nonconfining phase in four-dimensional U(1) lattice gauge theory. Physical Review D 21.
- Hasse, H. (1933). Beweis des Analogons der Riemannschen Vermutung für die Artinschen und F. K. Schmidtschen Kongruenzzetafunktionen in gewissen elliptischen Fällen. Vorläufige Mitteilung. Nachrichten der Gesellschaft der Wissenschaften zu Göttingen.
- Hasse, H. (1936). Zur Theorie der abstrakten elliptischen Funktionenkörper III. Journal für die reine und angewandte Mathematik 175 (nowa).
- Kato, K., Trihan, F. (2003). On the conjectures of Birch and Swinnerton-Dyer in characteristic p > 0. Inventiones Mathematicae 153.
- Koływagin, W. (Kolyvagin, V.) (1990). Euler systems. The Grothendieck Festschrift, tom II.
- Kuo, W., Murty, M. R. (2005). On a conjecture of Birch and Swinnerton-Dyer. Canadian Journal of Mathematics 57 (nowa).
- Lagarias, J. (2002). An elementary problem equivalent to the Riemann hypothesis. American Mathematical Monthly 109.
- Lefschetz, S. (1924). L'analysis situs et la géométrie algébrique. Gauthier-Villars.
- Levin, L. (1973). Universal sequential search problems. Problemy Peredachi Informatsii 9.
- Li, J., Yang, T. (2022). 3.1n − o(n) circuit lower bounds for explicit functions. STOC 2022.
- LMFDB. Krzywa eliptyczna 389.a1, baza danych lmfdb.org (nowa).
- Lüscher, M. (1983). Some analytic results concerning the mass spectrum of Yang–Mills gauge theories on a torus. Nuclear Physics B 219.
- Ładyżenska, O. (Ladyzhenskaya, O. A.) (1959). Solution “in the large” of the nonstationary boundary value problem for the Navier–Stokes system with two space variables. Communications on Pure and Applied Mathematics 12.
- Markman, E. (2025a). Cycles on abelian 2n-folds of Weil type from secant sheaves on abelian n-folds. arXiv:2502.03415 (nowa).
- Markman, E. (2025b). Secant sheaves and Weil classes on abelian varieties. arXiv:2509.23403.
- Mattuck, A., Tate, J. (1958). On the inequality of Castelnuovo–Severi. Abhandlungen aus dem Mathematischen Seminar der Universität Hamburg 22.
- NIST Digital Library of Mathematical Functions (DLMF), §9.9: zera funkcji Airy'ego (nowa).
- Osterwalder, K., Seiler, E. (1978). Gauge field theories on a lattice. Annals of Physics 110.
- Perelman, G. (2002). The entropy formula for the Ricci flow and its geometric applications. arXiv:math/0211159.
- Perelman, G. (2003a). Ricci flow with surgery on three-manifolds. arXiv:math/0303109.
- Perelman, G. (2003b). Finite extinction time for the solutions to the Ricci flow on certain three-manifolds. arXiv:math/0307245.
- Platt, D., Trudgian, T. (2021). The Riemann hypothesis is true up to $3 \times 10^{12}$. Bulletin of the London Mathematical Society 53.
- Politzer, H. D. (1973). Reliable perturbative results for strong interactions? Physical Review Letters 30.
- Razborow, A. (Razborov, A.), Rudich, S. (1997). Natural proofs. Journal of Computer and System Sciences 55.
- Research Square. Preprint rs-11440706/v1 o luce masowej w modelu O(3), 2026 (nowa).
- Rubinstein, J. H. (1995). An algorithm to recognize the 3-sphere. Proceedings of the International Congress of Mathematicians, Zürich 1994, tom 1, s. 601–611. Birkhäuser.
- Shannon, C. (1949). The synthesis of two-terminal switching circuits. Bell System Technical Journal 28.
- Simon, B. (1983). Some quantum operators with discrete spectrum but classically continuous spectrum. Annals of Physics 146.
- Tao, T. (2016). Finite time blowup for an averaged three-dimensional Navier–Stokes equation. Journal of the American Mathematical Society 29.
- Tate, J. (1966). On the conjectures of Birch and Swinnerton-Dyer and a geometric analog. Séminaire Bourbaki 306.
- Turing, A. (1936). On computable numbers, with an application to the Entscheidungsproblem. Proceedings of the London Mathematical Society 42. Turing dowodzi nierozstrzygalności dla maszyn „circle-free”.
- Voisin, C. (2002). A counterexample to the Hodge conjecture extended to Kähler varieties. International Mathematics Research Notices.
- Weil, A. (1952). Sur les « formules explicites » de la théorie des nombres premiers. Communications du Séminaire Mathématique de l'Université de Lund.
- Wiles, A. The Birch and Swinnerton-Dyer conjecture. Opis problemu, Clay Mathematics Institute (nowa).
- Williams, R. (2011). Non-uniform ACC circuit lower bounds. IEEE Conference on Computational Complexity 2011.

## Źródła z sieci

Sekcja zawiera 10 stron. Sprawdzenie z 2026-11-13 otworzyło 8 stron. Strona OpenAI wymaga JavaScriptu, więc raport cytuje stronę OpenAI za 2 innymi serwisami. Sprawdzenie nie otworzyło strony arXiv:2610.08144: raport zna tę pracę z przypisu Wikipedii.

- [Millennium Prize Problems (Wikipedia)](https://en.wikipedia.org/wiki/Millennium_Prize_Problems)
- [Millennium Problems (Clay Mathematics Institute)](https://www.claymath.org/millennium-problems/)
- [On the Navier–Stokes Millennium Prize Problem (OpenAI)](https://openai.com/index/navier-stokes-solution/)
- [Navier–Stokes priority controversy (Wikipedia)](https://en.wikipedia.org/wiki/Navier%E2%80%93Stokes_priority_controversy)
- [Z. Lei, X. Ren, 2026-09-28: Finite-Time Blowup for Navier-Stokes with Smooth Forcing, Part I (arXiv:2609.35406)](https://arxiv.org/abs/2609.35406)
- [Praca z 2026-10-06 o zgodności formalizacji w Lean z dowodem słownym (arXiv:2610.08144)](https://arxiv.org/abs/2610.08144)
- [Scientists confirm OpenAI's blockbuster quantum physics result (Scientific American)](https://www.scientificamerican.com/article/openais-shepherds-affirm-blockbuster-physics-result/)
- [Yang–Mills existence and mass gap (Wikipedia)](https://en.wikipedia.org/wiki/Yang%E2%80%93Mills_existence_and_mass_gap)
- [Hodge conjecture (Wikipedia)](https://en.wikipedia.org/wiki/Hodge_conjecture)
- [Has AI solved a Millennium Prize Problem? (Papex)](https://papex.org/blog/has-ai-solved-a-millennium-prize-problem)

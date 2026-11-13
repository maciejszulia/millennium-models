# Weryfikacja 40 odsyłaczy wykrywa 1 błędne przypisanie

Stan na 2026-11-13. Sprawdzenie objęło 40 pozycji bibliografii pliku `REPORT.md` z commita `44e87c9`. Numery wierszy wskazują wiersze tej wersji pliku. Słowo „notatka” oznacza 1 z 4 plików roboczych sprawdzenia. Repozytorium nie zawiera plików roboczych. Plik `REPORT.md` ma od 2026-11-13 naniesione poprawki z sekcji „Poprawki do pliku REPORT.md”.

## Wynik

Każda z 40 pozycji bibliografii istnieje; 37 pozycji ma poprawne dane, a 3 pozycje mają dane potwierdzone tylko w części. Żadna pozycja nie ma błędnych danych, ale 36 z 40 pozycji nie podaje stron ani DOI. Oceny twierdzeń: „potwierdzone w pracy” ma 9 twierdzeń, „potwierdzone w źródle wtórnym” ma 26 twierdzeń, „niepotwierdzone” ma 4 twierdzenia, „błędne” ma 1 twierdzenie. Błędne jest przypisanie dowodu przez ciąg wykładniczy snopów pracy Lefschetza z 1924 r. Plik `REPORT.md` wymaga 37 poprawek. Sekcja „Źródła z sieci” podaje arXiv:2609.35406, a praca z 2026-10-06 ma numer arXiv:2610.08144.

## Tabela 40 pozycji

Legenda ocen:

- „potwierdzone w pracy”: badacz przeczytał twierdzenie w pełnym tekście albo w abstrakcie pracy.
- „potwierdzone w źródle wtórnym”: inna praca, recenzja albo encyklopedia przypisuje twierdzenie tej pracy. Badacz nie otworzył pracy.
- „niepotwierdzone”: badacz nie znalazł źródła z treścią twierdzenia.
- „błędne”: źródło przeczy przypisaniu z raportu.

Dane są poprawne, gdy autorzy, tytuł, rok, miejsce wydania i tom zgadzają się z Crossref, zbMATH albo arXiv. Słowo „Uzupełnij” wskazuje strony i DOI, których raport nie podaje.

| Nr | Praca | Dane bibliograficzne | Ocena twierdzenia | Źródło potwierdzenia | Uwaga |
|---|---|---|---|---|---|
| 1 | Aaronson, Wigderson 2009 | Częściowo potwierdzone: Crossref podaje tytuł „Algebrization” bez podtytułu. Uzupełnij: ACM Trans. Comput. Theory 1(1), s. 1–54, DOI [10.1145/1490270.1490272](https://doi.org/10.1145/1490270.1490272). | potwierdzone w źródle wtórnym | [Williams, PDF](https://people.csail.mit.edu/rrw/acc-lbs.pdf) | Williams cytuje pracę jako barierę algebraizacji. |
| 2 | Atiyah, Hirzebruch 1962 | Poprawne. Uzupełnij: Topology 1(1), s. 25–45, DOI [10.1016/0040-9383(62)90094-0](https://doi.org/10.1016/0040-9383%2862%2990094-0). | potwierdzone w źródle wtórnym | [nLab](https://ncatlab.org/nlab/show/integral+Hodge+conjecture) | Kontrprzykład dotyczy całkowitej hipotezy Hodge'a: klasy torsyjne nie są algebraiczne. Repozytorium MPIM podaje s. 25–46. |
| 3 | Baker, Gill, Solovay 1975 | Poprawne. Uzupełnij: SIAM J. Comput. 4(4), s. 431–442, DOI [10.1137/0204037](https://doi.org/10.1137/0204037). | potwierdzone w źródle wtórnym | [Williams, PDF](https://people.csail.mit.edu/rrw/acc-lbs.pdf) | Williams cytuje pracę jako barierę relatywizacji. |
| 4 | Birch, Swinnerton-Dyer 1965 | Poprawne. Uzupełnij: s. 79–108, DOI [10.1515/crll.1965.218.79](https://doi.org/10.1515/crll.1965.218.79). | potwierdzone w źródle wtórnym | [Wikipedia, BSD](https://en.wikipedia.org/wiki/Birch_and_Swinnerton-Dyer_conjecture); [Kuo, Murty 2005](https://doi.org/10.4153/CJM-2005-014-0) | Wikipedia podaje dla tej pracy błędny tom 165. |
| 5 | Connes, Consani 2021 | Poprawne. Uzupełnij: Selecta Math. (N.S.) 27(4), artykuł 77, DOI [10.1007/s00029-021-00689-4](https://doi.org/10.1007/s00029-021-00689-4); arXiv:2006.13771. | potwierdzone w pracy | [arXiv:2006.13771](https://arxiv.org/abs/2006.13771) | Ocena opiera się na abstrakcie. Abstrakt mówi o „potential conceptual reason” dodatniości przy parametrze odcięcia równym 1. Zdanie raportu wymaga zawężenia. |
| 6 | Escauriaza, Seregin, Šverák 2003 | Poprawne. Uzupełnij: Russian Math. Surveys 58(2), s. 211–250, DOI [10.1070/RM2003v058n02ABEH000609](https://doi.org/10.1070/RM2003v058n02ABEH000609). | potwierdzone w źródle wtórnym | [Barker, arXiv:1612.04439](https://ar5iv.arxiv.org/html/1612.04439) | Wynik dotyczy rozwiązań w $\mathbb{R}^3$ i granicy górnej $\limsup$ normy $L^3$. |
| 7 | Fefferman 2000 | Częściowo potwierdzone: autor i tytuł są poprawne, rok 2000 jest niepotwierdzony. Plik PDF nie ma DOI. | potwierdzone w pracy | [Fefferman, PDF](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf) | Opis podaje 4 warianty. Warianty (C) i (D) dopuszczają gładką siłę $f$. Metadane PDF podają datę 2006-08-04. |
| 8 | Friedan 1980 | Poprawne. Uzupełnij: Phys. Rev. Lett. 45(13), s. 1057–1060, DOI [10.1103/PhysRevLett.45.1057](https://doi.org/10.1103/PhysRevLett.45.1057). | potwierdzone w źródle wtórnym | [INSPIRE](https://inspirehep.net/literature/155389) | Badacz zna źródło wtórne ze streszczenia wyszukiwarki. Wersja pełna: Annals of Physics 163 (1985), s. 318. |
| 9 | Fröhlich, Spencer 1982 | Poprawne. Uzupełnij: Commun. Math. Phys. 83(3), s. 411–454, DOI [10.1007/BF01213610](https://doi.org/10.1007/BF01213610). | potwierdzone w źródle wtórnym | [Crossref, DOI 10.1007/BF01213610](https://doi.org/10.1007/BF01213610) | Podstawą oceny jest tylko tytuł pracy. Wymiar i grupa są niesprawdzone. |
| 10 | Gross, Zagier 1986 | Poprawne. Uzupełnij: Invent. Math. 84(2), s. 225–320, DOI [10.1007/BF01388809](https://doi.org/10.1007/BF01388809). | potwierdzone w źródle wtórnym | [Wiles, PDF CMI](https://www.claymath.org/wp-content/uploads/2022/05/birchswin.pdf) | Dowód obejmuje równość rangi i krotności zera. Wzór na współczynnik wiodący nie ma pełnego dowodu. |
| 11 | Gross, Wilczek 1973 | Poprawne. Uzupełnij: Phys. Rev. Lett. 30(26), s. 1343–1346, DOI [10.1103/PhysRevLett.30.1343](https://doi.org/10.1103/PhysRevLett.30.1343). | potwierdzone w źródle wtórnym | [Wikipedia, Beta function](https://en.wikipedia.org/wiki/Beta_function_%28physics%29) | Wzór raportu to przypadek czystej teorii Yanga–Millsa bez fermionów. |
| 12 | Grothendieck 1958 | Poprawne. Uzupełnij: s. 208–215, DOI [10.1515/crll.1958.200.208](https://doi.org/10.1515/crll.1958.200.208). | niepotwierdzone | brak; [zbMATH](https://zbmath.org/?q=an:0084.16904) potwierdza tylko tytuł | Badacz nie znalazł recenzji z treścią twierdzenia. |
| 13 | Guth 1980 | Poprawne. Uzupełnij: Phys. Rev. D 21(8), s. 2291–2307, DOI [10.1103/PhysRevD.21.2291](https://doi.org/10.1103/PhysRevD.21.2291). | niepotwierdzone | brak | Tytuł mówi o fazie bez uwięzienia. Tytuł nie mówi o fazie bez luki masowej. |
| 14 | Hasse 1933 | Poprawne. Uzupełnij tytuł o słowa „Vorläufige Mitteilung”, nr 42, s. 253–262. Przedruk: DOI [10.1515/9783110835007.85](https://doi.org/10.1515/9783110835007.85). | potwierdzone w źródle wtórnym | [Roquette, PDF](https://www.mathi.uni-heidelberg.de/~roquette/rv3.pdf) | Nota obejmuje główne przypadki. Pełny dowód zawiera cykl Hassego w J. reine angew. Math. 175 (1936). |
| 15 | Kato, Trihan 2003 | Poprawne. Uzupełnij: Invent. Math. 153(3), s. 537–592, DOI [10.1007/s00222-003-0299-2](https://doi.org/10.1007/s00222-003-0299-2). | potwierdzone w źródle wtórnym | [Wiles, PDF CMI](https://www.claymath.org/wp-content/uploads/2022/05/birchswin.pdf) | Skończoność części $\ell$-pierwotnej grupy Ш dla 1 liczby $\ell$ daje pełną hipotezę BSD nad ciałem funkcyjnym. |
| 16 | Kolyvagin 1990 | Poprawne. Uzupełnij: Progr. Math. 87, Birkhäuser, s. 435–483, DOI [10.1007/978-0-8176-4575-5_11](https://doi.org/10.1007/978-0-8176-4575-5_11). | potwierdzone w źródle wtórnym | [Wiles, PDF CMI](https://www.claymath.org/wp-content/uploads/2022/05/birchswin.pdf) | Zastrzeżenie jak w wierszu 10. Crossref podaje rok 2007, bo rekord dotyczy przedruku. |
| 17 | Lagarias 2002 | Poprawne. Uzupełnij: 109(6), s. 534–543, DOI [10.1080/00029890.2002.11919883](https://doi.org/10.1080/00029890.2002.11919883). | potwierdzone w pracy | [arXiv:math/0008177, PDF](https://arxiv.org/pdf/math/0008177) | Twierdzenie 1.1 stoi w §1. Badacz czytał preprint arXiv. |
| 18 | Lefschetz 1924 | Poprawne według źródła wtórnego. Monografia nie ma DOI. | błędne | [Wikipedia, Lefschetz theorem](https://en.wikipedia.org/wiki/Lefschetz_theorem_on_%281,1%29-classes) | Twierdzenie o klasach $(1,1)$ pochodzi od Lefschetza. Lefschetz użył funkcji normalnych Poincarégo, a nie ciągu wykładniczego snopów. |
| 19 | Levin 1973 | Częściowo potwierdzone: Wikipedia potwierdza rok 1973. Tom 9(3), strony i DOI są niepotwierdzone. | potwierdzone w źródle wtórnym | [Wikipedia, P versus NP](https://en.wikipedia.org/wiki/P_versus_NP_problem) | Równoważność dotyczy tylko instancji z odpowiedzią „tak”. |
| 20 | Li, Yang 2022 | Poprawne. Uzupełnij: STOC 2022, s. 1180–1193, DOI [10.1145/3519935.3519976](https://doi.org/10.1145/3519935.3519976). | potwierdzone w źródle wtórnym | [Crossref](https://api.crossref.org/works/10.1145/3519935.3519976) | Ograniczenie ma postać $3{,}1n - o(n)$. Słowo „największe” jest niepotwierdzone na 2026-11-13. |
| 21 | Lüscher 1983 | Poprawne. Uzupełnij: 219(1), s. 233–261, DOI [10.1016/0550-3213(83)90436-4](https://doi.org/10.1016/0550-3213%2883%2990436-4). | potwierdzone w źródle wtórnym | [van Baal, arXiv:hep-ph/0008206](https://arxiv.org/pdf/hep-ph/0008206) | Minima potencjału tworzą „dolinę próżni” połączeń płaskich. |
| 22 | Ładyżenska 1959 | Poprawne. Uzupełnij: Comm. Pure Appl. Math. 12(3), s. 427–433, DOI [10.1002/cpa.3160120303](https://doi.org/10.1002/cpa.3160120303). | potwierdzone w źródle wtórnym | [Fefferman, PDF, s. 2](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf) | Fefferman cytuje monografię Ładyżenskiej, a nie pracę z 1959 r. Tytuł pracy z 1959 r. dotyczy obszaru z brzegiem. |
| 23 | Markman 2025 | Poprawne. Wersje: v1 2025-09-27, v2 2026-02-11. | potwierdzone w pracy | [arXiv:2509.23403](https://arxiv.org/abs/2509.23403) | Praca jest przeglądem. Dowód zawiera preprint arXiv:2502.03415. Oba teksty są preprintami bez potwierdzonej recenzji. |
| 24 | Mattuck, Tate 1958 | Poprawne. Uzupełnij: 22(1), s. 295–299, DOI [10.1007/BF02941959](https://doi.org/10.1007/BF02941959). | niepotwierdzone | brak | DOI 10.1007/BF02941960 wskazuje inną pracę (T. Nakayama). |
| 25 | Osterwalder, Seiler 1978 | Poprawne. Uzupełnij: 110(2), s. 440–471, DOI [10.1016/0003-4916(78)90039-8](https://doi.org/10.1016/0003-4916%2878%2990039-8). | niepotwierdzone | brak | Pełny tekst jest płatny. Badacz nie znalazł źródła wtórnego. |
| 26 | Perelman 2002 | Poprawne. arXiv:math/0211159, 2002-11-11. | potwierdzone w pracy | [arXiv:math/0211159, PDF, s. 8](https://arxiv.org/pdf/math/0211159) | Rozdział 3.1, wzór (3.4). Monotoniczność wymaga sprzężonego równania ciepła dla $f$ i warunku $\tau_t = -1$. |
| 27 | Perelman 2003, arXiv:math/0303109 | Poprawne. Abstrakt pozycji 28 potwierdza numer arXiv. | potwierdzone w źródle wtórnym | [arXiv:math/0307245](https://arxiv.org/abs/math/0307245) | Znaczniki raportu nie odróżniają 2 prac z 2003 r. |
| 28 | Perelman 2003, arXiv:math/0307245 | Poprawne. Data: 2003-07-17. Praca nie ma wydania w czasopiśmie. | potwierdzone w pracy | [arXiv:math/0307245](https://arxiv.org/abs/math/0307245) | Abstrakt obejmuje rozmaitości bez czynników asferycznych. Przypadek jednospójny wynika z rozkładu na czynniki pierwsze. |
| 29 | Platt, Trudgian 2021 | Poprawne. Uzupełnij: s. 792–797, DOI [10.1112/blms.12460](https://doi.org/10.1112/blms.12460); arXiv:2004.09765. | potwierdzone w pracy | [arXiv:2004.09765](https://arxiv.org/abs/2004.09765) | Ocena opiera się na abstrakcie. Zakres: $0 \lt \gamma \le 3 \times 10^{12}$. |
| 30 | Politzer 1973 | Poprawne. Uzupełnij: Phys. Rev. Lett. 30(26), s. 1346–1349, DOI [10.1103/PhysRevLett.30.1346](https://doi.org/10.1103/PhysRevLett.30.1346). | potwierdzone w źródle wtórnym | [Wikipedia, Beta function](https://en.wikipedia.org/wiki/Beta_function_%28physics%29) | Zastrzeżenie jak w wierszu 11. |
| 31 | Razborov, Rudich 1997 | Poprawne. Uzupełnij: J. Comput. System Sci. 55(1), s. 24–35, DOI [10.1006/jcss.1997.1494](https://doi.org/10.1006/jcss.1997.1494). | potwierdzone w źródle wtórnym | [Williams, PDF](https://people.csail.mit.edu/rrw/acc-lbs.pdf) | Williams cytuje pracę jako barierę dowodów naturalnych. |
| 32 | Rubinstein 1995 | Poprawne. Uzupełnij: red. S. D. Chatterji, Proceedings of the ICM, Zürich 1994, t. 1, Birkhäuser, s. 601–611, DOI [10.1007/978-3-0348-9078-6_54](https://doi.org/10.1007/978-3-0348-9078-6_54). | potwierdzone w źródle wtórnym | [IDEAS](https://ideas.repec.org/h/spr/sprchp/978-3-0348-9078-6_54.html); [Lackenby, arXiv:2002.02179](https://arxiv.org/pdf/2002.02179) | Algorytm używa powierzchni prawie normalnych. |
| 33 | Shannon 1949 | Poprawne. Uzupełnij: Bell Syst. Tech. J. 28(1), s. 59–98, DOI [10.1002/j.1538-7305.1949.tb03624.x](https://doi.org/10.1002/j.1538-7305.1949.tb03624.x). | potwierdzone w źródle wtórnym | [Wikipedia, Circuit complexity](https://en.wikipedia.org/wiki/Circuit_complexity) | Tytuł mówi o sieciach przekaźnikowych dwukońcówkowych, a nie o obwodach z bramkami. |
| 34 | Simon 1983 | Poprawne. Uzupełnij: Ann. Phys. 146(1), s. 209–220, DOI [10.1016/0003-4916(83)90057-X](https://doi.org/10.1016/0003-4916%2883%2990057-X). | potwierdzone w źródle wtórnym | [Fernández, García, arXiv:1310.5229](https://arxiv.org/abs/1310.5229) | Źródło wtórne potwierdza dyskretność widma. Postać nierówności z dowodu 4 jest niepotwierdzona w pracy. |
| 35 | Tao 2016 | Poprawne. Uzupełnij: J. Amer. Math. Soc. 29(3), s. 601–674, DOI [10.1090/jams/838](https://doi.org/10.1090/jams/838). Wydanie online: 2015-06-30. | potwierdzone w pracy | [arXiv:1402.0290](https://arxiv.org/abs/1402.0290) | Ocena opiera się na streszczeniu arXiv. |
| 36 | Tate 1966 | Poprawne. Uzupełnij: Séminaire Bourbaki, vol. 9, exposé 306, s. 415–440; [Numdam](https://www.numdam.org/item/SB_1964-1966__9__415_0/). Praca nie ma DOI. | potwierdzone w źródle wtórnym | [Wiles, PDF CMI](https://www.claymath.org/wp-content/uploads/2022/05/birchswin.pdf) | Wiles przypisuje wynik Artinowi i Tate'owi. |
| 37 | Turing 1936 | Poprawne. Uzupełnij: seria 2, t. 42, s. 230–265, DOI [10.1112/plms/s2-42.1.230](https://doi.org/10.1112/plms/s2-42.1.230). Crossref podaje rok 1937. | potwierdzone w źródle wtórnym | [Wikipedia, Halting problem](https://en.wikipedia.org/wiki/Halting_problem) | Turing dowodzi nierozstrzygalności dla maszyn „circle-free”. Nazwa „problem stopu” pochodzi z lat 50. XX w. |
| 38 | Voisin 2002 | Poprawne. Uzupełnij: Int. Math. Res. Not. 2002, nr 20, s. 1057–1075, DOI [10.1155/S1073792802111135](https://doi.org/10.1155/S1073792802111135). | potwierdzone w źródle wtórnym | [arXiv:math/0112247](https://arxiv.org/abs/math/0112247) | Wynik dotyczy klas Cherna snopów koherentnych. Badacz zna źródło tylko z wyniku wyszukiwania. |
| 39 | Weil 1952 | Poprawne. Uzupełnij: tome supplémentaire dédié à M. Riesz, s. 252–265; zbMATH 0049.03205. Praca nie ma DOI. | potwierdzone w źródle wtórnym | [Wikipedia, Weil's criterion](https://en.wikipedia.org/wiki/Weil%27s_criterion); [AIM](https://aimath.org/WWN/rh/articles/html/75a) | Kryterium dotyczy funkcji L Heckego; funkcja $\zeta$ jest przypadkiem szczególnym. |
| 40 | Williams 2011 | Poprawne. Uzupełnij: s. 115–125, DOI [10.1109/CCC.2011.36](https://doi.org/10.1109/CCC.2011.36). Wersja w czasopiśmie: J. ACM 61(1), 2014, DOI [10.1145/2559903](https://doi.org/10.1145/2559903). | potwierdzone w pracy | [Williams, PDF](https://people.csail.mit.edu/rrw/acc-lbs.pdf) | Praca formalnie omija 2 z 3 barier. Barierę dowodów naturalnych praca omija tylko intuicyjnie. Badacz czytał wersję autorską z 2012-07-31. |

## Poprawki do pliku REPORT.md

Zdanie obecne jest cytatem z pliku `REPORT.md`. Zdanie proponowane zapisuje wzory w LaTeX.

1. Wiersz 21, dowód 2.
   - Obecne: „**Hodge dla klas typu (1,1)** `[źródło: Lefschetz 1924]`.”
   - Proponowane: „**Hodge dla klas typu $(1,1)$** `[źródło: Lefschetz 1924 dla twierdzenia; Griffiths, Harris 1994, s. 163–164 dla dowodu]`.”
   - Podstawa: Lefschetz użył funkcji normalnych Poincarégo ([Wikipedia](https://en.wikipedia.org/wiki/Lefschetz_theorem_on_%281,1%29-classes)). Dane podręcznika Griffithsa i Harrisa pochodzą z Wikipedii.
2. Wiersz 28, dowód 4.
   - Obecne: „**Yang–Mills, hamiltonian H = −Δ + x²y²: widmo dyskretne oraz E₀ ≥ 1,0188** `[źródło: Simon 1983]`.”
   - Proponowane: „**Yang–Mills, hamiltonian $H = -\Delta + x^2y^2$: widmo dyskretne `[źródło: Simon 1983]` oraz $E_0 \ge 1{,}0188$ `[obliczenie: dowód 4]`**.”
   - Podstawa: wiersz 34 tabeli.
3. Wiersz 32, dowód 4.
   - Obecne: „Operator −Δ + |x| + |y| ma widmo dyskretne i poziom podstawowy 2 × 1,0188 `[obliczenie: skrypt]`.”
   - Proponowane: „Operator $-\Delta + \lvert x\rvert + \lvert y\rvert$ ma poziom podstawowy $2 \times \lvert a_1' \rvert = 2 \times 1{,}0188$ `[źródło: DLMF §9.9]`.”
   - Podstawa: $a_1' = -1{,}0187929716$ ([DLMF §9.9](https://dlmf.nist.gov/9.9)).
4. Wiersz 36, dowód 5.
   - Obecne: „Zatem algorytm deterministyczny zadaje n pytań, a certyfikat odpowiedzi „1” ma 1 bit.”
   - Proponowane: „Zatem deterministyczne drzewo decyzyjne zadaje $n$ pytań, a certyfikat odpowiedzi „1” ma 1 bit `[źródło: Buhrman, de Wolf 2002]`.”
   - Podstawa: $D(OR_n) = n$, a algorytm Grovera wymaga $\Theta(\sqrt{n})$ zapytań kwantowych ([Buhrman, de Wolf, PDF](https://homepages.cwi.nl/~rdewolf/publ/qc/dectree.pdf)).
5. Wiersz 37, dowód 6.
   - Obecne: „**Zliczanie obwodów** `[źródło: Shannon 1949]`.”
   - Proponowane: „**Zliczanie obwodów** `[źródło: Shannon 1949, argument dla sieci przekaźnikowych dwukońcówkowych]`.”
   - Podstawa: wiersz 33 tabeli.
6. Wiersz 46, dowód 9.
   - Obecne: „**Algorytm: zdanie klasy Π₁, którego teoria nie rozstrzyga, jest prawdziwe.**”
   - Proponowane: „**Algorytm: zdanie klasy $\Pi_1$, którego teoria nie rozstrzyga, jest prawdziwe** `[źródło: Aaronson, „P =? NP”]`.”
   - Podstawa: [Aaronson, PDF](https://www.scottaaronson.com/papers/pnp.pdf).
7. Wiersz 52, dowód 10.
   - Obecne: „Problem stopu nie ma algorytmu.”
   - Proponowane: „Problem stopu nie ma algorytmu `[źródło: Turing 1936]`. Turing dowiódł nierozstrzygalności dla maszyn „circle-free”; nazwa „problem stopu” pochodzi z lat 50. XX w.”
   - Podstawa: [Wikipedia, Halting problem](https://en.wikipedia.org/wiki/Halting_problem).
8. Wiersz 56, legenda.
   - Obecne: „Autor nie sprawdził żadnego odsyłacza w pracy źródłowej.”
   - Proponowane: „Raport „Verification of 40 report references” z 2026-11-13 podaje stan sprawdzenia każdego odsyłacza.”
9. Wiersz 77, tabela stanu.
   - Obecne: „Dowód istnieje. Clay Mathematics Institute (CMI) przyznał nagrodę w 2010 r.” ze znacznikiem `[źródło: Perelman 2002, 2003]`.
   - Proponowane: „Dowód istnieje `[źródło: Perelman 2002; Perelman 2003a; Perelman 2003b]`. CMI przyznał nagrodę G. Perelmanowi 2010-03-18. Perelman odrzucił nagrodę `[źródło: sieć]`.”
   - Podstawa: [claymath.org](https://www.claymath.org/millennium/poincare-conjecture/); [NBC News](https://www.nbcnews.com/id/wbna38039068).
10. Wiersz 78, tabela stanu.
    - Obecne: „W dniu 2026-09-18 niezależna weryfikacja wariantu (C) trwała.”
    - Proponowane: „W październiku 2026 r. wynik czekał na niezależną weryfikację. CMI oznacza problem statusem „Active” `[źródło: sieć]`.”
    - Podstawa: żadna z 8 stron nie podaje daty 2026-09-18 ([Wikipedia](https://en.wikipedia.org/wiki/Millennium_Prize_Problems); [Papex](https://papex.org/blog/has-ai-solved-a-millennium-prize-problem)).
11. Wiersz 79, tabela stanu.
    - Obecne: „Zespół D. Grossa potwierdził dowód i wydał formalizację w Lean 2026-11-10.”
    - Proponowane: „Firma OpenAI powołała komitet 5 osób pod kierunkiem D. Grossa. W nocy 2026-11-10 komitet opublikował objaśnienie dowodu i potwierdził weryfikację kodu Lean napisanego przez OpenAI. CMI oznacza problem statusem „Unsolved” `[źródło: sieć]`.”
    - Podstawa: [Scientific American](https://www.scientificamerican.com/article/openais-shepherds-affirm-blockbuster-physics-result/); [claymath.org](https://www.claymath.org/millennium-problems/).
12. Wiersz 82.
    - Obecne: „Lista CMI zawiera 6 problemów nierozwiązanych `[źródło: sieć]`.”
    - Proponowane: „Strona CMI oznacza 5 problemów statusem „Unsolved”, problem Naviera–Stokesa statusem „Active” i hipotezę Poincarégo statusem „Solved” `[źródło: sieć]`.”
    - Podstawa: [claymath.org](https://www.claymath.org/millennium-problems/).
13. Wiersz 104, Riemann w modelu 1.
    - Obecne: „Nierówność a² ≤ 4p jest hipotezą Riemanna dla funkcji dzeta krzywej E `[źródło: Hasse 1933]`.”
    - Proponowane: „Nierówność $a^2 \le 4p$ jest hipotezą Riemanna dla funkcji dzeta krzywej $E$ `[źródło: Hasse 1933, zapowiedź; Hasse 1936, dowód]`.”
    - Podstawa: wiersz 14 tabeli.
14. Wiersz 138, Navier–Stokes w modelu 2.
    - Obecne: „Wniosek dla d = 2 zgadza się z twierdzeniem o gładkości w 2 wymiarach `[źródło: Ładyżenska 1959]`.”
    - Proponowane: „Wniosek dla $d = 2$ zgadza się z twierdzeniem o gładkości w 2 wymiarach `[źródło: Ładyżenska 1959; Fefferman 2000, s. 2]`.”
    - Podstawa: wiersz 22 tabeli.
15. Wiersz 146, model 3.
    - Obecne: „W modelu zapytań odpowiednik zdania P ≠ NP ma dowód `[źródło: Baker, Gill, Solovay 1975]`.”
    - Proponowane: „Istnieje wyrocznia $A$, dla której $P^A = NP^A$, oraz wyrocznia $B$, dla której $P^B \neq NP^B$ `[źródło: Baker, Gill, Solovay 1975]`.”
    - Podstawa: wiedza badacza bez sprawdzenia w pracy. Autor MUSI sprawdzić to zdanie w pracy przed zmianą pliku.
16. Wiersz 147, model 3.
    - Obecne: „Największe opublikowane dolne ograniczenie dla funkcji podanej wzorem wynosi 3,1 × n bramek, czyli 62 bramki dla n = 20 `[źródło: Li, Yang 2022]`.”
    - Proponowane: „W 2022 r. Li i Yang dowiedli dolnego ograniczenia $3{,}1n - o(n)$ bramek dla funkcji podanej wzorem `[źródło: Li, Yang 2022]`. Dla $n = 20$ człon $3{,}1n$ wynosi 62 bramki.”
    - Podstawa: wiersz 20 tabeli.
17. Wiersz 153, propozycja 1.
    - Obecne: „Przypadek z wkładem samego miejsca archimedesowego ma dowód `[źródło: Connes, Consani 2021]`.”
    - Proponowane: „Connes i Consani badają przypadek samego miejsca archimedesowego i podają konceptualne źródło dodatniości przy parametrze odcięcia równym 1 `[źródło: Connes, Consani 2021]`.”
    - Podstawa: wiersz 5 tabeli.
18. Wiersz 154, propozycja 2.
    - Obecne: „Nad ciałem Q hipoteza ma dowód dla krzywych, których funkcja L ma w punkcie s = 1 zero o krotności co najwyżej 1 `[źródło: Gross, Zagier 1986; Koływagin 1990]`.”
    - Proponowane: „Nad ciałem $\mathbb{Q}$ równość rangi i krotności zera ma dowód dla krzywych z zerem w $s = 1$ o krotności co najwyżej 1. Dowód łączy prace Grossa i Zagiera, Koływagina oraz twierdzenie o modularności `[źródło: Gross, Zagier 1986; Koływagin 1990; Wiles, CMI]`. Wzór na współczynnik wiodący nie ma pełnego dowodu.”
    - Podstawa: [Wiles, PDF CMI](https://www.claymath.org/wp-content/uploads/2022/05/birchswin.pdf).
19. Wiersz 154, propozycja 2.
    - Obecne: „Pierwszy krok roboczy: udowodnij skończoność dla krzywej 389a1 o randze 2.”
    - Proponowane: „Pierwszy krok roboczy: udowodnij skończoność całej grupy Ш dla krzywej 389a1. Dla krzywej 389a1 równość ranga = 2 = krotność zera ma dowód `[źródło: LMFDB]`.”
    - Podstawa: [LMFDB 389.a1](https://www.lmfdb.org/EllipticCurve/Q/389/a/1); [LMFDB, ranga analityczna](https://www.lmfdb.org/knowledge/show/ec.q.analytic_rank).
20. Wiersz 155, propozycja 3.
    - Obecne: „Dowód MUSI używać współczynników wymiernych i rzutowości, bo hipoteza bez tych 2 założeń jest fałszywa `[źródło: Atiyah, Hirzebruch 1962; Voisin 2002]`.”
    - Proponowane: „Dowód MUSI używać współczynników wymiernych, bo wersja całkowita jest fałszywa `[źródło: Atiyah, Hirzebruch 1962]`. Dowód MUSI używać rzutowości, bo na rozmaitości Kählera klasy Cherna snopów koherentnych nie dają każdej wymiernej klasy Hodge'a `[źródło: Voisin 2002]`.”
    - Podstawa: wiersze 2 i 38 tabeli.
21. Wiersz 155, propozycja 3.
    - Obecne: „Wymiar co najwyżej 5 ma dowód `[źródło: Markman 2025; sieć]`.”
    - Proponowane: „Dla rozmaitości abelowych wymiaru co najwyżej 5 hipoteza wynika z preprintów Markmana bez potwierdzonej recenzji `[źródło: Markman 2025a, arXiv:2502.03415; Markman 2025b, arXiv:2509.23403]`.”
    - Podstawa: wiersz 23 tabeli.
22. Wiersz 156, propozycja 4.
    - Obecne: „Na kracie przy silnym sprzężeniu luka masowa ma dowód `[źródło: Osterwalder, Seiler 1978]`.”
    - Proponowane: „Na kracie przy silnym sprzężeniu luka masowa ma dowód `[założenie: Osterwalder, Seiler 1978, twierdzenie niesprawdzone w pracy]`.”
    - Podstawa: wiersz 25 tabeli.
23. Wiersz 156, propozycja 4.
    - Obecne: „Teoria U(1) na kracie w 4 wymiarach ma fazę bez luki masowej `[źródło: Guth 1980; Fröhlich, Spencer 1982]`.”
    - Proponowane: „Teoria U(1) na kracie w 4 wymiarach ma fazę bez uwięzienia `[źródło: Guth 1980]`. Abelowe teorie z cechowaniem mają fazy bezmasowe `[źródło: Fröhlich, Spencer 1982]`.”
    - Podstawa: wiersze 9 i 13 tabeli.
24. Wiersz 156, propozycja 4.
    - Obecne: „Pierwszy krok roboczy: luka masowa w modelu O(3) w 2 wymiarach przy każdej wartości sprzężenia `[założenie]`.”
    - Proponowane: zdanie obecne bez zmian oraz nowe zdanie: „Preprint z 2026 r. bez recenzji sprawdza lukę komputerowo w 8 punktach sprzężenia, najwyżej przy $\beta = 0{,}85$ `[źródło: Research Square rs-11440706/v1]`.”
    - Podstawa: [Research Square](https://www.researchsquare.com/article/rs-11440706/v1).
25. Wiersz 157, propozycja 5.
    - Obecne: „Osobliwość wymaga nieograniczonej normy L³ `[źródło: Escauriaza, Seregin, Šverák 2003]`.”
    - Proponowane: „Jeżeli rozwiązanie w $\mathbb{R}^3$ ma osobliwość w chwili $T^{\ast}$, to $\limsup_{t \uparrow T^{\ast}} \lVert u(t)\rVert_{L^3} = \infty$ `[źródło: Escauriaza, Seregin, Šverák 2003]`.”
    - Podstawa: wiersz 6 tabeli.
26. Wiersz 158, propozycja 6.
    - Obecne: „Droga, która omija 3 bariery: algorytm sprawdzania spełnialności, który wykonuje mniej kroków niż przegląd zupełny, daje dolne ograniczenie `[źródło: Williams 2011]`.”
    - Proponowane: „Algorytm sprawdzania spełnialności, który wykonuje mniej kroków niż przegląd zupełny, daje dolne ograniczenie `[źródło: Williams 2011]`. Ta droga omija relatywizację i algebraizację. Według Williamsa droga omija barierę dowodów naturalnych tylko intuicyjnie.”
    - Podstawa: wiersz 40 tabeli.
27. Wiersz 159, propozycja 7.
    - Obecne: „Każda zamknięta jednospójna rozmaitość wymiaru 3 kończy przepływ Ricciego z chirurgią w skończonym czasie, tak jak okrągła sfera z modelu 2 `[źródło: Perelman 2003]`.”
    - Proponowane: to samo zdanie ze znacznikiem `[źródło: Perelman 2003b, arXiv:math/0307245]`. W bibliografii oznacz arXiv:math/0303109 jako 2003a i arXiv:math/0307245 jako 2003b.
    - Podstawa: wiersze 27 i 28 tabeli.
28. Wiersz 159, propozycja 7.
    - Obecne: „Narzędzie dowodu: entropia W, która nie maleje wzdłuż przepływu i zachowuje wartość przy skalowaniu `[źródło: Perelman 2002]`.”
    - Proponowane: „Narzędzie dowodu: entropia $\mathcal{W}$ nie maleje wzdłuż przepływu, gdy $f$ spełnia sprzężone równanie ciepła i $\tau_t = -1$ `[źródło: Perelman 2002, rozdz. 3.1]`. Entropia $\mathcal{W}$ zachowuje wartość przy jednoczesnym skalowaniu $g$ i $\tau$.”
    - Podstawa: wiersz 26 tabeli.
29. Wiersz 192, tabela algorytmu, wiersz P a NP.
    - Obecne: „Zdanie P = NP ma postać „istnieje algorytm, który dla każdego wejścia…” `[założenie]`.”
    - Proponowane: „Zdanie $P = NP$ jest zdaniem klasy $\Sigma_2$, a zdanie $P \neq NP$ jest zdaniem klasy $\Pi_2$ `[źródło: Aaronson, „P =? NP”]`.”
    - Podstawa: [Aaronson, PDF](https://www.scottaaronson.com/papers/pnp.pdf).
30. Wiersz 192, tabela algorytmu, wiersz P a NP.
    - Obecne: „Algorytm przeszukiwania uniwersalnego rozwiązuje zadanie spełnialności w czasie wielomianowym wtedy i tylko wtedy, gdy P = NP `[źródło: Levin 1973]`.”
    - Proponowane: „Algorytm przeszukiwania uniwersalnego rozwiązuje w czasie wielomianowym każdą spełnialną instancję wtedy i tylko wtedy, gdy $P = NP$ `[źródło: Levin 1973]`. Dla instancji niespełnialnej algorytm pracuje bez końca.”
    - Podstawa: wiersz 19 tabeli.
31. Wiersz 214, sprawdziany.
    - Obecne: „Wzrost iloczynu jak (ln X)^r nie ma dowodu dla żadnej z 4 krzywych `[założenie]`.”
    - Proponowane: „Asymptotyka $\prod_{p \le X} N_p/p \sim C (\ln X)^r$ jest hipotezą. Goldfeld wykazał, że asymptotyka implikuje hipotezę Riemanna dla $L(E,s)$ i postać rangową BSD `[źródło: Goldfeld 1982; Kuo, Murty 2005]`.”
    - Podstawa: [Kuo, Murty 2005](https://doi.org/10.4153/CJM-2005-014-0).
32. Wiersz 214, sprawdziany, nowe zdanie po zdaniu „Sprawdziany 1 i 2 są równoważne…”.
    - Obecne: brak zdania.
    - Proponowane: „Wartość $E_0 = 1{,}10822$ ze sprawdzianu 5 zgadza się z wartością $1{,}10822315759$ z literatury `[źródło: Fernández, García 2014]`.”
    - Podstawa: [arXiv:1310.5229](https://arxiv.org/abs/1310.5229).
33. Wiersz 260, problematyka, punkt 10.
    - Obecne: „Autor nie sprawdził żadnego odsyłacza do literatury w pracy źródłowej.”
    - Proponowane: „Sprawdzenie z 2026-11-13 objęło tekst 4 prac i abstrakty 5 prac. Sprawdzenie nie potwierdziło 4 twierdzeń i wykazało 1 błędne przypisanie.”
34. Wiersz 304, bibliografia.
    - Obecne: „Autor nie sprawdził żadnej pozycji z egzemplarzem pracy.”
    - Proponowane: „Raport „Verification of 40 report references” z 2026-11-13 sprawdza dane każdej pozycji w Crossref, zbMATH albo arXiv.”
35. Wiersze od 306 do 345 włącznie, bibliografia.
    - Obecne: 36 pozycji bez stron i bez DOI.
    - Proponowane: dopisz do każdej pozycji strony i DOI z kolumny „Dane bibliograficzne” tabeli 40 pozycji.
36. Wiersz 354, źródła z sieci.
    - Obecne: „[Finite-Time Blowup for Navier-Stokes with Smooth Forcing, Part I (arXiv:2609.35406)](https://arxiv.org/abs/2609.35406)”.
    - Proponowane: zostaw tę pozycję z opisem „Z. Lei, X. Ren, 2026-09-28”. Dopisz pozycję: „[Navier-Stokes lost in translation: Why Lean verification of AI autoformalisation does not guarantee correct natural language proofs (arXiv:2610.08144)](https://arxiv.org/abs/2610.08144)”.
    - Podstawa: [arXiv:2609.35406](https://arxiv.org/abs/2609.35406); [Wikipedia, przypis](https://en.wikipedia.org/wiki/Navier%E2%80%93Stokes_priority_controversy). Badacze nie otworzyli strony arXiv:2610.08144.
37. Bibliografia, nowe pozycje dla poprawek 1, 3, 4, 6, 13, 18, 19, 21, 24, 29, 31 i 32.
    - Obecne: brak pozycji.
    - Proponowane: dopisz każdą pozycję z listy:
      - Buhrman, H., de Wolf, R. (2002). Complexity measures and decision tree complexity: a survey. Theoretical Computer Science 288(1), s. 21–43, DOI [10.1016/S0304-3975(01)00144-X](https://doi.org/10.1016/S0304-3975%2801%2900144-X).
      - Fernández, García (2014). Eigenvalues and eigenfunctions of the anharmonic oscillator $V(x,y)=x^2y^2$. Open Physics 12, DOI [10.2478/s11534-014-0474-7](https://doi.org/10.2478/s11534-014-0474-7).
      - Goldfeld, D. (1982). Sur les produits partiels eulériens attachés aux courbes elliptiques. C. R. Acad. Sci. Paris Sér. I Math. 294, s. 471–474.
      - Kuo, W., Murty, M. R. (2005). On a conjecture of Birch and Swinnerton-Dyer. Canad. J. Math. 57(2), s. 328–337, DOI [10.4153/CJM-2005-014-0](https://doi.org/10.4153/CJM-2005-014-0).
      - Hasse, H. (1936). Zur Theorie der abstrakten elliptischen Funktionenkörper III. J. reine angew. Math. 175, DOI [10.1515/crll.1936.175.193](https://doi.org/10.1515/crll.1936.175.193).
      - Markman, E. (2025). Cycles on abelian 2n-folds of Weil type from secant sheaves on abelian n-folds. [arXiv:2502.03415](https://arxiv.org/abs/2502.03415).
      - Aaronson, S. P =? NP. [PDF](https://www.scottaaronson.com/papers/pnp.pdf).
      - Wiles. Opis problemu Bircha i Swinnertona-Dyera, CMI `[DO USTALENIA: tytuł]`. [PDF](https://www.claymath.org/wp-content/uploads/2022/05/birchswin.pdf).
      - Griffiths, Harris (1994). `[DO USTALENIA: tytuł podręcznika]`, s. 163–164.
      - NIST DLMF, [§9.9](https://dlmf.nist.gov/9.9).
      - LMFDB, krzywa [389.a1](https://www.lmfdb.org/EllipticCurve/Q/389/a/1).
      - Research Square, [rs-11440706/v1](https://www.researchsquare.com/article/rs-11440706/v1).
    - Uwaga: notatki nie podają tytułu podręcznika Griffithsa i Harrisa, tytułu opisu Wilesa ani roku przeglądu Aaronsona. Autor MUSI ustalić te 3 dane przed zmianą pliku.

## Źródła z sieci o stanie z 2026 r.

Badacze otworzyli 7 z 8 stron w dniu 2026-11-13. Strona OpenAI wymaga JavaScriptu i cookies, więc badacze cytują stronę OpenAI za źródłami wtórnymi.

1. [Millennium Prize Problems (Wikipedia)](https://en.wikipedia.org/wiki/Millennium_Prize_Problems)
   - Potwierdza: CMI oficjalnie uznał za rozwiązaną tylko hipotezę Poincarégo. W październiku 2026 r. wynik dla równań Naviera–Stokesa czekał na walidację naukową.
   - Nie potwierdza: daty 2026-09-18.
2. [On the Navier–Stokes Millennium Prize Problem (OpenAI)](https://openai.com/index/navier-stokes-solution/)
   - Potwierdza: nic bezpośrednio, bo badacze nie otworzyli strony.
   - Cytaty z posta w serwisie Papex i w Wikipedii potwierdzają ogłoszenie z 2026-09-08 o wariantach (C) i (D). Według cytatu siła jest gładka i ma nośnik zwarty w przestrzeni i w czasie.
   - Nie potwierdza: opisu warunków zaniku (4) i (5) Feffermana na samej stronie.
3. [Navier–Stokes priority controversy (Wikipedia)](https://en.wikipedia.org/wiki/Navier%E2%80%93Stokes_priority_controversy)
   - Potwierdza: przebieg obliczenia trwał 88 h. Praca OpenAI ma 166 stron i formalizację w Lean. Ogłoszenie nastąpiło 2026-09-08 w południe. Przypis wskazuje pracę arXiv:2610.08144 z zarzutem niezgodności formalizacji. Według strony wynik nie miał niezależnej weryfikacji w 2026 r.
   - Nie potwierdza: daty 2026-09-18.
4. [arXiv:2609.35406](https://arxiv.org/abs/2609.35406)
   - Potwierdza: Z. Lei i X. Ren wysłali pracę 2026-09-28; wersja 2 pochodzi z 2026-09-29. Streszczenie ocenia wynik OpenAI jako „a major advance”.
   - Nie potwierdza: zarzutu niezgodności formalizacji w Lean. Praca nie jest pracą z 2026-10-06.
5. [Scientific American](https://www.scientificamerican.com/article/openais-shepherds-affirm-blockbuster-physics-result/)
   - Potwierdza: w nocy 2026-11-10 D. Gross i 4 członków komitetu opublikowali objaśnienie dowodu i potwierdzenie weryfikacji w Lean. Firma OpenAI powołała D. Grossa na przewodniczącego komitetu. Komitet pisze: „We do not claim to fully understand the proof yet.” Luka masowa pozostaje nierozwiązana.
   - Nie potwierdza: że komitet napisał formalizację w Lean. Nie potwierdza niezależności komitetu od OpenAI.
6. [Yang–Mills existence and mass gap (Wikipedia)](https://en.wikipedia.org/wiki/Yang%E2%80%93Mills_existence_and_mass_gap)
   - Potwierdza: firma OpenAI ogłosiła 2026-10-26 dowód części o istnieniu teorii. Luka masowa nie ma dowodu.
   - Nie potwierdza: stanu na liście CMI. Strona CMI w dniu 2026-11-13 oznacza problem statusem „Unsolved” ([claymath.org](https://www.claymath.org/millennium-problems/)).
7. [arXiv:2509.23403](https://www.arxiv.org/abs/2509.23403)
   - Potwierdza: hipoteza Hodge'a dla rozmaitości abelowych wymiaru co najwyżej 5 wynika z algebraiczności klas Weila na 4-wymiarowych rozmaitościach typu Weila. Wersja 1 pochodzi z 2025-09-27, wersja 2 z 2026-02-11.
   - Nie potwierdza: że ta praca zawiera dowód. Dowód zawiera arXiv:2502.03415. Nie potwierdza recenzji w czasopiśmie.
8. [Has AI solved a Millennium Prize Problem? (Papex)](https://papex.org/blog/has-ai-solved-a-millennium-prize-problem)
   - Potwierdza: cytat posta OpenAI o wariantach (C) i (D). CMI oznacza 5 problemów statusem „Unsolved” i problem Naviera–Stokesa statusem „Active”. Kopia w Internet Archive z 2026-09-09 ma poprzedni status, a kopia z 2026-09-10 ma status „Active”.
   - Potwierdza też: CMI rozważa nagrodę po publikacji w recenzowanym czasopiśmie, po 2 latach i po powszechnej akceptacji. T. Hales pisze 2026-10-09, że człowiek MUSI porównać tezę w Lean z tezą Feffermana. Grupa D. Grossa opublikowała 2026-11-10 kod Lean napisany przez OpenAI. B. Totaro nazywa dowód Markmana dla wymiaru 4 i 5 „a monumental piece of work”.
   - Nie potwierdza: daty 2026-09-18. Papex jest blogiem, a nie źródłem pierwotnym.

## Odpowiedzi na pytania dodatkowe

1. Czy istnieje krzywa eliptyczna nad $\mathbb{Q}$ o randze co najmniej 2 z dowodem skończoności grupy Ш? Badacze nie znaleźli takiej krzywej. Skończoność grupy Ш ma dowód dla krzywych o randze analitycznej 0 albo 1 ([Wiles, PDF CMI](https://www.claymath.org/wp-content/uploads/2022/05/birchswin.pdf)). Skończoność $p$-części grupy Ш dla wybranych par $(E,p)$ przy randze 2 wynika z definicji zbioru u W. Steina ([Stein 2011](https://www.williamstein.org/talks/2011-05-bsd_conference/2011-05-bsd_conference.pdf)). Badacz nie otworzył pliku Steina.
2. Czy dla krzywej 389a1 równość ranga = 2 = krotność zera ma dowód? Tak. LMFDB podaje rangę 2 i rangę analityczną 2 ([LMFDB 389.a1](https://www.lmfdb.org/EllipticCurve/Q/389/a/1)). Dla rangi 2 górne ograniczenie rangi analitycznej jest dokładne dzięki twierdzeniom Grossa i Zagiera, Kolyvagina i innych ([LMFDB](https://www.lmfdb.org/knowledge/show/ec.q.analytic_rank)). LMFDB podaje $Ш_{\mathrm{an}} \approx 1$ tylko numerycznie, więc pełny wzór BSD dla 389a1 nie ma dowodu.
3. Czy asymptotyka $\prod_{p \le X} N_p/p \sim C(\log X)^r$ ma dowód dla co najmniej 1 krzywej? Badacze nie znaleźli dowodu. Goldfeld w 1982 r. pokazał, że asymptotyka implikuje hipotezę Riemanna dla $L(E,s)$ ([Kuo, Murty 2005](https://doi.org/10.4153/CJM-2005-014-0)). Hipoteza Riemanna dla $L(E,s)$ nie ma dowodu dla żadnej krzywej.
4. Jaki postęp w dodatniości formy Weila opublikowano po 2021 r.? Connes, Consani i Moscovici rozwijają program z operatorami sferoidalnymi wydłużonymi i trójkami spektralnymi ([arXiv:2310.18423](https://arxiv.org/abs/2310.18423)). Praca z 2025-11-27 nazywa swój wkład strategią dowodu ([arXiv:2511.22755](https://arxiv.org/abs/2511.22755)). Żadna praca nie dowodzi pełnej dodatniości formy Weila.
5. Czy CMI przyznał nagrodę za hipotezę Poincarégo w 2010 r.? Tak. CMI ogłosił nagrodę dla G. Perelmana 2010-03-18 ([claymath.org](https://www.claymath.org/millennium/poincare-conjecture/)). CMI potwierdził odmowę Perelmana 2010-07-01 ([NBC News](https://www.nbcnews.com/id/wbna38039068)).
6. Jaki jest najmniejszy otwarty przypadek hipotezy Hodge'a? Hipoteza ma dowód dla rozmaitości wymiaru co najwyżej 3 ([Wikipedia, Hodge conjecture](https://en.wikipedia.org/wiki/Hodge_conjecture)). Według wymiaru najmniejszy otwarty przypadek to klasy $(2,2)$ na rozmaitościach wymiaru 4. Wśród rozmaitości abelowych najmniejszy otwarty wymiar wynosi 6 poza szczególnymi rodzinami ([arXiv:2603.20268](https://arxiv.org/html/2603.20268v1)).
7. Czy okrągła sfera $S^3$ pod przepływem $\partial_t g = -2 \mathrm{Ric}$ spełnia $r^2(t) = r_0^2 - 4t$? Tak. Dla metryki Einsteina $\mathrm{Ric} = \lambda g$ rodzina $g_t = (1 - 2\lambda t)g$ jest przepływem Ricciego ([Wikipedia, Ricci flow](https://en.wikipedia.org/wiki/Ricci_flow)). Dla $S^n$ zachodzi $r^2(t) = r_0^2 - 2(n-1)t$, więc dla $n = 3$ sfera znika w chwili $T = r_0^2/4$.
8. Czy pole wewnątrz krzywej pod przepływem skracającym krzywe maleje w tempie $2\pi$? Tak. Pole maleje w stałym tempie $2\pi$ jednostek pola na jednostkę czasu ([Wikipedia, Curve-shortening flow](https://en.wikipedia.org/wiki/Curve-shortening_flow)). Gage i Hamilton w 1986 r. udowodnili zbieganie krzywych wypukłych do punktu okrągłego ([DOI 10.4310/jdg/1214439902](https://doi.org/10.4310/jdg/1214439902)). Grayson w 1987 r. udowodnił, że każda zanurzona krzywa staje się wypukła ([DOI 10.4310/jdg/1214441371](https://doi.org/10.4310/jdg/1214441371)).
9. Jaką wartość $E_0$ hamiltonianu $-\Delta + x^2y^2$ podaje literatura? Literatura podaje $E_0 = 1{,}10822315759$ dla stanu 1A1 ([arXiv:1310.5229](https://arxiv.org/abs/1310.5229)). Wartość raportu 1,10822 zgadza się z literaturą w 6 cyfrach znaczących.
10. Czy poziom podstawowy operatora $-d^2/dx^2 + \lvert x\rvert$ wynosi 1,0188? Tak. Warunek $\mathrm{Ai}'(-E) = 0$ daje $E_0 = \lvert a_1' \rvert = 1{,}0187929716$ ([DLMF §9.9](https://dlmf.nist.gov/9.9)). Badacz wyprowadził warunek $\mathrm{Ai}'(-E) = 0$ sam; DLMF podaje tylko wartość zera.
11. Czy luka masowa w modelu O(3) w 2 wymiarach ma dowód dla każdej wartości sprzężenia? Nie. Preprint z 2026 r. bez recenzji sprawdza lukę komputerowo w 8 punktach, najwyżej przy $\beta = 0{,}85$ ([Research Square](https://www.researchsquare.com/article/rs-11440706/v1)). Przy $\beta = 0{,}85$ luka wynosi co najmniej 0,0195 `[DO USTALENIA: jednostka luki; notatka nie podaje jednostki]` w każdej objętości.
12. Czy enstrofia rozwiązania 2D Naviera–Stokesa bez siły nie rośnie? Tak na torusie $\mathbb{T}^2$ i na $\mathbb{R}^2$: $\tfrac{d}{dt}\lVert\omega\rVert_{L^2}^2 = -2\nu\lVert\nabla\omega\rVert_{L^2}^2 \le 0$. Rachunek pochodzi od badacza, a fakt monotoniczności dla przepływu okresowego podają streszczenia prac ([arXiv:2112.04923](https://arxiv.org/pdf/2112.04923)). Dla obszaru z brzegiem i warunkiem przylegania monotoniczność nie wynika z tego rachunku.
13. Jakie twierdzenia o modelu diadycznym mają dowód? Cheskidov dowodzi osobliwości dla stopnia dyssypacji $\alpha \lt 1/3$ i globalnej regularności dla $\alpha \ge 1/2$ ([arXiv:math/0601074](https://arxiv.org/abs/math/0601074)). Barbato, Morandin i Romito dowodzą gładkości dodatnich rozwiązań dla $\beta \in (2, 5/2]$ ([arXiv:1007.3401](https://ar5iv.labs.arxiv.org/html/1007.3401)). Katz i Pavlović dowodzą osobliwości w modelu diadycznym równań Eulera ([DOI 10.1090/S0002-9947-04-03532-9](https://doi.org/10.1090/S0002-9947-04-03532-9)).
14. Czy siła z dowodu OpenAI spełnia warunki wariantu (C)? Według cytatu z pracy OpenAI siła jest gładka i ma nośnik zwarty w przestrzeni i w czasie, a przepływ startuje ze spoczynku ([Papex](https://papex.org/blog/has-ai-solved-a-millennium-prize-problem)). Taka siła spełnia warunek (5), a pole $u^\circ = 0$ spełnia warunek (4) Feffermana ([Fefferman, PDF](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf)). Wniosek wynika z definicji; badacze nie otworzyli pracy OpenAI.
15. Jaka jest klasa arytmetyczna zdania $P = NP$? Zdanie $P \neq NP$ jest zdaniem klasy $\Pi_2$, więc zdanie $P = NP$ jest zdaniem klasy $\Sigma_2$ ([Aaronson, PDF](https://www.scottaaronson.com/papers/pnp.pdf)).
16. Czy hipoteza Riemanna jest równoważna zdaniu klasy $\Pi_1$? Tak. Aaronson nazywa hipotezę Riemanna zdaniem $\Pi_1$ ([Aaronson, PDF](https://www.scottaaronson.com/papers/pnp.pdf)). Nierówność Lagariasa ma postać „każda liczba $n$ spełnia warunek rozstrzygalny” ([arXiv:math/0008177](https://arxiv.org/pdf/math/0008177)).
17. Które źródło podaje, że nierozstrzygnięte zdanie $\Pi_1$ jest prawdziwe? Przegląd Aaronsona: fałszywe zdanie $\Pi_1$ ma obalenie w ZF przez kontrprzykład ([Aaronson, PDF](https://www.scottaaronson.com/papers/pnp.pdf)). Twierdzenie wymaga teorii, która dowodzi każdego prawdziwego zdania $\Sigma_0$.
18. Które źródło podaje, że $OR_n$ wymaga $n$ zapytań? Buhrman i de Wolf podają $D(OR_n) = n$ dla deterministycznych drzew decyzyjnych ([Buhrman, de Wolf, PDF](https://homepages.cwi.nl/~rdewolf/publ/qc/dectree.pdf)).

## Niezweryfikowane

Prace z bibliografii, których badacze nie otworzyli w pełnym tekście ani w abstrakcie (31 prac):

- Aaronson, Wigderson 2009; Atiyah, Hirzebruch 1962; Baker, Gill, Solovay 1975; Birch, Swinnerton-Dyer 1965.
- Escauriaza, Seregin, Šverák 2003; Friedan 1980; Fröhlich, Spencer 1982; Gross, Zagier 1986; Gross, Wilczek 1973.
- Grothendieck 1958; Guth 1980; Hasse 1933; Kato, Trihan 2003; Kolyvagin 1990; Lefschetz 1924; Levin 1973.
- Li, Yang 2022; Lüscher 1983; Ładyżenska 1959; Mattuck, Tate 1958; Osterwalder, Seiler 1978; Perelman 2003 (arXiv:math/0303109).
- Politzer 1973; Razborov, Rudich 1997; Rubinstein 1995; Shannon 1949; Simon 1983; Tate 1966; Turing 1936; Voisin 2002; Weil 1952.

Prace, których badacze przeczytali tylko abstrakt (5 prac): Connes, Consani 2021; Markman 2025; Perelman 2003 (arXiv:math/0307245); Platt, Trudgian 2021; Tao 2016.

Strony i pliki spoza bibliografii, których badacze nie otworzyli:

- strona OpenAI o problemie Naviera–Stokesa oraz praca OpenAI o 166 stronach;
- arXiv:2610.08144, arXiv:2502.03415, arXiv:2603.20268;
- oświadczenie komitetu w pliku PDF serwisu KITP z 2026-11-09;
- komunikaty CMI z 2010-03-18 i z 2010-07-01;
- wykład Steina z 2011 r. (serwer zwrócił HTTP 522) oraz praca Cohena arXiv:1809.10904;
- prace Goldfelda, Kuo i Murty'ego oraz Conrada.

Zdania oparte na pamięci badacza:

1. Mattuck i Tate wyprowadzają nierówność Castelnuovo–Severiego z twierdzenia Riemanna–Rocha. Ujęcie przez ujemną określoność formy przecięcia pochodzi od Grothendiecka. Jeżeli to zdanie jest prawdziwe, to opis dowodu 1 pasuje do pozycji Grothendieck 1958.
2. Baker, Gill i Solovay podają wyrocznię $A$ z $P^A = NP^A$ i wyrocznię $B$ z $P^B \neq NP^B$. Poprawka 15 opiera się na tym zdaniu.
3. Razborov i Rudich opublikowali wersję konferencyjną na STOC 1994.
4. Aaronson i Wigderson użyli podtytułu „a new barrier in complexity theory” w wersji STOC 2008.
5. Praca Levina ma strony 115–116 i przekład w „Problems of Information Transmission” 9(3), s. 265–266.
6. Wersja argumentu Shannona dla obwodów z bramkami pochodzi z późniejszych prac, na przykład Mullera z 1956 r.
7. Przegląd Aaronsona „P =? NP” ukazał się w tomie „Open Problems in Mathematics” (Springer, 2016).
8. Praca Perelmana arXiv:math/0303109 ma datę 2003-03-10.
9. Standardowym odsyłaczem dla wyniku „wymiar co najwyżej 5” są Moonen i Zarhin (1999) `[założenie]`.
10. Kodaira i Spencer w 1953 r. są autorami dowodu przez ciąg wykładniczy `[założenie]`; strona PNAS zwróciła HTTP 403.

Zdania znane tylko ze streszczeń wyszukiwarki:

1. W. Stein rozszerzył argument Kolyvagina na krzywą 389a. Badacz uznaje to zdanie za niewiarygodne.
2. Według Lüschera nieregularyzowany hamiltonian jest nieograniczony od dołu.
3. Preprint o modelu O(3) ma datę bliską 2026-10-21; datę badacz wyliczył z napisu „23 dni temu”.
4. Treść prac Connesa i Consaniego arXiv:2106.01715 oraz Connesa i van Suijlekoma.
5. Treść prac o enstrofii arXiv:2112.04923, arXiv:1409.2336, arXiv:2009.03980; badacz nie wie, która praca zawiera które zdanie.

Niespójności w notatkach:

1. Notatka z teorii liczb podaje numer arXiv:2511.22755 dla 2 różnych prac: Connes, van Suijlekom oraz Connes, Consani, Moscovici. Co najmniej 1 numer jest błędny.
2. Notatka z geometrii we wniosku podaje 2 pozycje z danymi do poprawki: Rubinstein i Voisin. Tabela tej notatki ocenia dane obu pozycji jako poprawne. Ten raport przyjmuje ocenę z tabeli.
3. Wikipedia nazywa zespół D. Grossa „independent team”. Scientific American podaje, że komitet powołała firma OpenAI.
4. Streszczenie pracy Cheskidova przypisuje Katzowi i Pavlović osobliwość w modelu z lepkością. Wstęp pracy Barbato i in. przypisuje Katzowi i Pavlović osobliwość w modelu bez lepkości.

Zdania pliku `REPORT.md`, których żadna notatka nie sprawdza:

1. Wiersz 261: „2 serwisy podają, że dowód OpenAI nie dotyczy problemu milenijnego.” Notatki nie wskazują tych 2 serwisów.
2. Wiersz 17, dowód 1: przypisanie metody pracom Mattucka i Tate'a oraz Grothendiecka. Oba twierdzenia są niepotwierdzone.
3. Rok 2000 opisu problemu autorstwa C. Feffermana. Wydruk w tomie „The Millennium Prize Problems” z 2006 r. też jest niesprawdzony.

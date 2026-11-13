/-
A figure computed and drawn by a Lean 4 program: the traces of the curve y² + y = x³ - x
over the fields F_p for the primes p < 200, inside the parabola a² = 4p.

Usage from the directory `lean`:  lake exe figure > ../figures/lean-hasse-bound.svg
The program exits with the code 1 if a trace violates a² ≤ 4p.
-/

/-- The number of points of y² + y = x³ - x over F_p, with the point at infinity. -/
def countPoints (p : Nat) : Nat := Id.run do
  let mut n := 1
  for x in [0:p] do
    for y in [0:p] do
      if (y * y + y) % p == (x * x * x + (p - 1) * x) % p then
        n := n + 1
  return n

def isPrime (p : Nat) : Bool :=
  p ≥ 2 && (List.range (p - 2)).all fun k => p % (k + 2) != 0

/-- The pairs (p, a) with a = p + 1 - N_p. The curve has bad reduction at p = 37. -/
def traces (bound : Nat) : List (Nat × Int) :=
  ((List.range bound).filter fun p => isPrime p && p != 37).map fun p =>
    (p, (p : Int) + 1 - (countPoints p : Int))

def width : Float := 900
def height : Float := 560
def left : Float := 70
def right : Float := 30
def top : Float := 118
def bottom : Float := 76
def pMax : Float := 200
def aMax : Float := 30

def px (p : Float) : Float := left + p / pMax * (width - left - right)
def py (a : Float) : Float := top + (aMax - a) / (2 * aMax) * (height - top - bottom)

/-- A number with 1 digit after the point, for SVG coordinates. -/
def num (x : Float) : String :=
  let scaled := (x * 10).round
  let sign := if scaled < 0 then "-" else ""
  let n := scaled.abs.toUInt64.toNat
  s!"{sign}{n / 10}.{n % 10}"

def text (x y : Float) (size : Nat) (fill anchor body : String) (weight : String := "normal") : String :=
  s!"<text x=\"{num x}\" y=\"{num y}\" font-size=\"{size}\" fill=\"{fill}\" text-anchor=\"{anchor}\" font-weight=\"{weight}\">{body}</text>"

def parabola (sign : Float) : String :=
  let points := (List.range 201).map fun i =>
    let p := i.toFloat
    s!"{num (px p)},{num (py (sign * 2 * p.sqrt))}"
  s!"<polyline points=\"{" ".intercalate points}\" fill=\"none\" stroke=\"#eb6834\" stroke-width=\"2\"/>"

def svg (data : List (Nat × Int)) : String :=
  let ink := "#0b0b0b"
  let ink2 := "#52514e"
  let grid := "#e1e0d9"
  let xTicks := [0, 50, 100, 150, 200].map fun (p : Nat) =>
    s!"<line x1=\"{num (px p.toFloat)}\" y1=\"{num (py (-aMax))}\" x2=\"{num (px p.toFloat)}\" y2=\"{num (py aMax)}\" stroke=\"{grid}\"/>"
      ++ text (px p.toFloat) (py (-aMax) + 20) 13 ink2 "middle" (toString p)
  let yTicks := [-20, -10, 0, 10, 20].map fun (a : Int) =>
    s!"<line x1=\"{num (px 0)}\" y1=\"{num (py (Float.ofInt a))}\" x2=\"{num (px pMax)}\" y2=\"{num (py (Float.ofInt a))}\" stroke=\"{grid}\"/>"
      ++ text (px 0 - 10) (py (Float.ofInt a) + 4) 13 ink2 "end" ((toString a).replace "-" "−")
  let dots := data.map fun (p, a) =>
    s!"<circle cx=\"{num (px p.toFloat)}\" cy=\"{num (py (Float.ofInt a))}\" r=\"4.5\" fill=\"#2a78d6\" stroke=\"#fcfcfb\" stroke-width=\"1.5\"/>"
  "\n".intercalate <|
    [s!"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 {num width} {num height}\" font-family=\"DejaVu Sans, Verdana, sans-serif\">",
     s!"<rect width=\"{num width}\" height=\"{num height}\" fill=\"#fcfcfb\"/>",
     text 24 36 19 ink "start" s!"Każdy ślad leży w paraboli: a² ≤ 4p dla {data.length} liczb pierwszych p &lt; 200" "bold",
     text 24 60 13 ink2 "start" "Krzywa y² + y = x³ − x nad ciałem o p elementach. Punkt: para (p, a), gdzie a = p + 1 − liczba punktów krzywej.",
     text 24 78 13 ink2 "start" "Linia pomarańczowa: parabola a² = 4p."]
    ++ xTicks ++ yTicks
    ++ [parabola 1, parabola (-1)] ++ dots
    ++ [text (px (pMax / 2)) (height - 34) 13 ink2 "middle" "liczba pierwsza p",
        text 24 (top - 8) 13 ink2 "start" "ślad a",
        text 24 (height - 10) 11 "#898781" "start" "Źródło: program lean/Figure.lean w języku Lean 4 liczy punkty krzywej i rysuje ten plik SVG.",
        "</svg>"]

def main : IO UInt32 := do
  let data := traces 200
  let violations := data.filter fun (p, a) => a * a > 4 * (p : Int)
  if violations.isEmpty then
    IO.println (svg data)
    return 0
  else
    IO.eprintln s!"violations of a² ≤ 4p: {violations}"
    return 1

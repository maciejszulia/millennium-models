/-
Kernels of the short proofs from REPORT.md, checked by Lean 4 with Mathlib.

Each theorem states the algebraic or logical kernel of 1 proof from the section
"Najkrótsze dowody". The geometric and analytic facts enter as hypotheses.
No theorem in this file proves an open problem.
-/
import Mathlib

namespace MillenniumModels

/-! ## Model 1 -/

/-- Proof 1 (Riemann in model 1). The intersection form is negative definite on the classes
orthogonal to `H` and `V`, so `-(r D' + s G', r D' + s G') / 2 = r² + a r s + p s²` is nonnegative.
A nonnegative form gives `a² ≤ 4p`. -/
theorem hasse_bound (a p : ℝ) (h : ∀ r s : ℝ, 0 ≤ r ^ 2 + a * r * s + p * s ^ 2) :
    a ^ 2 ≤ 4 * p := by
  nlinarith [h (-a) 2]

/-- Proof 2 (Hodge for classes of type (1,1)). In an exact sequence `A → B → C` a class of `B`
that maps to 0 in `C` comes from `A`. Here `A = Pic(X)`, `B = H²(X, ℤ)`, `C = H²(X, 𝒪)`. -/
theorem class_comes_from_pic {A B C : Type*} [AddCommGroup A] [AddCommGroup B] [AddCommGroup C]
    (f : A →+ B) (g : B →+ C) (h : Function.Exact f g) (b : B) (hb : g b = 0) : ∃ a, f a = b :=
  (h b).mp hb

/-! ## Model 2 -/

/-- Proof 3 (Poincaré for the round sphere). If `d(r²)/dt = -4`, then `r²(t) = r²(0) - 4t`. -/
theorem sphere_radius (f : ℝ → ℝ) (hf : ∀ t, HasDerivAt f (-4) t) (t : ℝ) :
    f t = f 0 - 4 * t := by
  have h : ∀ x, HasDerivAt (fun s => f s + 4 * s) 0 x := fun x => by
    have h1 : HasDerivAt (fun s => f s + 4 * s) (-4 + 4 * 1) x :=
      (hf x).add ((hasDerivAt_id x).const_mul (4 : ℝ))
    have h2 : (-4 : ℝ) + 4 * 1 = 0 := by norm_num
    rw [h2] at h1
    exact h1
  have hc := is_const_of_deriv_eq_zero (fun x => (h x).differentiableAt) (fun x => (h x).deriv) t 0
  simp at hc
  linarith

/-- The sphere of proof 3 vanishes at the time `T = r₀² / 4`. -/
theorem sphere_vanishes (r0 T : ℝ) : r0 ^ 2 - 4 * T = 0 ↔ T = r0 ^ 2 / 4 := by
  constructor <;> intro h <;> linarith

/-- Proof 4 (Yang–Mills cross-section), steps 2 and 3, for expectation values in 1 state:
`tx`, `ty` are the kinetic terms, `v` is the term `x²y²`, `ax`, `ay` are the terms `|x|`, `|y|`.
The oscillator bounds `ax ≤ ty + v` and `ay ≤ tx + v` give `-Δ + |x| + |y| ≤ 2H`. -/
theorem two_h_bound (tx ty v ax ay : ℝ) (h1 : ax ≤ ty + v) (h2 : ay ≤ tx + v) :
    (tx + ty) + ax + ay ≤ 2 * (tx + ty + v) := by
  linarith

/-- Proof 11 (Navier–Stokes in model 2), step 3, with squares in place of the square root.
The dimension is `d + 2`. The model gives `U'² = θ λ^(d+2) U²`, and the eddy size falls from
`l` to `l / λ`, so `Re'² = θ λ^d Re²`. -/
theorem reynolds_step (U U' l lam nu theta : ℝ) (d : ℕ) (hlam : lam ≠ 0) (hnu : nu ≠ 0)
    (hU : U' ^ 2 = theta * lam ^ (d + 2) * U ^ 2) :
    (U' * (l / lam) / nu) ^ 2 = theta * lam ^ d * (U * l / nu) ^ 2 := by
  have h : (U' * (l / lam) / nu) ^ 2 = U' ^ 2 * l ^ 2 / (lam ^ 2 * nu ^ 2) := by
    field_simp
  rw [h, hU]
  field_simp
  ring

/-! ## Model 3 -/

/-- The function OR of `n` bits. -/
def orN {n : ℕ} (x : Fin n → Bool) : Bool := decide (∃ i, x i = true)

/-- Proof 5 (P vs NP in the query model): a certificate for the answer 1 has 1 bit. -/
theorem certificate {n : ℕ} (x : Fin n → Bool) (i : Fin n) (h : x i = true) : orN x = true := by
  simp only [orN, decide_eq_true_eq]
  exact ⟨i, h⟩

/-- Proof 5: the adversary answers 0. Queries at the positions `S` that miss the position `i`
leave 2 inputs that agree with the answers and have different values of OR. -/
theorem adversary {n : ℕ} (S : Finset (Fin n)) (i : Fin n) (hi : i ∉ S) :
    ∃ x y : Fin n → Bool, (∀ j ∈ S, x j = false ∧ y j = false) ∧ orN x ≠ orN y := by
  refine ⟨fun _ => false, fun j => decide (j = i), ?_, ?_⟩
  · intro j hj
    refine ⟨rfl, ?_⟩
    simp only [decide_eq_false_iff_not]
    rintro rfl
    exact hi hj
  · simp [orN]

/-- Proof 5: fewer than `n` queries do not determine OR of `n` bits. -/
theorem fewer_queries_fail {n : ℕ} (S : Finset (Fin n)) (h : S.card < n) :
    ∃ x y : Fin n → Bool, (∀ j ∈ S, x j = false ∧ y j = false) ∧ orN x ≠ orN y := by
  obtain ⟨i, hi⟩ : ∃ i, i ∉ S := by
    by_contra hall
    have hS : S = Finset.univ := Finset.eq_univ_of_forall fun i => by
      by_contra hi
      exact hall ⟨i, hi⟩
    simp [hS] at h
  exact adversary S i hi

/-- Proof 6 (counting circuits). If there are fewer circuits than functions, then at least
1 function has no circuit. -/
theorem counting {Circuit Fn : Type*} [Fintype Circuit] [Fintype Fn] (eval : Circuit → Fn)
    (h : Fintype.card Circuit < Fintype.card Fn) : ∃ f : Fn, ∀ c, eval c ≠ f := by
  by_contra hall
  have hsurj : Function.Surjective eval := fun f => by
    by_contra hf
    exact hall ⟨f, fun c hc => hf ⟨c, hc⟩⟩
  exact absurd (Fintype.card_le_of_surjective eval hsurj) (not_le.mpr h)

/-- Proof 6: the number of Boolean functions of `n` variables is `2 ^ 2 ^ n`. -/
theorem card_boolean_functions (n : ℕ) : Fintype.card ((Fin n → Bool) → Bool) = 2 ^ 2 ^ n := by
  simp

/-- Proof 12. If polynomial-time algorithms give polynomial-size circuits and satisfiability
has no polynomial-size circuits, then satisfiability has no polynomial-time algorithm. -/
theorem missing_step_gives_p_ne_np (PolyTime PolyCircuits : Prop) (h : PolyTime → PolyCircuits)
    (step : ¬PolyCircuits) : ¬PolyTime :=
  fun a => step (h a)

/-! ## The two-thread algorithm -/

/-- Proofs 7 and 8. If a witness exists, then the search `k = 0, 1, 2, …` stops at the least
witness. A witness is a proof, a refutation or a counterexample. -/
theorem search_halts (P : ℕ → Prop) [DecidablePred P] (h : ∃ k, P k) :
    P (Nat.find h) ∧ ∀ k, P k → Nat.find h ≤ k :=
  ⟨Nat.find_spec h, fun _ hk => Nat.find_min' h hk⟩

/-- Proof 9. If each counterexample gives a refutation and the theory has no refutation,
then the statement `∀ n, W n` is true. -/
theorem undecided_pi1_is_true (W : ℕ → Prop) (Refutable : Prop) (h : (∃ n, ¬W n) → Refutable)
    (hn : ¬Refutable) : ∀ n, W n := by
  intro n
  by_contra hw
  exact hn (h ⟨n, hw⟩)

/-- Proof 10, the last step. An algorithm that recognises "the theory does not decide the
statement" gives a decision procedure for the halting problem, and no such procedure exists. -/
theorem no_recogniser (Recogniser HaltingDecider : Prop) (h : Recogniser → HaltingDecider)
    (turing : ¬HaltingDecider) : ¬Recogniser :=
  fun r => turing (h r)

/-- Proof 10: the halting problem is undecidable (Turing 1936), from Mathlib. -/
theorem halting_problem (n : ℕ) : ¬ComputablePred fun c => (Nat.Partrec.Code.eval c n).Dom :=
  ComputablePred.halting_problem n

end MillenniumModels

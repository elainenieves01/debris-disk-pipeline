# Debris disk stirring: 15-minute talk (rough draft)

Target: ~13 slides, about 1 min each, with the intro animation running longer on slide 2.
Items marked **[fill]** or **[check]** are things I could not confirm from the repo.

---

## Part 1: What is a debris disk? (~3.5 min)

### Slide 1. Title (0:15)
- Title: "How stirred is a debris disk? Self-stirring in N-body simulations"
- Name, affiliation, advisor/collaborators **[fill]**

### Slide 2. What is a debris disk? (1:30) ← your animation
- Belt of rock and ice leftover from planet formation, orbiting a main-sequence star (like the asteroid and Kuiper belts)
- Too much dust for its age: grains are removed in ~Myr by radiation pressure and Poynting-Robertson drag, so the dust must be continuously resupplied
- Resupply comes from collisions between larger planetesimals, which are never seen directly
- Narration over the animation: planetesimals collide, break apart, make dust, and we observe the dust
- Speaker note: say what the animation shows before it plays (what the dots are, what is being stirred)

### Slide 3. Why they matter (1:00)
- Fossil record of planet formation: the belt's size, mass and structure record how planetesimals formed
- Planet signposts: gaps, warps, sharp edges and asymmetries can point to unseen planets
- Context for our own system: Kuiper belt analogs, and the dust environment of habitable-zone planets
- Observational hook: resolved with ALMA/JWST/HST; the target in your configs is a ~100 AU belt (HD 216435? **[check which system your ntfy topic and a=100 AU belt are based on]**)

### Slide 4. The puzzle: collisions need stirring (0:45)
- Collisions only destroy planetesimals (and make dust) if relative velocities are high enough: v_rel ~ e·v_K
- A primordial disk is dynamically cold (e ~ 0, i ~ 0), so something must excite orbits
- Question for the rest of the talk: **what stirred the disk, and when?**

---

## Part 2: Stirring and how we measure it (~3.5 min)

### Slide 5. Two ways to stir (1:00)
- **Self-stirring**: the largest planetesimals (Pluto-size and up) gravitationally excite the rest; no planet needed
- **Planet stirring**: a giant planet's secular and resonant perturbations excite the belt
- **Stirring by a stellar flyby or a nearby star** (one line, skip if short on time)
- Diagram: cold belt, then (a) big bodies in the belt or (b) a planet interior to the belt
- Key distinction to set up the rest: self-stirring has a **time-dependent, outside-in "stirring front"**; a planet acts on a secular timescale

### Slide 6. Quantifying stirring: eccentricity (1:15)
- Define the RMS eccentricity of the disk, e_rms(t), and the inclination dispersion
- Why e_rms matters: sets collision velocity, collisional cascade rate, and the radial and vertical thickness of the disk
- Expected scaling: e_rms grows as a power law, e ∝ t^p (Krivov & Booth 2018 **[check the exponent you compare against and quote it]**)
- Show the equation for C_e (your coefficient from the Krivov & Booth comparison) **[fill the definition]**

### Slide 7. How we measure it from observations (1:15)
- Disk **width and radial profile** (ΔR/R, from resolved images) → e_rms
- Disk **scale height / vertical thickness** (edge-on systems) → i_rms
- Dust **brightness vs. age**: collisional evolution depends on v_rel
- Caveat: observations see the dust; we infer planetesimal stirring (this is where simulations help)

---

## Part 3: My simulations (~6.5 min)

### Slide 8. Simulation setup (1:15)
- Code: REBOUND with the Mercurius hybrid integrator (handles close encounters), N-body with full mutual gravity among the massive planetesimals
- Belt at 100 AU, 95–105 AU wide; initial e, i ≈ 3×10⁻⁵ (dynamically cold)
- 800 massive planetesimals (MPs) + optional test particles (TPs) that feel gravity but do not stir
- Total belt mass 1 or 10 M⊕; MP masses drawn from a power-law size distribution, slope q (q = 3.5 is the collisional equilibrium value; I also vary q = 2.5, 4.5 and a uniform-mass case)
- Semimajor axes: uniform, or a Lorentzian peak around 100 AU (newest runs)
- Show: schematic of the setup plus the size distribution

### Slide 9. Reproducible pipeline (0:30)
- Each run writes frozen config, git commit, environment and a run report; runs are dispatched to a lab machine over SSH
- One line only, unless the audience cares about this

### Slide 10. Result: e_rms grows as a power law (1:30)
- Figure: `calibration/rms_e_all_runs_overlay.png`
- All runs: e_rms ∝ t^p with **p ≈ 0.20–0.25** (from `rms_e_all_runs_fits.md`); 1 M⊕ q = 3.5 run: p = 0.25 over 10 Myr
- Takeaway: slope is robust to mass model and total mass; the amplitude changes (A ≈ 2.8×10⁻⁴ for 1 M⊕ uniform vs. 1.4×10⁻³ for 10 M⊕)
- Compare with the Krivov & Booth prediction **[say whether this agrees; the repo has a comparison for 500 kyr runs]**

### Slide 11. Dependence on the disk parameters (1:15)
- Mass: ×10 mass gives ×~5 in amplitude
- Size distribution slope q: shallow vs. steep slopes change how much of the mass is in the stirrers
- Stirrer mass ("10×, 30×, 50× Stir" runs, 100 Myr): more massive stirrers give a faster rise, A ≈ 1.4×10⁻³ → 2.8×10⁻³
- Test particles trace the same stirring as the massive bodies (p ≈ 0.20 vs 0.22) **[check wording]**
- Show: `rms_e_all_runs_plus_stir_overlay.png`

### Slide 12. Calibration against published models (0:45)
- 100 Myr run recreating the Krivov configuration with Mercurius, used to validate the setup against theory
- State the result **[fill: does it reproduce the published growth?]**

### Slide 13. Next step: add a planet (1:15)
- Currently `giant_planet: null`; the code already supports a giant planet (a–e/a–i figures mark it)
- Questions:
  - Does a planet stir faster than self-stirring? By how much, and out to what radius?
  - Does it truncate or warp the disk, and does secular forcing add structure that e_rms alone misses?
  - Can we tell planet-stirred from self-stirred disks from observables (width, thickness, edge sharpness)?
- Parameter plan: planet mass, a, e **[fill]**
- Timeline for results **[fill]**

### Slide 14. Summary (0:30)
1. Debris disks need stirring to make dust; stirring tells us about planet formation
2. Self-stirring in N-body runs gives e_rms ∝ t^~0.25, robust across mass models
3. Next: add a planet and compare the signatures

(Backup: questions slide, extra figures: a–e evolution, survival, Rayleigh outlier cut)

---

## Timing check

| Part | Min |
|---|---|
| Intro + animation (1–4) | 3.5 |
| Stirring + measurement (5–7) | 3.5 |
| Simulations (8–12) | 5.5 |
| Planet + summary (13–14) | 2.0 |
| Questions buffer | ~0.5 |

Total ≈ 15 min. If running long, cut slides 9 and 12 first.

## Figures already in the repo
- `calibration/rms_e_all_runs_overlay.png`: e_rms vs time for all runs (slide 10)
- `calibration/rms_e_all_runs_plus_stir_overlay.png`: adds the stirrer-mass runs (slide 11)
- `calibration/rms_e_all_runs_fits.md`: power-law fit table
- Per-run figures in `outputs/<name>/figures/` (a–e initial/final, survival)

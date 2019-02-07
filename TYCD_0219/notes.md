15 minutes, to showcase my PhD work

- include paper references
- include reference to effmass code

- Introduce myself and the group
- This is the theory and simulation of materials, so much of our work is about building models.
- And that is because we can't solve the schrodinger equation directly
- So like many others here I use DFT which approximates as exchange correlation is not exact. Predict ground state properties of a static lattice- but we want to predict more than this so we put other approximations on top: athermal so we introduce lattice vibrations, static but interested in dynamics of carriers so we introdcue concepts like effective mass.
Both of the approximations commonly used here is the harmonic or parabolic approximation.
- We approximate that as an atom moves away from it's site it is parabolic in energy - near the minimum the energy well is approximated by a parabolic
- We assume that KE of electron is parabolic.
- Parabolic approximation is nice, as we only need to make three calculations: or 2 if we use symmetry. 
- Much of my PhD has been based around: what if these aren't parabolic? What are the consequences for material properties?

- Let's start with effective mass
- under parabolic there is a single effective mass
- we can introduce a Kane term which means effective mass increases with energy
- we have calculated this for a number of materials in PV (outline what they are)
- Moss Burstein shift
- show that the mobility decreases (x2 papers). This is where I introduce perovskite better and reference perspective.

- then the phonons
- show crystal potential expanded
- just harmonic terms: infinite lifetimes
- show imaginary phonon modes, and what these correspond to. 
- band gap, thermal conductivity - reference
- polaron model and rate of cooling (tie to experimental measures) - reference


## Talk outline

Start with introduction: we need low-carbon energy. From a number of sources, one of which is the sun, which gives plentiful energy. Silicon is really good at what it does, but want to keep lowering cost to make it competitive. The way to do this is to increase the efficiency of the cell. HHP are under developing and promising as cheap. Currently being developed for use in commercial tandem (world record). Despite it's succes there is a lot we don't know about this material - it's an active area of research.

One commonly used experimental tool is PL. Carrier concentration increases and the fermi level increases to x and carriers are hot (above band gap energy). Simplified models are used - a single, parabolic band whose curvature is described by an effective mass. The effective mass a critical parameter in models for the optical and transport properties of a semiconductor.  However, experimental measurements of the effective mass in the hybrid halide perovskite MAPI vary widely, from $0.09-0.23\, m_e$. However, we know that the picture is more complicated than this. First project is to understand how the non-parabolicity, change in curvature, effects the physical properties of the bulk material: consequences for concentrator systems. MAPI more non-parabolic than the other materials. Developed software for calculating the effective mass, accounting for non-parabolicity, and available here.

When a carrier is excited, it cools emitting phonons. Slow cooling of carriers in the perovskites. With Jarvist Frost, we developed a model: the electron forms a polaron, then the heat dissipates from this solid sphere. The thermal conductivity is ultra-low, so the rate of cooling is slow. This accounts for the slow cooling.

So far I have considered bulk properties. But we know there are many defects in MAPI, and that these can heavily influence device performance. The rapid transport of ions at room temperature suggests a high concentration of mobile point defects,  We are particularly worried about defects in the band gap. These can form sites where electrons and hole recombine, so that they cannot reach the contacts to produce energy. Calculations indicate that a H-centre is formed, with a self trapped hole. Currently investigating the vibrational properties of this defect.

Last slide: Names of people associated with each project. Open source tools.

Following slides: Put many!


- effective mass theory. Many useful quantaties can be gotten from effective mass...
   - but the effective mass varies according to carrier density experimentally. Several reasons for this, one of these is linked to parabolicity. 
	- the parabolic approximation: effective mass is independant of carrier concentration
	- at high carrier concentrations the dispersion is non-parabolic - 
	- to persuade you of this: see the BM shift. This is the BM shift calculated assuming no, predicted BM shift for parabolic, nonparabolic
	- so the mass of the electron increases with carrier concentration
	- and the mobility (limited by optic-modes) will decrease accordingly






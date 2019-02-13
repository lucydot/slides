TODO:
- check projection on the screen which will be used.
- add in experimental motivation (reference other peoples work!)
- include my own paper references, and reference effmass code
- check timing (15 mins)

Abstract:

I use density functional theory to calculate the electronic and vibrational properties of thin-film photovoltaic materials. The majority of my PhD research has focused on hybrid halide perovskites. These materials are markedly different from their predecessors in photovoltaics – both organic and inorganic (e.g. CdTe, GaAs) – and present a number of simulation challenges [1]. 
Although the carrier concentration in a hybrid halide perovskite under one sun does not exceed 1016cm3, it can reach densities of 1019 cm3 under laser excitation for photoluminescence (PL) studies. I will use Effective Mass Theory to quantify the extent of electronic band non-parabolicity in CH3NH3PbI3 (MAPI). I will show that band non-parabolicity has a significant impact upon the optical effective mass, Burstein-Moss band gap shift and carrier mobility in the high carrier density regime [2]. I will also show that the slow thermalisation of above bandgap carriers, observed in PL studies, can be explained by using a classical heat diffusion model to calculate the rate of polaron cooling [3]. 
In the second half of my talk I will consider an imperfect crystal structure where the translational symmetry has been broken with a point defect. I will outline the lattice distortion and electronic localisation incurred when a H-centre (iodine split-interstitial with self-trapped hole) is formed in MAPI [4]. I will present on-going work related to identifying the vibrational states of this defect. 


Images:
- perovskite: https://www.comsol.com/blogs/piezoelectric-materials-crystal-orientation-poling-direction/
- silicon: https://archive.cnx.org/contents/e593b628-c26b-4e33-ba06-9f7de2989a4c@3/introduction-to-semiconductors

TODO: 

*Slide 1: Distortions and Defects in Hybrid Halide Perovskites*

Hello, my name is Lucy, and my talk is about distortions and defects in hybrid halide perovskites.

*Slide 2: Materials Design Group*

I am a PhD student in the materials design group led by Aron Walsh, here at Imperial. There are several research strands in the group, the part I am involved with focuses on the optimisation of materials for energy generation and storage. I'd say compared to other research groups in the TYC, we are focused more on applications than method development. We want to build accurate models and use the latest computational techniques, whilst always keeping the question 'but what consequences will this have for important physical properties?' at the forefront." Hopefully you will see that in my talk today - I will describe how I have modelled particular distortions or defects, and then outline what impact that will have on certain optical or transport properties.

Slide 3: Photovoltaic materials

So today I will talk about a photovoltaic material . Silicon currently dominates the market, is really good at what it does, and in some markets it is already the cheaper than fossil fuels. But to lower costs further, we need to increase the efficiency of the cell - the efficiency at which light is converted to electricity. Silicon is at 26.7%. HHP, which are the subject of my talk today, are at 20.9%, but they have the potential to be much more cheap than silicon solar cells. Researchers are now working to combine silicon and HHP in a tandem cell. Despite this success, There are improvements to be made around efficiency and stability - and there remains a lot unknown about the basic physical processes in this material - it's an active area of research.

Slide 4: Hybrid Halide Perovskites

Hybrid halide perovskites are formed by a series of inorganic octahedra  – each octahedra contains a metal and a halide. The octahedra form a cage within which an organic molecule sits. 
One of the most popular hybrid halide perovskites for PV research is methylammonium lead iodide and that is the one I will be focusing on today - I will call this MAPI.
Now this is a perfectly static picture, but that’s misleading. The hybrid halide perovskties are relatively soft materials with plenty of movement. The octahedra are continually tilting back and forth at room temperature, this motion is coupled to the molecule in the centre which is rotating. On top of that, there is ionic migration associated with the halide sub lattice. There are several interacting processes, across different timescales, and so this can be a challenging system to model.

Slide 5: Outline

I want to talk about 3 things today. The first is related to the concept of effective mass. We are interested in the effective mass because it is a critical parameter in models for the optical and transport properties of a semiconductor. 

Slide 5: Non-degenerate semiconductor

When a solar cell is operating beneath the sun, there is a relatively low carrier density of electrons and holes. At these low carrier densities the electronic bands can be approximated as parabolic, so they can be approximated with this dashed line.
When we calculate the effective mass of the carriers using this definition - we see that for a parabolic band, the effective mass is constant.


Slide 6: Degenerate semiconductor

However as the carrier density is increased - under illumination for a photoluminescence study, forexample - the carrier density increases. And at a certain carrier density, the bands can no longer be approximated with a parabola.
So we now approximate the electronic dispersion with two parameters - the mass at band edge, and the alpha parameter. 
This alpha parameter describes a flattening of the bands away from and edge. When alpha = 0 we have a perfectly parabolic dispersion.
And when we apply our definition for effective mass, we see that the effective mass increases as we move away in energy from the band edge. So this E here, thats referenced to the band edge. 

And my research questions for this project were:
What is the extent of band non-parabolicity in MAPI?
To what extent does this affect the effective mass and mobility of electrons?

slide 7: The alpha parameter

So we are able to quantify the extent of non-parabolicity with the alpha parameter.
alpha parameter of zero: perfectly parabolic
MAPI -perovskie
cdTe another PV material
Use Density Functional Theory to calculate the bandstructure of this material. cite effmass code.
Explain why I expect hole to be non-parabolic than electron

slide 8: the optical effective mass

slide 9: electron mobility

(so the title of my talk is distortions and defects that was my first distortion - a non-parabolic distortion. The second distortion is related to the atomic lattice)

slide 10: Lattice anharmonicity


phonon dispersion, linked to tilting of the lattice.
What affect does this have on optical properties?

Slide 11: Band Gap broadening


Electron-Phonon coupling
Map along the modes to calculate electronic structure. See a band gap broadening in the material.
Reference Jarvist work here

(now the final section of my talk where I will briefly outline defect)
So far considered distortions in the bulk. But we know that defects induce distortions in the surrounding lattice and through this mechanism they form centres for recombination

Slide 12: Killer defects

Slide 13: V-centres in MAPI 

We have predicted this defect
Link to experimental.

Slide 14: Summary


Defects and distortions combined
- What is the rate of carrier capture at a defect site?

Slide 15: Thank you!


Questions: 
- agreement with experiment (ffective mass)

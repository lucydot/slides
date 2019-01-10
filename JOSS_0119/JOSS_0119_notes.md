JOSS talk - 
Publishing your Software Project with the Journal of Open Source Software

INTRO
Hello, I'm Lucy and I am a PhD student in the materials department, I'm in the group of Aron Walsh - who is in the audience, along with a couple of other group members. 
We model materials on the atomic scale -  we are interested in the properties of the electrons and atoms, and how these properties can be tuned to design, for example, more efficient solar cells. To do this, we run calculations on supercomputers and we make use of codes like the ones which Laura develops. We also write our own code, smaller pieces of code which are published on github


- Effmass as an example code - this is a python package for calculating the effective mass of an electron in a semiconductor. Me, extended from another person. Other people using it, contributing to it.
- This accompanies a scientific study which is in review in a traditional journal. So I see this software package as a potentially useful tool for other researchers, but it also enables all the results in my paper to be reproduced.
- And also reviewed - so I have a fair feel for what they are looking for now.


It benefitted me, I learnt a lot from the process, but more importantly, I think publishing software is important for the scientific community.

- make sure outline basics at the beginning - who I am, the research group
- who I am: my perspective.
- highlight difference with Laura - keen to reflect the broad ways in which people write software.
-  I have submitted and I have reviewed for JOSS> Effective mass. This wa

- Before I continue I want to emphasise that JOSS works quite differently from other academic journals. Your work does not need to be on the cutting edge of software development - if it does something new, or does something better - easier to use, or faster  - for example, and follows this best practice, then it will get published.
It's there to promote best practice, and to give scientists and engineers appropriate credit for the work they do. This ties to what Jeremy mentioned earlier, developers getting appropriate credit. Its designed to improve the quality of software submitted through a peer review process.
JOSS addresses the dearth of rewards for key contributions to science made in the form of software. 
- I want other people to use my code, I see my code as a contribution - like toher scientific output - should be peer review
- current practices in publication/citation fo not recognise software as a research output 

Before I move onto  the submission workflow, I want to talk a little more about why JOSS is a great journal and why we should ll be submitting our softwsre to it
MOTIVATION
- so why publish with JOSS? Mention JORS also.
- motivation: two levels: personal: starting out: increase skills nad confidence, established: get recognition. the  we used to communicate methods in paper. could be contained. But now, the methods: the scripts, the workflow, are not in the paper. Not in the SI. Reproducibility crisis. To advance w need to build on previous work, to build on previous work we need to be able to reproduce the eresults. Traditional academic journals don't allow for this (though this is changing...) - we need a way to publish this so people can reproduce and, even better, extend, what we are doing. Impact - when people using or extending your code.
Aswell as the community getting better tested, documented code - really if we zoom out 
- avoid single-use software
software journals provide best alternative to link sotware outputs into traditional research structures.
- most of us will have had the experience of reading a computational paper, but not having access to the code, and unable to reprodce the results.
- if most time coding: recognition
- iflike me, new to many of the tools, provides incentive and space

community get well-documented

- unit tests written using the `pytest` framework
- continuous integration using `Travis CI`

PROCESS

- it is free to submit: volunteer, £ per article.
- an open process , through github.
- paper is a single side of A4 - looking for scholarship contained in the software itself. In the past a paper would be written, peer reviewed, pointing to the software. Here the software takes the place of the paper.

- The article is the entry point of a JOSS submission, which encompasses the full set of software artifacts. Submission and review proceed in the open, on GitHub. Editors, reviewers, and authors work collaboratively and openly. Unlike other journals, JOSS does not reject articles requiring major revision; while not yet accepted, articles remain visible and under review until the authors make adequate changes (or withdraw, if unable to meet requirements). Once an article is accepted, JOSS gives it a digital object identifier (DOI), deposits its metadata in Crossref, and the article can begin collecting citations on indexers like Google Scholar and other services

WHAT JOSS LOOK FOR
- not a standard process
- on github
- fully transparent
- Tesitng / documentation with effmass case study
Because software articles are “advertising” and simply pointers to the actual scholarship (the software), short abstract-length submissions are sufficient for these “advertisements.”

- combination of this and Jupyter notebook.

Final thoughts
- Esimtate of time invested.
- People are using my code (issue tracker, finding bugs, good thinkg) - and I am happy to have had it looked over
- end: speak to me, I'm interested in extending - funding. If you want to take par as participant, or help deliver .






- Compare working on large code base to working on smaller, perhaps with a couple of other people, who are often working in same lab
- Challenges are different
- How do you get recognition for this work? (Link to the RSE idea as a whole) Time spent writing, and the recognition it gets. 
- You could say - well, its part of process, this is science, the numbrs are your reward. But...No incentive for *quality*
- JOSS - write documentation, write testing. Incentivies / justifies.

- should mention other journals - JORS
- End: I'd like to help others to publish, if you have questions - contact me and I'd be happy to meet and support where I can. Discuss afterwards.
- sign up to be a reviewer
- available here lucydot.github.com/slides


“An article about a computational result is advertising, not scholarship. The actual scholarship is the full software environment, code and data, that produced the result”

final thoughts: for people already doing testing and documentation, I think JOSS could be very good for getting acknowledgement for your work. For people who don't currently but want to learn more, JOSS gives a great incentive. I think as a research community we should be supporting each to do this through training, code review or mentoring.
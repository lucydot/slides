### Publishing your Software Project with the Journal of Open Source Software
Lucy Whalley

#### INTRO
Hello, I'm Lucy and I am a PhD student in the materials department, I'm in the group of Aron Walsh - who is in the audience, along with a couple of other group members. 
We model materials on the atomic scale -  we are interested in the properties of the electrons and atoms, and how these properties can be tuned to design, for example, more efficient solar cells. To do this, we run calculations on supercomputers, using DFT codes like the ones which Laura develops. We also write our own code, but these tend to be smaller pieces of code used for post-processing the DFT output.

Effmass is an example of this. This is a python package for calculating the effective mass of an electron in a semiconductor. I think the story of effmass will be familiar to other people - I started my PhD, and was asked to extend an existing code. This grew into a standalone package, effmass, which I published with JOSS so that I am able to share this with other people who can use and contribute to it.
Effmass is accompanied by a scientific study which is in review with a more traditional research journal. So I see effmass as a tool that can be used and extended by other researchers, but it also enables all the results in my paper to be reproduced.

Before I continue I want to emphasise that JOSS works quite differently from other academic journals. Your work does not need to be on the cutting edge of software development - if you can demonstrate that there is a need for it, for example it may be easier to use, or faster than existing tools, and if it follows best practice, then it will get published.

Before I move onto the submission and review workflow, I want to talk a little more about why JOSS is beneficial to the individual, but also the scientific community as a whole.

#### MOTIVATION

Sp, what are the benefits to the individual?
Firstly, JOSS will give you credit for the work you do - this links to what Laura and Jeremy mentioned earlier - if you contribute to science via software, this should be recognised, and with JOSS you get a published paper and possible citations.
The following three points are drawn from my personal experience.
Secondly, JOSS gives an incentive to learn new tools and to use best practice in your work. This was certainly true for myself. Before preparing my JOSS submission, I had limited experience with documentation and testing, and I had never used continous integration. I was able to legitimise to myself the time spent learning these tools as it would lead to a publication.
I found that I was more confident in sharing my code once it had been through a peer review process.
And, because the reviewers are often from your field of research, it was a good way to promote my code to those who may use it.

Now, what about benefits to the wider scientific community?
With each JOSS submission there is another well-documented and well-tested piece of software freely available to the community.
Zooming out from this to consider one of the central features of the scientific process - reproducibility

 the  we used to communicate methods in paper. could be contained. But now, the methods: the scripts, the workflow, are not in the paper. Not in the SI. Reproducibility crisis. To advance w need to build on previous work, to build on previous work we need to be able to reproduce the eresults. Traditional academic journals don't allow for this (though this is changing...) - we need a way to publish this so people can reproduce and, even better, extend, what we are doing. Impact - when people using or extending your code.
Aswell as the community getting better tested, documented code - really if we zoom out 
- most of us will have had the experience of reading a computational paper, but not having access to the code, and unable to reprodce the results.
Its designed to improve the quality of software submitted through a peer review process.


#### THE JOSS WORKFLOW

- it is free to submit: volunteer, <£3 per article.
- an open transparent process , through github.
- paper is a single side of A4 - looking for scholarship contained in the software itself. In the past a paper would be written, peer reviewed, pointing to the software. Here the software takes the place of the paper.
 My code was also improved as a result of the peer review process.

- The article is the entry point of a JOSS submission, which encompasses the full set of software artifacts. Submission and review proceed in the open, on GitHub. Editors, reviewers, and authors work collaboratively and openly. Unlike other journals, JOSS does not reject articles requiring major revision; while not yet accepted, articles remain visible and under review until the authors make adequate changes (or withdraw, if unable to meet requirements). Once an article is accepted, JOSS gives it a digital object identifier (DOI), deposits its metadata in Crossref, and the article can begin collecting citations on indexers like Google Scholar and other services

#### TESTING AND DOCUMENTATION

- Tesitng / documentation with effmass case study
Because software articles are “advertising” and simply pointers to the actual scholarship (the software), short abstract-length submissions are sufficient for these “advertisements.”

- combination of this and Jupyter notebook.


- unit tests written using the `pytest` framework
- continuous integration using `Travis CI`

#### FINAL THOUGHTS

- motivation: two levels: personal: starting out: increase skills nad confidence, established: get recognition.

- acnkowledge that there is a time investment, but worth it.
- People are using my code (issue tracker, finding bugs, good thinkg) - and I am happy to have had it looked over
- should mention other journals - JORS
- sign up to be a reviewer - I have done this, and enjoyed the process.
- available here lucydot.github.com/slides

final thoughts: for people already doing testing and documentation, I think JOSS could be very good for getting acknowledgement for your work. For people who don't currently but want to learn more, JOSS gives a great incentive. I think as a research community we should be supporting each to do this through training, code review or mentoring.

“An article about a computational result is advertising, not scholarship. The actual scholarship is the full software environment, code and data, that produced the result”

 










### Publishing your Software Project with the Journal of Open Source Software
Lucy Whalley

#### INTRO
-----
Hello, I'm Lucy and I am a PhD student in the materials department and I'll be speaking over the next 10-15 minutes about publishing your software project with the journal of open source software - and when I refer to this journal I'm going to use the acronym JOSS.

So I'm a PhD student in the MDG group here in the materials department at Imperial, the group is led by aron walsh.
We model materials on the atomic scale -  we are interested in the properties of the electrons and atoms, and how these properties can be tuned to design, for example, more efficient solar cells. To do this, we run calculations on supercomputers, using DFT codes like the ones which Laura develops. We also write our own code, but these tend to be smaller pieces of code used for post-processing the DFT output.
-----
Effmass is an example of this. This is a python package for calculating the effective mass of an electron in a semiconductor. I think the story of effmass will be familiar to other people - I started my PhD, and was asked to extend an existing code. This grew into a standalone package, effmass, which I published with JOSS.
Effmass is accompanied by a scientific study which is in review with a more traditional research journal. So I see effmass as a tool that can be used and extended by other researchers, but it also enables all the results in my paper to be reproduced.
-----
Before I continue I want to emphasise that JOSS works quite differently from other academic journals. Your work does not need to be on the cutting edge of software development - if you can demonstrate that there is a need for it, for example it may be easier to use, or faster than existing tools, and if it follows best practice, then it will get published. And once you have this best practice in place, the process should be quick.

Before I move onto the submission and review workflow, I want to talk a little more about why JOSS is beneficial to the individual, but also the scientific community as a whole.
-----
#### MOTIVATION
-----
Sp, what are the individual benefits?
Firstly, JOSS will give you credit for the work you do - this links to what Laura and Jeremy mentioned earlier - if you contribute to science via software, this should be recognised, and with JOSS you get a published paper and possible citations.
Well if you don't currently use documentation and testing, JOSS gives a great incentive to learn about these aspects of software development.
I found that I was more confident in sharing my code once it had been through a peer review process.
And, because the reviewers are often from your field of research, it was a good way to promote my code to those who may use it.

-----
Now, what about benefits to the wider scientific community?
With each JOSS submission there is another well-documented and well-tested piece of software freely available to the community.
But more than this, it enables reproducibile - this article has an inflammatary title but it's an interesting read. The author points out that the traditional research journal model was established 400 years ago. Back then you could fit the derivation and table of data on a single page, but that's not the case now. Our methods now, increasingly, consist of various scripts, pieces of software - and if these are not reported then the results are not reproducible. JOSS provides a way to publish our computational methods, it enables reproducible science.
-----
#### THE JOSS WORKFLOW
-----
So hopefully I've convinced you JOSS is beneficial to the individual and science
Let's look at what the JOSS submission process looks like.
The first step is to make your software available in a repository (like github or gitlab) and give your software an open source licence. You then author a short paper in markdown and submit this to JOSS. The submission is free - JOSS is run by volunteers so it works out at less than £3 / article, which is covered by donations and sponsorship.
The editor assigns one or more reviewers who review the submission. This process is done through github. It it fully open and transparant. This review process is more of a conversation, a discussion, than the traditional review process.
Once an article is accepted, JOSS gives it a digital object identifier (DOI), deposits its metadata in Crossref, and the article can begin collecting citations.
-----
This is what the short paper which is submitted alongside your code must contain. It is a single side of A4 - as reviewers are looking for scholarship contained in the software itself. 
----
The submitted software will be reviewed against the following criteria. There is not enough time to look at each in turn, but I'll very briefly talk about the JOSS guidance around testing and documentation.
-----
#### TESTING AND DOCUMENTATION
-----

There are various types of testing.
Unit tests test that small pieces of code - usually an individual function or method - are working as expected. That for a particular input you get the correct output. There are also integration tests, which check that functions work together and end to end tests which test the full software pipeline. 
Instead of manually running every one of these tests, you can use a testing framework such as pytest, and this process can be automated so that the tests are run regularly using a continuous integration tool such as Travis CI.
I've included on this slide links to some of tools used, though its not exhaustive, and examples from my effmass project. 
JOSS expects you to have some level of testing, at a minimum you could have a sample input file and expected output, but ideally there should be automated tests using Travis or similar.  
-----
Documentation also comes in different flavours. tutorials are step by step guides for completing a particular task and I've seen these very succesfully done using a Jupyter notebook, explanations give background theory and could be in the form of a research paper whilst reference or API documentation gives information about each function or method - what are the inputs, what are the outputs. Again JOSS expects you to have some reference and tutorial documentation, but it is largely left to the reviewer to determine if it satisfactory.
-----
#### FINAL THOUGHTS
-----
Before I end I should mention that there are other journals out there - you can find a lit on this website.
If you are comfortable with testing, documentation, best practice in RS, then I think JOSS is important for getting acknoledgement for your work with minimum extra overhead. You could also consider reviewing for JOSS, I've done one review and it was a positive experience.
For people new to testing and documentation, JOSS gives a great incentive to learn these tools, and it is worth it - my package effmass has improved as a result of the JOSS process, and its great to see other people using it.
I think as a research community we should be supporting each to publish our code, andit'd be good to speak to people over lunch about how this might be achieved.
-----

“An article about a computational result is advertising, not scholarship. The actual scholarship is the full software environment, code and data, that produced the result”

 










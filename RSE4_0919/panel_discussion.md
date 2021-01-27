### Panel discussion RSE 2019

- Tips
     - look at the audience
     - don't start with "I agree with X"
     - stories and anecdotes to begin discussion
     - begin with a summary of who you are if not already done, what qualifies you

- Opening statement
    - "Until well-written code gets the recognition it deserves, competing pressures will prevent many researchers from writing sustainble software."
    - I'm sure everyone here has a list of 30,300,3000 other things they could be doing. Some people are probably multitasking, working through that list as we speak. So it means that we are always prioritisting. Those tasks which aren't being chased by our managers, or helping us secure our next job - they aren't going to get done. That's the reality of the situation. So until well-written software can help us secure our next job, or is being chased by our managers it's not going to get done. To promote best practices, we need to create a system and culture where best practice is recognised and rewarded. We need to provide a clear incentive to researchers.
    
- Closing statement
    - Yes we need more training to build confidence, and make aware of tools. But that won't be used unless we provide clear incentive. We need to publish code and cite code, and we need to discuss why best practice is critical for rigorous, reproducible science. We should be proud of having these discussions because I think we are ahead of many other disciplines, where there is too much emphasis on output.

**Documentation is essential but often happens “later”. How can documentation be part of the workflow to make sure it is not postponed to “never”?**

- I'm currently building on a piece of code with minimal documentation, so I feel the frustration.
- Version control workflow --> PR only accepted if accompanied by documentaiton. 
- Workflow so that the documentation is easy: Python with Sphinx and ReadTheDocs so that comments or docstrings at the funciton or class level can be converted into documentation with minimal overhead.
- Asking for users early on to locate where documentation is missing
- Incentivise documentation by making use of journals which publish software tutorials - an example in my field is the living journal of computational molecular science where you can publish software tutorials and update them as software developments occur
- highlight that documentation comes in several forms: reference/API, explanation (background theory), tutorials.

**Two students start at the same time - one uses best practices, the other does not. Who will publish more? What does it mean for the academic credit system?**

- If we are talking about publishing results - the student who doesn't use best practice. But there are other outputs, and a growing number are being supported by journals.
- . For example, there software outputs there is the journal of open source software, for methods in the life sciences there is nature methods. Journal articles in the form of registered reports - where the research question and methodology are peer reviewed, without any results - are growing in popularity. 
- And there are options to publish other outputs: data can be published in nature scientific data, and there are a number of discipline specific data journals. 
- So now, we should emphasise to our student of best practice that research outputs come in many forms and point them to these various journals.
- But I would argue that the academic credit system is broken anyhow. There is Goodharts law: when a measure becomes a target, it stops becoming a good measure. Once we say that getting X number of papers are needed to show that you are a leading researcher, then people will find ways to game the system. And we've seen that with excessive self-citations, for example. So we should also think about how to credit people beyond publishing papers.

**Is there a difference in uptake of best practices in computational research compared to experimental research? If yes, why?**

- Well some experimental fields are more used to strict protocols and close monitoring. For example, best practices around control of harmful or radioactive substances, to protect human participants in psychological studies, to minimise the distress caused to animals in biology research - there are frameworks in place. And these frameworks are enforced through personal and project licenses for example. 
- Perhaps the nature of computational research is such that it can be more exploratory. For example, if you are conducting a survey or marine wildlife, then you would go to the field and collect data, and then return to the lab to analyse. Going back out for more data is not easy, it might not be feasible at all. So you might spend a lot of time designing the experiment, making sure that you get it right the first time. Computational research lends itself much more to a collect data, analyse data, collect more data, analyse more data. Perhaps It's easier to go in without a very clear idea of what you want to achieve, so the design and methodology of a study will take a hit. 

**Is a lack of education/awareness around what constitutes software research best practice limiting its uptake?**
- For the majority of researchers yes. I think we've come a good way through initiatives like software carpentry, and the courses that many RSE teams are building. 
- However, from discussions I've had with colleagues I think there are still plenty of people we haven't reached. I mean the problem is you can design and advertise for example a version control course. But to sign up, you need to have already bought into the idea of version control enough to dedicate one day of your precious time to it. 
- I think SWcarpentry is a great starting step for the basics, but we need more training for the next step: testing, documentation, modular code. Radovan and code refinery.
- We need to build that education and awareness at the undergraduate level. First taste of research is during a summmer project or final year project. Aron using github with undergraduates for questions and course work.
- Of course this only works if the lecturers are on board - might be a difficult group to reach!
- We need good training that promotes confidence, doens't overload. I used to teach mathematics, and mathematics and programming are similar in that I think a lot of people think "I can't do it" and write it off. And if you are delivering training around software you will have a huge influence on the confidence of the participants. Remember that they are looking to you as the expert. Number one problem I see in university teaching is that people try to squeeze too much in to a session. I'm guilty of it myself. But if you're covering too much material in too short a time then students will get left behind, and this can be a big knock to confidence.


**How can we incentivize software research best practice on an individual level?**

- Publication is important: more easily justify to ourselves and our supervisors or boss about the time taken. JOSS has spread in the research group I'm in. Now to the point that people are developing software with JOSS criteria in the back of their minds - "may as well get a publication out of it"
- citation: Stephen has done a lot of work around, and there are sessions tomorrow focussing on this.
- importance of identity: when i speak to researchers about their work many will be quick to say oh I'm not a programmer, " I'm just someone who writes a collection of scripts that kind of work" - and its harder to persuade that person who writes scripts that kind of work to do best practice. Becoming a software carpentry instructor was a big step for me. The first time I really identified as a programmer and as someone who really should try to do things the right way, was teaching other people about it! Creating inclusive communities will allow people to form a professional identity that encourages best practice.
- best practice involves sharing your work, and acting on peer review. This is a great way to promote your code. One of the things I emphasise is how github acts as a great promotional tool.
- By emphasising that software research best practice is an integral part of robust and reproducible science - that we often need to test our code to know that our conclusions are true. That we need to allow other people access so that they can reproduce our work.
- I think we need to be honest about the extra effort involved. It is true that some things will save time down the line. But not almost. Masters / PhD students/ post docs often don't know if they will be in academia in two years time, never mind if they will still be using a piece of software etc...

 **How do software research best practices interact with academic publishing practices?**

- academic publishing is trying to promote best practice through their guidelines, in particular several journals ask that researchers make their code freely available upon request (nature and science). However this doesnt seem to be tested or enforced: Victoria stodden conducted a study of papers in the journal science and found that only roughly a third of authors provided code when contacted.
- required to make materials, data, code, and associated protocols promptly available to readers without undue qualifications. 
- There is a growing number of journals that focus on the methology or tools that are used to enable science. For example, JOSS Have a bit about what JOSS is: open source journal, on github, free to submit to, completely open and transparent review process. JOSS criteria demand best practice around documentation , testing and availability.
- JOSS: open source softare. That is, if the submitting authors have followed best practices (have documentation, tests, continuous integration, and a license) then their review should be rapid. Review the software itself, not a summary paper.
- livecommsjournal - living journal of computational molecular science. publish work and then continue development. Software analyses which report updates to softwsare, benchmarking, interoperability
- some journals you can submit a jupyter notebook as SI, and I have done this, but at the moment feels like extra work for the author, real change when you have to.
- It seems to me that publishing practices are still stuck way back in the middle ages compared to where they should be. Most of us don't read papers on paper anymore, but we use text and don't interact with the reported research as if the computer had never been invented. The methods we use, experimental or computational are increasingly complex but still relegated to a small paragraph at the end of the report. To me it would make much more sense to have a Jupyter type notebook. Now there are improvements.
- paper announcing first confirmed observation of gravitaitonal wave was accomopanied by a Jupyter notebook.

**How can a PI or group leader motivate students and post-docs to develop software according to FAIR software practices?**

- FAIR: simple, funders and journals, decision makers are familiar with them in the context of data (findable, accessible, interoperable, reusable).
- Discuss best practice in group meetings
- Report back on development progress in project meetings. 
- Allocate time for review of code
- Give opportunities to learn - write small tests, documentation for existing projects. In the research group I work in, there will often be a piece of software that is mostly written be one person, but newer members of the group will be asked to use the software in their research, write documentation or tests. This forms a good introduction.
- Leading by example. Having it stated as part of the group philosophy on the group website for example, as part of the identity of the group.

**How should an environment on the organizational (or another level) preferably look like to encourage researchers following software development best practice?**

**What is the influence of the culture (on team-level, organization level) with regard to software development best practice?**

- Need to feel comfortable sharing work that they know can be improved. We all write a lot of bad code - we know this. But people new to the world of programming don't - they think its just them. 
- I think we need an environment and culture that builds people confidence. I used to teach mathematics, and I see that students have a similar feeling around programming as they do mathematics; they think you were either born to do it, or you weren't and you should just give up. So we need to build peoples confidence. I think this is the reason many people attend SWcarpentry. We have so many resources online, why go to a physical session when you can do it at home or in the office at your own pace? I think interacting with people, and peer support builds confidence that many people are lacking.
- Process rather than the final result

**National level** 

- REF: Develop and manage individual and collaborative research projects to deliver appropriate outputs in sufficient volume, quality and impact to meet the terms of the next Research Excellent Framework (REF). The REF is the UK’s system for assessing the quality of research in universities. Open Access in REF 2021, journal articles. Software outputs.
- Need more funders to promote: who is?

**How do we fill the gap between bottom-up initiatives such the Carpentries, institutional guidelines, and top-down policies, to implement good practices?**

- carpentries are great for a general introduction, but for many researchers they want to see how this sits in the context of their domain.
- I realised this earlier this year. The RSE community at Imperial have been organising a series of talks, although attendance wasn't as goos as it could have been. We organised a domain specific lunchtime event in my department, materials and it got really great attendance. Most of the people there had not attended the university wide RSE events --> this told me that researchers are looking for training/events that explicitly link research software with their field of research. Laura Ratcliff / Jeremy Cohen.

**How can RSEs communicate the importance of following good practices to PIs/superiors, despite the cost in time and resources?**

- I think RSEs are leading the way ahead of other science and they will look to the work done in the RSE community around openness, reproducibility, testing.
- persuading people of version control can be difficult: other people don't use it, and because conceptually there are some large leaps. I spent two years using git, and honestly I didn't understand why I was using it. I was using it because I knew I was meant to. But I was self taught so I didn't have the benefit of someone telling me.
- Places where selfish aligns with the selfless. git-->github-->advertisement of youself. And great support for bugs. Easy to make websites, and again promote yourself and your work. Not obvious to researchers, it needs to be pointed out.
- Open research, including sharing your code and data, leads to more citations, media opportunities, job opps. "How open science helps researchers succeed" - eLife
- integrity of science / reproducibility: would link to recent studies that show 
- this isn't just about having long lasting software, about efficiency with which we use funders money or researcher time. It is more fundamental. We have so much science that depends on research software now, that the integrity of science depends on software best practice. This is fundamental to good science - it needs to be reproducible, the process needs to be interrogated.

**Why does no one believe in best practices? (at least not to the extent of embracing them, rather than just giving them lip-service?)**

- They are not invested in. On 10 April, astrophysicists announced that they had captured the first ever image of a black hole. This was exhilarating news, but none of the giddy headlines mentioned that the image would have been impossible without open-source software. The image was created using Matplotlib, a Python library for graphing data, as well as other components of the open-source Python ecosystem. Just five days later, the US National Science Foundation (NSF) rejected a grant proposal to support that ecosystem, saying that the software lacked sufficient impact. We can't all work for free, we need the resources.
- We don't have the selfish incentive for best practice. We're not all saintly all the time.

**Are there differences in adoption between disciplines?**

- astrophysics / high energy physics shared, tested, distributed code effectively
- you have very large teams of people which necessitate this
- there are resources for teams of RSEs
- I worked as an undergraduate for one summer with a group building analysis pipelines for gravitational wave data. A number of people in that group had an RSE-like role, even if, well this was 10 years ago so it wasn't called that. The size of some research initiatives allow more easily for such specialisms.
- For many people an entry point into the world of open access is through pre-print servers such as arxiv. Physicsists / mathematicians have been using arxiv since the mid 90s, so there is a culture of openness wrt publishing.

**How are other best practices enforced, e.g. in experimental discipline, natural sciences or medicine? **

- Journal policies. But they aren't actually enforced! Victoria Stodden - Science.
- checklists (Anna developing)
- research integrity as is routinely applied for animal husbandry, biosafety and clinical work

**What constitutes best practice?**

- Reliable and maintainable: CI, version control, unit testing, documentation, modularity
- planning for change and longevity -  having awkward conversations: who will take responsibility for this piece of code once I move on to another job. Best practice in the context of a workforce which are often on short term contracts.
- a lot of what we're talking about is software engineering best practice. What is particular to research? ---> domain experts. Openness/reproducibility.
     


































#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import
__author__ = "Laurent Perrinet INT - CNRS"
__licence__ = 'BSD licence'
DEBUG = True
DEBUG = False

import os
home = os.environ['HOME']
figpath_talkbcp = 'figures' # os.path.join(home, 'pool/ANR-REM/ASPEM_REWARD/AnticipatorySPEM/2017-11-24_Poster_GDR_Robotique/figures')
figpath_GDR = os.path.join(home, 'pool/ANR-REM/ASPEM_REWARD/AnticipatorySPEM/2017-11-24_Poster_GDR_Robotique/figures')
figpath_aSPEM = os.path.join(home, 'pool/ANR-REM/ASPEM_REWARD/AnticipatorySPEM/figures')
figpath_aSPEM = os.path.join(home, 'pool/ANR-REM/ASPEM_REWARD/AnticipatorySPEM/figures')
figpath_ms = os.path.join(home, 'pool/ANR-REM/ASPEM_REWARD/AnticipatorySPEM/ms/figures')
figpath_slides = os.path.join(home, 'nextcloud/libs/slides.py/figures/')

import sys
print(sys.argv)
tag = sys.argv[0].split('.')[0]
if len(sys.argv)>1:
    slides_filename = sys.argv[1]
else:
    slides_filename = None

print('😎 Welcome to the script generating the slides for ', tag)
YYYY = int(tag[:4])
MM = int(tag[5:7])
DD = int(tag[8:10])

# see https://github.com/laurentperrinet/slides.py
from slides import Slides
height_px = 80
height_ratio = .7

meta = dict(
 embed = True,
 draft = DEBUG, # show notes etc
 width= 1600,
 height= 1000,
 # width= 1280, #1600,
 # height= 1024, #1000,
 margin= 0.1618,#
 #  reveal_path = 'file://' + home + '/nextcloud/libs/slides.py/reveal.js/',
            # reveal_path = 'http://cdn.jsdelivr.net/reveal.js/3.0.0/',
 #reveal_path = 'https://s3.amazonaws.com/hakim-static/reveal-js/',
 #reveal_path = 'http://cdn.jsdelivr.net/reveal.js/3.0.0/',
 #reveal_path = 'https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.4.1/',
 reveal_path = 'https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.6.0/',
 #theme='night',
 #theme='sky',
 #theme='black',
 #theme='White',
 theme='simple',
 #theme='White',
 bgcolor = "white",
 author='Laurent Perrinet and Chloé Pasturel and Anna Montagnini, INT',
 #author_link='Chloé Pasturel, Laurent Perrinet and Anna Montagnini',
 author_link='<a href="http://invibe.net">Laurent Perrinet</a>, Chloé Pasturel and Anna Montagnini',
   short_title='Principles and psychophysics of Active Inference',
 # title='Principles and psychophysics of Active Inference: Anticipating a dynamic, switching probabilistic bias in visual motion direction',
 #title='Principles and psychophysics of Active Inference in anticipating a dynamic, switching probabilistic bias',
 title='Principles and psychophysics of Active Inference in anticipating a dynamic probabilistic bias',
 conference_url='https://opt-infer-brain.sciencesconf.org/',
 short_conference='Bayesian WS, Marseille - April 5th, 2018',
 conference='Probabilities and Optimal Inference to Understand the Brain',
 location='INT, Marseille (France)',
 YYYY = YYYY,
 MM = MM,
 DD = DD,
 tag = tag,
 url = 'http://invibe.net/LaurentPerrinet/Presentations/' + tag,
 abstract="""
""",
wiki_extras="""
----
<<Include(BibtexNote)>>
----
<<Include(PaceItnAknow)>>
----
TagYear18 TagTalks TagPublicationsProceedings [[TagPACEItn]]""",
 sections= ['Motivation', #A dynamic probabilistic bias in visual motion direction',
    'Raw psychophysical results',
    'The Bayesian Changepoint Detector',
    'Results using the BCP']
 )

# https://pythonhosted.org/PyQRCode/rendering.html
# pip3 install pyqrcode
# pip3 install pypng
figname = os.path.join(figpath_talkbcp, 'qr.png')
if not os.path.isfile(figname):
    import pyqrcode as pq

    code = pq.create(meta['url'])
    code.png(figname, scale=5)


do_section = [True] * (len(meta['sections']) + 2)
i_section = 0
s = Slides(meta)
# s.meta['Acknowledgements'] = '', #s.content_imagelet(os.path.join(figpath_talkbcp, 'qr.png'), height_px),
#
s.meta['Acknowledgements'] ="""<h4>Acknowledgements:</h4>
   <ul>
    <li>Jim Bednar @ Continuum Analytics &amp; University of Edinburgh</li>
    <li>Berk Mirza, Rick Adams and Karl Friston @ UCL - Wellcome Trust Centre for Neuroimaging</li>
    <li>Wahiba Taouali, Giacomo Benvenuti, Frédéric Chavane - ANR BalaV1 </li>
    <li>Jean-Bernard Damasse, Laurent Madelain - ANR REM</li>
   </ul>
"""
#    {Jim}{Karl}{Mina}{Anna}{GSM}<a href="https://github.com/laurentperrinet/slides.py">{Python}</a>
# """.format(Jim=s.content_imagelet(os.path.join(figpath_aSPEM, 'jim.jpg'), height_px),
#            Karl=s.content_imagelet(os.path.join(figpath_aSPEM, 'karl.jpg'), height_px),
# Mina=s.content_imagelet(os.path.join(figpath_aSPEM, 'mina.jpg'), height_px),
# Anna=s.content_imagelet(os.path.join(figpath_aSPEM, 'anna.jpg'), height_px),
# GSM=s.content_imagelet(os.path.join(figpath_aSPEM, 'gsm.jpg'), height_px),
# Python=s.content_imagelet(os.path.join(figpath_aSPEM_, 'python-powered-h-140x182.png'), height_px),
        #    )
if do_section[i_section]:
    s.open_section()
    #################################################################################
    ## 🏄🏄🏄🏄🏄🏄🏄🏄 Intro - 5''  🏄🏄🏄🏄🏄🏄🏄🏄
    #################################################################################
    #################################################################################

    s.hide_slide(content=s.content_figures(
        #[os.path.join(figpath_talkbcp, 'qr.png')], bgcolor="black",
        [os.path.join(figpath_slides, 'mire.png')], bgcolor=meta['bgcolor'],
        height=s.meta['height']*.90),
        #image_fname=os.path.join(figpath_aSPEM, 'mire.png'),
        notes="""
    Check-list:
    -----------

    * (before) bring miniDVI adaptors, AC plug, remote, pointer
    * (avoid distractions) turn off airport, screen-saver, mobile, sound, ... other running applications...
    * (VP) open monitor preferences / calibrate / title page
    * (timer) start up timer
    * (look) @ audience

    http://pne.people.si.umich.edu/PDF/howtotalk.pdf

     """)

    intro = """
    <h2 class="title">{title}</h2>
    <h3>{author_link}</h3>
    """.format(**meta)
    # intro += s.content_figures(
    # [os.path.join(figpath_aSPEM, "troislogos.png")], bgcolor="black",
    # height=s.meta['height']*.2, width=s.meta['height']*.75)
    intro += s.content_imagelet(os.path.join(figpath_slides, "troislogos.png"), s.meta['height']*.2) #bgcolor="black",
    #intro += s.content_imagelet(os.path.join(figpath_talkbcp, 'qr.png'), s.meta['height']*.2) #bgcolor="black",
    # height=s.meta['height']*.2, width=s.meta['height']*.2)
    #
    intro += """
    <h4><a href="{conference_url}">{conference}</a>, {DD}/{MM}/{YYYY} </h4>
    {Acknowledgements}
    """.format(**meta)

    s.add_slide(content=intro,
            notes="""
 * (AUTHOR) Hi, I am Laurent Perrinet from (LOGO) the Institute de Neurosciences de la Timone in Marseille, a joint unit from the CNRS and AMU. Using computational models, I am investigating the link between the efficiency of behavioural responses in vision, their underlying neural code and their adaptation to the structure of the world.

 * (SHOW TITLE - THEME) = In particular, I will try to give some principles of active inference, framed in a practical example of a dynamic, poissbly volatile environment and how we may use it to anticipate ---- and my main goal in general is to illustrate how this theory may give a creative and efficient tool to do psychophysics.

 """)

    figpath = 'figures'

    figname = os.path.join(figpath_talkbcp, 'qr.png')
    if not os.path.isfile(figname):
        # https://pythonhosted.org/PyQRCode/rendering.html
        # pip3 install pyqrcode
        # pip3 install pypng
        import pyqrcode as pq

        code = pq.create(meta['url'])
        code.png(figname, scale=5)

    s.add_slide(content=s.content_figures([figname], cell_bgcolor=meta['bgcolor'], height=s.meta['height']*height_ratio) + '<BR><a href="{url}"> {url} </a>'.format(url= meta['url']),
    notes=" All the material is available online - please flash this QRcode this leads to a page with links to further references and code ")

    s.add_slide(content=intro,
        notes="""
 * (ACKNO) this endeavour involves different techniques, tools and... persons. From the head on, I wish to acknowledezg Chloe and Anna for doing most of this work +  thank the people who collaborated directly or indeirectly to this project and in particular Berk Mirza, Rick Adams and Karl Friston and the Wellcome Trust Centre for Neuroimaging for providing the tools for a successful visit and finally Jean-Bernard and Laurent Madelain for their essential knowledge in adaptation and reinforcement.

""")

    s.close_section()

figpath_GDR = os.path.join(home, 'pool/ANR-REM/ASPEM_REWARD/AnticipatorySPEM/2017-11-24_Poster_GDR_Robotique/figures')
figpath_aSPEM = os.path.join(home, 'pool/ANR-REM/ASPEM_REWARD/AnticipatorySPEM/figures')

i_section += 1
if do_section[i_section]:
    #################################################################################
    ## 🏄🏄🏄🏄🏄🏄🏄🏄 MOTIVATION - 10''  🏄🏄🏄🏄🏄🏄🏄🏄
    #################################################################################
    #################################################################################

    s.open_section()
    title = meta['sections'][i_section-1]
    s.add_slide_outline(i_section-1, notes="""
 * Let's me first describe the motivation of this work...

 * We live in a fundamentally volatile world - Think for instance to the evolution  of prices on the stock market: Any Socio-economic contextual index may make the price evolve up or down, slowly or more Rapidly ...

 * Take for instance this very common source of information of the text of all tweets by Donald Trump In a last few years. It's just a Cheap Way Of accessing Big data if you'd prefer - If now I crossed time we extract other tweetsWhich contained onto not containA list of words that please selected

    """)

    for txt in ['fixed', 'hindsight']:
        s.add_slide(content=s.content_figures(
        [os.path.join(figpath_aSPEM, 'trump_' + txt + '.png')],
                title=title + ' - a Real-life example', height=s.meta['height']*.825),
    notes="""

 * When plotting The occurrence of theses words As a function of time smoothed in a small Time window We may guess that there is some tendenciesWhichHappen toBelong to different blocks

 * On way to think about The way These words are used is that This words appear with different a priori probabilities In time And  that the context that drives this probabitlities Is changing In different blocks Which is corresponds to different contexts: a pre-election phase,

* This may look like this boxes That a plot here as a function of time. Such a representation allows to anticipate = infer for future outcomes but more importantly to better understand The motives behind the context and use of these words (if any)

    """)
    bib =  'Montagnini A, Souto D, and Masson GS (2010) <a href="http://jov.arvojournals.org/article.aspx?articleid=2138664">J Vis (VSS Abstracts) 10(7):554</a>,<BR> Montagnini A, Perrinet L, and Masson GS (2015) <a href="https://arxiv.org/abs/1611.07831">BICV book chapter</a>'

    s.add_slide(content=s.content_figures(
    [os.path.join(figpath_aSPEM, 'protocol_recording.png')],
            title=title + ' - Eye Movements', height=s.meta['height']*.825) + bib,
    notes="""
 * This was shown to happen in the more  experimental setting While recording smooth pursuit eye movements : Anna Montagnini has previously shown that if you use a probabilistic bias in the direction of the movement of the target, the the eye will (uncousciously) anticipate in the direction of this bias.

 * this protocol used a random length fixation period then a pause of fixed duration, and then a traget moving at 15 deg / s

 * the value p gives the probability of going to the right : at .5 it is unbisaed, and at .75 for instance it goes 75% to the right and 25% to the left
    """)

    for txt in ['1', '2']:
        s.add_slide(content=s.content_figures(
    [os.path.join(figpath_GDR, 'image_anna_' + txt + '.png')],
                title=title + ' - Eye Movements', height=s.meta['height']*.825),
       notes="""

 * we show in this plot the velocity of the eye that she recorded when tracking the target.

 * we observe that as you depart from .5, there is an anticipatory component to the SPEM

 * Moreover, she has proved that this behaviour is progressive and increases with the value of p

    """)

    for tag, notes_ in zip(['Experiment_randomblock_', 'Experiment_classique_', 'Experiment_randomblock_'], ["""
* our initial goal was to extend these results to a more volatile environment. This Is well described by a three layered architecture decribing the evolution of outcomes (left or right) as a function of the trial number in an experimental block:

- at the bottom we have switches, that is moments were we know that there was a change in context:

- then we have an intermediate layer which describes this context as the probability p which defines the bias towards one direction. as switches happen at random times but with a given hazard rate, blocks are of average length of here 40.

- finally, we draw the directions as a sequences of binary events following this bernouilli trials

 If we draw another exmple of this generative model
""","""

This has to be put in contrast with a more classical protocol such as that used in the previously described experiment where different blocks of fixed length were drawn, but with different probabilities.

""","""

Here, we

 """]):
        for txt in [str(i) for i in range(4)[::-1]]:
            s.add_slide(content=s.content_figures(
        [os.path.join(figpath_aSPEM, tag + txt + '.png')],
                    title=title + ' - Eye Movements', height=s.meta['height']*.775),
           notes=notes_)

    s.add_slide(content=s.content_figures(
    [os.path.join(figpath_aSPEM, 'Experiment_randomblock.png')],
            title=title + ' - Random-length block design', height=s.meta['height']*.825),
    notes="""

In summary, the design of our experimental setting is therefore very similar to the previous experiment but with a more general construct:

- using the same 3-layered generative model, we generated sequences of directions

- and generated 3 blocks of 200 trials

- with an average block length of 40 trials

We anticipated that such an  experiment for which we simply recordedd the eye movements should be more difficult for observers compared to the classical experiments with longer (400 trials), fixed blocks and...


    """)

    s.add_slide(content=s.content_figures(
    [os.path.join(figpath_aSPEM, 'protocol_bet.png')],
            title=title + ' - Random-length block design', height=s.meta['height']*.825),
    notes="""

This is why we added a supplementary experiment for each observer but on a different day for which we asked at every trial to give a subjective, conscious evaluation of the direction of the next trial + a confidence about this inference. Once this information given by the subject, we were showing the actual outcome.

Interestingly, we used exactly the same sequence, allowing to make a direc comparison of the results of both experiments

We called this experiment the bet experiment.


    """)
    s.close_section()


i_section += 1
if do_section[i_section]:
    #################################################################################
    ## 🏄🏄🏄🏄🏄🏄🏄🏄 RAW RESULTS - 10''  🏄🏄🏄🏄🏄🏄🏄🏄
    #################################################################################
    #################################################################################

    s.open_section()
    ############################################################################
    title = meta['sections'][i_section-1]
    s.add_slide_outline(i_section-1, notes="")

    url =  'full code @ <a href="https://github.com/chloepasturel/AnticipatorySPEM">github.com/chloepasturel/AnticipatorySPEM</a>'

    s.add_slide(content=s.content_figures(
    [os.path.join(figpath_aSPEM, 'Experiment_randomblock.png')],
            title=title + ' - Random-length block design', height=s.meta['height']*.825) + url,
    notes="""

 * the whole experiment was coded by Chloé using :
 - python for the generative model,
 - the psychopy library for the stimulus display + connection to the eyelink 1000 that we used to record EMs
 - numpy, pandas and pylab for the data analysis

  * all this code is available : for running the experiments, re-analyzing the data and doing all plots are on github


Let's now have a look at the raw psychophysical results..

    """)


    s.add_slide(content=s.content_figures(
    [os.path.join(figpath_aSPEM, 'Experiment_randomblock_bet.png')],
            title=title, height=s.meta['height']*.825),
    notes="""
First, we overlay the results of the bet result for one of the 12 subjects

We rescaled th value given by the observer so that it fits to 0 (sure it goes left) to 1 (sure it goes right)

We observe a pretty good fit of this trace as a function of trial number


In particular, we see 2 main effects:
- results are more variable when the bias is around .5 than when it is high (close to zero or one)
- switches were detected quite rapidly but with a certain delay of a few trials. Indeed, note that this plot shows the entire sequence but that observers had only access to some internal representation of the memory of the previous observations. When faced with some new observations, the observer has to constantly adapt his response to either exploit this information by considering that this observation belongs to the same sub-block or to explore a novel hypothesis. This compromise is one of the crucial component that we wish to explore.

Let's now have a look at EMs...

    """)


    # for txt in ['results_pari', 'results_enregistrement']:
    #     s.add_slide(content=s.content_figures(
    # [os.path.join(figpath_GDR, txt + '.png')],
    #             title=title, height=s.meta['height']*.825),
    #    notes="""
    #
    # """)


    for txt in ['raw_trace', 'raw_fitted']: # 'raw_fit',
        s.add_slide(content=s.content_figures(
    [os.path.join(figpath_aSPEM, txt + '.png')],
                title=title + ' - Fitting eye movements', height=s.meta['height']*.825),
       notes="""

I show here a typical velocity traces for one subject / 2 trials

- x-axis is time in milliseconds aligned on target onset, and we show respectively from left to right the fixation in gray, the GAP in pink (300ms) and the run in light gray.

- y-axis is the velocity as computed as the gradient of position. Remark that the eyelink provides with the periods of saccades or blinks that we removed from the signal. it is quite noisy and to complement existing signal processing methods, Chloe implemented a robust

- fitting method which allows to extract some key components of the velocity traces: maximum speed, latency, temporal inertia ($\tau$) and most interestingly acceleration before motion onset. We cross-validated that this method was givinfg similar results to other classical methods but in a more robust fashion/

While being sensible to recording errors, this allows us to extract the anticipatory component of SPEMs and..

    """)

    s.add_slide(content=s.content_figures(
    [os.path.join(figpath_aSPEM, 'Experiment_randomblock_EM.png')],
            title=title, height=s.meta['height']*.825),
    notes="""

 * I show here the overlay of this variable on the plot of probability biases

 * these accelarations values were here scaled according to their extremal values.

 * there seems to be a trend with the polarity of the accelration being negative for p values below .5 and positive for values above .5



    """)

    s.add_slide(content=s.content_figures(
    [os.path.join(figpath_aSPEM, 'Experiment_randomblock_bet_EM.png')],
            title=title, height=s.meta['height']*.825),
    notes="""

... to make this clearer, and because we used the same sequence, we can overlay the results of both experiments in one plot:

which qualitatively confirms such an intuition...

    """)

    for txt in ['P_real', 'p_bet--v_a']: # TODO : make a sequence to uncover parts
        s.add_slide(content=s.content_figures(
    [os.path.join(figpath_GDR, txt + '.png')],
                title=title, height=s.meta['height']*.75),
       notes="""
 * quantitatively, one can now plot the results for all subjects

 * the x-axis corresponds to the probability that was coded at the second layer and which is unknown to the observer
 * the y -axis shows either the bet or the
 * dots represent single responses - the saturation giving the identity of the observer

 we notice a quite nice linear correlation (black line) for both experiments; of the order of that found in the classical experiment with fixed blocks and a vartiety of bias values. This is surprising as the blocks are of random length, observer can still adapt to such a volatile environment.

Another visualization, the scatter plot of acceleration  as a function of probability bet shows also that there is a correlation between both  variables.

This allows to make a first point: it is possible to use more genreal models such as hierarchical generative models.

However, while this results seem encouraging, a more finer analysis may be necessary.

    """)
    s.close_section()

try:
    os.mkdir(figpath_talkbcp)
except:
    pass

import bayesianchangepoint as bcp
import numpy as np
import matplotlib.pyplot as plt
fig_width = 12

i_section += 1
if do_section[i_section]:
    #################################################################################
    ## 🏄🏄🏄🏄🏄🏄🏄🏄 MODEL - 10''  🏄🏄🏄🏄🏄🏄🏄🏄
    #################################################################################
    #################################################################################

    s.open_section()
    s.add_slide_outline(i_section-1, notes="""
Indeed, these raw psycholophysical results are encouraging but since we used a generative model for generating the sequence, let's see if we can build a Bayesian model which would be optimal wrt to this generative model.

Indeed, such a model already exists, the onlin BCP, and we will adapt it for our specific setting.
""")
    ############################################################################
    title = meta['sections'][i_section-1]

    s.add_slide(content=s.content_figures(
    [os.path.join(figpath_GDR, 'exp.png')],
            title=title, height=s.meta['height']*.825),
    notes="""
Let's remember our hierarchical generative model.

At any given trial, we wish to construct an algorithm which

We will introduce a fundamental component of Bayesian models : a latent variable

this new variable will be used to test different hypothesis which will be evaluated to predict future states. it is called latent because it aims at representing a variable that is latent (or hidden) to the observer

in our case, we will assume that the bayesian model knows about the structure of the generative model and we will set it to the current run-length $r$, that is, at any given trial, the hypothesis that the past r observations belong to the same block. of course a wrong choice of a latent variables (let's say the temperture in the experimental room) may give unexpected results, even is the bayesian model is "optimal" - an essential point to understand in bayesian inference

    """)

    tag = 'bcp_model_layer_' #  'model_bcp_'
    blobs = ["""
Initialize $P(r_0=0)=1$ and  $ν^{(0)}_1 = ν_{prior}$ and $χ^{(0)}_1 = χ_{prior}$
 ""","""
Observe New Datum $x_t$  and   Perform Prediction $P (x_{t+1} | x_{1:t}) =   P (x_{t+1}|x_{1:t} , r_t) \cdot P (r_t|x_{1:t})$
<br<a href="http://arxiv.org/abs/0710.3742"Adams &amp; MacKay 2007 "Bayesian Online Changepoint Detection</a>
""","""
Evaluate (likelihood) Predictive Probability $π_{1:t} = P(x_t |ν^{(r)}_t,χ^{(r)}_t)$
<br>
Calculate Growth Probabilities $P(r_t=r_{t-1}+1, x_{1:t}) = P(r_{t-1}, x_{1:t-1}) \cdot π^{(r)}_t \cdot (1−H(r^{(r)}_{t-1}))$
<br>
<font color="FF0000">Calculate Changepoint Probabilities $P(r_t=0, x_{1:t})= \sum_{r_{t-1}} P(r_{t-1}, x_{1:t-1}) \cdot π^{(r)}_t \cdot H(r^{(r)}_{t-1})$
</font>""","""
Calculate Evidence $P(x_{1:t}) = \sum_{r_{t-1}} P (r_t, x_{1:t})$
<br>
Determine Run Length Distribution $P (r_t | x_{1:t}) = P (r_t, x_{1:t})/P (x_{1:t}) $
""","""
Update Sufficient Statistics :
 $ν^{(r+1)}_{t+1} = ν^{(r)}_{t} +1$, $χ^{(r+1)}_{t+1} = χ^{(r)}_{t} + u(x_t)$
<br>
<font color="FF0000"> $ν^{(0)}_{t+1} = ν_{prior}$, $χ^{(0)}_{t+1} = χ_{prior}$</font>

"""]
    for txt, blob, notes_ in zip([str(i) for i in range(5)], blobs, ["""
* in this graph information will be represented at different nodes. each node represent a belief which takes the form of a probability distribution over the set of parameters that we wish to describe.
* it can be the mean and variance of a gaussain, but in general it will be 2 parameters. in our case, we wish to estimate p (between zero and one) - it is characterized by the beta distribution (mathematically it is the conjugate of the bernouilli distribution)
* (mathematically, we will use th family of exponenetial distributions:, gaussians, binomials) among which the beta distribution belongs
First, we initialize the first node to prior values
* at trial zero, there is no information
""","""

""","""

""","""

""","""

"""]):
        s.add_slide(content=s.content_figures(
    [os.path.join(figpath_aSPEM, tag + txt + '.png')],
                title=title, height=s.meta['height']*.775)+blob,
       notes=notes_)
    # https://raw.githubusercontent.com/laurentperrinet/bayesianchangepoint/master/README.md
    for text, md in zip(["""
<h2>Bayesian Changepoint Detector</h2>

<ol>
<li> Initialize
</li>
 <ul>
  <li>
   $P(r_0)= S(r)$ or $P(r_0=0)=1$ and
 </li>
  <li>
   $ν^{(0)}_1 = ν_{prior}$ and $χ^{(0)}_1 = χ_{prior}$
 </li>
  </ul>
 <li>
 Observe New Datum $x_t$
</li>
 <li>
  Evaluate Predictive Probability $π_{1:t} = P(x_t |ν^{(r)}_t,χ^{(r)}_t)$
</li>
 <li>
  Calculate Growth Probabilities $P(r_t=r_{t-1}+1, x_{1:t}) = P(r_{t-1}, x_{1:t-1}) \cdot π^{(r)}_t \cdot (1−H(r^{(r)}_{t-1}))$
</li>
 <li>
  Calculate Changepoint Probabilities $P(r_t=0, x_{1:t})= \sum_{r_{t-1}} P(r_{t-1}, x_{1:t-1}) \cdot π^{(r)}_t \cdot H(r^{(r)}_{t-1})$
</li>
 <li>
  Calculate Evidence $P(x_{1:t}) = \sum_{r_{t-1}} P (r_t, x_{1:t})$
</li>
 <li>
  Determine Run Length Distribution $P (r_t | x_{1:t}) = P (r_t, x_{1:t})/P (x_{1:t}) $
</li>
 <li>
  Update Sufficient Statistics :
</li>
 <ul>
  <li>
   $ν^{(0)}_{t+1} = ν_{prior}$, $χ^{(0)}_{t+1} = χ_{prior}$
 </li>
  <li>
   $ν^{(r+1)}_{t+1} = ν^{(r)}_{t} +1$, $χ^{(r+1)}_{t+1} = χ^{(r)}_{t} + u(x_t)$
 </li>
  </ul>
 <li>
  Perform Prediction $P (x_{t+1} | x_{1:t}) =   P (x_{t+1}|x_{1:t} , r_t) \cdot P (r_t|x_{1:t})$
</li>
 <li>
  go to (2)
</li>
 </ol>
        ""","""
Bayesian Changepoint Detector
-----------------------------

* an implementation of
[Adams &amp; MacKay 2007 "Bayesian Online Changepoint Detection"](http://arxiv.org/abs/0710.3742)
in Python.

````
@TECHREPORT{ adams-mackay-2007,
AUTHOR = "Ryan Prescott Adams and David J.C. MacKay",
TITLE  = "Bayesian Online Changepoint Detection",
INSTITUTION = "University of Cambridge",
ADDRESS = "Cambridge, UK",
YEAR = "2007",
NOTE = "arXiv:0710.3742v1 [stat.ML]",
URL = "http://arxiv.org/abs/0710.3742"
}
````

* adapted from https://github.com/JackKelly/bayesianchangepoint by Jack Kelly (2013) for a binomial input.

* This code is based on the  [MATLAB implementation](http://www.inference.phy.cam.ac.uk/rpa23/changepoint.php) provided by Ryan Adam. available at http://hips.seas.harvard.edu/content/bayesian-online-changepoint-detection

"""], [False, True]):
        s.add_slide(content=text, notes='', md=md)
    #
    # s.add_slide_summary(
    #         ['Go fullscreen using the f key',
    #          'You can have an overlook using the o key',
    #          'Navigate using the arrow keys',
    #          'see notes using $P(x) = \exp(i)$ the n key'
    #           'You can have an overlook using the o key',
    #           'Navigate using the arrow keys',
    #           'see notes using the n key'],
    #           title='The Bayesian Changepoint Algorithm', fragment=True,
    #                       notes="""
    # * and write notes using markdown
    #
    # """)

    s.add_slide(content=s.content_figures(
    [os.path.join(figpath_talkbcp, 'github.png')],
            title=title, height=s.meta['height']*.825),
    notes="""

    """)


    modes = ['max'] # 'expectation',#for mode in ['expectation']:#, 'max']:# for mode in ['expectation', 'max']:
    for mode in modes:

        figname = os.path.join(figpath_talkbcp, 'bayesianchangepoint_' + mode + '.png')
        if not os.path.isfile(figname):

            T = 400
            mode = 'max'
            p_gen = .25 * np.ones(T)
            p_gen[100:300] = .75
            np.random.seed(2018)
            o = 1 * (p_gen > np.random.rand(T))

            p_bar, r, beliefs = bcp.inference(o, h=1/200, p0=.5)
            fig, axs = bcp.plot_inference(o, p_gen, p_bar, r, beliefs, max_run_length=250, mode=mode, fig_width=fig_width)
            fig.savefig(figname, dpi=400)

        s.add_slide(content=s.content_figures([figname],
                    title=title, height=s.meta['height']*.825),
           notes="""

        """)

    s.close_section()

i_section += 1
if do_section[i_section]:
    #################################################################################
    ## 🏄🏄🏄🏄🏄🏄🏄🏄 RESULTS - 5''  🏄🏄🏄🏄🏄🏄🏄🏄
    #################################################################################
    #################################################################################

    s.open_section()
    s.add_slide_outline(i_section-1)
    ############################################################################
    title = meta['sections'][i_section-1]

    # tag = 'bayesianchangepoint_'
    # s.add_slide(content=s.content_figures(
    #     [os.path.join(figpath_aSPEM, txt + '.png') for txt in [tag + 'm', tag + 'e']],
    #             title=title, height=s.meta['height']*.825, transpose=True, fragment=True),
    #    notes="""
    #
    # """)

    for i_block in range(3):
        for mode in modes:
            figname = os.path.join(figpath_talkbcp, 'bayesianchangepoint_exp_' + mode + '_' + str(i_block) + '.png')
            if not os.path.isfile(figname):

                seed = 42
                np.random.seed(seed)
                #N_time = 1000
                #N_trials = 4

                tau = 25.
                N_blocks = 3 # 4 blocks avant
                seed = 51 #119 #2017
                N_trials = 200
                tau = N_trials/5.
                (trials, p) = bcp.switching_binomial_motion(N_trials=N_trials, N_blocks=N_blocks, tau=tau, seed=seed)

                h = 1./tau # a.exp['tau']
                print('this experiment uses', N_trials, 'trials and a switch rate of h=', h, '(that is, one switch every', 1/h, 'trials on average)')
                print('i_block=', i_block)
                o = p[:, i_block, 0]
                p_bar, r, beliefs = bcp.inference(o, h=h, p0=.5)
                fig, axs = bcp.plot_inference(p[:, i_block, 0], p[:, i_block, 1], p_bar, r, beliefs, max_run_length=250, mode=mode, fig_width=fig_width)
                fig.savefig(figname, dpi=400)

            s.add_slide(content=s.content_figures([figname],
                        title=title +  ' - inference with BCP', height=s.meta['height']*.825),
               notes="""

            """)
    # tag = 'results_bayesianchangepoint_'
    # for txt in [tag + 'm', tag + 'e']:
    #     s.add_slide(content=s.content_figures(
    #         [os.path.join(figpath_ms, txt + '.png')],
    #         # [os.path.join(figpath_aSPEM, txt + '.png')],
    #                 title=title, height=s.meta['height']*.825),
    #        notes="""
    #
    #     """)

    tag = 'Results_BCP_sujet'
    for txt in [str(i) for i in [6, 10, 5, 2]]:
        s.add_slide(content=s.content_figures(
            [os.path.join(figpath_aSPEM, tag + '_' + txt + '.png')],
                    title=title +  ' - fit with BCP', height=s.meta['height']*.825),
           notes="""

        """)

    # TODO : average KDE
    tag = 'kde_mean'
    for mode in modes:
        s.add_slide(content=s.content_figures(
            [os.path.join(figpath_ms, tag + '_' + txt + '_' + mode + '.png') for txt in ['v_a', 'p_bet']],
                    title=title +  ' - fit with BCP', height=s.meta['height']*.7, transpose=False, fragment=True),
           notes="""

        """)
    s.close_section()


if do_section[i_section]:
    #################################################################################
    ## 🏄🏄🏄🏄🏄🏄🏄🏄 OUTRO - 5''  🏄🏄🏄🏄🏄🏄🏄🏄
    #################################################################################
    #################################################################################

    s.open_section()
    s.add_slide(content=intro,
        notes="""
* Thanks for your attention!
 """)
    #
    # s.add_slide(content=s.content_figures([figname],
    #         title='', height=s.meta['height']*.825),
    # notes="""
    #
    # """)

    s.close_section()


if slides_filename is None:

    with open("/tmp/wiki.txt", "w") as text_file:
        text_file.write("""\
#acl All:read

= {title}  =

 Quoi:: [[{conference_url}|{conference}]]
 Qui:: {author}
 Quand:: {DD}/{MM}/{YYYY}
 Où:: {location}
 Support visuel:: http://blog.invibe.net/files/{tag}.html


 What:: talk @ the [[{conference_url}|{conference}]]
 Who:: {author}
 When:: {DD}/{MM}/{YYYY}
 Where:: {location}
 Slides:: http://blog.invibe.net/files/{tag}.html

== reference ==
{{{{{{
#!bibtex
@inproceedings{{{tag},
    Author = "{author}",
    Booktitle = "{conference}, {location}",
    Title = "{title}",
    Url = "{url}",
    Year = "{YYYY}",
}}
}}}}}}
## add an horizontal rule to end the include
{wiki_extras}
""".format(**meta) )

else:
    s.compile(filename=slides_filename)


#
# Preparing Effective Presentations
# ---------------------------------
#
# Clear Purpose - An effective image should have a main point and not be just a collection of available data. If the central theme of the image isn't identified readily, improve the paper by revising or deleting the image.
#
# Readily Understood - The main point should catch the attention of the audience immediately. When trying to figure out the image, audience members aren't fully paying attention to the speaker - try to minimize this.
#
# Simple Format - With a simple, uncluttered format, the image is easy to design and directs audience attention to the main point.
#
# Free of Nonessential Information - If information doesn't directly support the main point of the image, reserve this content for questions.
#
# Digestible - Excess information can confuse the audience. With an average of seven images in a 10-minute paper, roughly one minute is available per image. Restrict information to what is extemporaneously explainable to the uninitiated in the allowed length of time - reading prepared text quickly is a poor substitute for editing.
#
# Unified - An image is most effective when information is organized around a single central theme and tells a unified story.
#
# Graphic Format - In graphs, qualitative relationships are emphasized at the expense of precise numerical values, while in tables, the reverse is true. If a qualitative statement, such as "Flow rate increased markedly immediately after stimulation," is the main point of the image, the purpose is better served with a graphic format. A good place for detailed, tabular data is in an image or two held in reserve in case of questions.
#
# Designed for the Current Oral Paper - Avoid complex data tables irrelevant to the current paper. The audience cares about evidence and conclusions directly related to the subject of the paper - not how much work was done.
#
# Experimental - There is no time in a 10-minute paper to teach standard technology. Unless the paper directly examines this technology, only mention what is necessary to develop the theme.
#
# Visual Contrast - Contrasts in brightness and tone between illustrations and backgrounds improves legibility. The best color combinations include white letters on medium blue, or black on yellow. Never use black letters on a dark background. Many people are red/green color blind - avoid using red and green next to each other.
#
# Integrated with Verbal Text - Images should support the verbal text and not merely display numbers. Conversely, verbal text should lay a proper foundation for each image. As each image is shown, give the audience a brief opportunity to become oriented before proceeding. If you will refer to the same image several times during your presentation, duplicate images.
#
# Clear Train of Thought - Ideas developed in the paper and supported by the images should flow smoothly in a logical sequence, without wandering to irrelevant asides or bogging down in detail. Everything presented verbally or visually should have a clear role supporting the paper's central thesis.
#
# Rights to Use Material - Before using any text, image, or other material, make sure that you have the rights to use it. Complex laws and social rules govern how much of someone's work you can reproduce in a presentation. Ignorance is no defense. Check that you are not infringing on copyright or other laws or on the customs of academic discourse when using material.

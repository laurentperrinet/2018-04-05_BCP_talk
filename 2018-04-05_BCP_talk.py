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
figpath_ms = os.path.join(home, 'pool/ANR-REM/ASPEM_REWARD/AnticipatorySPEM/ms/figures')


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
 title='Principles and psychophysics of Active Inference in anticipating a dynamic, switching probabilistic bias',
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
s.meta['Acknowledgements'] = '', #s.content_imagelet(os.path.join(figpath_talkbcp, 'qr.png'), height_px),
#
# s.meta['Acknowledgements'] ="""<h3>Acknowledgements:</h3>
#    <ul>
#     <li>Jim Bednar @ Continuum Analytics &amp; University of Edinburgh</li>
#     <li>Rick Adams and Karl     Friston @ UCL - Wellcome Trust Centre for Neuroimaging</li>
#     <li>Wahiba Taouali, Giacomo Benvenuti, Frédéric Chavane - ANR BalaV1 </li>
#     <li>Mina Aliakbari Khoei, Guillaume Masson and Anna Montagnini - FACETS-ITN Marie Curie Training</li>
#    </ul>
#    {Jim}{Karl}{Mina}{Anna}{GSM}<a href="https://github.com/laurentperrinet/slides.py">{Python}</a>
# """.format(Jim=s.content_imagelet(os.path.join(figpath_aSPEM, 'jim.jpg'), height_px),
#            Karl=s.content_imagelet(os.path.join(figpath_aSPEM, 'karl.jpg'), height_px),
# Mina=s.content_imagelet(os.path.join(figpath_aSPEM, 'mina.jpg'), height_px),
# Anna=s.content_imagelet(os.path.join(figpath_aSPEM, 'anna.jpg'), height_px),
# GSM=s.content_imagelet(os.path.join(figpath_aSPEM, 'gsm.jpg'), height_px),
# Python=s.content_imagelet(os.path.join(figpath_aSPEM_, 'python-powered-h-140x182.png'), height_px),
#            )
if do_section[i_section]:
    s.open_section()
    #################################################################################
    ## Intro - 5''
    #################################################################################
    #################################################################################
    figpath_slides = os.path.join(home, 'nextcloud/libs/slides.py/figures/')
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
    intro += s.content_imagelet(os.path.join(figpath_talkbcp, 'qr.png'), s.meta['height']*.2) #bgcolor="black",
    # height=s.meta['height']*.2, width=s.meta['height']*.2)
    # {Acknowledgements}
    intro += """
    <h4><a href="{conference_url}">{conference}</a></h4>
    """.format(**meta)

    s.add_slide(content=intro,
            notes="""
    * (AUTHOR) Hi, I am Laurent Perrinet from (LOGO) the Institute de Neurosciences de la Timone in Marseille, a joint unit from the CNRS and AMU. Using computational models, I am investigating the link between the efficiency of behavioural responses in vision, their underlying neural code and their adaptation to the structure of the world.

    * (SHOW TITLE - THEME) = In particular, I will use today a visual illusion -the FLE- to provide evidence that we use predictive mechanism to compensate for neural delays and perceive the visual world in **real-time** (I will try to define today what I mean by that...)

    * (ACKNO) this endeavour involves different techniques, tools and... persons. From the head on, I wish to thank the people who collaborated to this project and in particular Rick Adams and Karl Friston and the Wellcome Trust Centre for Neuroimaging for providing the tools for a successful visit / but also Mina, Guillaume and Anna for the great oppportunity to link  theories with psychophysical data; Wahiba, Giacomo and Frédéric for the challenging task of linking such models to the neural activity in NHP, and finally Jean-Bernard, Sohir and Laurent Madelain for their essential knowledge in adaptation and reinforcement.


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
    notes=""" All the material is available online - please flash this QRcode this leads to a page with """)
    s.add_slide(content=intro,
        notes="""

* (SHOW TITLE) of interest for biologists to understand what the neural activity (or behavior) they record relates to something relevant (a function, a particular object)

* here, I will try to introduce you to the concept that Probabilities and Bayesian inference can offer a language to alleviate this question

""")

    s.close_section()

figpath_GDR = os.path.join(home, 'pool/ANR-REM/ASPEM_REWARD/AnticipatorySPEM/2017-11-24_Poster_GDR_Robotique/figures')
figpath_aSPEM = os.path.join(home, 'pool/ANR-REM/ASPEM_REWARD/AnticipatorySPEM/figures')


######################## MOTIVATION #################################
i_section += 1
if do_section[i_section]:
    s.open_section()
    title = meta['sections'][i_section-1]
    s.add_slide_outline(i_section-1)

    s.add_slide(content=s.content_figures(
    [os.path.join(figpath_aSPEM, 'protocol_recording.png')],
            title=title + ' - a Real-life example', height=s.meta['height']*.825*.001), # HACK
    notes="""

    """)

    s.add_slide(content=s.content_figures(
    [os.path.join(figpath_aSPEM, 'protocol_recording.png')],
            title=title + ' - Eye Movements', height=s.meta['height']*.825),
    notes="""

    """)

    for txt in ['1', '2']:
        s.add_slide(content=s.content_figures(
    [os.path.join(figpath_GDR, 'image_anna_' + txt + '.png')],
                title=title + ' - Eye Movements', height=s.meta['height']*.825),
       notes="""

    """)

    for tag in ['Experiment_classique_', 'Experiment_randomblock_']:
        for txt in [str(i) for i in range(4)]:
            s.add_slide(content=s.content_figures(
        [os.path.join(figpath_aSPEM, tag + txt + '.png')],
                    title=title + ' - Eye Movements', height=s.meta['height']*.775),
           notes="""

        """)

    s.add_slide(content=s.content_figures(
    [os.path.join(figpath_aSPEM, 'Experiment_randomblock.png')],
            title=title + ' - Random-length block design', height=s.meta['height']*.825),
    notes="""

    """)

    s.add_slide(content=s.content_figures(
    [os.path.join(figpath_aSPEM, 'protocol_bet.png')],
            title=title + ' - Random-length block design', height=s.meta['height']*.825),
    notes="""

    """)
    s.close_section()


i_section += 1
if do_section[i_section]:
    s.open_section()
    ############################################################################
    title = meta['sections'][i_section-1]
    s.add_slide_outline(i_section-1)


    s.add_slide(content=s.content_figures(
    [os.path.join(figpath_aSPEM, 'Experiment_randomblock.png')],
            title=title + ' - Random-length block design', height=s.meta['height']*.825),
    notes="""

    """)


    s.add_slide(content=s.content_figures(
    [os.path.join(figpath_aSPEM, 'Experiment_randomblock_bet.png')],
            title=title, height=s.meta['height']*.825),
    notes="""

    """)


    # for txt in ['results_pari', 'results_enregistrement']:
    #     s.add_slide(content=s.content_figures(
    # [os.path.join(figpath_GDR, txt + '.png')],
    #             title=title, height=s.meta['height']*.825),
    #    notes="""
    #
    # """)


    for txt in ['Fit_vitesse', 'Fonction_Fit']:
        s.add_slide(content=s.content_figures(
    [os.path.join(figpath_ms, txt + '.png')],
                title=title + ' - Fitting eye movements', height=s.meta['height']*.825),
       notes="""

    """)

    s.add_slide(content=s.content_figures(
    [os.path.join(figpath_aSPEM, 'Experiment_randomblock_EM.png')],
            title=title, height=s.meta['height']*.825),
    notes="""

    """)

    s.add_slide(content=s.content_figures(
    [os.path.join(figpath_aSPEM, 'Experiment_randomblock_bet_EM.png')],
            title=title, height=s.meta['height']*.825),
    notes="""

    """)

    for txt in ['P_real', 'p_bet--v_a']:
        s.add_slide(content=s.content_figures(
    [os.path.join(figpath_GDR, txt + '.png')],
                title=title, height=s.meta['height']*.75),
       notes="""

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
    s.open_section()
    s.add_slide_outline(i_section-1)
    ############################################################################
    title = meta['sections'][i_section-1]

    s.add_slide(content=s.content_figures(
    [os.path.join(figpath_GDR, 'exp.png')],
            title=title, height=s.meta['height']*.825),
    notes="""

    """)

    tag = 'bcp_model_layer_' #  'model_bcp_'

    for txt in [str(i) for i in range(1, 6)]:
        s.add_slide(content=s.content_figures(
    [os.path.join(figpath_aSPEM, tag + txt + '.png')],
                title=title, height=s.meta['height']*.775),
       notes="""

    """)
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
  Evaluate Predictive Probability $π_{1:t} = P(x |ν^{(r)}_t,χ^{(r)}_t)$
</li>
 <li>
  Calculate Growth Probabilities $P(r_t=r_{t-1}+1, x_{1:t}) = P(r_{t-1}, x_{1:t-1}) π^{(r)}_t (1−H(r^{(r)}_{t-1}))$
</li>
 <li>
  Calculate Changepoint Probabilities $P(r_t=0, x_{1:t})= \sum_{r_{t-1}} P(r_{t-1}, x_{1:t-1}) π^{(r)}_t H(r^{(r)}_{t-1})$
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
  Perform Prediction $P (x_{t+1} | x_{1:t}) =   P (x_{t+1}|x_{1:t} , r_t) P (r_t|x_{1:t})$
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

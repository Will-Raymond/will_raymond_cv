---
layout: page-fullwidth
#
# Content
#

categories:
  - publication
tags:
  - paper mechanistic-modeling ODE mRNA bursting-gene-model
permalink: /publications/physical_biology_2018
header: False

---

<div class="row" style="font-size: 20px; z-index: -1; background: rgba(0,0,22,.5); padding-left: 35px; padding-top: 35px; padding-right: 35px;box-shadow: 0 0 4px 4px rgba(0,0,22,.5);">    
  <div class="row" style="font-size: 35px;">
    Identification of gene regulation models from single-cell data
  </div> 



  <div class="row" style="font-size: 15px;"> 
    Lisa Weber, <span style="color: #57ffe6;"> William Raymond</span>, Brian Munsky
  </div>


<div class="row"  style="font-size: 25px; padding-bottom: 20px;"> Link to the paper: <a href="https://iopscience.iop.org/article/10.1088/1478-3975/aabc31"> <span class='internalicon' style="display:inline-block;"> <img src="../images/external-link.svg" width="25" height="25">  </span> </a></div> 

<div class="row" style="background: rgba(87, 255, 230, 0.20); padding-bottom: 35px; padding-left: 15px; padding-right: 15px;outline:.3em solid #57ffe6;"> 

  <h3 style="color: white;">
    Key Takeaway:
  </h3>
  <h4 style="color: white;">
   A primer on using ODE analyses, stochastic simulations, and metropolis-hastings for fitting bursting gene models.
  </h4>
</div>

<div class="row" style="padding: 10px"> 

I provided a simple tkinter GUI for the models described in this paper.

  <h3 style="padding-bottom: 10px; padding-top: 10px; margin 5px;">
    Key Figure:
  </h3>
  <img src="../images/phybio_2018_fig.jpg" style="padding-top: 0px; padding-left: 10px; padding-right: 10px;">

  <sub> Screenshot of the GUI made for the paper. </sub>

</div>

<div class="row" style="padding: 10px"> 
  <h3 style="padding-top: 10px;">
    Abstract:
  </h3>

In quantitative analyses of biological processes, one may use many different scales of models (e.g. spatial or non-spatial, deterministic or stochastic, time-varying or at steady-state) or many different approaches to match models to experimental data (e.g. model fitting or parameter uncertainty/sloppiness quantification with different experiment designs). These different analyses can lead to surprisingly different results, even when applied to the same data and the same model. We use a simplified gene regulation model to illustrate many of these concerns, especially for ODE analyses of deterministic processes, chemical master equation and finite state projection analyses of heterogeneous processes, and stochastic simulations. For each analysis, we employ Matlab and Python software to consider a time-dependent input signal (e.g. a kinase nuclear translocation) and several model hypotheses, along with simulated single-cell data. We illustrate different approaches (e.g. deterministic and stochastic) to identify the mechanisms and parameters of the same model from the same simulated data. For each approach, we explore how uncertainty in parameter space varies with respect to the chosen analysis approach or specific experiment design. We conclude with a discussion of how our simulated results relate to the integration of experimental and computational investigations to explore signal-activated gene expression models in yeast (Neuert et al 2013 Science 339 584–7) and human cells (Senecal et al 2014 Cell Rep. 8 75–83)5.

</div>



<div class="row"  style="font-size: 25px; padding-bottom: 20px;">

<div class="large-8 columns"> </div>
<div class="large-3 columns"> 
 Back to publications &nbsp; <span class='internalicon' style="display:inline-block;" onclick="window.location='{{site.url}}{{site.baseurl}}/publications/'"> <img src="../images/next-arrow.svg" width="20" height="20"> </span>
 </div>
 </div> 
</div>
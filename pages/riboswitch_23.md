---
layout: page-fullwidth
#
# Content
#

categories:
  - publication
tags:
  - paper mechanistic-modeling ODE mRNA bursting-gene-model
permalink: /publications/riboswitch_23
header: False

---

<div class="row" style="font-size: 20px; z-index: -1; background: rgba(0,0,22,.5); padding-left: 35px; padding-top: 35px; padding-right: 35px;box-shadow: 0 0 4px 4px rgba(0,0,22,.5);">    
  <div class="row" style="font-size: 35px;">
    Identification of Potential Riboswitch Elements in Homo Sapiens mRNA 5'UTR Sequences Using Positive-Unlabeled Machine Learning
  </div> 



  <div class="row" style="font-size: 15px;"> 
    <span style="color: #57ffe6;"> William Raymond</span>, Jacob DeRoo, Dr Brian Munsky
  </div>


<div class="row"  style="font-size: 25px; padding-bottom: 20px;"> Link to the paper: <a href="https://www.biorxiv.org/content/10.1101/2023.11.23.568398v1.full.pdf6"> <span class='internalicon' style="display:inline-block;"> <img src="../images/external-link.svg" width="25" height="25">  </span> </a></div> 

<div class="row" style="background: rgba(87, 255, 230, 0.20); padding-bottom: 35px; padding-left: 15px; padding-right: 15px;outline:.3em solid #57ffe6;"> 

  <h3 style="color: white;">
    Key Takeaway:
  </h3>
  <h4 style="color: white;">
    436 potential riboswitch elements detected for future experimental validation with a cross-validated positive unlabeled machine learning ensemble trained on known riboswitches.
  </h4>
</div>

<div class="row" style="padding: 10px"> 

I provided a simple tkinter GUI for the models described in this paper.

  <h3 style="padding-bottom: 10px; padding-top: 10px; margin 5px;">
    Key Figure:
  </h3>
  <img src="../images/rs_graphical_abstract.jpg" style="padding-top: 0px; padding-left: 10px; padding-right: 10px;">

  <sub> Graphical Abstract </sub>

</div>

<div class="row" style="padding: 10px"> 
  <h3 style="padding-top: 10px;">
    Abstract:
  </h3>

Riboswitches are a class of noncoding RNA structures that interact with target ligands to cause a conformational change that can then execute some regulatory purpose within the cell. Riboswitches are ubiquitous and well characterized in bacteria and prokaryotes, with additional examples also being found in fungi, plants, and yeast. To date, no purely RNA-small molecule riboswitch has been discovered in Homo Sapiens. Several analogous riboswitch-like mechanisms have been described within the H. Sapiens translatome within the past decade, prompting the question: Is there a H. Sapiens riboswitch dependent on only small molecule ligands? In this work, we set out to train positive unlabeled machine learning classifiers on known riboswitch sequences and apply the classifiers to H. Sapiens mRNA 5’UTR sequences found in the 5’UTR database, UTRdb, in the hope of identifying a set of mRNAs to investigate for riboswitch functionality. 67,683 riboswitch sequences were obtained from RNAcentral and sorted for ligand type and used as positive examples and 48,031 5’UTR sequences were used as unlabeled, unknown examples. Positive examples were sorted by lig- and, and 20 positive-unlabeled classifiers were trained on sequence and secondary structure features while withholding one or two ligand classes. Cross validation was then performed on the withheld ligand sets to obtain a validation accuracy range of 75%-99%. The joint sets of 5’UTRs identified as potential riboswitches by the 20 classifiers were then analyzed. 15333 sequences were identified as a riboswitch by one or more classifier(s) and 436 of the H. Sapiens 5’UTRs were labeled as harboring potential riboswitch elements by all 20 classifiers. These 436 sequences were mapped back to the most similar riboswitches within the positive data and examined. An online database of identified and ranked 5’UTRs, their features, and their most similar matches to known riboswitches, is provided to guide future experimental efforts to identify H. Sapiens riboswitches.

</div>



<div class="row"  style="font-size: 25px; padding-bottom: 20px;">

<div class="large-8 columns"> </div>
<div class="large-3 columns"> 
 Back to publications &nbsp; <span class='internalicon' style="display:inline-block;" onclick="window.location='{{site.url}}{{site.baseurl}}/publications/'"> <img src="../images/next-arrow.svg" width="20" height="20"> </span>
 </div>
 </div> 
</div>
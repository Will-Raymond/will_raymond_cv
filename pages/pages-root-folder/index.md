---
#
# Use the widgets beneath and the content will be
# inserted automagically in the webpage. To make
# this work, you have to use › layout: frontpage
#
layout: page
header:
  image_fullwidth: ../will_raymond_cv/images/celllong_lightpurple5.gif

#
# Use the call for action to show a button on the frontpage
#
# To make internal links, just use a permalink like this
# url: /getting-started/
#
# To style the button in different colors, use no value
# to use the main color or success, alert or secondary.
# To change colors see sass/_01_settings_colors.scss
#
permalink: /index.html
#
# This is a nasty hack to make the navigation highlight
# this page as active in the topbar navigation
#
homepage: True
title: ""
teaser: ""


---
<!--
<video class="background-video" autoplay loop muted poster="https://assets.codepen.io/6093409/river.jpg">
<source src="../will_raymond_cv/images/bc4.mp4" type="video/mp4">
</video> -->

<div class="row t10" style="font-size: 20px; z-index: -1; background: rgba(10,40,60,.5); padding: 15px; box-shadow: 0 0 4px 4px rgba(10,40,60,.5);">
<div class="row t40minus" style="font-size: 35px; padding: 7px;"> <h3> William Scott Raymond </h3> </div>
<div class="row t10" style="font-size: 22px;  padding: 7px;"> 
  Computational Biologist  &nbsp;&nbsp; • &nbsp;&nbsp;  mRNA modeler &nbsp;&nbsp; • &nbsp;&nbsp;  Painter &nbsp;&nbsp;
</div></div>

<div class="row t10" style="font-size: 20px; z-index: -1; background: rgba(0,0,22,.5); padding: 15px; box-shadow: 0 0 4px 4px rgba(0,0,22,.5);">
  <div class="row t10" style="font-size: 20px; opacity: 1;">
    <div class="large-6 columns"> 
      <div> 
        <img src="/will_raymond_cv/images/wsr_photo_small.png" alt="Photo of William Raymond hiking">
      </div>
    </div>
    <div class="large-6 columns">
      <h4> About me 
      </h4> 
      <div>
      I am a computational biologist with a background in quantitative data analysis, mechanistic model building, and RNA biology.
      I graduated with a PhD in Bioengineering at Colorado State University in spring 2024 from Dr. Brian Munsky's Lab. 
      While there I focused on coding TASEP based mRNA models to fit, reproduce, and classify Nascent Chain Tracking (NCT) experiments with the ultimate goal of designing more informative experiments. Besides writing software for TASEP model building, I used machine learning to classify potential riboswitches within the human genome.
      </div>
    </div>
  </div>
  <div class="row t10" style="font-size: 20px; padding: 15px;">
      <div>
            I have a strong interest in the open questions in the field of RNA biology and hope to provide insight to the scientific community about mRNA dynamics such as ribosomal collision dynamics, mRNA codon selection, mRNA decay, and tRNA abundances during my upcoming career.
          Besides RNA, I am passionate about ethics in machine learning, as well ethics in scientific research as a whole. AI and machine learning have become dominant in public and scientific discourse, with questionable approaches, data sets, and abuses outpacing ethics focused research practices. To respond, scientists must adapt by increasing our focus on ethical practices through constant awareness and training.
      </div>
  </div>
  <div class="row t10" style="font-size: 20px; padding: 15px;">
      <div>
      When I am not working, I love to spend afternoons painting, swimming, or hiking with my partner. Feel free to reach out, I will be fastest to respond over email!
      </div>
  </div>
  <div class="row t10" style="font-size: 20px; opacity: 1; padding: 15px">
    <p style="font-size: 30px;"> Check out my <a href="{{site.baseurl}}/publications/" > publications! </a> </p>
  </div>

</div>



title: A new 2.5D representation for lymph node detection using random sets of deep convolutional neural network observations

## Roth, H. R. and Lu, L. and Seff, A. and Cherry, K. M. and Hoffman, J. and Wang, S. and Liu, J. and Turkbey, E. and Summers, R. M.
MICCAI

<a href="https://doi.org/10.1007/978-3-319-10404-1_65">DOI</a>

## Abstract
Automated Lymph Node (LN) detection is an important clinical diagnostic task but very challenging due to the low contrast of surrounding structures in Computed Tomography (CT) and to their varying sizes, poses, shapes and sparsely distributed locations. State-of-the-art studies show the performance range of 52.9% sensitivity at 3.1 false-positives per volume (FP/vol.), or 60.9% at 6.1 FP/vol. for mediastinal LN, by one-shot boosting on 3D HAAR features. In this paper, we first operate a preliminary candidate generation stage, towards -100% sensitivity at the cost of high FP levels (-40 per patient), to harvest volumes of interest (VOI). Our 2.5D approach consequently decomposes any 3D VOI by resampling 2D reformatted orthogonal views N times, via scale, random translations, and rotations with respect to the VOI centroid coordinates. These random views are then used to train a deep Convolutional Neural Network (CNN) classifier. In testing, the CNN is employed to assign LN probabilities for all N random views that can be simply averaged (as a set) to compute the final classification probability per VOI. We validate the approach on two datasets: 90 CT volumes with 388 mediastinal LNs and 86 patients with 595 abdominal LNs. We achieve sensitivities of 70%/83% at 3 FP/vol. and 84%/90% at 6 FP/vol. in mediastinum and abdomen respectively, which drastically improves over the previous state-of-the-art work.

A <b>pdf file</b> of this publication is available for personal use.Enter your e-mail address in the box below and press the button. You will receive an e-mail message with a link to the pdf file.
<form action="sender.php">  <input type="text" name="email">  <input type="submit" value="Send Roth14.pdf:pdfRoth14.pdf:PDF by e-mail"></form>
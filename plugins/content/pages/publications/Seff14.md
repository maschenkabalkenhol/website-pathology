title: 2D view aggregation for lymph node detection using a shallow hierarchy of linear classifiers

## Seff, Ari and Lu, Le and Cherry, Kevin M. and Roth, Holger R. and Liu, Jiamin and Wang, Shijun and Hoffman, Joanne and Turkbey, Evrim B. and Summers, Ronald M.
MICCAI

<a href="https://doi.org/10.1007/978-3-319-10404-1_68">DOI</a>

## Abstract
Enlarged lymph nodes (LNs) can provide important information for cancer diagnosis, staging, and measuring treatment reactions, making automated detection a highly sought goal. In this paper, we propose a new algorithm representation of decomposing the LN detection problem into a set of 2D object detection subtasks on sampled CT slices, largely alleviating the curse of dimensionality issue. Our 2D detection can be effectively formulated as linear classification on a single image feature type of Histogram of Oriented Gradients (HOG), covering a moderate field-of-view of 45 by 45 voxels. We exploit both max-pooling and sparse linear fusion schemes to aggregate these 2D detection scores for the final 3D LN detection. In this manner, detection is more tractable and does not need to perform perfectly at instance level (as weak hypotheses) since our aggregation process will robustly harness collective information for LN detection. Two datasets (90 patients with 389 mediastinal LNs and 86 patients with 595 abdominal LNs) are used for validation. Cross-validation demonstrates 78.0% sensitivity at 6 false positives/volume (FP/vol.) (86.1% at 10 FP/vol.) and 73.1% sensitivity at 6 FP/vol. (87.2% at 10 FP/vol.), for the mediastinal and abdominal datasets respectively. Our results compare favorably to previous state-of-the-art methods.

A <b>pdf file</b> of this publication is available for personal use.Enter your e-mail address in the box below and press the button. You will receive an e-mail message with a link to the pdf file.
<form action="sender.php">  <input type="text" name="email">  <input type="submit" value="Send Seff14.pdf:pdfSeff14.pdf:PDF by e-mail"></form>
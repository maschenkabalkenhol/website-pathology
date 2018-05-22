title: Towards automated segmentation of the pathological lung in CT

## I.C. Sluimer and M. Prokop and B. van Ginneken
TMI

<a href="https://doi.org/10.1109/TMI.2005.851757">DOI</a>

## Abstract
Conventional methods of lung segmentation rely on a large gray value contrast between lung fields and surrounding tissues. These methods fail on scans with lungs that contain dense pathologies, and such scans occur frequently in clinical practice. We propose a segmentation-by-registration scheme in which a scan with normal lungs is elastically registered to a scan containing pathology. When the resulting transformation is applied to a mask of the normal lungs, a segmentation is found for the pathological lungs. As a mask of the normal lungs, a probabilistic segmentation built up out of the segmentations of 15 registered normal scans is used. To refine the segmentation, voxel classification is applied to a certain volume around the borders of the transformed probabilistic mask. Performance of this scheme is compared to that of three other algorithms: a conventional, a user-interactive and a voxel classification method. The algorithms are tested on 10 three-dimensional thin-slice computed tomography volumes containing high-density pathology. The resulting segmentations are evaluated by comparing them to manual segmentations in terms of volumetric overlap and border positioning measures. The conventional and user-interactive methods that start off with thresholding techniques fail to segment the pathologies and are outperformed by both voxel classification and the refined segmentation-by-registration. The refined registration scheme enjoys the additional benefit that it does not require pathological (hand-segmented) training data.

A <b>pdf file</b> of this publication is available for personal use.Enter your e-mail address in the box below and press the button. You will receive an e-mail message with a link to the pdf file.
<form action="sender.php">  <input type="text" name="email">  <input type="submit" value="Send Slui05a.pdf:pdfSlui05a.pdf:PDF by e-mail"></form>
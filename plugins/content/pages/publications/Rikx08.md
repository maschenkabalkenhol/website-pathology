title: Adaptive Local Multi-Atlas Segmentation: Application to Heart Segmentation in Chest CT Scans

## E. M. van Rikxoort and I. Isgum and M. Staring and S. Klein and B. van Ginneken
MI

<a href="https://doi.org/10.1117/12.773209">DOI</a>

## Abstract
Segmentation of anatomical structures is a prerequisite for many medical image analysis tasks. We propose a method that integrates local voxel classification and global shape models. The method starts by computing a local feature vector for every voxel and mapping this, via a classifier trained from example segmentations, to a probability that the voxel belongs to the structure to be segmented. Next, this probabilistic output is entered into a global shape model. This shape model is constructed by mapping aligned blurred versions of reference segmentations of the training data into a vector space and applying principal component analysis (PCA). The mapping onto a vector space that is applied guarantees valid results from the PCA. An advantage of using such a shape model is that there is no need to define corresponding landmarks on all training scans, which is a hard task on 3D data. Segmentation of unseen test data is performed by a least squares fit of the results of the voxel classification, after alignment and blurring, into the PCA space. The result of this procedure is for each voxel a probability that it belongs to the structure to be segmented conditioned on both local and global information. We demonstrate the effectiveness of the method on segmentation of lungs containing pathologic abnormalities in 3D CT data.

A <b>pdf file</b> of this publication is available for personal use.Enter your e-mail address in the box below and press the button. You will receive an e-mail message with a link to the pdf file.
<form action="sender.php">  <input type="text" name="email">  <input type="submit" value="Send Rikx08.pdf:pdfRikx08.pdf:PDF by e-mail"></form>
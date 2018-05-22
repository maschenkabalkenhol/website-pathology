title: Fovea Detection in Optical Coherence Tomography using Convolutional Neural Networks

## Bart Liefers and Freerk G. Venhuizen and Thomas Theelen and Carel Hoyng and Bram van Ginneken and Clara~I.~S'anchez
MI

<a href="https://doi.org/10.1117/12.2254301">DOI</a>

## Abstract
The fovea is an important clinical landmark that is used as a reference for assessing various quantitative measures, such as central retinal thickness or drusen count. In this paper we propose a novel method for automatic detection of the foveal center in Optical Coherence Tomography (OCT) scans. Although the clinician will generally aim to center the OCT scan on the fovea, post-acquisition image processing will give a more accurate estimate of the true location of the foveal center. A Convolutional Neural Network (CNN) was trained on a set of 781 OCT scans that classifies each pixel in the OCT B-scan with a probability of belonging to the fovea. Dilated convolutions were used to obtain a large receptive field, while maintaining pixel-level accuracy. In order to train the network more effectively, negative patches were sampled selectively after each epoch. After CNN classification of the entire OCT volume, the predicted foveal center was chosen as the voxel with maximum output probability, after applying an optimized three-dimensional Gaussian blurring. We evaluate the performance of our method on a data set of 99 OCT scans presenting different stages of Age-related Macular Degeneration (AMD). The fovea was correctly detected in 96.9% of the cases, with a mean distance error of 73 +- 112 micro meter. This result was comparable to the performance of a second human observer who obtained a mean distance error of 69 +- 94 micro meter. Experiments showed that the proposed method is accurate and robust even in retinas heavily affected by pathology.

A <b>pdf file</b> of this publication is available for personal use.Enter your e-mail address in the box below and press the button. You will receive an e-mail message with a link to the pdf file.
<form action="sender.php">  <input type="text" name="email">  <input type="submit" value="Send Lief17.pdf:pdfLief17.pdf:PDF by e-mail"></form>
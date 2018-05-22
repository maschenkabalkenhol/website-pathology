title: Computer-aided Detection of Cancer in Automated 3D Breast Ultrasound

## Tan, Tao and Platel, Bram and Mus, Roel and Tabar, Laszlo and Mann, Ritse and Karssemeijer, Nico
TMI

<a href="https://doi.org/10.1109/TMI.2013.2263389">DOI</a>

## Abstract
Automated 3D breast ultrasound (ABUS) has gained a lot of interest and may become widely used in screening of dense breasts, where sensitivity of mammography is poor. However, reading ABUS images is time consuming, and subtle abnormalities may be missed. Therefore, we are developing a computer aided detection (CAD) system to help reduce reading time and prevent errors. In the multi-stage system we propose, segmentations of the breast, the nipple and the chestwall are performed, providing landmarks for the detection algorithm. Subsequently, voxel features characterizing coronal spiculation patterns, blobness, contrast, and depth are extracted. Using an ensemble of neuralnetwork classifiers, a likelihood map indicating potential abnormality is computed. Local maxima in the likelihood map are determined and form a set of candidates in each image. These candidates are further processed in a second detection stage, which includes region segmentation, feature extraction and a final classification. On region level, classification experiments were performed using different classifiers including an ensemble of neural networks, a support vector machine, a k-nearest neighbors, a linear discriminant, and a gentle boost classifier. Performance was determined using a dataset of 238 patients with 348 images (views), including 169 malignant and 154 benign lesions. Using free response receiver operating characteristic (FROC) analysis, the system obtains a view-based sensitivity of 64% at 1 false positives per image using an ensemble of neuralnetwork classifiers.

A <b>pdf file</b> of this publication is available for personal use.Enter your e-mail address in the box below and press the button. You will receive an e-mail message with a link to the pdf file.
<form action="sender.php">  <input type="text" name="email">  <input type="submit" value="Send Tan13a.pdf:pdfTan13a.pdf:PDF by e-mail"></form>
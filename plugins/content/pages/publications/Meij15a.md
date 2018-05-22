title: The evaluation of multi-structure, multi-atlas pelvic anatomy features in a prostate MR Lymphography CAD system

## Midas Meijs and Oscar A. Debats and Henkjan J. Huisman
MI

<a href="https://doi.org/10.1117/12.2082708">DOI</a>

## Abstract
In prostate cancer, the detection of metastatic lymph nodes indicates progression from localized disease to metastasized cancer. The detection of positive lymph nodes is, however, a complex and time consuming task for experienced radiologists. Assistance of a two-stage Computer-Aided Detection (CAD) system in MR Lymphography (MRL) is not yet feasible due to the large number of false positives in the first stage of the system. By introducing a multi-structure, multi-atlas segmentation, using an affine transformation followed by a B-spline transformation for registration, the organ location is given by a mean density probability map. The atlas segmentation is semi-automatically drawn with ITK-SNAP, using Active Contour Segmentation. Each anatomic structure is identified by a label number. Registration is performed using Elastix, using Mutual Information and an Adaptive Stochastic Gradient optimization. The dataset consists of the MRL scans of ten patients, with lymph nodes manually annotated in consensus by two expert readers. The feature map of the CAD system consists of the Multi-Atlas and various other features (e.g. Normalized Intensity and multi-scale Blobness). The voxel-based Gentleboost classifier is evaluated using ROC analysis with cross validation. We show in a set of 10 studies that adding multi-structure, multi-atlas anatomical structure likelihood features improves the quality of the lymph node voxel likelihood map. Multiple structure anatomy maps may thus make MRL CAD more feasible.

A <b>pdf file</b> of this publication is available for personal use.Enter your e-mail address in the box below and press the button. You will receive an e-mail message with a link to the pdf file.
<form action="sender.php">  <input type="text" name="email">  <input type="submit" value="Send Meij15a.pdf:pdfMeij15a.pdf:PDF by e-mail"></form>
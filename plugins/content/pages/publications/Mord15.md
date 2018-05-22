title: Vessel segmentation in screening mammograms

## Jan-Jurre Mordang and Nico Karssemeijer
MI

<a href="https://doi.org/10.1117/12.2081804">DOI</a>

## Abstract
Blood vessels are a major cause of false positives in computer aided detection systems for the detection of breast cancer. Therefore, the purpose of this study is to construct a framework for the segmentation of blood vessels in screening mammograms. The proposed framework is based on supervised learning using a cascade classifier. This cascade classifier consists of several stages where in each stage a GentleBoost classifier is trained on Haar-like features. A total of 30 cases were included in this study. In each image, vessel pixels were annotated by selecting pixels on the centerline of the vessel, control samples were taken by annotating a region without any visible vascular structures. This resulted in a total of 31,000 pixels marked as vascular and over 4 million control pixels. After training, the classifier assigns a vesselness likelihood to the pixels. The proposed framework was compared to three other vessel enhancing methods, i) a vesselness filter, ii) a gaussian derivative filter, and iii) a tubeness filter. The methods were compared in terms of area under the receiver operating characteristics curves, the Az values. The Az value of the cascade approach is 0:85. This is superior to the vesselness, Gaussian, and tubeness methods, with Az values of 0:77, 0:81, and 0:78, respectively. From these results, it can be concluded that our proposed framework is a promising method for the detection of vessels in screening mammograms.

A <b>pdf file</b> of this publication is available for personal use.Enter your e-mail address in the box below and press the button. You will receive an e-mail message with a link to the pdf file.
<form action="sender.php">  <input type="text" name="email">  <input type="submit" value="Send Mord15.pdf:pdfMord15.pdf:PDF by e-mail"></form>
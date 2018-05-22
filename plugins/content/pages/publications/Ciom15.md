title: Automatic detection of spiculation of pulmonary nodules in Computed Tomography images

## Francesco Ciompi and Colin Jacobs and Ernst Th Scholten and Sarah van Riel and Mathilde M. W. Wille and Mathias Prokop and Bram van Ginneken
MI

<a href="https://doi.org/10.1117/12.2081426">DOI</a>

## Abstract
We present a fully automatic method for the assessment of spiculation of pulmonary nodules in low-dose Com- puted Tomography (CT) images. Spiculation is considered as one of the indicators of nodule malignancy and an important feature to assess in order to decide on a patient-tailored follow-up procedure. For this reason, lung cancer screening scenario would benet from the presence of a fully automatic system for the assessment of spiculation. The presented framework relies on the fact that spiculated nodules mainly dier from non-spiculated ones in their morphology. In order to discriminate the two categories, information on morphology is captured by sampling intensity proles along circular patterns on spherical surfaces centred on the nodule, in a multi-scale fashion. Each intensity prole is interpreted as a periodic signal, where the Fourier transform is applied, obtain- ing a spectrum. A library of spectra is created by clustering data via unsupervised learning. The centroids of the clusters are used to label back each spectrum in the sampling pattern. A compact descriptor encoding the nodule morphology is obtained as the histogram of labels along all the spherical surfaces and used to classify spiculated nodules via supervised learning. We tested our approach on a set of nodules from the Danish Lung Cancer Screening Trial (DLCST) dataset. Our results show that the proposed method outperforms other 3-D descriptors of morphology in the automatic assessment of spiculation.

A <b>pdf file</b> of this publication is available for personal use.Enter your e-mail address in the box below and press the button. You will receive an e-mail message with a link to the pdf file.
<form action="sender.php">  <input type="text" name="email">  <input type="submit" value="Send Ciom15.pdf:pdfCiom15.pdf:PDF by e-mail"></form>
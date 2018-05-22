title: Supervised segmentation by Iterated Contextual Pixel Classification

## M. Loog and B. van Ginneken
ICPR

<a href="https://doi.org/10.1109/ICPR.2002.1048456">DOI</a>

## Abstract
We propose a general iterative contextual pixel classifier for supervised image segmentation. The iterative procedure is statistically well-founded and can be considered a variation on the iterated conditional modes (ICM) of Besag (1983). Having an initial segmentation, the algorithm iteratively updates it by reclassifying every pixel, based on the original features and, additionally, contextual information. This contextual information consists of the class labels of pixels in the neighborhood of the pixel to be reclassified. Three essential differences with the original ICM are: (1) our update step is merely based on a classification result, hence a voiding the explicit calculation of conditional probabilities; (2) the clique formalism of the Markov random field framework is not required; (3) no assumption is made w.r.t. the conditional independence of the observed pixel values given the segmented image. The important consequence of properties 1 and 2 is that one can easily incorporate rate common pattern recognition tools in our segmentation algorithm. Examples are different classifiers-e.g. Fisher linear discriminant, nearest-neighbor classifier, or support vector machines-and dimension reduction techniques like LDA, or PCA. We experimentally compare a specific instance of our general method to pixel classification, using simulated data and chest radiographs, and show that the former outperforms the latter.

A <b>pdf file</b> of this publication is available for personal use.Enter your e-mail address in the box below and press the button. You will receive an e-mail message with a link to the pdf file.
<form action="sender.php">  <input type="text" name="email">  <input type="submit" value="Send Loog02a.pdf:pdfLoog02a.pdf:PDF by e-mail"></form>
title: Organ detection in thorax abdomen CT using multi-label convolutional neural networks

## Humpire Mamani, Gabriel Efrain and Arnaud Arinda Adiyoso Setio and Bram van Ginneken and Colin Jacobs
MI

<a href="https://doi.org/10.1117/12.2254349">DOI</a>

## Abstract
A convolutional network architecture is presented to determine bounding boxes around six organs in thorax-abdomen CT scans. A single network for each orthogonal view determines the presence of lungs, kidneys, spleen and liver. We show that an architecture that takes additional slices before and after the slice of interest as an additional input outperforms an architecture that processes single slices. From the slice-based analysis, a bounding box around the structures of interest can be computed. The system uses 6 convolutional, 4 pooling and one fully connected layer and uses 333 scans for training and 110 for validation. The test set contains 110 scans. The average Dice score of the proposed method was 0.95 and 0.95 for the lungs, 0.59 and 0.58 for the kidneys, 0.83 for the liver and 0.63 for the spleen. This paper shows that automatic localization of organs using multi-label convolution neural networks is possible. This architecture can likely be used to identify other organs of interest as well.

A <b>pdf file</b> of this publication is available for personal use.Enter your e-mail address in the box below and press the button. You will receive an e-mail message with a link to the pdf file.
<form action="sender.php">  <input type="text" name="email">  <input type="submit" value="Send Hump17.pdf:pdfHump17.pdf:PDF by e-mail"></form>
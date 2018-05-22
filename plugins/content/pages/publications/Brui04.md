title: Interactive segmentation of abdominal aortic aneurysms in CTA images

## M. de Bruijne AND B. van Ginneken AND M. A. Viergever AND W. J. Niessen
MIA

<a href="https://doi.org/10.1016/j.media.2004.01.001">DOI</a>

## Abstract
A model-based approach to interactive segmentation of abdominal aortic aneurysms from CTA data is presented. After manual delineation of the aneurysm sac in the first slice, the method automatically detects the contour in subsequent slices, using the result from the previous slice as a reference. If an obtained contour is not sufficiently accurate, the user can intervene and provide an additional manual reference contour. The method is inspired by the active shape model (ASM) segmentation scheme (), in which a statistical shape model, derived from corresponding landmark points in manually labeled training images, is fitted to the image in an iterative manner. In our method, a shape model of the contours in two adjacent image slices is progressively fitted to the entire volume. The contour obtained in one slice thus constrains the possible shapes in the next slice. The optimal fit is determined on the basis of multi-resolution gray level models constructed from gray value patches sampled around each landmark. We propose to use the similarity of adjacent image slices for this gray level model, and compare these to single-slice features that are more generally used with ASM. The performance of various image features is evaluated in leave-one-out experiments on 23 data sets. Features that use the similarity of adjacent image slices outperform measures based on single-slice features in all cases. The average number of slices in our datasets is 51, while on average eight manual initializations are required, which decreases operator segmentation time by a factor of 6.

A <b>pdf file</b> of this publication is available for personal use.Enter your e-mail address in the box below and press the button. You will receive an e-mail message with a link to the pdf file.
<form action="sender.php">  <input type="text" name="email">  <input type="submit" value="Send Brui04.pdf:pdfBrui04.pdf:PDF by e-mail"></form>
title: Fast 2-D ultrasound strain imaging: the benefits of using a GPU

## Idzenga, Tim and Gaburov, Evghenii and Vermin, Willem and Menssen, Jan and De Korte, Chris
TUFF

<a href="https://doi.org/10.1109/TUFFC.2014.6689790">DOI</a>

## Abstract
Deformation of tissue can be accurately estimated from radio-frequency ultrasound data using a 2-dimensional normalized cross correlation (NCC)-based algorithm. This procedure, however, is very computationally time-consuming. A major time reduction can be achieved by parallelizing the numerous computations of NCC. In this paper, two approaches for parallelization have been investigated: the OpenMP interface on a multi-CPU system and Compute Unified Device Architecture (CUDA) on a graphics processing unit (GPU). The performance of the OpenMP and GPU approaches were compared with a conventional Matlab implementation of NCC. The OpenMP approach with 8 threads achieved a maximum speed-up factor of 132 on the computing of NCC, whereas the GPU approach on an Nvidia Tesla K20 achieved a maximum speed-up factor of 376. Neither parallelization approach resulted in a significant loss in image quality of the elastograms. Parallelization of the NCC computations using the GPU, therefore, significantly reduces the computation time and increases the frame rate for motion estimation.

A <b>pdf file</b> of this publication is available for personal use.Enter your e-mail address in the box below and press the button. You will receive an e-mail message with a link to the pdf file.
<form action="sender.php">  <input type="text" name="email">  <input type="submit" value="Send Idze14.pdf:pdfIdze14.pdf:PDF by e-mail"></form>
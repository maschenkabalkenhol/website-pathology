title: Automated detection of nodules attached to the pleural and mediastinal surface in low-dose CT scans

## B. van Ginneken and A. Tan and K. Murphy and B. J. de Hoop and M. Prokop
MI

<a href="https://doi.org/10.1117/12.772298">DOI</a>

## Abstract
This paper presents a new computer-aided detection scheme for lung nodules attached to the pleural or mediastinal surface in low dose CT scans. First the lungs are automatically segmented and smoothed. Any connected set of voxels attached to the wall - with each voxel above minus 500 HU and the total object within a specified volume range - was considered a candidate finding. For each candidate, a refined segmentation was computed using morphological operators to remove attached structures. For each candidate, 35 features were defined, based on their position in the lung and relative to other structures, and the shape and density within and around each candidate. In a training procedure an optimal set of 15 features was determined with a k-nearest-neighbor classifier and sequential floating forward feature selection. The algorithm was trained with a data set of 708 scans from a lung cancer screening study containing 224 pleural nodules and tested on an independent test set of 226 scans from the same program with 58 pleural nodules. The algorithm achieved a sensitivity of 52% with an average of 0.76 false positives per scan. At 2.5 false positive marks per scan, the sensitivity increased to 80%.

A <b>pdf file</b> of this publication is available for personal use.Enter your e-mail address in the box below and press the button. You will receive an e-mail message with a link to the pdf file.
<form action="sender.php">  <input type="text" name="email">  <input type="submit" value="Send Ginn08b.pdf:pdfGinn08b.pdf:PDF by e-mail"></form>
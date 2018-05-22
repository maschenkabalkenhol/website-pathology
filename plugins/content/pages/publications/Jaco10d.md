title: Performance evaluation for volumetric segmentation of multiple sclerosis lesions using MATLAB and computing engine in the graphical processing unit (GPU)

## Anh H. Le and Young W. Park and Kevin Ma and Colin Jacobs and Brent J. Liu
MI

<a href="https://doi.org/10.1117/12.844811">DOI</a>

## Abstract
Multiple Sclerosis (MS) is a progressive neurological disease affecting myelin pathways in the brain. Multiple lesions in the white matter can cause paralysis and severe motor disabilities of the affected patient. To solve the issue of inconsistency and user-dependency in manual lesion measurement of MRI, we have proposed a 3-D automated lesion quantification algorithm to enable objective and efficient lesion volume tracking. The computer-aided detection (CAD) of MS, written in MATLAB, utilizes K-Nearest Neighbors (KNN) method to compute the probability of lesions on a per-voxel basis. Despite the highly optimized algorithm of imaging processing that is used in CAD development, MS CAD integration and evaluation in clinical workflow is technically challenging due to the requirement of high computation rates and memory bandwidth in the recursive nature of the algorithm. In this paper, we present the development and evaluation of using a computing engine in the graphical processing unit (GPU) with MATLAB for segmentation of MS lesions. The paper investigates the utilization of a high-end GPU for parallel computing of KNN in the MATLAB environment to improve algorithm performance. The integration is accomplished using NVIDIA's CUDA developmental toolkit for MATLAB. The results of this study will validate the practicality and effectiveness of the prototype MS CAD in a clinical setting. The GPU method may allow MS CAD to rapidly integrate in an electronic patient record or any disease-centric health care system.

A <b>pdf file</b> of this publication is available for personal use.Enter your e-mail address in the box below and press the button. You will receive an e-mail message with a link to the pdf file.
<form action="sender.php">  <input type="text" name="email">  <input type="submit" value="Send Jaco10d.pdf:pdf/Jaco10d.pdf:PDF by e-mail"></form>
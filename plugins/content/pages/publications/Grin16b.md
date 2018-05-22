title: Fast Convolutional Neural Network Training Using Selective Data Sampling: Application to Hemorrhage Detection in Color Fundus Images

## M. J. J. P. van Grinsven and B. van Ginneken and C. B. Hoyng and T. Theelen and C. I. S'anchez.
TMI

<a href="https://doi.org/10.1109/TMI.2016.2526689">DOI</a>

## Abstract
Convolutional neural networks (CNNs) are deep learning network architectures that have pushed forward the state-of-the-art in a range of computer vision applications and are increasingly popular in medical image analysis. However, training of CNNs is time-consuming and challenging. In medical image analysis tasks, the majority of training examples are easy to classify and therefore contribute little to the CNN learning process. In this paper, we propose a method to improve and speed-up the CNN training for medical image analysis tasks by dynamically selecting misclassified negative samples during training. Training samples are heuristically sampled based on classification by the current status of the CNN. Weights are assigned to the training samples and informative samples are more likely to be included in the next CNN training iteration. We evaluated and compared our proposed method by training a CNN with (SeS) and without (NSeS) the selective sampling method. We focus on the detection of hemorrhages in color fundus images. A decreased training time from 170 epochs to 60 epochs with an increased performance â€“ on par with two human experts â€“ was achieved with areas under the receiver operating characteristics curve of 0.894 and 0.972 on two data sets. The SeS CNN statistically outperformed the NSeS CNN on an independent test set.

A <b>pdf file</b> of this publication is available for personal use.Enter your e-mail address in the box below and press the button. You will receive an e-mail message with a link to the pdf file.
<form action="sender.php">  <input type="text" name="email">  <input type="submit" value="Send Grin16b.pdf:pdfGrin16b.pdf:PDF by e-mail"></form>
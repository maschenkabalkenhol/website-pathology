title: Automatic detection and classification of leukocytes using convolutional neural networks

## Zhao, Jianwei and Zhang, Minshu and Zhou, Zhenghua and Chu, Jianjun and Cao, Feilong
Medical & Biological Engineering & Computing

<a href="https://doi.org/10.1007/s11517-016-1590-x">DOI</a>

## Abstract
The detection and classification of white blood cells (WBCs, also known as Leukocytes) is a hot issue because of its important applications in disease diagnosis. Nowadays the morphological analysis of blood cells is operated manually by skilled operators, which results in some drawbacks such as slowness of the analysis, a non-standard accuracy, and the dependence on the operator's skills. Although there have been many papers studying the detection of WBCs or classification of WBCs independently, few papers consider them together. This paper proposes an automatic detection and classification system for WBCs from peripheral blood images. It firstly proposes an algorithm to detect WBCs from the microscope images based on the simple relation of colors R, B and morphological operation. Then a granularity feature (pairwise rotation invariant co-occurrence local binary pattern, PRICoLBP feature) and SVM are applied to classify eosinophil and basophil from other WBCs firstly. Lastly, convolution neural networks are used to extract features in high level from WBCs automatically, and a random forest is applied to these features to recognize the other three kinds of WBCs: neutrophil, monocyte and lymphocyte. Some detection experiments on Cellavison database and ALL-IDB database show that our proposed detection method has better effect almost than iterative threshold method with less cost time, and some classification experiments show that our proposed classification method has better accuracy almost than some other methods.


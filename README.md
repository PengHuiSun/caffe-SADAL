# Similarity-Aware Deep Adversarial Learning for Facial Age Estimation

## Main Results
### MORPH
**Table 1.** Comparisons of MAEs with different state-of-the-art approaches on the ***MORPH*** dataset. The MAE (in years) is reported for each method.  

| Method | MAE  | Year |
|:------------: |:---------------:|:-----:|
| BIF+KNN      | 9.64 | - |
| OHRanker      |  6.49        |   2011 |
| LDL | 5.69       |   2013 |
| CPNN      | 5.67 | 2013 |
| CA-SVR      |  4.87       |   2013 |
| CS-LBFL | 4.52        |   2015 |
| CS-LBMFL    | 4.37 | 2015 |
| CSOHR      | 3.74 | 2015 |
| DeepRank      |  3.57        |   2015 |
| DeepRank+ | 3.49       |   2015 |
| OR-CNN     | 3.27 | 2016 |
| ODFL      |  3.12       |   2017 |
| LSDML | 3.08      |   2018 |
| M-LSDML    | 2.89 | 2018 |
| **SADAL**     |  **2.75**         |  - |

**Table 2.** Comparisons of MAEs with different deep learning approaches on the ***MORPH*** dataset.

| Method | MAE  |
|:------------: |:---------------:|
| unsupervised VGG + KNN      | 7.21 |
| unsupervised VGG + OHRanker     | 4.58 |
| VGG + Single Label     | 3.63 |
| VGG + Gaussian Label     | 3.44 |
| ODFL     | 3.12 |
| **SADAL**      | **2.75** |

### FGNET
**Table 3.** Comparisons of MAEs compared with state-of-the-art approaches on the ***FG-NET*** dataset. The MAE (in years) is reported for each method.

| Method | MAE  | Year |
|:------------: |:---------------:|:-----:|
| BIF+KNN      | 8.24 | - |
| OHRanker      |  4.48        |   2011 |
| LDL | 5.77       |   2013 |
| CPNN      | 4.76 | 2013 |
| CSOHR      | 4.70 | 2015 |
| CS-LBFL | 4.43        |   2015 |
| CS-LBMFL    | 4.36 | 2015 |
| ODFL      |  3.89       |   2017 |
| LSDML | 3.92      |   2018 |
| M-LSDML    | 3.74 | 2018 |
| **SADAL**     |  **3.67**         |  - |

## Citing SADAL
If you find SADAL useful in your research, please consider citing:

　　@INPROCEEDINGS{SADAL,  
　　　　author={Penghui Sun, **Hao Liu***, Xing Wang, Zhenhua Yu, Suping Wu},  
　　　　booktitle={2019 IEEE International Conference on Multimedia and Expo (ICME)},  
　　　　title={Similarity-Aware Deep Adversarial Learning for Facial Age Estimation},  
　　　　year={2019},  
　　　　pages={260-265},  
　　　　doi={10.1109/ICME.2019.00053},  
　　　　ISSN={1945-7871},  
　　　　month={July}  
　　} 

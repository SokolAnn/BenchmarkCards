# InDL: A New Dataset and Benchmark for In-Diagram Logic Interpretation based on Visual Illusion

## 📊 Benchmark Details

**Name**: InDL: A New Dataset and Benchmark for In-Diagram Logic Interpretation based on Visual Illusion

**Overview**: This paper introduces a novel approach to evaluating deep learning models’ capacity for in-diagram logic interpretation. Leveraging the realm of visual illusions, the authors establish a dataset, InDL, designed to rigorously test and benchmark models on their handling of visual illusions and in-diagram logical reasoning, providing a quantifiable measure to rank models.

**Data Type**: image (visual illusion / in-diagram stimuli)

**Domains**:
- Computer Vision
- Cognitive Psychology

**Similar Benchmarks**:
- CLEVR
- NLVR
- ImageNet

**Resources**:
- [GitHub Repository](https://github.com/rabbit-magic-wh/InDL)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate deep learning models' capacity for in-diagram logic interpretation using visual illusions and to provide a quantifiable benchmarking framework (InDL) to rank and analyze models' logical comprehension in visual stimuli.

**Target Audience**:
- ML Researchers
- Model Developers
- Cognitive Scientists

**Tasks**:
- Visual Reasoning
- Image Classification (in-diagram logic detection)

**Limitations**: N/A

## 💾 Data

**Source**: The InDL dataset is composed of images derived from classic geometric optical/visual illusions (Hering, Wundt, Muller-Lyer, Poggendorff, Vertical-horizontal, Zollner), organized into five dataset groups as summarized in Table 1 (Hering & Wundt combined as one dataset plus Muller-Lyer, Poggendorff, Vertical-horizontal, Zollner).

**Size**: 10,000 samples (30% positive samples, 70% negative samples)

**Format**: N/A

**Annotation**: Ground truth labels indicating presence or absence of specific in-diagram logic (true positive/false negative definitions provided).

## 🔬 Methodology

**Methods**:
- Automated metrics (Recall)
- Model-based evaluation (training and testing multiple pre-trained deep learning models; fine-tuning with AdamW optimizer)
- Comparison against ImageNet performance (reported top-1 and top-5 accuracies for reference)

**Metrics**:
- Recall
- Top-1 Accuracy
- Top-5 Accuracy

**Calculation**: Recall = TruePositive / (TruePositive + FalseNegative). A true positive is an instance where both the model and the ground truth agree that the sample contains a specific in-diagram logic; a false negative is where the model fails to recognize the in-diagram logic but the ground truth indicates it is present.

**Interpretation**: High recall indicates a model is effective at detecting the presence of in-diagram logic; low recall suggests the model fails to recognize in-diagram logic (i.e., misses positives).

**Baseline Results**: Baseline Xception results on InDL: dataset01 99.49%, dataset02 88.14%, dataset03 83.88%, dataset04 93.85%, dataset05 83.21%, mean 89.81%. ImageNet: top-1 79.05%, top-5 94.39%.

**Validation**: Models were trained until no improvement in validation loss over a certain number of epochs and then evaluated on a separate test set.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Misuse
- Fairness
- Ethics

**Atlas Risks**:
- **Robustness**: Evasion attack
- **Misuse**: Improper usage
- **Fairness**: Data bias

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable

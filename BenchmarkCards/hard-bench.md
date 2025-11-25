# Hard-Bench

## 📊 Benchmark Details

**Name**: Hard-Bench

**Overview**: Hard-Bench: a challenging low-resource benchmark that selects "hard examples" (by loss or gradient-norm scores using a short/early-stopped biased predictor) from existing datasets to better evaluate learning and generalization in low-resource settings. The benchmark covers 11 datasets (3 computer vision datasets and 8 natural language processing datasets) and provides two variants: Hard-Bench (Loss) and Hard-Bench (GradNorm). Code is available at https://github.com/Qian2333/Hard-Bench.

**Data Type**: image classification samples; text classification and sentence-pair classification examples

**Domains**:
- Computer Vision
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- BigBench
- superGLUE
- GLUE
- miniImageNet
- CIFAR-FS
- Wilds

**Resources**:
- [GitHub Repository](https://github.com/Qian2333/Hard-Bench)
- [Resource](https://arxiv.org/abs/2303.03840)

## 🎯 Purpose and Intended Users

**Goal**: To build a challenging low-resource benchmark that includes hard and biased examples to better evaluate the learning ability and robustness of neural networks in low-resource settings.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Image Classification
- Text Classification
- Natural Language Inference
- Paraphrase Identification

**Limitations**: Default setting selects fixed examples per label for reported results (authors note space limitations and additional experiments in appendices).

## 💾 Data

**Source**: Subsets selected from CIFAR-10, CIFAR-100, ImageNet-1K (CV) and 8 GLUE datasets (SST-2, CoLA, MNLI, QNLI, MRPC, QQP, RTE, WNLI) (NLP). Hard examples are selected by scoring samples with a biased predictor trained for one epoch and ranking by Loss or GradNorm.

**Size**: CIFAR-10: 500 examples per label (10% of training set); CIFAR-100: 50 examples per label; ImageNet-1K: 100 examples per label; GLUE datasets: 500 examples per label (100 examples for WNLI).

**Format**: N/A

**Annotation**: Selected hard examples undergo a human-check process to avoid mislabeled examples (authors state: "To avoid involving mislabelled examples, we add the human-check process in this work").

## 🔬 Methodology

**Methods**:
- Automated metrics (test/validation Accuracy)
- Model-based evaluation across 11 models (including 7 pre-trained models)
- Repeated trials and averaging (experiments run three times and averaged)

**Metrics**:
- Accuracy

**Calculation**: Accuracy is computed on the test/validation set (for GLUE tasks the validation set is used as the test set). Reported results are averages over three runs. Hard-Bench variants are constructed by selecting top-k samples per label ranked by Loss score or Gradient Norm score computed using a biased predictor trained for one epoch.

**Interpretation**: Large drops in Accuracy on Hard-Bench relative to randomly-sampled low-resource benchmarks indicate that Hard-Bench better exposes weaknesses and a robustness/generalization gap of models. The authors report that Hard-Bench (Loss) is generally more challenging than Hard-Bench (GradNorm).

**Baseline Results**: Representative results reported by authors: On SST-2 Random-Bench RoBERTa: 91.54% test accuracy; On SST-2 Hard-Bench (GradNorm) RoBERTa: 51.01%; On SST-2 Hard-Bench (Loss) RoBERTa: 50.55%. On CIFAR-10 Random-Bench DenseNet-121: 71.33% -> Hard-Bench (GradNorm): 59.87% -> Hard-Bench (Loss): 44.81%.

**Validation**: Validation procedures include using the GLUE validation set as the test set (to avoid hidden test set issues), averaging results over three runs, human-check of selected examples to avoid mislabeled data, and ablation studies including 100 random samplings to compare worst-case Random-Bench performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: ['Over-estimated model performance on traditional low-resource benchmarks', 'Generalization failures revealed by hard and biased low-resource examples']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable

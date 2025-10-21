# NoisywikiHow: A Benchmark for Learning with Real-world Noisy Labels in Natural Language Processing

## 📊 Benchmark Details

**Name**: NoisywikiHow: A Benchmark for Learning with Real-world Noisy Labels in Natural Language Processing

**Overview**: We present NoisywikiHow, a new NLP benchmark for evaluating learning with noisy labels (LNL) methods focusing on the intention identification task. NoisywikiHow is built from wikiHow procedural-event data and explicitly injects multiple, instance-dependent noise sources to simulate heterogeneous human annotation errors, and it provides controlled noise levels (0%, 10%, 20%, 40%, 60%) to support systematic evaluation.

**Data Type**: text (procedural event -> intention classification pairs)

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- NoisyNER
- Red MiniImageNet
- Red Stanford Cars
- Food-101N
- Animal-10N
- Clothing1M
- WebVision
- AudioSet
- FSDnoisy18K
- FSDKaggle2019

**Resources**:
- [GitHub Repository](https://github.com/tangminji/NoisywikiHow)
- [Resource](https://arxiv.org/abs/2305.10709)
- [Resource](https://www.wikihow.com/robots.txt)

## 🎯 Purpose and Intended Users

**Goal**: Provide a large-scale NLP benchmark with heterogeneous, instance-dependent, and controlled real-world label noise to systematically evaluate learning with noisy labels (LNL) methods on the intention identification task.

**Target Audience**:
- ML Researchers
- Model Developers
- Academic Research Community

**Tasks**:
- Text Classification
- Intention Identification

**Limitations**: We simplify intention identification into a sentence classification task using a single procedural event rather than an entire event process; a more realistic formulation would use the entire event process.

## 💾 Data

**Source**: Crawled from the wikiHow website (procedural event headers as inputs and wikiHow article finest-granularity categories as labels).

**Size**: 89,143 instances in 158 classes (Train: 73,343; Validation: 7,900; Test: 7,900).

**Format**: N/A

**Annotation**: Each category was annotated by three graduate students in the NLP field and regarded as an event if more than two annotators agreed (Fleiss kappa = 0.84). The dataset was produced with minimal human supervision via a series of automated labeling procedures and controlled programmatic noise injection.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation (fine-tuning pre-trained language models)
- Controlled noise injection experiments

**Metrics**:
- Top-1 Accuracy
- Top-5 Accuracy

**Calculation**: Models are trained on noisy training sets and evaluated on the clean validation/test sets. Report Top-1 and Top-5 accuracy on the clean test set under controlled noise levels (0%, 10%, 20%, 40%, 60%).

**Interpretation**: Higher Top-1/Top-5 accuracy indicates better generalization to clean data; increases in noise level generally lead to decreased Top-1/Top-5 accuracy, reflecting reduced robustness to noisy labels.

**Baseline Results**: Examples: BART (base) achieves Top-1 61.72% (Top-5 86.90%) at 0% noise and Top-1 49.75% (Top-5 78.84%) at 60% noise (Table 4). SEAL achieves Top-1 63.29% (Top-5 87.65%) at 0% noise and Top-1 52.73% (Top-5 81.56%) at 60% noise (Table 8). Full baseline tables are provided in the paper.

**Validation**: Randomly split 15,800 instances from clean data equally into validation and test sets; remaining 73,343 instances used as training set. Evaluate methods trained on noisy training sets on the clean validation/test sets. Controlled noise levels are 0%, 10%, 20%, 40%, and 60%.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Data contamination, Unrepresentative data, Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: Model overfitting to noisy labels and degraded generalization performance caused by label noise.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The paper states there is no privacy issue: data is constructed from the wikiHow website which is free and open for academic usage, and the authors declare compliance with the ACL Ethics Policy.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Authors state the dataset was obtained and presented following the ACL Ethics Policy and that wikiHow content used is free and open for academic usage.

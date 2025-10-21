# GSCLIP : A Framework for Explaining Distribution Shifts in Natural Language

## 📊 Benchmark Details

**Name**: GSCLIP : A Framework for Explaining Distribution Shifts in Natural Language

**Overview**: We propose a novel task, dataset explanation. Given two image data sets, dataset explanation aims to automatically point out their dataset-level distribution shifts with natural language. We introduce GSCLIP, a training-free framework that uses a hybrid generator group (rule-based + LM-based) to produce candidate natural-language explanations and an explanation selector (based on CLIP embeddings and a projection + two-sample t-test) to quantitatively evaluate and rank candidate explanations.

**Data Type**: multimodal (image inputs with natural language explanations)

**Domains**:
- Computer Vision
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MetaShift
- MetaShift-Attributes
- ImageNet
- ImageNet-C
- DomainNet
- GQA

**Resources**:
- [GitHub Repository](https://github.com/Weixin-Liang/MetaShift)
- [GitHub Repository](https://github.com/moein-shariatnia/OpenAI-CLIP)
- [GitHub Repository](https://github.com/IlyaSemenov/wikipedia-word-frequency)
- [Resource](https://arxiv.org/abs/2206.15007)

## 🎯 Purpose and Intended Users

**Goal**: Automatically explain dataset-level distribution shifts between two image datasets in natural language to help users comprehend shifts and assist data-centric AI tasks (e.g., model error discovery, subgroup bias detection).

**Target Audience**:
- End users
- AI deployment practitioners
- Data-centric AI practitioners
- Model Developers

**Tasks**:
- Dataset Explanation
- Distribution Shift Explanation

**Limitations**: N/A

## 💾 Data

**Source**: MetaShift and MetaShift-Attributes datasets (Liang & Zou, 2022)

**Size**: MetaShift: 12,868 sets of natural images across 410 classes; experiments sample 100 dataset pairs for systematic evaluation

**Format**: N/A

**Annotation**: MetaShift provides explicit annotations of the differences between sub-datasets (used to evaluate explanations)

## 🔬 Methodology

**Methods**:
- Automated quantitative evaluation using an explanation selector
- Model-based evaluation using CLIP cross-modal embeddings
- Rule-based generator for candidate explanations
- Language model-based generation using GPT-2 for candidate explanations
- Statistical testing (two-sample t-test) to evaluate explanations

**Metrics**:
- Top-x Accuracy (Acc@1, Acc@3, Acc@5, Acc@15)
- Key Word metric (matches ground truth labels and WordNet synonyms)
- p-value from two-sample t-test

**Calculation**: Top-x accuracy: rank candidate explanations returned by the framework and check whether the explanation contains annotation words of any test image set (Key Word metric also considers WordNet synonyms). Explanation selector: compute projections of image embeddings onto the difference vector between a candidate sentence embedding and its negation; obtain projection lists LA and LB for the two image sets; conduct a two-sample t-test on LA and LB and obtain a p-value for each candidate explanation.

**Interpretation**: Candidate explanations are sorted by p-value in ascending order; p-value < 0.05 is considered evidence that the projection distributions differ in a way consistent with the candidate explanation. Higher Acc@x indicates better explanation ranking; lower p-value indicates stronger statistical support for the explanation.

**Baseline Results**: Systematic evaluation (rule-based generator + selector) on MetaShift: Acc@1 30%, Acc@3 50%, Acc@5 63%. MetaShift-Attributes: Acc@1 34%, Acc@3 57%, Acc@5 71%. With GPT-2 (hybrid generator + selector) on MetaShift: Label Acc@1 28%, Acc@5 46%, Acc@15 55%; Key Words Acc@1 39%, Acc@5 54%, Acc@15 64%. Wikipedia baseline results and Meta-Attr results are reported in Table 2 of the paper.

**Validation**: Validated via large-scale experiments on MetaShift and MetaShift-Attributes: randomly sample 100 dataset pairs (with same main object) and evaluate the selector's ability to rank ground-truth explanations using top-x accuracy metrics and p-values from two-sample t-tests.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: ['Dataset bias', 'Model errors', 'Subgroup bias']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable

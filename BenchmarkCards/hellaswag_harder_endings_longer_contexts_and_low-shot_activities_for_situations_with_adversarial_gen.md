# HellaSwag (Harder Endings, Longer contexts, and Low-shot Activities for Situations With Adversarial Generations)

## 📊 Benchmark Details

**Name**: HellaSwag (Harder Endings, Longer contexts, and Low-shot Activities for Situations With Adversarial Generations)

**Overview**: HellaSwag is a new benchmark/dataset for commonsense natural language inference (commonsense NLI). The dataset is constructed via Adversarial Filtering (AF) to produce 70,000 problems that are easy for humans (≈95.6% accuracy) yet challenging for state-of-the-art models (≈50% accuracy). AF iteratively selects adversarial machine-generated wrong answers using discriminators to create a dataset robust to current pretrained models.

**Data Type**: text (context and multiple-choice endings; multiple-choice commonsense natural language inference)

**Domains**:
- Natural Language Processing
- Commonsense Reasoning

**Similar Benchmarks**:
- SWAG

**Resources**:
- [Resource](https://rowanzellers.com/hellaswag)
- [Resource](https://arxiv.org/abs/1905.07830)

## 🎯 Purpose and Intended Users

**Goal**: Provide a challenging evaluation benchmark for commonsense natural language inference that is easy for humans (≈95% accuracy) but difficult for state-of-the-art models (≈50%), using Adversarial Filtering to remove dataset-specific artifacts and produce robust test splits including zero-shot categories.

**Tasks**:
- Natural Language Inference
- Question Answering
- Multiple-choice Commonsense Inference

**Limitations**: N/A

## 💾 Data

**Source**: ActivityNet Captions and WikiHow (scraped). Endings were machine-generated (OpenAI GPT) and filtered via Adversarial Filtering (AF); final examples were human-validated using crowd workers.

**Size**: 70,000 examples (25,000 ActivityNet; 45,000 WikiHow)

**Format**: N/A

**Annotation**: Human validation via Amazon Mechanical Turk: multiple rounds of annotation where workers are given a context and six ending choices (one true ending and five AF-generated endings); aggregated via worker probabilities and majority vote (five workers used for final human evaluation in reported results).

## 🔬 Methodology

**Methods**:
- Automated metrics (model accuracy)
- Human evaluation (crowd workers majority vote)
- Model-based evaluation (baseline models trained and evaluated)
- Adversarial Filtering (iterative discriminator-based data collection)

**Metrics**:
- Accuracy

**Calculation**: Reported as percentage correct in a four-way multiple-choice setting (4-way accuracy). Models are trained with a four-way cross-entropy loss to predict the correct ending. Human accuracy is reported via majority vote over crowd workers.

**Interpretation**: Higher Accuracy (%) indicates better performance. Human performance is ≈95.6% (reference), while state-of-the-art models achieve under 50% overall, indicating substantial gap to human-level performance.

**Baseline Results**: Baseline test accuracies (Overall test): BERT-Large 47.3% (Overall test), BERT-Base 40.5% (Overall test), OpenAI GPT 41.7% (Overall test), ESIM + ELMo 33.3% (Overall test), Human 95.6% (Overall test).

**Validation**: Adversarial Filtering: iterative 80%/20% splits where discriminators (e.g., BERT-Large) are trained to classify real vs generated endings and easy-to-classify generations are replaced until convergence. Multiple rounds of human validation on Mechanical Turk were applied to filter and replace machine generations rated realistic; final dataset includes in-domain and zero-shot evaluation subsets (5,000 examples each for validation/test subsets as described).

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Potential Harm**: ['Unwanted social biases induced when humans write endings (gender and race), as cited in the paper (Rudinger et al., 2015).']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable

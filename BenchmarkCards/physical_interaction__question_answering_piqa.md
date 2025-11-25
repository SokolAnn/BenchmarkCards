# Physical Interaction: Question Answering (PIQA)

## 📊 Benchmark Details

**Name**: Physical Interaction: Question Answering (PIQA)

**Overview**: Introduces the task of physical commonsense reasoning and a benchmark dataset, Physical Interaction: Question Answering (PIQA), to evaluate language representations on their knowledge of physical commonsense via multiple-choice goal-solution pairs.

**Data Type**: multiple-choice question-answering pairs (goal-solution pairs)

**Domains**:
- Natural Language Processing
- Computer Vision
- Robotics

**Languages**:
- English

**Similar Benchmarks**:
- SWAG
- HellaSwag
- Winogrande
- SocialIQA
- SQuAD

**Resources**:
- [Resource](http://yonatanbisk.com/piqa)
- [Resource](https://arxiv.org/abs/1911.11641)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and study physical commonsense understanding in natural language models and provide a benchmark (PIQA) for progress toward language representations that capture physical commonsense.

**Target Audience**:
- Natural Language Processing Researchers
- Computer Vision Researchers
- Robotics Researchers
- Model Developers
- Machine Learning Researchers

**Tasks**:
- Question Answering
- Physical commonsense reasoning

**Limitations**: Authors note that learning about the world from language alone is limiting; matching human performance via heavy fine-tuning on large in-domain data is possible but not the stated goal. Examples requiring expert-level domain knowledge were removed during validation so the dataset focuses on commonsense accessible to the average person.

## 💾 Data

**Source**: Seeded from instructables.com and collected via crowdworker Human Intelligence Tasks (HITs) where annotators wrote a Goal, a valid Solution, and a 'trick' (invalid) solution; validated by additional annotators and cleaned using the AFLite algorithm.

**Size**: Over 16,000 training QA pairs; approximately 2,000 development examples; approximately 3,000 test examples. Training data contains over 3.7 million lexical tokens.

**Format**: N/A

**Annotation**: Human-annotated by crowdworkers who provided goal, valid solution, and an incorrect 'trick' solution; qualification HITs were used (>80% required); examples were validated by other annotators and low-agreement examples were removed; AFLite was applied to remove annotation artifacts.

## 🔬 Methodology

**Methods**:
- Model-based evaluation (fine-tuning pretrained transformer models: GPT, BERT, RoBERTa)
- Automated metrics (Accuracy)
- Human evaluation (majority vote on development set)

**Metrics**:
- Accuracy

**Calculation**: Accuracy is computed as the percentage of correct choices on validation and test splits. Models are fine-tuned with a cross-entropy loss over the two options; GPT included an additional language modeling loss. Human performance was computed by majority vote among annotators on the development set. Best model hyperparameters were selected via grid search on the validation set.

**Interpretation**: Higher Accuracy approaching human performance (human 94.9% on development) indicates strong physical commonsense; automatic models substantially below human accuracy (best model RoBERTa ~77.1% test) indicate gaps in learning physical commonsense from text alone.

**Baseline Results**: Random Chance: 50.0% (validation/test). Majority Class: 50.5% (validation) / 50.4% (test). OpenAI GPT (124M): 70.9% (validation) / 69.2% (test). Google BERT (340M): 67.1% (validation) / 66.8% (test). FAIR RoBERTa (355M): 79.2% (validation) / 77.1% (test). Human: 94.9% (development).

**Validation**: Examples were validated by additional annotators; low-agreement examples were removed. Train, development, and test folds were produced by AFLite. A qualification HIT (workers had to identify well-formed pairs at >80% to participate). Model hyperparameters were tuned by grid search on the validation set.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Data contamination

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable

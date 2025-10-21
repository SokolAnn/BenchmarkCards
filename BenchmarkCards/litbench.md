# LitBench

## 📊 Benchmark Details

**Name**: LitBench

**Overview**: LitBench is the first standardized benchmark and paired dataset for creative writing verification, aimed at evaluating existing zero-shot judges and enabling the development of learned verifiers that better align with human preferences.

**Data Type**: paired comparisons of human-written stories

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/euclaise/WritingPrompts_preferences)
- [GitHub Repository](https://github.com/SAA-Lab/LitBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a reliable resource for automated evaluation and optimization of creative writing systems through robust benchmarks.

**Target Audience**:
- ML Researchers
- Creative Writers
- Model Developers

**Tasks**:
- Creative Writing Verification

**Limitations**: A key limitation includes the reliance on upvotes from Reddit as indicators of human preferences, which may not account for all underlying factors.

## 💾 Data

**Source**: Data collected from Reddit's r/WritingPrompts subreddit.

**Size**: 43,827 pairwise comparisons (training dataset) and 2,480 pairwise comparisons (test dataset)

**Format**: N/A

**Annotation**: Human preference labels collected through Reddit interactions.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy calculated as the percentage of cases where the preferred story according to the judge's score is also the one chosen by human preferences.

**Interpretation**: Higher agreement with human preferences indicates better performance of the verification model.

**Baseline Results**: The best Bradley-Terry reward model achieves 78% human agreement, outperforming the strongest zero-shot judge (Claude-3.7-Sonnet) at 73%.

**Validation**: Validating the dataset's curation by benchmarking trained reward models against LitBench.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: The dataset reflects the preferences of a largely male, educated, and middle-aged demographic, as reported for Reddit.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: MIT license for the dataset from Hugging Face.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable

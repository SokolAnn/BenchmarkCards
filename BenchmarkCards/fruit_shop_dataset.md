# Fruit Shop Dataset

## 📊 Benchmark Details

**Name**: Fruit Shop Dataset

**Overview**: To adapt to the use case of ChatDB and enable quantitative comparisons with other models, we constructed a synthetic dataset simulating the management of a fruit shop. The dataset simulates four common operations in a shop: purchasing, selling, changing prices, and goods returns, and is used to evaluate multi-hop reasoning and precise calculation capabilities.

**Data Type**: question-answering pairs (text records and question-answer pairs)

**Domains**:
- Natural Language Processing

**Resources**:
- [Resource](https://chatdatabase.github.io/)
- [Resource](https://arxiv.org/abs/2306.03901)

## 🎯 Purpose and Intended Users

**Goal**: Enable quantitative comparisons to evaluate the effectiveness of augmenting LLMs with databases as symbolic memory (ChatDB) on tasks requiring precise recording, multi-hop reasoning, and calculations in a management setting.

**Tasks**:
- Question Answering
- Multi-hop Reasoning
- Numerical Reasoning

**Limitations**: We deliberately design the token length of the dataset to be within the maximum token length of ChatGPT to avoid using memory and maximize the model’s performance.

## 💾 Data

**Source**: Synthetic dataset constructed by the authors simulating fruit shop management records (referred to as the "Fruit Shop Dataset").

**Size**: 70 records; approximately 3.3k tokens; 50 questions (15 easy, 35 hard).

**Format**: N/A

**Annotation**: 50 questions with annotated standard answers (annotation method not specified).

## 🔬 Methodology

**Methods**:
- Automated evaluation against annotated answers

**Metrics**:
- Accuracy

**Calculation**: Accuracy computed as number of correctly answered questions divided by total number of questions (50), reported as counts and percentage.

**Interpretation**: Higher accuracy indicates better performance; reported to show ChatDB substantially outperforms the ChatGPT baseline, especially on hard (multi-hop) questions.

**Baseline Results**: ChatGPT: Easy 10/15, Hard 1/35, All 11/50 (22%). ChatDB (ours): Easy 13/15, Hard 28/35, All 41/50 (82%).

**Validation**: N/A

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable

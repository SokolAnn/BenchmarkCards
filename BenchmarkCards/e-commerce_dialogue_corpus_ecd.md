# E-commerce Dialogue Corpus (ECD)

## 📊 Benchmark Details

**Name**: E-commerce Dialogue Corpus (ECD)

**Overview**: A public e-commerce dialogue corpus extracted from real human conversations collected from Taobao, released to facilitate research on multi-turn conversation and retrieval-based response matching. The corpus contains over 5 types of conversations (commodity consultation, logistics express, recommendation, negotiation, chitchat) across over 20 commodities and is evaluated as a benchmark in the paper.

**Data Type**: text (multi-turn conversational context-response pairs)

**Domains**:
- Natural Language Processing
- E-commerce

**Languages**:
- Chinese

**Similar Benchmarks**:
- Ubuntu Dialogue Corpus
- Douban Conversation Corpus

**Resources**:
- [GitHub Repository](https://github.com/cooelf/DeepUtteranceAggregation)
- [Resource](https://arxiv.org/abs/1806.09102)
- [Resource](https://www.taobao.com)
- [Resource](http://lucene.apache.org/)

## 🎯 Purpose and Intended Users

**Goal**: Provide the first public e-commerce dialogue corpus extracted from real human conversations to facilitate research and development on multi-turn conversation and retrieval-based response matching for dialogue systems.

**Target Audience**:
- Research communities
- Dialogue system developers

**Tasks**:
- Response Selection (Multi-turn Retrieval-based Response Matching)
- Multi-turn Conversation Modeling

**Limitations**: Evaluation assumes a single correct response per conversation (same setting as Ubuntu Dialogue Corpus), which may mark valid alternative responses as wrong. The dataset presents challenges such as multiple intentions in one message and topic ambiguity across turns.

## 💾 Data

**Source**: Collected real-world conversations between customers and customer service staff from the authors' E-commerce partners on Taobao.

**Size**: 1,000,000 training context-response pairs; 10,000 validation context-response pairs; 10,000 test context-response pairs.

**Format**: N/A

**Annotation**: Negative responses added automatically by ranking the response corpus using Apache Lucene; positive:negative ratio is 1:1 in training and validation, and 1:9 in testing. Texts tokenized using BaseSeg.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Baseline model comparison

**Metrics**:
- Mean Average Precision (MAP)
- Mean Reciprocal Rank (MRR)
- Precision at 1 (P@1)
- Recall at position k (Rn@k) (e.g., R10@1, R10@2, R10@5)

**Calculation**: Evaluation computed over candidate sets per context (test set uses 10 candidates per context with one positive and nine negatives for testing); metrics MAP, MRR, P@1 and Recall@k are reported. Maximum number of utterances per context is 10; each utterance contains at most 50 words; truncation and zero-padding applied as needed.

**Interpretation**: Higher metric values indicate better response relevance/matching. Improvements in R10@1, MAP, MRR and P@1 over baselines are treated as evidence of better model performance.

**Baseline Results**: Examples reported in the paper: On E-commerce Dialogue Corpus (ECD) DUA: R10@1 = 0.501 (SMN: 0.453). On Ubuntu Dialogue Corpus DUA: R10@1 = 0.752 (SMN: 0.726). On Douban Conversation Corpus DUA: R10@1 = 0.421 (SMN: 0.397).

**Validation**: Model selection based on validation set performance; models run up to 5 epochs and the model with best validation result is selected.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy

**Atlas Risks**:
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All the data have been carefully desensitized and anonymized with the consent of the partners to avoid privacy issues (as stated in the paper).

**Data Licensing**: Not Applicable

**Consent Procedures**: Data collected with the consent of the e-commerce partners; data desensitized and anonymized according to the paper.

**Compliance With Regulations**: Not Applicable

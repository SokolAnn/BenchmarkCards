# BBT-CFLEB (Chinese Financial Language understanding and generation Evaluation Benchmark)

## 📊 Benchmark Details

**Name**: BBT-CFLEB (Chinese Financial Language understanding and generation Evaluation Benchmark)

**Overview**: BBT-CFLEB, a Chinese Financial Language understanding and generation Evaluation Benchmark, which includes six datasets covering both understanding and generation tasks. The benchmark is designed to facilitate research in the development of NLP within the Chinese financial domain.

**Data Type**: text (financial news articles, company announcements, research reports, social media posts, question-answer pairs, summary pairs)

**Domains**:
- Natural Language Processing
- Finance

**Languages**:
- Chinese

**Similar Benchmarks**:
- GLUE
- SuperGLUE
- CLUE
- FLUE

**Resources**:
- [GitHub Repository](https://github.com/ssymmetry/BBT-FinCUGE-Applications)
- [Resource](https://arxiv.org/abs/2302.09432)
- [Resource](https://finance.sina.com.cn/)
- [Resource](https://new.qq.com/ch/finance/)
- [Resource](https://finance.ifeng.com/)
- [Resource](https://36kr.com/)
- [Resource](https://www.huxiu.com/)
- [Resource](https://www.eastmoney.com/)
- [Resource](https://guba.eastmoney.com/)
- [Resource](https://xueqiu.com/)

## 🎯 Purpose and Intended Users

**Goal**: Facilitate research and evaluate Chinese language understanding and generation capabilities in the financial domain by providing a benchmark composed of six practical tasks.

**Target Audience**:
- Researchers
- Open-source community

**Tasks**:
- Multi-label Text Classification
- Text Summarization
- Relation Extraction
- Sentiment Analysis
- Question Answering
- Event/Subject Detection

**Limitations**: N/A

## 💾 Data

**Source**: BBT-FinCorpus composed of corporate announcements, research reports, financial news, and social media posts. Crawled sources mentioned include Sina Finance, Tencent Finance, Phoenix Finance, 36Kr, Huxiu, Eastmoney, Guba, and Xueqiu.

**Size**: About 300GB raw text (per paper: corporate announcements ~105GB after conversion, research reports ~11GB after conversion, financial news ~20GB, social media ~120GB; paper states ~300GB overall).

**Format**: Text files (converted from PDF where applicable)

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics (task-specific)
- Model fine-tuning (generative models: text-to-text; BERT-based models: classification head)
- Leaderboards for ranking models

**Metrics**:
- F1 Score
- ROUGE
- Accuracy

**Calculation**: Each task is evaluated on its test set using the metric specified per task (e.g., F1 Score for FinNL on the test set, ROUGE for FinNA on the test set, Accuracy for FinFE on the test set). Train/validation/test splits are provided per task.

**Interpretation**: Higher metric scores indicate better performance; models are ranked on leaderboards (Overall, Understanding ability, Generation ability) based on these metrics.

**Baseline Results**: Table 4 (selected overall averages): GPT2-base Avg 68.37; T5-base Avg 74.89; BBT-FinT5-base Avg 76.29; BBT-FinT5-base-KE Avg 76.84; BBT-FinT5-large Avg 77.07. (Full per-task scores presented in Table 4 of the paper.)

**Validation**: Train/validation/test splits are specified per task (see task descriptions). Models are fine-tuned on training sets, validated on validation sets, and evaluated on test sets; results are reported on the test sets and collected on leaderboards.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable

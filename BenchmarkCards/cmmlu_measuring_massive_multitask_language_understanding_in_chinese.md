# CMMLU (Measuring Massive Multitask Language Understanding in Chinese)

## 📊 Benchmark Details

**Name**: CMMLU (Measuring Massive Multitask Language Understanding in Chinese)

**Overview**: CMMLU is a comprehensive Chinese benchmark designed to evaluate the advanced knowledge and reasoning abilities of large language models in a Chinese linguistic and cultural context. It covers a wide range of subjects (67 topics) from elementary to advanced professional levels, including China-specific and general world knowledge. The benchmark fills the gap in evaluating the knowledge and reasoning capabilities of large language models in the Chinese context.

**Data Type**: text (multiple-choice question-answer pairs; 4 choices per question)

**Domains**:
- Natural Sciences
- Social Sciences
- Engineering
- Humanities
- Education

**Languages**:
- Mandarin Chinese

**Similar Benchmarks**:
- MMLU
- C-Eval
- M3KE
- ACLUE
- MMCU
- AGIEval
- CLUE
- SuperCLUE

**Resources**:
- [GitHub Repository](https://github.com/haonan-li/CMMLU)
- [Resource](https://arxiv.org/abs/2306.09212v2)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive multitask test suite for Mandarin Chinese that evaluates the knowledge and reasoning capabilities of large language models across diverse subjects and Chinese linguistic/cultural contexts.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering (Multiple-choice)
- Knowledge and Reasoning Evaluation

**Limitations**: The authors estimate around 2% noise in the data (correct answer not present or incorrectly labeled). Many tasks are China-specific and their answers may not be universally applicable in other regions. Some tasks cannot be easily translated from other languages due to contextual nuances.

## 💾 Data

**Source**: Questions and answers were manually collected by four annotators (undergraduate or higher) from freely available resources, mock exam questions, quiz shows, and non-publicly available materials; more than 80% of data was crawled from PDFs (after OCR) to reduce occurrence in LLM training data.

**Size**: 11,528 questions across 67 subjects

**Format**: N/A

**Annotation**: Manual collection by four annotators (undergraduate or higher education), paid 50 CNY per hour.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Zero-shot and few-shot evaluation
- Next-token prediction (logit comparison over tokens 'A','B','C','D')
- Free generation with regex extraction
- Perplexity comparison (discussed)

**Metrics**:
- Accuracy (macro average over subjects)
- Proportion of unmatchable outputs when using regex extraction (% E)

**Calculation**: For open-source models: obtain logits for next token and compare probabilities among tokens 'A','B','C','D' and select the highest-probability token. For commercial models (GPT-4, ChatGPT): use free generation and extract choices via regular expressions. Report macro average accuracy over subjects and per-subject accuracies.

**Interpretation**: Results are interpreted relative to random accuracy of 25% and the Chinese exam pass mark of 60% (authors note most models struggle to reach 60%; GPT4 achieves ~71% average). Higher accuracy indicates better Chinese knowledge and reasoning as measured by CMMLU.

**Baseline Results**: Key reported five-shot overall accuracies: GPT4: 70.95%; ChatGPT: 55.51%; Baichuan2-13B: 61.92%; Random baseline: 25.00%. (Numerical results for many models reported in paper tables.)

**Validation**: Quality check: randomly sampled 5% of questions with answers per subject and performed detailed verification through online resources; authors estimate ~2% noise. Each subject has at least 105 questions; split into a few-shot development set with 5 questions and a test set with >100 questions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Data contamination
- **Fairness**: Data bias

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable

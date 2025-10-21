# Xiezhi: An Ever-Updating Benchmark for Holistic Domain Knowledge Evaluation

## 📊 Benchmark Details

**Name**: Xiezhi: An Ever-Updating Benchmark for Holistic Domain Knowledge Evaluation

**Overview**: Xiezhi is a comprehensive, auto-updating evaluation suite designed to assess holistic domain knowledge. Xiezhi comprises 249,587 multiple-choice questions across 516 disciplines (13 categories) and is accompanied by Xiezhi-Specialty (14,041 questions) and Xiezhi-Interdiscipline (10,746 questions). The benchmark is designed for fine-grained domain evaluation and uses a generation-probability-based ranking evaluation.

**Data Type**: question-answering pairs (multiple-choice questions)

**Domains**:
- Philosophy
- Economics
- Law
- Education
- Literature
- History
- Natural Sciences
- Engineering
- Agriculture
- Medicine
- Military Science
- Management
- Art Studies

**Languages**:
- Chinese
- English

**Similar Benchmarks**:
- MMLU
- BIG-bench
- HELM
- AGI-Eval
- MMCU
- C-Eval
- M3KE
- LexTreme
- BIG-Bench-Hard
- HellaSwag
- Physical IQA
- CosmosQA

**Resources**:
- [GitHub Repository](https://github.com/MikeGu721/XiezhiBenchmark)
- [GitHub Repository](https://github.com/MikeGu721/EasyLLM)
- [Resource](https://huggingface.co/LinkSoul/Chinese-Llama-2-7b)

## 🎯 Purpose and Intended Users

**Goal**: To comprehensively evaluate the domain knowledge capabilities of large language models (LLMs) across a broad taxonomy of human knowledge using a large, up-to-date multiple-choice question benchmark.

**Target Audience**:
- Researchers
- Industry Practitioners
- Academic community

**Tasks**:
- Question Answering
- Multiple-choice Question Answering

**Limitations**: Xiezhi currently offers only Chinese and English language versions and lacks comprehensive coverage of knowledge from different cultures and industries.

## 💾 Data

**Source**: Questions collected from six Chinese examinations (primary school, middle school entrance examination, college entrance examination, undergraduate exams, graduate entrance examinations, and adult education examinations) (~170,000 questions); ~80,000 multiple-choice questions generated from Chinese academic surveys/reviews; Xiezhi-Meta: 20,124 manually annotated questions from the Chinese Graduate Entrance Examination; Xiezhi-Train: 2,555 questions.

**Size**: 249,587 questions (Xiezhi-All); Xiezhi-Specialty: 14,041 questions; Xiezhi-Interdiscipline: 10,746 questions; Xiezhi-Meta: 20,124 questions; Xiezhi-Train: 2,555 questions; ~170,000 exam-sourced questions; ~80,000 generated questions.

**Format**: N/A

**Annotation**: Manual annotation by graduate student annotators (each sample annotated by at least three annotators) for Xiezhi-Meta and verification of Xiezhi-Specialty and Xiezhi-Interdiscipline; automatic annotation using ChatGPT and an Annotation Model (fine-tuned Llama-7B) for coarse-grained labels, followed by ChatGPT for finer labels (Annotation Model + ChatGPT pipeline).

## 🔬 Methodology

**Methods**:
- Automated metrics
- Few-shot evaluation (0-shot, 1-shot, 3-shot)
- Generation-probability-based ranking of options
- Human baseline comparison

**Metrics**:
- Mean Reciprocal Rank (MRR)
- Hit@k (Hit@1, Hit@4)
- Mean Rank (MR)
- Accuracy

**Calculation**: For each question, models assign generative probabilities to all 50 options and options are ranked by probability. Mean Reciprocal Rank (MRR) is computed as the mean of the reciprocal rank of the correct answer. Hit@k is the fraction of queries whose correct answer is ranked in the top k. Mean Rank measures the average rank position of the correct answer divided by the number of options. Accuracy is computed in the conventional way.

**Interpretation**: MRR closer to 1 indicates the model tends to place the correct answer near the front of the ranking; MRR closer to 0 indicates the correct answer tends to be ranked near the bottom. Hit@k indicates whether correct answer appears in top-k. Higher values indicate better performance. Human baselines (average exam scores) are used for comparison; values above human baseline indicate models exceed average human performance in that domain as reported.

**Baseline Results**: Random-Guess baseline MRR: 0.089. Example model baseline: GPT-4 MRR reported as 0.402 (0-shot), 0.415 (1-shot), 0.517 (3-shot) in the paper's reported tables.

**Validation**: Xiezhi-Meta, Xiezhi-Train, Xiezhi-Specialty and Xiezhi-Interdiscipline underwent manual verification. The Annotation Model was evaluated against manual labels using Wrong Rate, Missing Rate, and Error Rate. The English translations of Specialty and Interdiscipline were post-processed and revised by annotators. Human baselines were derived from published average examination scores where available.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy
- Legal
- Societal Impact
- Transparency

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Data contamination, Unrepresentative data
- **Intellectual Property**: Data usage rights restrictions
- **Legal Compliance**: Model usage rights restrictions
- **Societal Impact**: Impact on cultural diversity
- **Transparency**: Lack of training data transparency

**Demographic Analysis**: N/A

**Potential Harm**: ['Chinese-centric dataset bias that may advantage models with stronger Chinese knowledge (explicitly noted as a bias risk).', 'Potential encouragement of poor LLM development if discriminatory or prejudiced content were present (the paper states efforts to remove such content).']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset does not contain personally identifiable information; instances are domain-knowledge questions and the paper states individuals cannot be identified from the dataset.

**Data Licensing**: Released under the CC BY-SA 4.0 license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable

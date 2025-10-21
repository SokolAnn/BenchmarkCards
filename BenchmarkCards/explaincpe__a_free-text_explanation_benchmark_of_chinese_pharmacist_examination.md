# ExplainCPE: A Free-text Explanation Benchmark of Chinese Pharmacist Examination

## 📊 Benchmark Details

**Name**: ExplainCPE: A Free-text Explanation Benchmark of Chinese Pharmacist Examination

**Overview**: We propose ExplainCPE, a challenging medical dataset consisting of over 7K problems from Chinese Pharmacist Examination, specifically tailored to assess the model-generated explanations. ExplainCPE is a free-text explanation benchmark in Chinese aimed to evaluate the capacity of model explainability in a specialized, high-stakes medical domain.

**Data Type**: text (multiple-choice questions with free-text explanations)

**Domains**:
- Natural Language Processing
- Healthcare

**Languages**:
- Chinese

**Similar Benchmarks**:
- MMLU
- AGIEval
- C-EVAL
- GAOKAO-Benchmark (GAOKAO-Bench)

**Resources**:
- [GitHub Repository](https://github.com/HITsz-TMG/ExplainCPE)

## 🎯 Purpose and Intended Users

**Goal**: Provide a challenging benchmark for generating free-text explanations in Chinese medical QA, offer a baseline for future research on explanation generation by LLMs, and enable study of how to improve model explanation ability.

**Target Audience**:
- Research community
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering
- Explanation Generation

**Limitations**: We only contribute to Explanation Generation. Most current interpretable methods are aimed at classification tasks; automatic assessment of interpretability is still lacking. The dataset and analysis are a preliminary exploration with room for further improvement in quality and diversity of explanations.

## 💾 Data

**Source**: Questions sourced from the National Licensed Pharmacist Examination in China (official examination examples from 2020-2021 with official examination solutions); additional instances collected from the internet and exercise books; 320 samples manually reviewed by three doctoral students from Peking Union Medical College.

**Size**: 7,556 examples total (6,867 training; 500 development; 189 test)

**Format**: N/A

**Annotation**: Gold explanations sourced from official examination solutions; manual review of 320 samples by three doctoral students (resulting in 318/317 correct out of 320 in two checks, reported 99.4%/99.0% accuracy). Duplicates and incomplete questions removed; instances with edit distance < 0.1 inspected and semantically duplicate questions removed.

## 🔬 Methodology

**Methods**:
- Automated metrics (ROUGE, Accuracy)
- Human evaluation (annotators rate explanations 1-5 on multiple criteria)
- Model-based evaluation (GPT-4 used to evaluate responses)

**Metrics**:
- Accuracy
- ROUGE-1
- ROUGE-2
- ROUGE-L
- Human evaluation ratings (Well-formed, Support, Correctness, Validity, Novelty; 1-5 scale)

**Calculation**: Accuracy measured as percentage of correct answers on the test set. ROUGE computed between model-generated explanations and gold explanations. Human evaluation: annotators rate each explanation from 1 to 5 on five criteria (Well-formed, Support, Correctness, Validity, Novelty).

**Interpretation**: Higher Accuracy indicates better question-answering performance (e.g., GPT-4 achieved 75.7% and is reported to pass the pharmacist examination). Higher ROUGE and higher human evaluation scores indicate better explanation quality and interpretability.

**Baseline Results**: GPT-4: Accuracy 75.7%; ROUGE-1 0.384; ROUGE-2 0.140; ROUGE-L 0.247. ChatGPT: Accuracy 54.5%; ROUGE-1 0.341; ROUGE-2 0.114; ROUGE-L 0.216. GPT-3: Accuracy 40.2% (ROUGE scores not reported). ChatGLM-6B: Accuracy 29.1%; ROUGE-1 0.315; ROUGE-2 0.099; ROUGE-L 0.184. BELLE-7B-2M: Accuracy 33.3% (ROUGE scores not reported). ChatYuan: Accuracy 27.0% (ROUGE scores not reported).

**Validation**: Manual review of 320 randomly selected samples by three doctoral students from Peking Union Medical College (reported 99.4% / 99.0% correctness for reviewed samples). Duplicate and incomplete questions removed; manual inspection of low edit-distance pairs to remove semantically duplicate instances.

## ⚠️ Targeted Risks

**Risk Categories**:
- Interpretability
- Safety
- Accuracy
- Robustness
- Fairness

**Atlas Risks**:
- **Explainability**: Unexplainable output
- **Robustness**: Hallucination
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Transparency**: Uncertain data provenance

**Potential Harm**: ['Reduce misdiagnosis']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The cases in the exercises are fictitious; the authors state there is no personal privacy, discrimination or attack content in the dataset.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable

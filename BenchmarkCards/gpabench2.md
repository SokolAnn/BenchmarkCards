# GPABench2

## 📊 Benchmark Details

**Name**: GPABench2

**Overview**: GPABench2 is a benchmarking dataset of over 2.8 million comparative samples of human-written, GPT-written, GPT-completed, and GPT-polished abstracts of scientific writing in computer science, physics, and humanities and social sciences, created to study the detectability of ChatGPT-generated content in academic literature and to serve as a resource for benchmarking GPT detectors.

**Data Type**: text (research paper abstracts: human-written, GPT-written, GPT-completed, GPT-polished)

**Domains**:
- Computer Science
- Physics
- Humanities and Social Sciences

**Similar Benchmarks**:
- HC3
- M4
- MULTITuDE
- MGTBench
- ArguGPT
- Wiki Abstracts
- ASAP Essays
- BBC News

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To present a large-scale corpus (GPABench2) and comprehensive study to evaluate the detectability of ChatGPT-generated academic abstracts, to benchmark existing GPT detectors, and to assist the design of new detection methods and policies in academia.

**Target Audience**:
- Academic community
- Researchers developing GPT detectors
- Policy makers in academia

**Tasks**:
- Text Classification
- Machine-generated Text Detection

**Limitations**: Focuses on abstracts of research papers (does not include full papers). Focuses primarily on the clean boundary between purely human-generated text and raw ChatGPT output (raw/unedited ChatGPT outputs). Does not claim transferability to non-GPT LLMs.

**Out of Scope Uses**:
- Detection of partially human-edited or paraphrased ChatGPT outputs (the paper focuses on raw ChatGPT output vs purely human-written text)
- Full-text (entire paper) detection (GPABench2 focuses on abstracts only)

## 💾 Data

**Source**: Human-written abstracts collected from top-tier conference proceedings and arXiv (Computer Science), arXiv (Physics), and Springer’s SSRN (Humanities and Social Sciences). GPT-generated abstracts collected via OpenAI API (gpt-3.5-turbo) using crafted prompts and advanced prompt engineering.

**Size**: 2.385 million samples total (2,235,000 GPT-GEN samples and 150,000 HUM samples)

**Format**: N/A

**Annotation**: Labels assigned based on generation/source process: HUM (human-written), GPT-WRI (GPT-written full abstracts), GPT-CPL (GPT-completed abstracts), GPT-POL (GPT-polished abstracts).

## 🔬 Methodology

**Methods**:
- Human evaluation (user study with two cohorts: 155 and 87 participants)
- Automated metrics (TPR, TNR, Accuracy, F1 Score)
- Benchmarking of existing online and open-source detectors
- Hand-crafted linguistic & semantic features models (NELA features + Gradient Boosting)
- Deep neural framework training and evaluation (CheckGPT: RoBERTa representation + LSTM classification head)
- Cross-prompt, cross-task, cross-disciplinary transfer experiments
- Adversarial/robustness testing (rephrasing, copyediting, mixing attacks, prompt-engineering attacks)

**Metrics**:
- True Positive Rate (TPR)
- True Negative Rate (TNR)
- Accuracy
- F1 Score
- Detection accuracy (binary)
- Average detector score (as reported by specific detectors)

**Calculation**: TPR = TP / (TP + FN); TNR = TN / (TN + FP); Accuracy = (TP + TN) / (TP + FP + TN + FN). (Formulas and definitions provided in Section 5.1.)

**Interpretation**: Higher TPR, TNR, Accuracy, and F1 indicate better detectability. The paper reports human evaluators' overall accuracy of 48.82% (Experiment 1) and 61.69% (Experiment 2) and characterizes these as too low for reliable detection. CheckGPT's high accuracies (≈99% average) are interpreted as outstanding performance.

**Baseline Results**: Open-source/statistics-based detectors (e.g., PPL, TP, HLR) achieve satisfactory F1 on Task 1 (e.g., PPL F1 ≈ 0.913) but perform poorly on Tasks 2 and 3. Fine-tuned language models (BERT, DistillBERT, RoBERTa, GPT-2) obtain very high F1 (≈0.95–0.999). CheckGPT achieves very high accuracy (≈99% accuracy and F1 reported across tasks and disciplines). Commercial detectors (GPTZero, ZeroGPT, OpenAI classifier) show modest to poor performance on GPABench2 as reported in Table 1.

**Validation**: Primarily 80/20 train-test splits on GPABench2 (examples: 80K train / 20K test for task/discipline-specific experiments). Additional validation includes cross-prompt and cross-discipline testing, fine-tuning experiments with 5% target-domain data, evaluations on external datasets (Wiki Abstracts, ASAP Essays, BBC News), testing on SOTA ChatGPT datasets (ArguGPT, HC3, M4, MULTITuDE, MGTBench), temporal evaluation on ChatLog-HC3, and robustness/adversarial attack experiments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Misuse
- Robustness
- Privacy
- Accuracy
- Intellectual Property
- Societal Impact
- Governance

**Atlas Risks**:
- **Misuse**: Improper usage
- **Robustness**: Prompt injection attack, Evasion attack
- **Privacy**: Data privacy rights alignment
- **Accuracy**: Poor model accuracy
- **Intellectual Property**: Data usage rights restrictions
- **Societal Impact**: Impact on education: plagiarism, Impact on education: bypassing learning
- **Governance**: Incomplete usage definition

**Demographic Analysis**: User study includes demographic breakdowns by role (faculty, researchers, students), discipline (CS, Physics, HSS), self-claimed familiarity with research papers, and publication experience. Results show only slight differences across groups and largely low detection performance overall.

**Potential Harm**: ['Academic integrity violations (cheating and plagiarism)', 'Flooding publication systems with false or redundant information', 'Facilitating phishing and romance scams (security harms)']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The user study was reviewed and approved by the Human Research Protection Program at the University of [Anonymized]. All collected research paper abstracts are publicly available. Training samples were collected following OpenAI's policy. The paper discusses the need for privacy-preserving local deployment because users may not agree to share manuscripts or review content.

**Data Licensing**: Not Applicable

**Consent Procedures**: User study reviewed and approved by the Human Research Protection Program at the University of [Anonymized].

**Compliance With Regulations**: Not Applicable

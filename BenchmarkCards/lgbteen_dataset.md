# LGBTeen dataset

## 📊 Benchmark Details

**Name**: LGBTeen dataset

**Overview**: A new annotated dataset (LGBTeen dataset) of interactions between queer youth and Large Language Models (LLMs), created to evaluate LLM responses as emotional supporters for queer youth using a novel ten-question rating scale inspired by psychological standards and expert input.

**Data Type**: text (post-response pairs)

**Domains**:
- Natural Language Processing
- Mental Health

**Languages**:
- English
- Hebrew
- Russian
- Arabic

**Resources**:
- [GitHub Repository](https://github.com/nitaytech/LGBTeenDataset)
- [Resource](https://arxiv.org/abs/2402.11886)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and improve LLMs as emotional supporters for queer youth by (1) developing a ten-question evaluation questionnaire, (2) constructing the LGBTeen dataset of Reddit posts, human comments and LLM responses, (3) evaluating multiple SOTA LLMs and human baselines, and (4) proposing methods (prompts and a blueprint) to improve reliability, empathy, and personalization.

**Target Audience**:
- NLP Researchers
- NLP Practitioners
- Mental Health Experts

**Tasks**:
- Text Generation Evaluation
- Question Answering (post-response evaluation)
- Text Classification (annotation of response attributes / questionnaire labels)

**Limitations**: The questionnaire is preliminary and designed for research purposes; it scores single responses (not multi-turn conversations); human evaluation used a small evaluator pool; primary dataset focus is English; subjective nature of some questions leads to lower inter-annotator agreement on some traits.

**Out of Scope Uses**:
- Use of LLMs/dataset outputs as a replacement for psychotherapy or professional therapeutic interventions
- Assuming LLMs can fully replace human evaluators in tasks requiring high emotional intelligence

## 💾 Data

**Source**: 1,000 posts collected from the r/LGBTeens Reddit forum; for each post the most-upvoted human Reddit comment was collected as a human baseline; responses were generated from multiple LLMs (UI: ChatGPT, BARD; API/open models: GPT3.5, GPT4, Orca v2 7b/13b, Mistral-7b, NeuralChat) using multiple prompts (No prompt, Queer Supporter, Guided Supporter, Redditor, Therapist).

**Size**: 1,000 posts; 11,320 responses in total across models and prompts; human-annotated subset: 80 posts with 4 UI responses each (320 responses) and over 5,000 human-provided labels.

**Format**: N/A

**Annotation**: Human annotation using a ten-question questionnaire (answers: 'Yes', 'Partially', 'No', 'Irrelevant') provided by trained evaluators (two females and one male, all identifying as queers, one-hour training, compensated); automatic annotation using GPT3.5 and GPT4 (JSON output format following the annotation guidelines).

## 🔬 Methodology

**Methods**:
- Qualitative case-study analysis (ChatGPT examples / case studies)
- Human evaluation (labeling responses with a ten-question questionnaire via Label Studio)
- Automatic evaluation using LLM-based annotators (GPT3.5 and GPT4)
- Computational analyses of response diversity (sentence embeddings cosine similarity, BLEU, t-SNE)
- Bootstrap-based pairwise model comparison (1,000 iterations)

**Metrics**:
- Weighted questionnaire score (0 for 'Irrelevant'/'No', 0.5 for 'Partially', 1 for 'Yes')
- Accuracy (for LLM-human agreement comparisons)
- Fleiss's Kappa (inter-annotator agreement)
- BLEU Score
- Cosine similarity of sentence embeddings (RoBERTa SentenceTransformer)
- Spearman's correlation (for ranking agreement)

**Calculation**: Questionnaire answers are converted to weighted scores (0 for 'Irrelevant' and 'No', 0.5 for 'Partially', 1 for 'Yes') and averaged per question; inter-annotator agreement reported as pairwise agreement percentages and Fleiss's κ; diversity computed as average cosine similarity over the K most similar instances using RoBERTa SentenceTransformer embeddings; BLEU scores computed between responses; bootstrap (1,000 iterations) sampling subsets of 35 posts used to measure pairwise model comparison agreement and Spearman correlation.

**Interpretation**: Higher weighted questionnaire scores (closer to 1) indicate better performance on the evaluated trait; higher Accuracy and Fleiss's κ indicate stronger LLM-human agreement or human IAA; lower cosine similarity and lower BLEU indicate greater diversity (less generic/templated responses); higher Spearman correlation and higher proportion of correct pairwise comparisons indicate agreement between automatic and human rankings. Table 2 notation: ↑ is better for questionnaire-weighted scores; in diversity plots ↓ is better (indicating higher diversity).

**Baseline Results**: Baseline (most-upvoted Reddit comment) weighted scores (Q1-Q10): Q1 0.98, Q2 0.37, Q3 0.34, Q4 0.20, Q5 0.11, Q6 0.08, Q7 0.07, Q8 0.55, Q9 0.97, Q10 0.23

**Validation**: Validated via human annotation (80 posts, multiple evaluators, >5,000 labels) and automatic evaluation (GPT3.5 / GPT4) with comparisons against human majority vote; bootstrapped pairwise comparisons (1,000 iterations) to assess consistency of automatic rankings with human judgments; inter-annotator agreement (pairwise agreement and Fleiss's κ) reported for the human evaluators.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness
- Fairness
- Accuracy
- Misuse

**Atlas Risks**:
- **Transparency**: Lack of training data transparency
- **Privacy**: Data privacy rights alignment, Exposing personal information
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Value Alignment**: Incomplete advice, Harmful output
- **Robustness**: Hallucination
- **Misuse**: Spreading toxicity, Spreading disinformation
- **Legal Compliance**: Legal accountability
- **Societal Impact**: Impact on affected communities
- **Governance**: Lack of testing diversity

**Demographic Analysis**: Evaluators: two females and one male, all identifying as queers and holding academic degrees (one-hour training). Dataset posts sourced from r/LGBTeens (reflecting queer youth). Authors discuss the need for socio-cultural and persona diversity in collections and alignment.

**Potential Harm**: ["Potentially harmful or dangerous advice that may jeopardize personal safety (e.g., encouraging 'coming out' without context)", 'Misinformation and hallucinated resources (inaccurate or non-existent support links)', 'Cultural insensitivity / cultural ignorance leading to unsafe recommendations for users in conservative contexts', 'Privacy and confidentiality risks for minors and vulnerable users']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The paper emphasizes that ensuring privacy and confidentiality is critical given the sensitive nature of the data; authors note data protection and minors' rights must be rigorously adhered to.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: The paper states that legal and ethical compliance, including data protection and minors' rights, must be adhered to rigorously.

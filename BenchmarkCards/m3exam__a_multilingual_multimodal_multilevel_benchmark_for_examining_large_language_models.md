# M3Exam: A Multilingual, Multimodal, Multilevel Benchmark for Examining Large Language Models

## 📊 Benchmark Details

**Name**: M3Exam: A Multilingual, Multimodal, Multilevel Benchmark for Examining Large Language Models

**Overview**: M3Exam is a novel benchmark sourced from real and official human exam questions for evaluating LLMs in a multilingual, multimodal, and multilevel context. It contains 12,317 multiple-choice questions in 9 languages across three educational levels, with meta-information and images for questions that require them. The benchmark is designed to assess multilingual proficiency, multimodal understanding, and performance across educational levels.

**Data Type**: multiple-choice question-answer pairs (text and images)

**Domains**:
- Natural Language Processing
- Computer Vision
- Education

**Languages**:
- English
- Chinese
- Italian
- Portuguese
- Vietnamese
- Thai
- Swahili
- Afrikaans
- Javanese

**Similar Benchmarks**:
- MMLU
- AGIEval
- C-Eval
- GAOKAO
- IgakuQA

**Resources**:
- [GitHub Repository](https://github.com/DAMO-NLP-SG/M3Exam)
- [Resource](https://arxiv.org/abs/2306.05179)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective is to evaluate the artificial general intelligence of large language models by offering a multilingual, multimodal, and multi-level assessment using real human exam questions.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering (Multiple-choice)

**Limitations**: M3Exam only considers multiple-choice questions for now, making it unsuitable to evaluate LLMs for questions requiring creative writing.

**Out of Scope Uses**:
- Evaluating LLMs for questions requiring creative writing

## 💾 Data

**Source**: Official human exam papers collected from nine countries (435 exam papers) covering primary, middle, and high school graduation exams.

**Size**: 12,317 questions (2,816 questions with images)

**Format**: JSON for question data with separate clipped image files and image placeholders (e.g., (image)[image-x.jpg])

**Annotation**: Manual annotation by native speakers: OCR correction of scanned/imagery papers, separation of question text and candidate options, input of correct answers, inclusion of necessary contextual background, conversion of special formats (e.g., equations to LaTeX), image placeholders, and multiple rounds of quality checks.

## 🔬 Methodology

**Methods**:
- Model-based evaluation (inference on various LLMs, both closed-source via API and open-source via pre-trained weights)
- Zero-shot evaluation
- Few-shot evaluation (held-out in-context examples)
- Automated metrics (accuracy)

**Metrics**:
- Accuracy

**Calculation**: For multiple-choice outputs, take the first alphabetic letter of the model's output as the prediction and compare it with the ground-truth answer to compute accuracy.

**Interpretation**: Higher accuracy indicates better model performance on exam-style questions. The paper highlights that most models achieve less than 60% accuracy on M3Exam; GPT-4 achieving over 60% (72.92% average) is noted as a strong result compared to other models. The authors also reference conventional 'passing' scores per country as an indicator of relative question difficulty.

**Baseline Results**: Key reported results: GPT-4 average accuracy 72.92%; ChatGPT (gpt-3.5-turbo) average 57.57%; Claude average 51.80%; Vicuna 32.29%; BLOOM 23.19%; random baseline ~25.47%; passing conventional scores average 54.44%. Multimodal results on English-with-images: BLIP-2 overall 49.06%, InstructBLIP 46.62%, Fromage 22.77%, OpenFlamingo 29.81%, Flan-T5 (text-only baseline) 48.30%, ChatGPT (text-only) 55.60%.

**Validation**: Multiple rounds of quality checks during annotation; held-out development set created by randomly selecting three questions per subject category per level per language for in-context examples; remaining data used as test data for evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset does not involve any specific person and does not contain information that might be offensive, insulting, or threatening.

**Data Licensing**: CC BY-NC-SA License

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable

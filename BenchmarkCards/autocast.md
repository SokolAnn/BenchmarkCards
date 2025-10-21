# Autocast

## 📊 Benchmark Details

**Name**: Autocast

**Overview**: We introduce Autocast, a dataset containing thousands of forecasting questions and an accompanying news corpus. Questions are taken from forecasting tournaments, ensuring high quality, real-world importance, and diversity. The news corpus is organized by date, allowing us to precisely simulate the conditions under which humans made past forecasts (avoiding leakage from the future).

**Data Type**: question-answering pairs; dated news articles (text)

**Domains**:
- Natural Language Processing
- Politics
- Economics
- Science
- Social

**Similar Benchmarks**:
- ForecastQA

**Resources**:
- [GitHub Repository](https://github.com/andyzoujm/autocast)
- [Resource](https://arxiv.org/abs/2206.15474)
- [Resource](https://data.commoncrawl.org/crawl-data/CC-NEWS/index.html)

## 🎯 Purpose and Intended Users

**Goal**: A dataset for measuring ML models' forecasting ability on real-world forecasting questions, paired with a dated news corpus to simulate the information state available to forecasters prior to outcomes.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering
- Binary Classification (True/False forecasting)
- Multiple-Choice Question Answering
- Numerical Prediction
- Calibration (probabilistic forecasting)

**Limitations**: Autocast contains unresolved questions (about half of questions are unresolved) and a distribution shift over time that is inherent to forecasting. The Autocast training set has fewer than 1,000 numerical training questions. If a model is pre-trained on data from after mid-2021, this will not simulate forecasting faithfully (possible information leakage).

## 💾 Data

**Source**: Forecasting questions collected from three public forecasting tournaments: Metaculus, Good Judgment Open, and CSET Foretell. A news corpus scraped from CommonCrawl CC-NEWS (articles derived from diverse sources between 2016 to mid-2022). IntervalQA curated from existing NLP datasets: SQuAD, 80K Hours Calibration, Eighth Grade Arithmetic, TriviaQA, Jeopardy, MATH, and MMLU.

**Size**: 6,707 unique forecasting questions total (expanded to 9,757 after true/false augmentation); training set (expanded) 4,411 examples; test set (expanded) 1,292 examples; news corpus >200GB of data; IntervalQA ~30,000 numerical questions; IntervalQA calibration dataset splits: training 32,200 examples, validation 3,443 examples, test 6,170 examples.

**Format**: N/A

**Annotation**: Questions include ground truth outcomes and time-series of crowd forecasts (aggregated human predictions) and detailed background metadata and resolution criteria. True/false questions were balanced by negating questions using OpenAI's GPT-3-175B Edit model and manually checking negations.

## 🔬 Methodology

**Methods**:
- Automated metrics (percent accuracy for T/F and MCQ; L1 distance for numerical questions)
- Human baseline (crowd aggregate of forecasters)
- Retrieval-augmented evaluation using BM25 + Fusion-in-Decoder (FiD Static) and FiD Temporal (daily retrieval embeddings + autoregressive model)
- Fine-tuning of pre-trained language models (T5, DeBERTa-v3, UniﬁedQA-v2, GPT-2 for FiD Temporal)

**Metrics**:
- Percent Accuracy (for True/False and Multiple-Choice questions)
- L1 distance bounded between 0% and 100% (for Numerical questions)
- Combined Score metric (T/F+MCQ—Numerical)/2 (upper bound 100%)
- Average score (average of combined metric across model sizes)
- RMS Calibration Error (for IntervalQA confidence intervals)
- Point Estimate Distance (median prediction error)
- Confidence Interval Length (median interval size)

**Calculation**: For true/false and multiple-choice questions we evaluate percent accuracy. For numerical questions we use L1 distance, bounded between 0% and 100%. We denote question types as T/F, MCQ, and Numerical. To evaluate aggregate performance, we use a combined Score metric (T/F+MCQ—Numerical)/2, which has an upper bound of 100%. RMS Calibration Error is computed using adaptive binning across target dynamic range and averaging RMS over fixed confidence levels (detailed in the Supplementary Material).

**Interpretation**: For T/F and MCQ higher percent accuracy is better. For Numerical lower L1 distance is better. The combined Score metric has an upper bound of 100% (perfect prediction across question types). Low RMS Calibration Error indicates better calibration across the dynamic range.

**Baseline Results**: Retrieval-based methods substantially outperform non-retrieval baselines. On forecasting binary outcomes the best ML model achieves ~65% accuracy versus 92% for the human crowd baseline. Retrieval (FiD Static and FiD Temporal) improves performance and larger models generally perform better. DeBERTa-v3 models on IntervalQA show decreasing point estimate error and RMS Calibration Error with model size.

**Validation**: Train/test split uses a date cutoff of mid-2021: training questions close or resolve before 5-11-2021; test questions resolve after this date (mid-2021 to mid-2022). Unresolved questions are excluded from the test set. Retrieval from the news corpus is restricted to articles published on or before the forecasting time to avoid future leakage.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Data Laws
- Misuse
- Value Alignment
- Societal Impact

**Atlas Risks**:
- **Accuracy**: Data contamination, Unrepresentative data, Poor model accuracy
- **Data Laws**: Data usage restrictions
- **Misuse**: Improper usage, Dangerous use
- **Value Alignment**: Over- or under-reliance
- **Societal Impact**: Impact on human agency, Impact on affected communities

**Potential Harm**: ['Eroded epistemics (failure modes the work aims to address)', 'Risks from poor institutional decision-making (including potential weaponization of AI or risky policy decisions)']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Follows the Terms of Use for the Common Crawl website (as stated in the paper); no additional dataset license specified in the paper.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable

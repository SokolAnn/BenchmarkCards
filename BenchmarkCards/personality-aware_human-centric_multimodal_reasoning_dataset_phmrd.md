# Personality-aware Human-centric Multimodal Reasoning Dataset (PHMRD)

## 📊 Benchmark Details

**Name**: Personality-aware Human-centric Multimodal Reasoning Dataset (PHMRD)

**Overview**: A dataset and benchmark for the task Personality-aware Human-centric Multimodal Reasoning (PHMR, T1): forecasting the most probable future behavior of a particular individual in social interactions by integrating multimodal signals from past moments (video, audio, dialogue) and personality traits. The authors construct PHMRD from six television shows (TVQA source), covering 225 characters and 12,616 samples, and propose baselines and an extension task Personality-predicted Human-centric Multimodal Reasoning (T2) with a corresponding dataset (MPPD).

**Data Type**: multimodal (video frames, dialogue text, audio waveforms, and personality annotations; multiple-choice behavior descriptions)

**Domains**:
- Natural Language Processing
- Computer Vision
- Affective Computing

**Languages**:
- English

**Similar Benchmarks**:
- Social-IQ
- VLEP
- PMR
- TVQA

**Resources**:
- [Resource](https://arxiv.org/abs/2304.02313v2)
- [Resource](https://www.personality-database.com)

## 🎯 Purpose and Intended Users

**Goal**: Forecast the most probable behavior of a specific individual at a future timepoint using past multimodal information (video, audio, dialogue) together with personality annotations; additionally, provide an extension that predicts personality from multimodal cues and uses predicted personality for reasoning (T2).

**Tasks**:
- Multimodal Reasoning
- Question Answering
- Personality Prediction

**Limitations**: This work is a preliminary study; the task was not defined as a generation task. Due to space limitation, focus is on presentation of the task and dataset. The proposed baseline is simple and there is room for improvement. The review of literature may not fully cover the research in personality computing.

## 💾 Data

**Source**: Primary video/question-answer data sourced from TVQA (Lei et al., 2018). Personality annotations for characters obtained from the Personality Database (PDB) website (crowd-sourced voting). Datasets constructed from six television shows drawn from TVQA.

**Size**: PHMRD: 12,616 samples (Train 8,768; Dev 1,938; Test 1,910); 225 distinct individuals; average clip duration 74.95 seconds. MPPD (personality-prediction dataset): 11,645 samples (Train 8,152; Dev 1,746; Test 1,747); average number of personalities per clip ~3.28.

**Format**: N/A

**Annotation**: Personality annotations taken from Personality Database (PDB) via crowd-sourced voting; adopted the personality with largest proportion of votes per character. Behavior descriptions and multiple-choice options were rewritten using ChatGPT and manually verified on subsets (manual checks reported: kappa=0.89 for ChatGPT filtering; MASI=0.72 for rewriting agreement).

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation (fine-tuned models and baselines)
- Zero-shot evaluation (multimodal large language models)
- Ablation studies
- Statistical significance testing

**Metrics**:
- Accuracy
- Hamming Loss
- Ranking Loss
- Average Precision

**Calculation**: Accuracy computed as standard accuracy for the multiple-choice selection task; reported as average performance over four runs. For personality prediction, Hamming Loss and Ranking Loss (lower is better) and Average Precision (higher is better) are reported.

**Interpretation**: Higher Accuracy indicates better multimodal reasoning performance. For personality prediction, lower Hamming Loss and Ranking Loss are better; higher Average Precision is better. The paper reports that improvements from incorporating personality are statistically significant (p < 0.05).

**Baseline Results**: Selected reported results (Accuracy): PRM: 53.13% (w/o personality) and 54.06% (w/ personality). Reserve-adapt: 52.43% (w/o) and 53.07% (w/). TVQA-adapt: 43.37% (w/o) and 43.92% (w/). PRM vanilla: 43.03% (w/o) and 44.14% (w/). Zero-shot: Chat-UniVi 23.50% (w/o) and 20.61% (w/); Gemini 33.17% (w/o) and 34.08% (w/).

**Validation**: Dataset split ratio 14:3:3 for train:validation:test. Models trained with early stopping for up to 20 epochs; reported average over four runs. ChatGPT filtering validated via manual labeling on 200 samples (kappa=0.89). Rewriting agreement measured with MASI score (0.72).

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Societal Impact

**Atlas Risks**:
- **Societal Impact**: Impact on affected communities

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Personality annotations obtained from the Personality Database (PDB), described as an open-source website accessible without registration. No additional anonymization procedures are described for PHMRD.

**Data Licensing**: TVQA (data source) is licensed under MIT. PHMRD will be made publicly available later but no license for PHMRD is specified in the paper.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable

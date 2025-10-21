# VAIDA (Visual Analytics for Interactively Discouraging Artifacts)

## 📊 Benchmark Details

**Name**: VAIDA (Visual Analytics for Interactively Discouraging Artifacts)

**Overview**: VAIDA is a novel benchmark-creation paradigm for Natural Language Processing that provides continuous, real-time visual feedback and recommendations to crowdworkers and analysts (human-and-metric-in-the-loop) to identify and reduce dataset artifacts and improve sample quality. It is domain-, model-, task-, and metric-agnostic and includes modules such as DQI (Data Quality Index), AutoFix, and TextFooler to support interactive sample correction, analyst review, and adversarial transformations.

**Data Type**: text (premise-hypothesis pairs for Natural Language Inference)

**Domains**:
- Natural Language Processing

**Similar Benchmarks**:
- SNLI
- SQuAD
- ImageNet
- Quizbowl
- Dynabench
- ANLI
- AFLite
- StoryCLOZE

**Resources**:
- [GitHub Repository](https://github.com/aarunku5/VAIDA-EACL-2023.git)
- [Resource](https://arxiv.org/abs/2302.04434)

## 🎯 Purpose and Intended Users

**Goal**: To provide a human-and-metric-in-the-loop workflow for creating higher-quality benchmarks by (i) identifying artifacts during sample creation, (ii) giving real-time visual feedback and recommendations to crowdworkers, and (iii) enabling analysts to review and reconcile samples to reduce spurious bias and improve generalization.

**Target Audience**:
- Crowdworkers
- Analysts
- ML Researchers
- Benchmark/data creators

**Tasks**:
- Natural Language Inference
- StoryCloze

**Limitations**: Current work is a prototype and design/usability evaluation; it does not integrate with a full-scale crowdsourcing infrastructure or perform full-scale dataset creation. The paper does not explicitly address computational quality control or fairness in depth (though metrics can be added). Real-time deployment at scale requires additional back-end engineering, analyst availability, and budget.

**Out of Scope Uses**:
- Full-scale dataset creation integrated with external crowdsourcing infrastructure (stated as out of scope for this paper)

## 💾 Data

**Source**: Demonstrated by mimicking SNLI dataset creation with premises from the Flickr30k corpus; samples were generated during the user study (NLI) and additional StoryCLOZE samples were created in a separate experiment. Dataset samples generated during the ablation user study are included in the supplemental GitHub.

**Size**: 345 examples created during the user study (69 samples per ablation round across 5 rounds); 100 high-quality SNLI samples present in the system during the study (DQI>0.7).

**Format**: N/A

**Annotation**: Samples were authored by crowdworkers (study participants) and reviewed by analysts; automated modules (AutoFix, TextFooler) were used to propose or perform sample modifications; expert review and analyst decisions were part of the workflow.

## 🔬 Methodology

**Methods**:
- Expert review (Pair-Analytics sessions)
- User study with ablation rounds (NASA Task Load Index evaluation)
- Automated model evaluation (BERT, RoBERTa, GPT-3 fewshot)
- Metric-in-the-loop sample scoring using Data Quality Index (DQI)
- Adversarial transformation (TextFooler)

**Metrics**:
- Data Quality Index (DQI)
- NASA Task Load Index (NASA-TLX)
- Model performance (reported as percent change in performance)

**Calculation**: Overall sample quality is calculated by averaging the artifact percentiles of the seven DQI components for the sample. NASA-TLX scores are collected per standard (0-100 scale, 5-point steps). Model performance differences are reported as percent changes relative to model performance on baseline/standard conditions; models (BERT, RoBERTa) were trained on full SNLI, GPT-3 evaluated in few-shot setting.

**Interpretation**: Higher DQI corresponds to higher sample quality (lower artifact presence / greater expected generalization). DQI components map to traffic-signal color flags (red/yellow/green) based on tuned thresholds; NASA-TLX higher scores indicate higher perceived workload; decreases in model performance on created samples indicate increased robustness/adversarial difficulty of samples.

**Baseline Results**: User study and expert evaluation report a 45.8% decrease in artifact levels across created samples. User-study reported improvements: crowdworkers experienced decreases in mental/temporal demand, effort, and frustration and a +34.6% increase in performance; analysts saw a -14.3% average decrease in difficulty and +30.8% performance. Model performance drops on samples created with VAIDA (TextFooler round) were reported as: BERT -31.3%, RoBERTa -22.5%, GPT-3 (fewshot) -14.98%. In other full-system conditions, model performance decreases and artifact reductions are also reported (see paper for detailed per-condition numbers).

**Validation**: Validated through expert review (3 NLP/visualization researchers), a user study with 23 crowdworkers and 8 analysts using ablation rounds and NASA-TLX (results reported with p ≤ 0.02), and automated evaluation of created samples against pretrained models (BERT, RoBERTa) and GPT-3 (fewshot). Supplementary experiments include StoryCLOZE sample creation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Accuracy
- Data Quality

**Atlas Risks**:
- **Transparency**: Lack of training data transparency, Uncertain data provenance
- **Fairness**: Data bias
- **Accuracy**: Data contamination, Unrepresentative data, Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: ['Spurious bias/artifacts in benchmarks that inflate reported model performance', 'Poor model generalization due to artifact-laden datasets', 'Overstated model robustness/accuracy because of dataset artifacts']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: IRB approval obtained for the user study (stated in paper).

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable

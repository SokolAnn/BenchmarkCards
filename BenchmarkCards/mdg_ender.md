# MDG ENDER

## 📊 Benchmark Details

**Name**: MDG ENDER

**Overview**: A novel, crowdsourced evaluation benchmark of utterance-level gender rewrites for evaluating multi-dimensional (ABOUT, TO, AS) gender bias classification in text.

**Data Type**: utterance-level gender rewrites (text)

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- PASTEL
- Social Bias Frames

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: Provide a gold-labeled evaluation dataset for performing gender identification along three conversational dimensions (ABOUT, TO, AS) and enable training and evaluation of finer-grained gender bias classifiers.

**Target Audience**:
- Machine Learning Researchers
- Model Developers
- Natural Language Processing Practitioners

**Tasks**:
- Text Classification
- Bias Detection
- Controllable Generation
- Offensive Language Detection

**Limitations**: Intersectionality with other identity characteristics (e.g., race, dialect, class) is acknowledged but set aside for follow-up work. Training data used for classifier training is weakly supervised and noisy, particularly for the masculine and feminine classes. Crowdworkers may perform genders in a non-authentic or idiosyncratic way when persona gender does not match their own.

## 💾 Data

**Source**: Crowdsourced rewrites of conversational utterances: annotators were shown an utterance with a persona (including gender) and asked to rewrite the utterance so it clearly indicates ABOUT/TO/AS a man or a woman; original conversations were drawn from dialogue sources and framed with small biography excerpts to encourage gender mentions.

**Size**: Per-dimension counts as reported in Table 2: ABOUT: 384 masculine + 401 feminine = 785 examples; AS: 396 masculine + 371 feminine = 767 examples; TO: 411 masculine + 382 feminine = 793 examples.

**Format**: N/A

**Annotation**: Crowdsourced manual rewrites with subsequent confidence labels: annotators rewrote utterances to make the target dimension (ABOUT/TO/AS) indicate a man or a woman, then reported confidence that the rewritten utterance would be perceived as such.

## 🔬 Methodology

**Methods**:
- Automated metrics (model accuracy evaluation)
- Crowdsourced human annotation (gold evaluation set creation)
- Model-based evaluation using pretrained Transformer classifiers (single-task and multitask)

**Metrics**:
- Accuracy

**Calculation**: Percentage accuracy measured separately for masculine, feminine, and neutral classes; unknown class is not evaluated. Averages reported include M-F averages and averages across dimensions as described in the paper.

**Interpretation**: Higher accuracy indicates better detection of genderedness per dimension. The paper reports that the multitask classifier yields the best average performance across the three dimensions.

**Baseline Results**: Reported baselines include single-task and multitask Transformer-based classifiers. On the MDG ENDER evaluation (Table 3), Multitask All Avg. = 67.13. Example single-task results: ABOUT All Avg. = 60.87; TO All Avg. = 49.97; AS All Avg. = 60.82. Ablation on Wikipedia (Table 5) shows Multi-Task on Wikipedia: Avg. = 77.22; Wikipedia Only: Avg. = 81.82; masking gender words reduces but does not eliminate performance.

**Validation**: MDG ENDER is presented as a gold-labeled evaluation dataset collected via crowdsourcing for reliable evaluation. Models are validated by evaluating accuracy on MDG ENDER and on held-out test sets from the annotated training datasets; early stopping used on average accuracy during training.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy
- Societal Impact

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: Includes analysis across gender groups (masculine, feminine, neutral) — e.g., masculine genderedness scores reported for Wikipedia biographies split by biographies of men and women (Table 8).

**Potential Harm**: ['Gender bias in text', 'Offensive and disparaging language tied to gender', 'Reinforcement of negative societal stereotypes']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable

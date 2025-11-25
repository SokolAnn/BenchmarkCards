# Bike Frames

## 📊 Benchmark Details

**Name**: Bike Frames

**Overview**: We introduce a new dataset called “Bike Frames” to detect the perceived perception of cyclists within news headlines. The dataset consists of 31,480 news headlines and 1,500 annotations. We focus on analyzing 11,385 headlines from the United States. We also introduce the BikeFrame Chain-of-Code (CoC) framework to predict cyclist perception, identify accident-related headlines, and determine fault, integrating news agency bias analysis to improve predictions.

**Data Type**: text (news headlines)

**Domains**:
- Natural Language Processing
- Transportation
- Urban Informatics

**Languages**:
- English

**Similar Benchmarks**:
- Media Frames Corpus
- Gun Violence Frame Corpus (GVFC)
- Misinfo Reaction Frames
- Social Bias Frames

**Resources**:
- [Resource](https://arxiv.org/abs/2301.06178)
- [Resource](https://news.google.com/news/rss)

## 🎯 Purpose and Intended Users

**Goal**: Develop a dataset and methods to analyze how news headlines portray cyclists by (1) detecting accident-related headlines, (2) identifying implicit suggestions of who was at fault, and (3) measuring perception towards cyclists.

**Target Audience**:
- Transportation researchers
- Urban Informatics researchers
- Natural Language Processing researchers

**Tasks**:
- Text Classification (Accident Detection)
- Text Classification (Fault Attribution)
- Sentiment/Framing Classification (Perception)

**Limitations**: Analysis limited to headlines (not full articles), potential for click-bait headlines to affect labels, English-centric and US-annotator-based approach which may not capture global perceptions.

**Out of Scope Uses**:
- Using the dataset to generate intentionally anti-cycling headlines (the paper notes there could be tools developed that generate headlines that are anti-cycling on purpose).

## 💾 Data

**Source**: Collected from Google News using the Google News XML RSS Feed API with keywords 'cycling', 'cyclist', and 'bike' (2001-2021). US-based headlines were identified by manually reviewing news website URLs.

**Size**: 31,480 news headlines (non-labeled) and 1,500 labeled annotations; 11,385 US-based headlines.

**Format**: Plain text files (.txt) for headlines; annotation guidelines provided as Word documents (.docx).

**Annotation**: Manual annotation by annotators in a two-stage process (two annotators independently, followed by discussions and a third adjudicator). Labels: Perception (Negative, Neutral, Positive), Related to Accident (Yes/No), Fault (Cyclist, Unknown, Other). Cohen's Kappa reported for agreement and disagreements adjudicated to form final gold standard.

## 🔬 Methodology

**Methods**:
- Large Language Model prompting using Chain-of-Code (CoC)
- Few-shot and Zero-shot prompting with GPT-3.5-Turbo
- Self-Consistency (multiple reasoning paths aggregation)
- RoBERTa fine-tuning (including Multi-Task RoBERTa and MTLPT RoBERTa)
- Logistic Regression with TF-IDF (with and without LIWC features)
- LIWC feature analysis
- Ablation studies (removing news source analysis and/or self-consistency)

**Metrics**:
- F1 Score
- Cohen's Kappa

**Calculation**: Models trained using a train/dev/test split of 7:1:2. F1 scores computed per class on test set. Self-Consistency aggregated multiple outputs using top-k sampling (k=0.9) with 20 sampled reasoning paths. Cohen's Kappa computed between annotators for annotation agreement.

**Interpretation**: Higher F1 indicates better model/class performance. Incorporating news bias analysis increased average F1 (reported improvement from .739 to .815). Cohen's Kappa ranged from .62 to .90, indicating substantial to almost perfect annotator agreement.

**Baseline Results**: Reported baseline comparisons include Logistic Regression, Logistic Regression + LIWC, multiple RoBERTa variants, and prompt-based baselines. Example reported results: RoBERTa detecting accident-related content (.970) versus BikeFrame Chain-of-Code (.941) for that task. The paper reports that incorporating news bias improved average F1 from .739 to .815 and that the Few-Shot GPT-3.5 + CoC + News + Self-Consistency model outperforms other models based on average F1.

**Validation**: Annotation validation via two annotators with a third adjudicator and Cohen's Kappa (.62-.90). Model validation via train/dev/test split (7:1:2), selection of best model on validation data, and ablation studies to test component impact.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Misuse
- Societal Impact

**Atlas Risks**:
- **Fairness**: Data bias
- **Misuse**: Spreading disinformation
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: Gender analysis using gendered pronouns in headlines (male vs female). The paper reports disproportionate media coverage for female-related headlines and provides summary statistics comparing male and female articles.

**Potential Harm**: ['Detect and highlight media framing that may discourage cycling and reduce the number of people opting to cycle.', 'Identify framing that could lead to reduced government funding for cycling infrastructure.', 'Detect and quantify gendered biases in news coverage that may disadvantage female cyclists.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Creative Commons Attribution License (CC BY 4.0)

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable

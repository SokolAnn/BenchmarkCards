# French Insurance Job Oﬀer (FIJO)

## 📊 Benchmark Details

**Name**: French Insurance Job Oﬀer (FIJO)

**Overview**: A free and public non-annotated and annotated dataset of French insurance job offers focusing on soft skills; the dataset includes de-identified job ads and annotations intended to facilitate research in automatic skill recognition.

**Data Type**: text (de-identified job offer texts with token-level soft-skill annotations)

**Domains**:
- Natural Language Processing
- Insurance
- Labor Market Analysis
- Human Resources

**Languages**:
- French

**Similar Benchmarks**:
- mycareersfuture public dataset
- AQESSS public skills repositories

**Resources**:
- [Resource](https://arxiv.org/abs/2204.05208)
- [Resource](https://creativecommons.org/licenses/by/4.0/legalcode)

## 🎯 Purpose and Intended Users

**Goal**: Provide a public annotated and non-annotated French dataset of insurance job offers to facilitate research and development of machine learning models for automatic soft skill recognition in job ads.

**Target Audience**:
- Machine Learning Researchers
- Model Developers
- Domain Experts (Human Resources, Recruiters)
- Industry Practitioners

**Tasks**:
- Named Entity Recognition
- Sequence Classification
- Token-wise Soft Skill Detection

**Limitations**: Annotated portion is small and class-imbalanced; lexical overlapping between classes; soft skill class boundaries can be ambiguous, making annotation and learning difficult.

## 💾 Data

**Source**: Collected in partnership with four Canadian insurance companies; consists of non-annotated and annotated French job ads published by those companies and their metadata between 2009 and 2020. Job offer text was manually extracted and semi-manually cleaned; de-identification performed using regex substitution, a SpaCy French pre-trained NER model (fr_core_news_lg), and manual checks to substitute names, locations, postal addresses and company-identifying elements.

**Size**: 867 de-identified French job ads (non-annotated); annotated subset: 47 annotated job offers; reported annotation counts include '499 annotations' (section 3.2) and '932 entities' (section 3.3); additional statistics: # of Words (non-annotated) 260,942; average ad length 300.97 words; annotated words 12,702.

**Format**: N/A

**Annotation**: Manual annotation by a domain expert using a skills reference; non-overlapping sentence entities annotated individually with context of the whole job offer; four skill classes defined (French tags: "Pensée", "Résultats", "Relationnel", "Personnel"); entities span from one token up to full sentences.

## 🔬 Methodology

**Methods**:
- Named Entity Recognition (token-wise) using model-based evaluation
- Model training and evaluation with bi-LSTM and transformer-based models (CamemBERT frozen, CamemBERT unfrozen, CamemBERT unfrozen with warmup)
- Repeated runs across random seeds for robustness analysis

**Metrics**:
- Token-wise Accuracy (mean and standard deviation across seeds)
- Per-class token-wise Accuracy (mean and standard deviation)
- McNemar test for statistical comparison

**Calculation**: Data split with simple random sampling into 80% train / 10% validation / 10% test (resulting in 400 training samples). Models trained 5 times with seeds [5,10,15,20,25]; reported mean token-wise accuracy and one standard deviation across seeds. Experiments run with multiple training subset sizes (50,100,150,200,250,300,350,400). Training procedures: up to 300 epochs with early stopping (patience 15); specific learning rates: 0.01 for bi-LSTM and CamemBERT frozen, 0.0001 for CamemBERT unfrozen; learning rate scheduling and warmup used for some CamemBERT unfrozen experiments.

**Interpretation**: Fine-tuning CamemBERT (CamemBERT unfrozen) yields the best token-wise accuracy but shows training instability (high variance across seeds). CamemBERT frozen is less sensitive to initialization; bi-LSTM has lowest performance. Results improve with more training data but are sensitive to company distribution in train/test splits. Token-wise results do not directly translate to correct skill-span extraction (skill-wise results are poorer). More annotated data and rebalancing are needed for improved and stable performance.

**Baseline Results**: For full training subset (400): CamemBERT unfrozen mean token-wise accuracy 83.69% ± 1.80; CamemBERT unfrozen warmup 80.85% ± 1.67; CamemBERT frozen 67.29% ± 0.23; bi-LSTM 60.69% ± 9.23. Per-class accuracies for subset size 400 (CamemBERT unfrozen warmup vs CamemBERT unfrozen): O: 84.50% ±4.51 vs 80.77% ±4.97; Thoughts: 82.72% ±7.84 vs 83.30% ±3.63; Results: 91.21% ±0.00 vs 80.97% ±6.56; Relational: 73.41% ±4.44 vs 92.31% ±4.85; Personal: 80.77% ±4.97 vs 85.21% ±9.65. A McNemar test comparing unfrozen models (best seeds) yielded p=0.5334 (no significant difference).

**Validation**: Models trained and evaluated across 5 random seeds; early stopping used; comparisons across models and training subset sizes; statistical comparison using McNemar test on contingency tables for best-seed models; observed sensitivity to random initialization and train/test company distribution.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Intellectual Property
- Fairness
- Accuracy
- Explainability
- Governance

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Intellectual Property**: Data usage rights restrictions
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Explainability**: Unexplainable output
- **Governance**: Unrepresentative risk testing, Lack of testing diversity

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: De-identification performed: regex substitution for company name and email variations; SpaCy French pre-trained NER model (fr_core_news_lg) used to identify potential names and locations; manual check conducted to substitute names, locations, postal addresses and miscellaneous identifying elements. Substitution tags used: <anon_name>, <anon_location>, <anon_company>, <anon_misc>.

**Data Licensing**: Creative Commons Attribution (CC BY 4.0) as stated in article header (https://creativecommons.org/licenses/by/4.0/legalcode).

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable

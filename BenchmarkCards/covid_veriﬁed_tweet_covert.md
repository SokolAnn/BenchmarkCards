# Covid VERiﬁed Tweet (CoVERT)

## 📊 Benchmark Details

**Name**: Covid VERiﬁed Tweet (CoVERT)

**Overview**: A fact-checked corpus of tweets focusing on biomedical and COVID-19-related (mis)information. The corpus consists of 300 tweets, each annotated with medical named entities and relations, and each tweet annotated with crowdsourced fact-checking labels (SUPPORTS, REFUTES, NOT ENOUGH INFORMATION) together with supporting evidence URLs and text snippets. The authors propose a crowdsourcing methodology for collecting fact-checking labels and evidence and demonstrate use of the retrieved evidence in a fact-checking pipeline.

**Data Type**: text (tweet texts) with claim-evidence pairs and medical named entity and relation annotations

**Domains**:
- Natural Language Processing
- Healthcare
- Biomedical

**Languages**:
- N/A

**Similar Benchmarks**:
- FEVER
- FakeCovid
- COVID-Fact
- HealthVer

**Resources**:
- [Resource](https://www.ims.uni-stuttgart.de/data/bioclaim)
- [GitHub Repository](https://github.com/allenai/scispacy)
- [Resource](https://www.google.com/forms/about/)
- [Resource](https://prolific.co/)
- [Resource](https://www.nlm.nih.gov/mesh/meshhome.html)

## 🎯 Purpose and Intended Users

**Goal**: To create a corpus of fact-checked biomedical COVID-19-related tweets to facilitate evidence-based fact-checking, including entity and relation annotations and crowdsourced supporting evidence.

**Target Audience**:
- N/A

**Tasks**:
- Named Entity Recognition
- Relation Extraction
- Fact Checking
- Evidence Retrieval
- Verdict Prediction

**Limitations**: Dataset consists of 300 tweets (small size). Crowdsourced verification yields moderate inter-annotator agreement for verification labels (average Cohen's kappa = 0.44). The NOT ENOUGH INFORMATION (NEI) class inherently has no substantiating evidence, making this class challenging for evidence-based approaches. Evidence extracts and verdicts may become outdated as biomedical knowledge about SARS-CoV-2 evolves.

## 💾 Data

**Source**: Sampled from an in-house tweet repository using MeSH and frequently occurring medical terms; tweets posted between January 2020 and June 2021 containing mentions of COVID-19 and selected terms (effect, side-effect, vaccine, symptom, treatment) and the lexeme 'caus*'. After filtering and duplicate removal, 300 tweets were randomly sampled for annotation.

**Size**: 300 tweets

**Format**: N/A

**Annotation**: Entities and relations: manual annotation supported by scispaCy with manual revision; entity types: Medical Condition, Treatment, Symptom/Side-effect, Other; relations: cause of, causative agent of, notcause of (UMLS relations). Fact-checking: crowdsourced via Prolific with 3 annotators per tweet; annotators searched the web (Google Search) for credible sources, provided a URL and evidence snippet, and assigned a label (SUPPORTS, REFUTES, NOT ENOUGH INFORMATION). Majority vote (>=2 annotators) used to adjudicate gold labels. Attention checks and qualification filters were used for crowdworkers; payment and bonus scheme described in paper.

## 🔬 Methodology

**Methods**:
- Automated metrics (Acc@k for probing)
- Model-based evaluation using a fact-checking pipeline (MLP-FEVER, MLP-Evidence)
- Probing language models with BioLAMA
- Crowdsourced annotation with majority-vote adjudication

**Metrics**:
- Accuracy (Acc@1, Acc@5)
- F1 Score
- Precision
- Recall
- Cohen's kappa
- Inter-annotator F1

**Calculation**: Acc@k (top-k accuracy) equals 1 if any of the top-k predicted object entities match an object in the gold annotated object list. Inter-annotator F1 for entities computed by treating one annotator's labels as gold and the other's as predictions. Cohen's kappa for verification labels computed per annotation task (10 tweets with 3 annotators) by averaging pairwise kappas across annotator pairs.

**Interpretation**: Moderate agreement on verification labels (average Cohen's kappa = 0.44) indicates moderate crowd consensus; high inter-annotator F1 for entity annotations (weighted macro average F1 = 0.88) indicates reliable entity annotations after manual revision. Improved F1 for the fact-checking pipeline when using real-world evidence extracts (MLP-Evidence) indicates that external evidence can be more useful than LM-generated evidence.

**Baseline Results**: Verdict-prediction results: MLP-FEVER on Tweet + LM: Precision 0.60, Recall 0.61, F1 0.60. MLP-FEVER on Tweet + Evidence: Precision 0.61, Recall 0.38, F1 0.46. MLP-Evidence (fine-tuned on CoVERT evidence) on Tweet + Evidence: Precision 0.68, Recall 0.74, F1 0.69. FEVER test results: MLP-FEVER F1 0.49, MLP-Evidence F1 0.46. BioLAMA probing: BERT Acc@1 on SUPPORTS 4.6%, REFUTES 3.62%, NEI 0.0%; BERT Acc@5 reported as well.

**Validation**: Entity annotation quality: second annotator labeled a random subset of 100 tweets for validation. Fact-checking annotation: each tweet annotated by three crowdworkers; majority vote used as gold label; attention checks included to filter low-quality submissions. For model evaluation, MLP-Evidence fine-tuned using an 80/10/10 train/develop/test split of CoVERT evidence-text pairs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Safety
- Societal Impact

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: Detecting and preventing dissemination of health-related misinformation that can pose a danger to people's health (explicitly discussed in the paper).

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: All crowdworkers agreed to participate and signed a consent form prior to participation (explicitly stated).

**Compliance With Regulations**: Not Applicable

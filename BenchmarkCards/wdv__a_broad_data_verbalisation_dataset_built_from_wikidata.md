# WDV: A Broad Data Verbalisation Dataset Built from Wikidata

## 📊 Benchmark Details

**Name**: WDV: A Broad Data Verbalisation Dataset Built from Wikidata

**Overview**: WDV is a large KG claim verbalisation dataset built from Wikidata, with a tight coupling between triples and text, covering a wide variety of entities and predicates. It provides 7.6k claim-verbalisation pairings, with 1.4k entries annotated by humans for fluency and adequacy, and is intended as a benchmarking dataset for data verbalisation models applied on Wikidata.

**Data Type**: text (single triple-to-sentence pairs / claim-verbalisation pairs)

**Domains**:
- Natural Language Processing
- Semantic Web

**Languages**:
- English

**Similar Benchmarks**:
- WebNLG
- T-REx
- NYT-FB
- FB15K-237
- TACRED

**Resources**:
- [Resource](https://doi.org/10.6084/m9.figshare.17159045.v1)
- [GitHub Repository](https://github.com/gabrielmaia7/WDV)
- [Resource](https://arxiv.org/abs/2205.02627)

## 🎯 Purpose and Intended Users

**Goal**: Provide a benchmarking dataset for data verbalisation models applied on Wikidata, with tight coupling between single triple-based claims and natural language sentences and a broad, balanced coverage of entity types and predicates.

**Target Audience**:
- ML Practitioners
- Developers
- Semantic Web Researchers
- Wikidata Research Community

**Tasks**:
- Data-to-Text Generation
- Graph-to-Text Generation
- Natural Language Generation

**Limitations**: Annotations were collected for approximately 20% of the dataset (1,426 of 7,607 claims) due to budget constraints; annotated subset limited to claims with all labels in English.

## 💾 Data

**Source**: Claims extracted from Wikidata using SPARQL queries; data extraction and processing used a Wikipedia JSON dump from August 2021.

**Size**: 7,607 claim-verbalisation pairs; 1,426 annotated pairs (approximately 20% annotated)

**Format**: JSON (flattened claim-centered schema derived from Wikipedia JSON dump format)

**Annotation**: Crowdsourced via Amazon Mechanical Turk: fluency ratings on a 0-5 scale and adequacy labels (Yes/No/Not Sure) with at least five different workers per item; quality control via golden data, grammar screening quiz, time checks, worker qualification filters, and pilot studies.

## 🔬 Methodology

**Methods**:
- Crowdsourced human evaluation
- Automated metric evaluation
- Model-based evaluation (T5 fine-tuned verbalisation model)

**Metrics**:
- BLEU Score
- Fluency (mean and median)
- Adequacy percentage
- Majority-vote adequacy
- Krippendorff's Alpha (inter-annotator agreement)

**Calculation**: BLEU scores calculated with Moses. Fluency aggregated using mean and median of worker scores. Adequacy aggregated by majority voting and by computing the percentage of workers voting Yes (adequacy percentage). Inter-annotator agreement measured with Krippendorff's Alpha.

**Interpretation**: A fluency score of 3 indicates 'Comprehensible text with minor grammatical errors' (authors use median and mean fluency to assess quality). Krippendorff's Alpha values reported (0.4272 for fluency, 0.4583 for adequacy) are interpreted as moderate agreement according to Landis & Koch. High percentages of median fluency >= 3 and high majority-voted adequacy indicate good verbalisation quality.

**Baseline Results**: Verbalisation model (T5-base fine-tuned on WebNLG) BLEU: SEEN 65.51, UNSEEN 51.71, ALL 59.41. Overall: over 96% of verbalisations have median fluency >= 3; almost 93% of verbalisations are majority-voted as adequate. Partition-level results (from Table 3): Mean Fluency - WD_UNSEEN 3.684, WebNLG_UNSEEN 3.884, WebNLG_SEEN 3.91; Adequacy Percentage - WD_UNSEEN 80.3%, WebNLG_UNSEEN 80.6%, WebNLG_SEEN 82%; Majority-Adequate Percentage - WD_UNSEEN 92.5%, WebNLG_UNSEEN 92.8%, WebNLG_SEEN 93.1%.

**Validation**: Stratified sampling per theme using 95% confidence interval and 5% margin of error with sampling weights recorded to adjust estimates; crowdsourcing pilots to set pay and task design; golden data (90 poor examples + 45 manually annotated) used for worker quality control; worker qualifications (>=1000 HITs and >80% acceptance) and grammar screening quiz employed; multiple annotators per item and aggregation procedures applied.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Hallucination
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Tasks were released on AMT after receiving ethical approval; workers were anonymous and informed that continuing the task constituted consent. Worker selection and procedures aimed to respect worker privacy; tasks and consent details are included in the repository.

**Data Licensing**: Not Applicable

**Consent Procedures**: Workers informed of pay and conditions and told that continuing with the task means consenting to both; ethical approval was obtained for the tasks.

**Compliance With Regulations**: Not Applicable

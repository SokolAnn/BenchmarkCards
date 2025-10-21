# Visual Abductive Reasoning (VAR)

## 📊 Benchmark Details

**Name**: Visual Abductive Reasoning (VAR)

**Overview**: We propose a new task and dataset, Visual Abductive Reasoning (VAR), for examining abductive reasoning ability of machine intelligence in everyday visual situations. Given an incomplete set of visual events, AI systems are required to not only describe what is observed, but also infer the hypothesis that can best explain the visual premise.

**Data Type**: multimodal: video and text (event-level videos with abductive reasoning oriented event descriptions and explanatory hypotheses)

**Domains**:
- Computer Vision
- Natural Language Processing

**Similar Benchmarks**:
- ActivityNet Captions
- Dense Video Captioning (DVC)
- VLEP
- TVC dataset

**Resources**:
- [GitHub Repository](https://github.com/leonnnop/VAR)
- [Resource](https://arxiv.org/abs/2203.14040)
- [Resource](https://cs.stanford.edu/people/ranjaykrishna/densevid/)
- [GitHub Repository](https://github.com/jayleicn/VideoLanguageFuturePred)
- [GitHub Repository](https://github.com/jayleicn/TVCaption)
- [Resource](https://www.movieclips.com/)
- [Resource](https://creativecommons.org/licenses/by/4.0/)
- [Resource](https://www.fandango.com/policies/terms-of-use)

## 🎯 Purpose and Intended Users

**Goal**: To test the abductive reasoning ability of machine intelligence in everyday visual environments by requiring systems to describe partially observable premise events and infer the most plausible explanatory hypothesis.

**Tasks**:
- Visual Abductive Reasoning
- Dense Video Captioning

**Limitations**: During annotation process, we observe a bias against women and minorities due to the highly biased nature of movie and web sourced video data [54, 56, 63]. V AR, derived from these data, inevitably runs into the same problem [16, 77]. We thus suggest that models trained on V AR dataset should be cautiously examined before being deployed onto real-world applications.

## 💾 Data

**Source**: Collected from three sources: 23,457 YouTube lifestyle Vlog videos from ActivityNet Captions and VLEP; 13,799 TV show and movie videos from TVC dataset and the YouTube channel Fandango MovieClips. A part of the dataset is sourced from ActivityNet Captions.

**Size**: 8,606 examples from 3,718 unique videos (total ~153 hours of video). Dataset contains 15,486 events and ~15K descriptive sentences. Average event duration 37.8 seconds; average 4.17 events per video; average sentence length 13.5 words. Dataset split: train 7,053 examples, val 460 examples, test 1,093 examples.

**Format**: N/A

**Annotation**: Three-step human annotation: (1) Event type annotation by human experts labeling events as premise or explanation (preserving examples with >2 affirmative votes); (2) Abductive reasoning oriented description annotation where annotators write premise and explanation descriptions while the explanation event is hidden; (3) Validation: each annotated example is examined by three verifiers shown only the premise events and the language-based explanation and vote for 'Is the explanation sound?'; majority approval required.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation (user studies)
- Ablation studies
- Baseline benchmarking

**Metrics**:
- BLEU@4
- CIDEr
- METEOR
- ROUGE-L
- BERTScore

**Calculation**: Five automated metrics (BLEU@4, CIDEr, METEOR, ROUGE-L, BERTScore) are used. BERTScore is evaluated under a static/reproducible setting: roberta-large L17 no-idf version =0.3.0 (hug_trans=2.3.0) - rescaled. (Other metrics are used as standard implementations cited in the paper.)

**Interpretation**: Higher metric scores indicate better descriptive and hypothesis generation. The paper reports that REASONER outperforms prior dense video captioning baselines but remains substantially below human performance (example: REASONER BERT-S 33.44 vs best competitor BERT-S 28.71; human BERT-S 42.96), indicating large headroom for abductive reasoning.

**Baseline Results**: REASONER outperforms top DVC baselines on VAR (example given: REASONER BERT-S 33.44 vs best competitor 28.71) but is still below human performance (BERT-S 42.96). Detailed per-metric results are reported in Table 2 of the paper.

**Validation**: Annotation validation: each example is validated by three verifiers with majority approval required. Human evaluation: ten volunteers wrote descriptions/hypotheses on 500 sampled test examples for human upper-bound evaluation; additional user studies with three volunteers performed pairwise model preference comparisons on 500 sampled examples.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Misuse
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Misuse**: Spreading disinformation
- **Privacy**: Personal information in data

**Demographic Analysis**: During annotation process, we observe a bias against women and minorities due to the highly biased nature of movie and web sourced video data. VAR, derived from these data, inevitably runs into the same problem.

**Potential Harm**: ['Bias against women and minorities in dataset and downstream models', 'Potential for generating deceptive content / disinformation ("fabricating deceptive facts")']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All human experts were informed that annotation and evaluation will be used for academic research and individual consents were obtained with signed agreements. The annotation will not leak any personal information about the experts.

**Data Licensing**: VAR dataset will be released under CC-BY 4.0 license, respecting the licenses of its source videos. Source assets: ActivityNet Captions (CC-BY 4.0), VLEP (CC-BY 4.0), TVC (CC-BY 4.0), MovieClips (copyright © 2021 Fandango; site/services available for non-commercial use).

**Consent Procedures**: Individual consents were reached with signed agreements for annotators and evaluators; annotators were notified that their annotation and evaluation will be used for academic research.

**Compliance With Regulations**: Not Applicable

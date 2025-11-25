# CPED: A Large-Scale Chinese Personalized and Emotional Dialogue Dataset for Conversational AI

## 📊 Benchmark Details

**Name**: CPED: A Large-Scale Chinese Personalized and Emotional Dialogue Dataset for Conversational AI

**Overview**: We propose CPED, a large-scale Chinese personalized and emotional dialogue dataset, which consists of multi-source knowledge related to empathy and personal characteristic. These knowledge covers gender, Big Five personality traits, 13 emotions, 19 dialogue acts and 10 scenes. CPED contains more than 12K dialogues of 392 speakers from 40 TV shows. We release the textual dataset with audio features and video features according to the copyright claims, privacy issues, terms of service of video platforms. We provide detailed description of the CPED construction process and introduce three tasks for conversational AI, including personality recognition, emotion recognition in conversations as well as personalized and emotional conversation generation.

**Data Type**: multimodal (text, audio features, video features; utterance-level videos and subtitles)

**Domains**:
- Natural Language Processing
- Human-Computer Interaction
- Healthcare

**Languages**:
- Chinese

**Similar Benchmarks**:
- OpenSubtitles
- Ubuntu Dialogue Corpus
- STC
- LCCC
- OpenViDial
- IEMOCAP
- DailyDialog
- MELD
- EmpatheticDialogues
- ESTC
- MEmoR
- PERSONA-CHAT
- PersonalDialog
- FriendsPersona
- PELD

**Resources**:
- [GitHub Repository](https://github.com/scutcyr/CPED)
- [Resource](https://arxiv.org/abs/2205.14727)

## 🎯 Purpose and Intended Users

**Goal**: To propose a dataset to be widely adopted by the NLP community as a new open benchmark for conversational AI research, considering speakers' personalities and dynamic emotions to support personality recognition, emotion recognition in conversations, and personalized and emotional conversation generation.

**Target Audience**:
- Natural Language Processing Researchers
- Conversational AI Researchers
- Model Developers

**Tasks**:
- Personality Recognition in Conversations
- Emotion Recognition in Conversations
- Personalized and Emotional Conversation Generation

**Limitations**: Dataset is derived from TV dramas which may differ from natural conversations in scenario and interaction types; emotion and DA label distributions are unbalanced; potential for models trained on dataset to learn negative or dangerous expressions.

## 💾 Data

**Source**: Collected from 40 popular TV series (TV shows). Dialogue segments selected from videos, subtitles obtained via OCR, and multimodal context (video, audio, text) used for annotation. Original video sources cited include Tencent Video, Youku Video and iQiyi Video.

**Size**: 11,835 dialogues (reported as >12K in abstract); 133K utterances; 392 speakers; 40 TV shows

**Format**: Textual data (subtitles) with associated audio features and video features; utterance-level video/audio referenced by Utterance ID; dataset split by TV series into train/valid/test (7:1:2).

**Annotation**: Annotated by three psychology experts. Utterance-level annotation: sentiment (positive/neutral/negative), emotion (13 categories), dialogue act (19 labels), scene (10 categories). Speaker-level annotation: name, gender, age group (children, teenager, young, middle-aged, elderly), Big Five personality traits via Chinese BFI-2 (high/low/unknown). Majority vote used; reannotation for disagreements; ambiguous samples discarded.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation by experts
- Baseline model evaluations (PRC, ERC, PEC) including BERT variants, DialogueRNN, DialogueGCN, DialogXL, bcLSTM, GPT and CDial-GPT based models

**Metrics**:
- Perplexity (PPL)
- BLEU Score
- Distinct-N (D-1, D-2)
- Greedy Matching
- Embedding Average
- BERTScore
- Accuracy
- Macro-F1
- Fleiss' kappa (inter-rater agreement for manual evaluation)

**Calculation**: Automatic generation metrics (PPL, BLEU, Distinct-N, Greedy, Embedding Average, BERTScore) computed on test set; PRC and ERC evaluated with Accuracy and Macro-F1. Manual evaluation: three experts rated content consistency, emotion correlation and personification on a 0-2 scale. Dataset split by TV series (7:1:2) to avoid speaker overlap.

**Interpretation**: Higher automatic metric scores (e.g., lower PPL, higher BLEU/DISTINCT/BERTScore) indicate better generation quality; higher Accuracy and Macro-F1 indicate better recognition performance. Manual scores (0-2) measure content consistency, emotional relevance and personification; Fleiss' kappa reported to indicate inter-rater agreement. Paper reports that explicit infusion of emotions and personalities improves personification and emotional expression in generated responses; specific baseline findings are reported per task.

**Baseline Results**: Reported baselines: PRC (Personality Recognition) evaluated with BERT-based methods (variants BERTs, BERTc, BERTc_senet, BERTc_ssenet) with BERTc_ssenet achieving best Macro-F1/average accuracy among reported PRC baselines. ERC (Emotion Recognition) baselines include utterance-level (TextCNN, TextRNN, TextRCNN, FastText, BERT) and dialogue-level (bcLSTM, DialogueRNN, DialogueGCN, DialogXL, EmoBERTa); BERT+AVG+MLP achieves best average accuracy and Macro-F1 among reported ERC baselines. PEC (Personalized and Emotional Conversation) baselines include Seq2Seq, Transformer, GPT, implicit embedding method (femo+da g-GPT) and explicit fusion methods (GPT-fper/emo/da variants); explicit fusion (e.g., GPT-fper+emo+da_g) yields improved automatic and manual personification and emotion correlation metrics as reported in Table VIII.

**Validation**: Quality control: three psychology experts with prelabeling rounds and labeling rules; each utterance annotated by 3 experts and majority rule used; inconsistent samples reannotated or discarded. Dataset split by TV series (7:1:2) to avoid speaker overlap between splits.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Intellectual Property
- Accuracy

**Atlas Risks**:
- **Data Laws**: Data usage restrictions
- **Intellectual Property**: Copyright infringement, Data usage rights restrictions
- **Privacy**: Data privacy rights alignment
- **Fairness**: Data bias
- **Misuse**: Dangerous use, Spreading toxicity
- **Value Alignment**: Toxic output
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Dataset includes speaker gender and age group annotations; male-to-female ratio close to 1:1; age groups annotated as children, teenager, young, middle-aged, elderly; Big Five distributions provided per dimension (Neuroticism, Extraversion, Openness, Agreeableness, Conscientiousness).

**Potential Harm**: ['Negative responses (responses that make the emotions of both sides develop in a worse direction)', 'Dangerous responses (responses involving suicide, abetting suicide, intimidation)']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All dialogue materials are based on TV dramas; character names are fictitious; personal attributes are annotated from character performances; dataset release limited to textual dataset with audio features and video features according to copyright claims, privacy issues and platform terms of service.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Materials are described as licensed under the Copyright Law of the People's Republic of China; release constrained by copyright claims, privacy issues and terms of service of Tencent Video, Youku Video and iQiyi Video.

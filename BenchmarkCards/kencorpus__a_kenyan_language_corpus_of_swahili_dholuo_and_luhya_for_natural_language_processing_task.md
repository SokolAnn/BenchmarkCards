# Kencorpus: A Kenyan Language Corpus of Swahili, Dholuo and Luhya for Natural Language Processing Tasks

## 📊 Benchmark Details

**Name**: Kencorpus: A Kenyan Language Corpus of Swahili, Dholuo and Luhya for Natural Language Processing Tasks

**Overview**: The Kencorpus dataset is a text and speech corpus for three languages predominantly spoken in Kenya: Swahili, Dholuo and Luhya (three dialects of Lumarachi, Lulogooli and Lubukusu). The project collected and stored text and speech data to support data-driven solutions in applications such as machine translation, question answering and transcription. The Kencorpus collection comprises 5,594 items: 4,442 texts (about 5.6 million words) and 1,152 speech files (about 176.5 hours). From this corpus the project also developed POS-tagged datasets, parallel translations, and a Kiswahili QA dataset (KenSwQuAD).

**Data Type**: text (cleaned text documents, tweets, QA pairs, POS-tagged texts, parallel sentence translations) and audio (speech files)

**Domains**:
- Natural Language Processing

**Languages**:
- Swahili
- Dholuo
- Luhya (Lumarachi)
- Luhya (Lulogooli)
- Luhya (Lubukusu)

**Similar Benchmarks**:
- SQuAD
- TyDiQA
- MCTest
- WikiQA
- TREC-QA

**Resources**:
- [Resource](https://kencorpus.maseno.ac.ke/)
- [Resource](https://doi.org/10.7910/DVN/OTL0LM)
- [Resource](https://doi.org/10.7910/DVN/YHXJSU)

## 🎯 Purpose and Intended Users

**Goal**: Collect and curate text and speech data for low-resource Kenyan languages (Swahili, Dholuo, Luhya) and develop derived datasets (POS annotations, translations, QA pairs) to enable machine learning applications such as machine translation, question answering and transcription.

**Target Audience**:
- Machine learning researchers
- Natural Language Processing researchers
- Enterprises interested in human language technology
- Model developers
- Domain experts working on low-resource languages

**Tasks**:
- Machine Translation
- Question Answering
- Speech-to-Text (Transcription)
- Part of Speech Tagging

**Limitations**: Challenges in developing the corpus included deficiencies in the data sources, data cleaning challenges, relatively short project timelines and the Coronavirus disease (COVID-19) pandemic that restricted movement and hence the ability to get the data in a timely manner.

## 💾 Data

**Source**: Primary data (communities, schools, colleges, volunteers) and secondary data (partnering media houses, publishers). Additional sources: story-writing competitions, web-scraped tweets (Swahili and Dholuo) collected via Twitter API. Research assistants (native speakers) collected and digitized data; media houses provided speech MP3 files.

**Size**: Total 5,594 items: 4,442 texts (5,601,915 words) and 1,152 speech files (176 hours 29 minutes 46 seconds). Swahili: 2,585 texts (1,829,727 words), 104 speech files (19:10:57). Dholuo: 546 texts (1,346,481 words), 512 speech files (99:03:08). Luhya: 987 texts (2,272,957 words), 536 speech files (58:15:41). Additional datasets: 13,400 translation sentence pairs (Dholuo-Swahili and Luhya-Swahili), 143,000 words POS-tagged (Dholuo and Luhya dialects), 7,537 QA pairs (from 1,445 Swahili texts).

**Format**: Cleaned text files in TXT format for texts; speech files converted to WAV format for speech. (Tweets were processed and retained as text.)

**Annotation**: POS annotation: manual tagging by at least two research assistants per document using the 12-tag universal tagset (Petrov et al., 2011) with lead linguist resolving disagreements. QA annotation: five QA pairs per eligible Swahili text created via Google Forms following methodology similar to SQuAD and TyDiQA; 70% of Kiswahili texts were annotated. Translation: sentence-level translations (literal/equivalence) performed by native speakers and linguistic experts; dictionaries used as references. Annotation work used spreadsheets and Google Forms as described.

## 🔬 Methodology

**Methods**:
- Participatory primary data collection (community, schools)
- Secondary data acquisition from media houses and publishers
- Web scraping (Twitter API) for tweets
- Digitization and OCR (Pen-to-Print, Expert PDF OCR, Google Docs converter)
- Human data cleaning with multi-stage pipeline (Digitize, Screening, Diagnosis, Treatment, Documentation)
- Manual annotation (POS tagging, translation, QA creation) with multi-annotator checks
- Proof-of-concept model evaluation (QA models using XLM-RoBERTa/BERT and semantic networks; STT using CMU Sphinx)

**Metrics**:
- Exact Match (EM)
- F1 Score
- Word Error Rate (WER)

**Calculation**: QA models evaluated using held-out test split (example: 80% training / 20% testing for a 100-story subset with 500 QA pairs). EM and F1 computed for QA evaluation as reported. WER computed for the speech-to-text evaluation on the evaluated speech subset.

**Interpretation**: For QA: higher Exact Match (EM) and higher F1 Score indicate better performance. For STT: lower Word Error Rate (WER) indicates better performance. Reported example comparisons: semantic network method achieved higher EM (80%) than the data-driven BERT-based method (59.4% F1) on the tested subset; STT WER of 18.87% reported as relatively good for low-resource settings.

**Baseline Results**: QA system using deep learning (XLM-RoBERTa/BERT) on a 100-story / 500 QA-pair subset: 59.4% F1 score. QA system using semantic network: 80% Exact Match. STT using CMU Sphinx on a 27h31m50s Swahili subset: 18.87% WER.

**Validation**: Quality control included: informed consent procedures; metadata capture for each item; primary and secondary data cleaners with swap-and-review; linguist random sampling checks; POS tagging rechecked by subject matter experts on a random 10% sample of annotated words; translation and QA samples checked (10% sampling for translations; annotators cross-checked QA pairs with lead researcher resolving disagreements).

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Data Laws
- Accuracy

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Data Laws**: Data usage restrictions
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: Respondents were purposively drawn from different genders, age groups and geographical locations; metadata captured includes gender and age group information as per project metadata forms.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Informed consent forms were developed and used. Consent forms captured participant full names and contacts; group consent (e.g., by school managers) was used for institutions with individual willingness respected. Metadata capture included personally identifying information as described in the project documentation.

**Data Licensing**: All Kencorpus collections and derived datasets are available under the Creative Commons Attribution (CC BY 4.0) international license.

**Consent Procedures**: Informed consent forms were provided and signed by willing participants; group consent for institutions was executed by school managers with individual participation optional. Copies of consent forms were retained.

**Compliance With Regulations**: Not Applicable

# S2DV HepG2 toxicity

Flags compounds likely to be cytotoxic to HepG2 liver carcinoma cells, a first-pass safety filter when triaging antiviral candidates. Shao and colleagues borrowed word2vec from natural language processing, treating ECFP substructure identifiers as tokens so that a compound and its fragments share an embedding space, then fitted a support vector classifier on the resulting drug vectors. Training drew on 2,270 ChEMBL records with measured CC50 values, and the authors also tested the classifier on compounds they assayed themselves in HepG2 2.2.15 cells.

This model was incorporated on 2023-03-27.Last packaged on 2026-10-07.

## Information
### Identifiers
- **Ersilia Identifier:** `eos2fy6`
- **Slug:** `s2dv-hepg2-toxicity`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Activity prediction`
- **Biomedical Area:** `ADMET`
- **Target Organism:** `Homo sapiens`
- **Tags:** `ChEMBL`, `IC50`, `Toxicity`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1`
- **Output Consistency:** `Fixed`
- **Interpretation:** Probability of HepG2 cytotoxicity, with actives defined at a CC50 below 30 uM.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| hepg2_proba1 | float | high | Probability of citotoxicity assessed in HepG2 cells |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos2fy6](https://hub.docker.com/r/ersiliaos/eos2fy6)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos2fy6.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos2fy6.zip)

### Resource Consumption
- **Model Size (Mb):** `43`
- **Environment Size (Mb):** `1132`
- **Image Size (Mb):** `1233.96`

**Computational Performance (seconds):**
- 10 inputs: `23.88`
- 100 inputs: `15.69`
- 10000 inputs: `158.1`

### References
- **Source Code**: [https://github.com/NTU-MedAI/S2DV](https://github.com/NTU-MedAI/S2DV)
- **Publication**: [https://doi.org/10.1093/bib/bbab593](https://doi.org/10.1093/bib/bbab593)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2022`
- **Ersilia Contributor:** [emmakodes](https://github.com/emmakodes)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [Apache-2.0](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos2fy6
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos2fy6
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!

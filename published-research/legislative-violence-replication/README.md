# Legislative Violence Replication Code

Code and selected documentation accompanying Yang Zhang's public replication deposit for *When Conflict Leaves the Rules: Party Institutionalisation, System Closure and Legislative Violence in Europe*.

本儲存庫整理已公開的 2.0 版重現程式與方法說明。Harvard Dataverse API 已確認該版本於 2026-07-23 發布；整理於 2026-10-11 完成公開版本與本機 ZIP 的一致性核對。

- Dataset and complete replication package: [Harvard Dataverse, version 2.0](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/B2ZUV8&version=2.0).
- Public manuscript: [SSRN](https://doi.org/10.2139/ssrn.5352214). This identifies a public preprint; journal publication is not established here.
- Public archive: `Harvard_Dataverse_Replication_v2.0.zip`, Dataverse file ID `14092442`.

## Contents and execution

`code/` contains the eight deposited Python/R scripts. `documentation/` contains the variable codebook, source inventory, Hybrid Poisson specification, software environment, R package list, and figure descriptions. `CITATION.cff` and `LICENSE.txt` retain the public attribution and deposit terms; contact email fields have been removed from the citation file.

To run the full workflow, obtain the complete version 2.0 archive from the official deposit and extract it to a separate working directory. Follow that package's instructions and install its documented Python/R dependencies. Its data, figure inputs, reference outputs and validation records are needed for complete reproduction. The code here matches the deposited scripts; statistical models were not rerun during repository preparation.

資料來源清單記載部分第三方來源的再散布條件未完整保留，因此本程式庫以官方資料下載連結提供資料入口。下載後應依各來源條款使用。

## Interpretation

The deposited README reports agreement with 36 of 41 displayed manuscript coefficient/standard-error pairs. Its five Hybrid Poisson differences and missing original final model specification are documented in `documentation/HYBRID_POISSON_SPECIFICATION.md`. These are deposit-reported results, not new validation performed for this repository.

## License and citation

The deposit applies CC0 to material within the depositor's rights and explicitly preserves third-party terms. See `LICENSE.txt` and `documentation/SOURCE_INVENTORY.csv`. Cite the dataset DOI and retain the scholarly attribution in `CITATION.cff`.

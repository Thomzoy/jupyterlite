1) Copy an existing folder (e.g. `Bio`) and rename it to the name you want (eg `MyVar`)
2) Change `Bio` to `MyVar` in:
    * index.md
    * data.md
3) **Input data**:
    * In `generate_data.py`, paste functions used to generate the data used for plotting (these functions won't be called, but is here for imformative purposes)
    * Replace `data.parquet` with your actual data
4) **Altair plot**. In `generate_plot.py`, update the `get_plot` function that:
    * Accepts the DF loaded from `data.parquet`
    * Returns an Altair chart object
5) Update `mkdocs.yml` to add the new pages. For instance, when starting from :
```yaml
nav:
  - index.md
  - Domains:
    - Domains: domains/index.md
    - Bio: 
      - domains/index.md
      - Plot: domains/Bio/index.md
      - Data: domains/Bio/data.md
```
turn it into:
```yaml
nav:
  - index.md
  - Domains:
    - Domains: domains/index.md
    - Bio: 
      - domains/index.md
      - Plot: domains/Bio/index.md
      - Data: domains/Bio/data.md
    - MyVar: 
      - domains/index.md
      - Plot: domains/MyVar/index.md
      - Data: domains/MyVar/data.md
```

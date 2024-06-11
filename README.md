# odtp-pygwalker

CSV interactive visualization

| Tool Info | Links |
| --- | --- |
| Original Tool | [https://github.com/Kanaries/pygwalker-in-streamlit](https://github.com/Kanaries/pygwalker-in-streamlit) |
| Current Tool Version  | [commit-hash](link-to-commit-hash) |


## ODTP command 

```
odtp new odtp-component-entry \
--name odtp-pygwalker \
--component-version 0.1.0 \
--repository https://github.com/caviri/odtp-pygwalker
``` 

## Data sheet

### Parameters

No parameter

### Input Files

| File/Folder | Description |
| --- | --- | 
| *.csv | Any number of csv files |

### Output Files

No output

## Tutorial

### How to run this component as docker

1. Build the dockerfile 

```
docker build -t odtp-pygwalker .
```

2. Create a folder called `odtp-input` and place some `.csv` files inside.

3. Run the following command. Mount the correct volumes for input/output folders. 

```
docker run -it --rm \
-v $PWD/odtp-input:/odtp/odtp-input \
-p 8501:8501 \
--env-file .env odtp-pygwalker
```


## Developed by

SDSC

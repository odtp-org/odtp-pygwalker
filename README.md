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
| Input | Folder where streamlit compatible files are located |

### Output Files

No output

## Tutorial

### How to run this component as docker

Build the dockerfile 

```
docker build -t odtp-pygwalker .
```

Run the following command. Mount the correct volumes for input/output folders. 

```
docker run -it --rm \
-v ./odtp-input:/odtp/odtp-input \
--env-file .env odtp-pygwalker
```


## Developed by

SDSC


# EXCEL TRAINING MANUAL

Now choose any cell in this table and choose Pivot Table wizard in the Data menu. Excel asks for the data source and suggests this table. Click OK.

| Name of Worker<br/>A | Name of Worker<br/>B | Name of Worker<br/>C | Name of Worker<br/>D | Name of Worker<br/>E |
| -------------------- | -------------------- | -------------------- | -------------------- | -------------------- |
| 1                    | Washing Allowance    | 25                   |                      |                      |
| 1                    | Conveyance Expenses  | 30                   |                      |                      |
| 1                    | Wages                |                      |                      |                      |
| 2                    | Miscellaneous        |                      |                      |                      |


| Home                                                                             | Insert        | Page Layout |
| -------------------------------------------------------------------------------- | ------------- | ----------- |
| PivotTable (highlighted in yellow)<br/>Table<br/>Picture<br/>Clip Art<br/>Shapes | Illustrations |             |


Insert PivotTable  
Click here to summarize data using a PivotTable or to insert a PivotChart.  
PivotTables make it easy to arrange and summarize complicated data and drill down on details.

----

Create PivotTable dialog box:

| Choose the data that you want to analyze | Choose the data that you want to analyze  |
| ---------------------------------------- | ----------------------------------------- |
| \[x] Select a table or range             | Table/Range: `Sheet1!$A$2:$D$50`          |
|  Use an external data source             | Choose Connection...<br/>Connection name: |


| Choose where you want the PivotTable report to be placed | Choose where you want the PivotTable report to be placed |
| -------------------------------------------------------- | -------------------------------------------------------- |
| \[x] New Worksheet                                       |                                                          |
| \[ ] Existing Worksheet                                  | Location:                                                |


<button>OK</button> <button>Cancel</button>

----

Here, we need to understand the data range. Excel suggests the table as shown in the above slide. If you expect to add data in the future, set the data range to include as many rows as you think you will ever need. Rather than `A1:D50`, you may want to specify `$A$1:$D$500`.

One more suggestion is, as shown in the graphic, you can define the destination of the Pivot Table as New Sheet or Existing Sheet.

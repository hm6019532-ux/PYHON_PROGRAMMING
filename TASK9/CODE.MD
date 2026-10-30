1. Problem Statement
Write a Python program to process formatted invoice strings using basic string operations. Extract product codes, quantities, and amounts and identify malformed invoice records.



2. Algorithm
1. Start.
2. Read invoice record.
3. Split the record using commas.
4. Check whether three fields are available.
5. Extract product code.
6. Convert quantity into integer.
7. Convert amount into float.
8. Validate the extracted values.
9. Display invoice details or malformed record.
10. Stop.


3. Flowchart ---(Mermaid)
 flowchart TD
    A([Start]) --> B[/Enter invoice record/]
    B --> C[Split using comma]
    C --> D{Three fields available?}
    D -- No --> E[Malformed Record]
    D -- Yes --> F[Extract product code]
    F --> G[Extract quantity and amount]
    G --> H{Valid values?}
    H -- No --> E
    H -- Yes --> I[Display invoice details]
    E --> J([Stop])
    I --> J
---



5. Sample Input
Enter invoice record: P101,5,2500


6. Sample Output
Product Code: P101
Quantity: 5
Amount: 2500.0

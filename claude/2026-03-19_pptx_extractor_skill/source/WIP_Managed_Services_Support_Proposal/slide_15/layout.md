# Slide 15 - Spatial Layout

```
+-----------------------------------------------------------------------------------------------+
|                                                                                               |
|                            High Level Support Process Flow                                    |
|                                                                                               |
| +----+ +------------------------------------------------------------------------------------+ |
| | B  | | L0 / L1 Flow                                                                       | |
| | a  | |                                                                                    | |
| | y  | |  [Start] -> [User support email / VM] -> [Create Fresh Service ticket]               | |
| | O  | |                                           |                                        | |
| | n  | |                                           v                                        | |
| | e  | |                                   <Is this supported ticket> --No--> [Inform user] -> [Close Ticket] | |
| |    | |                                           | Yes                                    | |
| | E  | | --------------------------------------------+-------------------------------------- | |
| | n  | | L2 / L3 Flow                              |                                        | |
| | d  | |                                           v                                        | |
| | -  | | (from Update DB) --> [Assign ticket]   [Acknowledge user]                            | |
| | t  | |                       |                    |                                       | |
| | o  | |           [Close Ticket]                 <Can you resolve?> --No--> [Assign to agent]  | |
| | -  | |                                            | Yes                                     | |
| | e  | |                                            +---------------------------------+     | |
| | n  | |                                                                              |     | |
| | d  | |                                         <Can other agent resolve?> --No--> [Assign to L3 team] -> [Resolve/Close] | |
| |    | |                                            | Yes         | 3rd party ticket |                   |        |     | |
| | o  | |                                            v             v                        v        (Update DB) |     | |
| | w  | |                                      [Resolve & Close] [Co-ordinate w/ 3rd party] ---+                |     | |
| | n  | |                                            |                                                        |     | |
| | e  | |                                            +------------------------> [Update Knowledge DB] <---------+     | |
| | r  | |                                                                                                      | |
| | s  | |                                                                [Legend]      [Key Callouts]          | |
| | h  | |                                                                [ ] BayOne      * Text...             | |
| | i  | |                                                                [ ] McGrath                           | |
| | p  | |                                                                                                      | |
| +----+ +------------------------------------------------------------------------------------+ |
|                                                                                               |
|  [BAYONE #TheFutureWorksHere.]                                                             15 |
+-----------------------------------------------------------------------------------------------+
```
